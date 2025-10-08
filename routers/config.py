from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from typing import Dict, Any
from utils.database import get_db
from models.models import Config
import utils.schemas as schemas

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
             description="Store multiple configuration values grouped by a key")
def create_config(
    configs: Dict[str, Any],
    key: str = Header(...,
                      description="Key to group configs, e.g. 'pos-app/local/frontend'"),
    db: Session = Depends(get_db)
):
    saved_configs = []

    for config_key, value in configs.items():
        # Check if config exists at this key
        db_config = db.query(Config).filter(
            Config.path == key, Config.key == config_key).first()

        if db_config:
            # Update existing config
            db_config.value = str(value)
        else:
            # Create new config
            new_config = Config(path=key, key=config_key, value=str(value))
            db.add(new_config)

        saved_configs.append(config_key)

    db.commit()
    return {
        "message": "Configs stored successfully",
        "path": key,
        "saved_keys": saved_configs
    }


@router.get("/config/",
            summary="Get all configurations at a key",
            description="Retrieve all configuration values at a specific key as a JSON object")
def read_configs_by_key(
    key: str = Header(...,
                      description="Key to group configs, e.g. 'pos-app/local/frontend'"),
    db: Session = Depends(get_db)
):
    configs = db.query(Config).filter(Config.path == key).all()

    if not configs:
        raise HTTPException(
            status_code=404, detail=f"No configs found for key: {key}")

    # Convert results to a dictionary
    result = {}
    for config in configs:
        result[config.key] = _parse_value(config.value)

    return result


@router.get("/config/item/",
            response_model=schemas.ConfigResponse,
            summary="Get a specific configuration",
            description="Retrieve a specific configuration value by its config_key and key")
def read_config_by_key(
    config_key: str,
    key: str = Header(...,
                      description="Key to group configs, e.g. 'pos-app/local/frontend'"),
    db: Session = Depends(get_db)
):
    db_config = db.query(Config).filter(
        Config.path == key, Config.key == config_key).first()

    if not db_config:
        raise HTTPException(
            status_code=404, detail=f"Config key '{config_key}' not found in key '{key}'")

    return db_config


@router.put("/config/",
            response_model=schemas.ConfigUpdateResponse,
            summary="Update multiple configurations",
            description="Update multiple configuration values at a specific key")
def update_configs(
    configs: Dict[str, Any],
    key: str = Header(...,
                      description="Key to group configs, e.g. 'pos-app/local/frontend'"),
    db: Session = Depends(get_db)
):
    updated_keys = []
    not_found_keys = []

    for config_key, value in configs.items():
        db_config = db.query(Config).filter(
            Config.path == key, Config.key == config_key).first()

        if db_config:
            db_config.value = str(value)
            updated_keys.append(config_key)
        else:
            not_found_keys.append(config_key)

    if not updated_keys:
        raise HTTPException(
            status_code=404, detail=f"No matching configs found in key '{key}'")

    db.commit()

    response = {
        "message": "Config(s) updated successfully", "updated_keys": updated_keys}
    if not_found_keys:
        response["not_found_keys"] = not_found_keys

    return response


@router.delete("/config/key-group/",
               response_model=schemas.ConfigDeleteResponse,
               summary="Delete all configurations at a key",
               description="Delete all configuration values at a specific key")
def delete_configs_by_key(
    key: str = Header(...,
                      description="Key to group configs, e.g. 'pos-app/local/frontend'"),
    db: Session = Depends(get_db)
):
    configs = db.query(Config).filter(Config.path == key).all()

    if not configs:
        raise HTTPException(
            status_code=404, detail=f"No configs found for key: {key}")

    deleted_count = len(configs)
    for config in configs:
        db.delete(config)

    db.commit()
    return {"message": f"All configs deleted successfully", "deleted_count": deleted_count}


@router.delete("/config/item/",
               response_model=schemas.ConfigDeleteResponse,
               summary="Delete a specific configuration",
               description="Delete a specific configuration value by its config_key and key")
def delete_config(
    config_key: str,
    key: str = Header(...,
                      description="Key to group configs, e.g. 'pos-app/local/frontend'"),
    db: Session = Depends(get_db)
):
    db_config = db.query(Config).filter(
        Config.path == key, Config.key == config_key).first()

    if not db_config:
        raise HTTPException(
            status_code=404, detail=f"Config key '{config_key}' not found in key '{key}'")

    db.delete(db_config)
    db.commit()
    return {"message": f"Config '{config_key}' deleted successfully from key '{key}'"}
