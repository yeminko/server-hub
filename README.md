# Server Hub

Server Hub is a simple configuration-as-a-service platform that allows you to easily store and retrieve your configurations through REST APIs.

## Project Setup

### Install `uv`

- Install `uv` using Homebrew: `brew install uv`

## Sync the Project

- Run `uv sync` to download and install required dependencies.

## Run the Project

- Execute `uv run fastapi dev` to start the development server.
  
### Alternative way to run

- Run as follow:

```shell
    source .venv/bin/activate # Activate virtual environment
    fastapi dev # Run the server
    deactivate # Deactivate virtual environment
```

## API Documentation (Swagger)

Once the server is running, you can access the interactive API documentation through Swagger UI:

### Swagger UI Paths

- **Interactive API Documentation**: `http://localhost:8000/docs`
- **Alternative Documentation**: `http://localhost:8000/redoc`
- **OpenAPI JSON Schema**: `http://localhost:8000/openapi.json`

### How to Use Swagger

1. **Start the server** using `uv run fastapi dev`
2. **Open your browser** and navigate to `http://localhost:8000/docs`
3. **Explore the API endpoints**:
   - View all available endpoints organized by tags (Health, Configuration)
   - See detailed request/response schemas
   - Try out endpoints directly from the browser
4. **Test API calls**:
   - Click on any endpoint to expand it
   - Click "Try it out" button
   - Fill in required parameters
   - Click "Execute" to make real API calls
5. **View responses** including status codes, response bodies, and headers

### API Features Available in Swagger

- **Health Endpoints**: Check server status and health
- **Configuration Management**:
  - Store configurations as JSON objects
  - Retrieve configurations by path
  - Update and delete configurations
  - Path-based organization for hierarchical configuration management

The Swagger interface provides a complete reference for all API endpoints, request/response formats, and allows you to test the API without writing any code.

## Additional Information

### Common `uv` Commands

- Initialize a new project: `uv init`
- Add a new dependency: `uv add package_name`
- Remove a dependency: `uv remove package_name`
- Learn more in the [Working on Projects](https://docs.astral.sh/uv/guides/projects/) documentation.

## Useful Resources

- [Virtual Environments](https://fastapi.tiangolo.com/virtual-environments/)
- [Using uv with FastAPI](https://docs.astral.sh/uv/guides/integration/fastapi/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Swagger UI Documentation](https://swagger.io/tools/swagger-ui/)