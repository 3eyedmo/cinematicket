import axios from "axios";
import getApiDomain from "./endpoints";

export const login = async (email, password) => {
  const response = await axios.post(getApiDomain() + "/api/users/token/", {
    email,
    password,
  });
  localStorage.setItem("access", response.data.access);
  localStorage.setItem("refresh", response.data.refresh);
  return response.data;
};

export const refreshToken = async () => {
  const refresh = localStorage.getItem("refresh");
  console.log("refresh Tokennnnn" + refresh);
  const response = await axios.post(
    getApiDomain() + "/api/users/token/refresh/",
    {
      refresh,
    }
  );
  console.log(`access token is: ${response}`);
  localStorage.setItem("access", response.data.access);
  return response.data;
};

export const logout = () => {
  localStorage.removeItem("access");
  localStorage.removeItem("refresh");
};
