"""Deployment schemas"""
from datetime import datetime

from pydantic import BaseModel

class DeploymentResponse(BaseModel):
    """Deployment response schema"""
    id: str
    service: str
    status: str
    duration: int
    timestamp: datetime
    commit_sha: str

    class Config:
        """Config for deployment response schema"""
        from_attributes = True


class DeploymentListResponse(BaseModel):
    """Deployment list response schema"""

    data: list[DeploymentResponse]
    count: int