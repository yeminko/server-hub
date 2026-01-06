# Docker Guide for ServerHub

This guide provides instructions to run the ServerHub application using Docker. There are two ways to get started:

## Method 1: Recommended Way (Pre-built Image)

For the simplest setup, use the pre-built image directly from Docker Hub. This command will automatically pull the latest image and run it locally - no complex setup needed:

```bash
docker run -p 9222:8000 -d --rm --name server-hub-app -v server-hub-db:/app/db yeminko/server-hub:latest
```

This is the fastest way to get ServerHub running on your local machine.

> More on this image can be found at: <https://hub.docker.com/r/yeminko/server-hub>

## Method 2: Manual Local Build Guide

If you want to build the image from source code locally, follow these steps:

### Build the Image

```bash
docker build -t server-hub:latest .
```

This command builds a Docker image from the Dockerfile in the current directory and tags it as `server-hub:latest`.

### Run the Container

```bash
docker run -p 9222:8000 -d --rm --name server-hub-app -v server-hub-db:/app/db server-hub:latest
```

This command does the following:

- `-p 9222:8000` - Maps port 9222 on your host to port 8000 inside the container
- `-d` - Runs the container in detached mode (in the background)
- `--rm` - Automatically removes the container when it stops
- `--name server-hub-app` - Assigns a name to the container for easy reference
- `-v server-hub-db:/app/db` - Creates a persistent volume for the database files
- `server-hub:latest` - Uses the image we built in the previous step

## Access the Application

Once running, you can access the ServerHub application at:

- API: <http://localhost:9222>
- Documentation: <http://localhost:9222/docs>
- Health Check: <http://localhost:9222/health>