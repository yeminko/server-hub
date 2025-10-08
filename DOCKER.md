# Docker Guide for ServerHub

This guide provides simple instructions to containerize and run the ServerHub application using Docker.

## Build the Image

```bash
docker build -t server-hub:latest .
```

This command builds a Docker image from the Dockerfile in the current directory and tags it as `server-hub:latest`.

## Run the Container

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