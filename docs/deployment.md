# Deployment Guide

This document provides instructions for deploying the Document Translation Benchmark Platform to a Linux server.

## Prerequisites

- A Linux server with Docker and Docker Compose installed
- At least 4GB RAM and 2 CPU cores
- Network access to pull Docker images

## Deployment Steps

1. Clone the repository to your server:
   ```
   git clone <repository-url>
   cd document-translation-platform
   ```

2. Build and start the services:
   ```
   docker-compose up -d
   ```

3. Access the application:
   - Frontend: http://your-server-ip:3000
   - Backend API: http://your-server-ip:8000

## Nginx Configuration

For production deployment, it's recommended to use Nginx as a reverse proxy.

Create an Nginx configuration file at `/etc/nginx/sites-available/translation-platform`:

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://localhost:3000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location /api {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

Enable the site by creating a symlink:
```
sudo ln -s /etc/nginx/sites-available/translation-platform /etc/nginx/sites-enabled/
sudo nginx -t && sudo systemctl reload nginx
```

## SSL Configuration

To enable HTTPS, use Let's Encrypt with Certbot:

1. Install Certbot:
   ```
   sudo apt install certbot python3-certbot-nginx
   ```

2. Obtain SSL certificate:
   ```
   sudo certbot --nginx -d your-domain.com
   ```

3. Test the renewal process:
   ```
   sudo certbot renew --dry-run
   ```