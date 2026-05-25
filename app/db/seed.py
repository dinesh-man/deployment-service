import random
import uuid

from datetime import datetime
from datetime import timedelta
from datetime import timezone

from app.db.session import SessionLocal
from app.models.deployment import Deployment

SERVICES = [
    "billing-api",
    "auth-service",
    "search-api",
    "notification-service"
]

STATUSES = [
    "success",
    "failed",
    "in_progress"
]

def seed_data():
    db = SessionLocal()

    existing_records = db.query(Deployment).count()

    if existing_records > 0:
        print("Database already seeded")
        db.close()
        return

    for index in range(30):
        deployment = Deployment(
            id=f"deploy_{uuid.uuid4().hex[:8]}",
            service=random.choice(SERVICES),
            status=random.choice(STATUSES),
            duration=random.randint(60, 600),
            timestamp=datetime.now(timezone.utc) - timedelta(hours=index),
            commit_sha=uuid.uuid4().hex[:7]
        )

        db.add(deployment)

    db.commit()
    db.close()

    print("Seeded 30 deployment events")