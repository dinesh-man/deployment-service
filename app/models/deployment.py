from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import DateTime

from app.db.database import Base


class Deployment(Base):
    __tablename__ = "deployments"

    id = Column(String, primary_key=True, index=True)

    service = Column(String, nullable=False, index=True)

    status = Column(String, nullable=False, index=True)

    duration = Column(Integer, nullable=False)

    timestamp = Column(DateTime, nullable=False)

    commit_sha = Column(String, nullable=False)