# Todo Backend API

Backend for the Evolution of Todo - Phase 2 Full-Stack Web Application

## Overview
This is the backend API for the Todo application, built with FastAPI and SQLModel. It provides a REST API for managing tasks with proper authentication and user isolation.

## Features
- JWT-based authentication using Better Auth
- Task CRUD operations with user isolation
- RESTful API under `/api/v1/`
- Proper error handling and validation
- Comprehensive test coverage

## Tech Stack
- Python 3.12+
- FastAPI
- SQLModel
- PostgreSQL (Neon)
- Alembic for migrations
- Pydantic for validation

## Setup

1. Clone the repository
2. Navigate to the backend directory
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   Or using the pyproject.toml:
   ```bash
   pip install .
   ```
4. Copy `.env.example` to `.env` and update the configuration values
5. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```

## API Endpoints

### Authentication Required
All task endpoints require a valid JWT in the Authorization header:
```
Authorization: Bearer <jwt_token>
```

### Task Endpoints
- `GET /api/v1/{user_id}/tasks` - Get all tasks for a user
- `POST /api/v1/{user_id}/tasks` - Create a new task
- `GET /api/v1/{user_id}/tasks/{id}` - Get a specific task
- `PUT /api/v1/{user_id}/tasks/{id}` - Update a task
- `DELETE /api/v1/{user_id}/tasks/{id}` - Delete a task
- `PATCH /api/v1/{user_id}/tasks/{id}/complete` - Toggle task completion

## Environment Variables

- `DATABASE_URL`: Database connection string
- `BETTER_AUTH_SECRET`: Shared secret for JWT verification
- `JWT_ALGORITHM`: Algorithm for JWT signing (default: HS256)
- `ACCESS_TOKEN_EXPIRE_MINUTES`: Token expiry in minutes (default: 1440)
- `ALLOWED_ORIGINS`: Comma-separated list of allowed origins for CORS
- `APP_NAME`: Application name (default: Todo Backend API)
- `DEBUG`: Enable debug mode (default: False)

## Running Tests

To run the tests:
```bash
pytest
```

For coverage report:
```bash
pytest --cov=app --cov-report=html
```

## Migrations

To run database migrations:
```bash
alembic upgrade head
```

To create a new migration:
```bash
alembic revision --autogenerate -m "migration message"
```