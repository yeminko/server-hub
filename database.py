from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Database configuration
DATABASE_URL = "sqlite:///./config.db"

# Create engine with SQLite-specific parameters
engine = create_engine(
    DATABASE_URL, 
    connect_args={"check_same_thread": False}
)

# Session factory
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Base class for models
Base = declarative_base()

# Database dependency
def get_db():
    """Database session dependency for FastAPI endpoints"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    """Initialize the database and create tables"""
    from models import Config  # Import here to avoid circular imports
    
    # Create tables if they don't exist
    Base.metadata.create_all(bind=engine)
    
    # Check if database file exists before initializing
    db_exists = os.path.exists("./config.db")
    return db_exists
