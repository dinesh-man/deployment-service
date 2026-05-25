from fastapi import HTTPException
from fastapi import status


class DeploymentNotFoundException(
    HTTPException
):
    def __init__(self):

        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Deployment not found"
        )