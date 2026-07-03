# Stage 1: Production Lightweight Web Server Container
FROM nginx:alpine

# Metadata labels for DevOps identification
LABEL maintainer="ABC Technologies DevOps Team <devops@abctechnologies.io>"
LABEL version="2.0.0"
LABEL description="ABC Technologies Corporate Website Container Image"

# Remove default Nginx config and static files
RUN rm -rf /usr/share/nginx/html/* /etc/nginx/conf.d/default.conf

# Copy custom Nginx configuration
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copy compiled production website assets into Nginx web root
COPY website/ /usr/share/nginx/html/

# Expose HTTP port 80
EXPOSE 80

# Health check probe for container runtime stability
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD wget -qO- http://localhost/healthz || exit 1

# Start Nginx daemon in foreground
CMD ["nginx", "-g", "daemon off;"]
