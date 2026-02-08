# Backend Quickstart

## Prerequisites
- Python 3.12+
- pip
- Git

## Environment Setup
Create `.env` file with:
```bash
cp .env.example .env
```

Update these variables in `.env`:
- `NEON_DATABASE_URL`: Your Neon PostgreSQL connection string
- `BETTER_AUTH_SECRET`: JWT secret key

## Install Dependencies
```bash
pip install -r requirements.txt
```

## Run Database Migrations
```bash
python -m backend.database.migrate
```

## Start Backend Server
```bash
cd backend
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
uvicorn main:app --reload --port 8000
```

## Verify Backend is Running
Visit: `http://localhost:8000/health`

Expected response: `{"status": "healthy"}`

## Common Issues
- Port 8000 in use: Change port in uvicorn command
- Database connection error: Verify NEON_DATABASE_URL in .env
- Missing dependencies: Run pip install again