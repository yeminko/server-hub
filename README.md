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

## Additional Information

### Common `uv` Commands

- Initialize a new project: `uv init`
- Add a new dependency: `uv add package_name`
- Remove a dependency: `uv remove package_name`
- Learn more in the [Working on Projects](https://docs.astral.sh/uv/guides/projects/) documentation.

## Useful Resources

- [Virtual Environments](https://fastapi.tiangolo.com/virtual-environments/)
- [Using uv with FastAPI](https://docs.astral.sh/uv/guides/integration/fastapi/)