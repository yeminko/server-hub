# ServerHub

ServerHub is a simple configuration-as-a-service platform that allows you to store and retrieve configurations through REST APIs. Store your application settings, feature flags, and environment variables in a centralized location with path-based organization.

## Quick Start with Docker 🐳

If you have Docker installed, check out our [DOCKER.md](DOCKER.md) guide for the easiest way to run ServerHub. You can get started with just one command!

## Environment Setup

### Prerequisites

- Python 3.x
- `uv` package manager

### Installation

1. Install `uv` (if not already installed):

   ```bash
   brew install uv
   ```

2. Sync dependencies:

   ```bash
   uv sync
   ```

3. Start the development server:

   ```bash
   uv run fastapi dev
   ```

The server will start at `http://localhost:8000`

## API Examples

### Health Check

Check if the API is running:

```bash
curl -X GET "http://localhost:8000/health"
```

### Configuration Management

All configuration endpoints require a `key` header to group configurations.

#### Create/Update Multiple Configurations

```bash
curl -X POST "http://localhost:8000/config/" \
  -H "key: my-app-config" \
  -H "Content-Type: application/json" \
  -d '{
    "database_url": "postgresql://localhost:5432/mydb",
    "debug": true,
    "max_connections": 100
  }'
```

#### Get All Configurations by Key

```bash
curl -X GET "http://localhost:8000/config/" \
  -H "key: my-app-config"
```

#### Get Specific Configuration

```bash
curl -X GET "http://localhost:8000/config/item/?config_key=database_url" \
  -H "key: my-app-config"
```

#### Update Multiple Configurations

```bash
curl -X PUT "http://localhost:8000/config/" \
  -H "key: my-app-config" \
  -H "Content-Type: application/json" \
  -d '{
    "debug": false,
    "max_connections": 200
  }'
```

#### Delete Specific Configuration

```bash
curl -X DELETE "http://localhost:8000/config/item/?config_key=debug" \
  -H "key: my-app-config"
```

#### Delete All Configurations by Key

```bash
curl -X DELETE "http://localhost:8000/config/key-group/" \
  -H "key: my-app-config"
```

## Swagger Documentation

Access the interactive API documentation at:

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

The Swagger interface allows you to explore all endpoints, view request/response schemas, and test API calls directly from your browser.
