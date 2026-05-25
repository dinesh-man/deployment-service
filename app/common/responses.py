from typing import Generic
from typing import TypeVar

from pydantic import BaseModel


T = TypeVar("T")


class ErrorResponse(BaseModel):
    message: str

    status_code: int