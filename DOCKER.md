# Docker Guide for ServerHub

## Quick Start

### Build the Image
```bash
docker build -t serverhub .
```

### Run the Container
```bash
docker run -p 8000:8000 serverhub
```

### Access the Application
- API: http://localhost:8000
- Docs: http://localhost:8000/docs
- Health: http://localhost:8000/health

## Development

### Run with Volume Mount (for development)
```bash
docker run -p 8000:8000 -v $(pwd):/app serverhub
```

### Run in Background
```bash
docker run -d -p 8000:8000 --name serverhub-app serverhub
```

### View Logs
```bash
docker logs serverhub-app
```

### Stop Container
```bash
docker stop serverhub-app
docker rm serverhub-app
```

## Production

### Build for Production
```bash
docker build -t serverhub:latest .
docker tag serverhub:latest serverhub:v1.0.0
```

### Run with Restart Policy
```bash
docker run -d \
  --name serverhub-prod \
  --restart unless-stopped \
  -p 8000:8000 \
  serverhub:latest
```

## Docker Compose (Optional)

Create `docker-compose.yml`:
```yaml
version: '3.8'

services:
  serverhub:
    build: .
    ports:
      - "8000:8000"
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
```

Run with compose:
```bash
docker-compose up -d
```

## Troubleshooting

### Check Container Status
```bash
docker ps -a
```

### Execute Shell in Container
```bash
docker exec -it serverhub-app bash
```

### Check Health Status
```bash
docker inspect serverhub-app | grep Health -A 10
```

### View Resource Usage
```bash
docker stats serverhub-app
```