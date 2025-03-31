# Stage 1: Build the application
FROM node:22.14.0-bookworm as builder

WORKDIR /app
COPY cinematicket_frontend/package*.json ./
RUN npm install --omit=dev --fund=false --audit=false
RUN npm install @rollup/rollup-linux-x64-gnu --save-optional
COPY cinematicket_frontend .
RUN npm run build

# Stage 2: Production server
FROM nginx:1.25.5-alpine3.19

# Copy built assets from builder
COPY --from=builder /app/dist /usr/share/nginx/html
EXPOSE 80
# Stage 1: Build React app
# FROM node:20-alpine as builder

# WORKDIR /app
# COPY react_app/package.json react_app/package-lock.json ./
# RUN npm ci --silent
# COPY react_app/ ./
# RUN npm run build

# # Stage 2: Serve with Nginx
# FROM nginx:1.25-alpine

# # Copy built assets from builder
# COPY --from=builder /app/build /usr/share/nginx/html

# # Copy custom nginx config (optional)
# # COPY react_app/nginx.conf /etc/nginx/conf.d/default.conf

# # Expose port 80
# EXPOSE 80

# # Start Nginx
# CMD ["nginx", "-g", "daemon off;"]