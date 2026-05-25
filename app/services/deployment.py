"""Deployment service"""
from sqlalchemy.orm import Session

from app.models.deployment import Deployment

def get_deployments(
    db: Session,
    service: str | None = None,
    status: str | None = None
):
    """Get all deployments from the database filtered by service and status."""

    query = db.query(Deployment)

    if service:
        query = query.filter(
            Deployment.service == service
        )

    if status:
        query = query.filter(
            Deployment.status == status
        )

    return (
        query
        .order_by(Deployment.timestamp.desc())
        .all()
    )


def get_deployment_by_id(
    db: Session,
    deployment_id: str
):
    """Get a deployment by its ID."""

    return (
        db.query(Deployment)
        .filter(Deployment.id == deployment_id)
        .first()
    )