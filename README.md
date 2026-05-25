# Deployment Service API

A lightweight deployment tracking service built with FastAPI and SQLite.

# Tech Stack

- Python 3.14
- FastAPI
- SQLAlchemy
- SQLite
- Docker

---

# Project Structure

```text
deployment_service/
├── app/
│   ├── api/            # API HTTP route handlers
│   ├── common/         # Shared exceptions and responses
│   ├── core/           # App configuration Settings (e.g. database URL)
│   ├── db/             # Database setup and seed logic
│   ├── models/         # SQLAlchemy ORM models
│   ├── schemas/        # Pydantic request/response schemas
│   ├── services/       # Business logic and DB queries
│   └── main.py         # FastAPI application entrypoint
├── .dockerignore
├── .gitignore
├── Dockerfile
├── README.md
├── requirements.txt
```

---

# Local Setup

### 1. Create virtual environment and activate

```bash
python3 -m venv .venv_deployment_service
source .venv_deployment_service/bin/activate
```

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Run application

```bash
uvicorn app.main:app --reload
```

---

### 5. Swagger API Docs

Open:

```text
http://127.0.0.1:8000/docs
```

---

# Run With Docker

### Build image

```bash
docker build -t deployment-service .
```

### Run container

```bash
docker run -p 8000:8000 deployment-service
```

---

# Available Endpoints

### Health Check

```http
GET /health
```

---

### List Deployments

```http
GET /deployments
```

Optional query params:

```http
GET /deployments?service=billing-api
GET /deployments?status=failed
GET /deployments?service=billing-api&status=failed
```

---

### Get Deployment By ID

```http
GET /deployments/{deployment_id}
```

---

### Example Deployment Event

```json
{
  "id": "deploy_123",
  "service": "billing-api",
  "status": "failed",
  "duration": 320,
  "timestamp": "2025-04-28T14:32:00Z",
  "commit_sha": "abc123"
}
```

