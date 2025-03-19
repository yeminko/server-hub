from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from typing import Dict, Any
from database import get_db
from models import Config
import schemas

# Initialize router
router = APIRouter(
    tags=["configuration"],
    responses={404: {"model": schemas.ErrorResponse}}
)

def _parse_value(value: str) -> Any:
    """Helper function to parse string values into appropriate types"""
    # Handle boolean values
    if value.lower() == "true":
        return True
    elif value.lower() == "false":
        return False
    # Handle numeric values
    elif value.isdigit():
        return int(value)
    elif value.replace('.', '', 1).isdigit() and value.count('.') == 1:
        return float(value)
    # Return as string if no conversion applies
    return value

@router.post("/config/", 
             response_model=schemas.ConfigCreateResponse,
             summary="Create or update multiple configurations",
             description="Store multiple configuration values grouped by a path")
def create_config(
    configs: Dict[str, Any],
    path: str = Header(..., description="Path to group configs, e.g. 'pos-app/local/frontend'"),
    db: Session = Depends(get_db)
):
    saved_configs = []
    
    for key, value in configs.items():
        # Check if config exists at this path
        db_config = db.query(Config).filter(Config.path == path, Config.key == key).first()
        
        if db_config:
            # Update existing config
            db_config.value = str(value)
        else:
            # Create new config
            new_config = Config(path=path, key=key, value=str(value))
            db.add(new_config)
        
        saved_configs.append(key)
    
    db.commit()
    return {
        "message": "Configs stored successfully",
        "path": path,
        "saved_keys": saved_configs
    }

@router.get("/config/",
            summary="Get all configurations at a path",
            description="Retrieve all configuration values at a specific path as a JSON object")
def read_configs_by_path(
    path: str = Header(..., description="Path to group configs, e.g. 'pos-app/local/frontend'"),
    db: Session = Depends(get_db)
):
    configs = db.query(Config).filter(Config.path == path).all()
    
    if not configs:
        raise HTTPException(status_code=404, detail=f"No configs found for path: {path}")
    
    # Convert results to a dictionary
    result = {}
    for config in configs:
        result[config.key] = _parse_value(config.value)
    
    return result

@router.get("/config/key/", 
            response_model=schemas.ConfigResponse,
            summary="Get a specific configuration",
            description="Retrieve a specific configuration value by its key and path")
def read_config_by_key(
    key: str,
    path: str = Header(..., description="Path to group configs, e.g. 'pos-app/local/frontend'"),
    db: Session = Depends(get_db)
):
    db_config = db.query(Config).filter(Config.path == path, Config.key == key).first()
    
    if not db_config:
        raise HTTPException(status_code=404, detail=f"Key '{key}' not found in path '{path}'")
    
    return db_config

@router.put("/config/",
           response_model=schemas.ConfigUpdateResponse,
           summary="Update multiple configurations",
           description="Update multiple configuration values at a specific path")
def update_configs(
    configs: Dict[str, Any],
    path: str = Header(..., description="Path to group configs, e.g. 'pos-app/local/frontend'"),
    db: Session = Depends(get_db)
):
    updated_keys = []
    not_found_keys = []
    
    for key, value in configs.items():
        db_config = db.query(Config).filter(Config.path == path, Config.key == key).first()
        
        if db_config:
            db_config.value = str(value)
            updated_keys.append(key)
        else:
            not_found_keys.append(key)
    
    if not updated_keys:
        raise HTTPException(status_code=404, detail=f"No matching configs found in path '{path}'")
    
    db.commit()
    
    response = {"message": "Config(s) updated successfully", "updated_keys": updated_keys}
    if not_found_keys:
        response["not_found_keys"] = not_found_keys
    
    return response

@router.delete("/config/path/",
              response_model=schemas.ConfigDeleteResponse,
              summary="Delete all configurations at a path",
              description="Delete all configuration values at a specific path")
def delete_configs_by_path(
    path: str = Header(..., description="Path to group configs, e.g. 'pos-app/local/frontend'"),
    db: Session = Depends(get_db)
):
    configs = db.query(Config).filter(Config.path == path).all()
    
    if not configs:
        raise HTTPException(status_code=404, detail=f"No configs found for path: {path}")
    
    deleted_count = len(configs)
    for config in configs:
        db.delete(config)
    
    db.commit()
    return {"message": f"All configs deleted successfully", "deleted_count": deleted_count}

@router.delete("/config/key/",
              response_model=schemas.ConfigDeleteResponse,
              summary="Delete a specific configuration",
              description="Delete a specific configuration value by its key and path")
def delete_config(
    key: str,
    path: str = Header(..., description="Path to group configs, e.g. 'pos-app/local/frontend'"),
    db: Session = Depends(get_db)
):
    db_config = db.query(Config).filter(Config.path == path, Config.key == key).first()
    
    if not db_config:
        raise HTTPException(status_code=404, detail=f"Key '{key}' not found in path '{path}'")
    
    db.delete(db_config)
    db.commit()
    return {"message": f"Config '{key}' deleted successfully from path '{path}'"}
