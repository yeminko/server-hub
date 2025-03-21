from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from utils.database import init_db
from routers import config, health
from utils.logger import setup_logger

# Set up logging
logger = setup_logger()

# Application metadata for API documentation
app_description = """
## Summary

ServerHub provides configuration management through a RESTful API.

## Features

* **Configuration Management**: Store, retrieve, update and delete configurations
* **Path-based Organization**: Group configurations by hierarchical paths
* **JSON Format**: Store and retrieve configurations as JSON objects
"""

# Lifespan context manager for startup and shutdown events


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic
    db_exists = init_db()
    if db_exists:
        logger.info("Database already exists. Tables verified.")
    else:
        logger.info("Database initialized successfully.")
    yield
    # Shutdown logic (if needed)
    logger.info("Shutting down application")

# FastAPI application with metadata for documentation
app = FastAPI(
    lifespan=lifespan,
    title="ServerHub API",
    description=app_description,
    version="1.0.0",
    contact={
        "name": "ServerHub Team"
    },
    openapi_tags=[
        {
            "name": "health",
            "description": "Health check endpoints"
        },
        {
            "name": "configuration",
            "description": "Configuration management endpoints"
        }
    ]
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with specific origins if needed
    allow_credentials=True,  # Allow credentials like cookies or tokens
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Include routers
app.include_router(config.router)
app.include_router(health.router)
