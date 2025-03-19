from pydantic import BaseModel
from typing import List, Optional


class ConfigResponse(BaseModel):
    """Schema for an individual config response"""
    path: str
    key: str
    value: str

    class Config:
        from_attributes = True


class ConfigCreateResponse(BaseModel):
    """Schema for config creation response"""
    message: str
    path: str
    saved_keys: List[str]


class ConfigUpdateResponse(BaseModel):
    """Schema for config update response"""
    message: str
    updated_keys: List[str]
    not_found_keys: Optional[List[str]] = None


class ConfigDeleteResponse(BaseModel):
    """Schema for config deletion response"""
    message: str
    deleted_count: Optional[int] = None


class HealthResponse(BaseModel):
    """Schema for health check response"""
    status: str
    message: str


class ErrorResponse(BaseModel):
    """Schema for error response"""
    detail: str
