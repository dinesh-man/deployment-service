from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.db.database import get_db

from app.schemas.deployment import DeploymentListResponse, DeploymentResponse
from app.common.exceptions import (
    DeploymentNotFoundException
)

from app.services.deployment import (
    get_deployments,
    get_deployment_by_id
)

router = APIRouter(
    prefix="/deployments",
    tags=["deployments"]
)

"""List all deployments."""
@router.get(
    "",
    response_model=DeploymentListResponse
)
def list_deployments(
    service: str | None = None,
    status: str | None = None,
    db: Session = Depends(get_db)
):
    deployments = get_deployments(
        db=db,
        service=service,
        status=status
    )
    return DeploymentListResponse(
        data=deployments,
        count=len(deployments)
    )

"""Get a deployment by its ID."""
@router.get(
    "/{deployment_id}",
    response_model=DeploymentResponse
)
def get_deployment(
    deployment_id: str,
    db: Session = Depends(get_db)
):

    deployment = get_deployment_by_id(
        db=db,
        deployment_id=deployment_id
    )

    if not deployment:
        raise DeploymentNotFoundException()

    return deployment