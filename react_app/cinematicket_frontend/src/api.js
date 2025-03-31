import axios from "axios";
import { refreshToken } from "./auth";
import getApiDomain from "./endpoints";

const api = axios.create({
  baseURL: getApiDomain() + "/api/",
});

let isRefreshing = false;
let failedRequests = [];

// Request interceptor to add auth token
api.interceptors.request.use((config) => {
  const token = localStorage.getItem("access");
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Response interceptor to handle token refresh
api.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config;

    if (error.response?.status === 401 && !originalRequest._retry) {
      if (isRefreshing) {
        return new Promise((resolve) => {
          failedRequests.push(() => {
            originalRequest.headers.Authorization = `Bearer ${localStorage.getItem(
              "access"
            )}`;
            resolve(api(originalRequest));
          });
        });
      }

      originalRequest._retry = true;
      isRefreshing = true;

      try {
        const newTokens = await refreshToken();

        localStorage.setItem("access", newTokens.access);

        // Retry failed requests
        failedRequests.forEach((cb) => cb());
        failedRequests = [];

        return api(originalRequest);
      } catch (refreshError) {
        return Promise.reject(refreshError);
      } finally {
        isRefreshing = false;
      }
    }

    return Promise.reject(error);
  }
);

export default api;
