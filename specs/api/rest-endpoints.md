# Evolution of Todo - Phase 2 API Documentation

## API Overview
RESTful API for todo application with JWT authentication and user-scoped endpoints.

## Base Configuration
- **Base URL (Dev):** `http://localhost:8000`
- **Base URL (Prod):** `https://your-backend.com`
- **API Version:** v1 (implicit, no version in path for Phase 2)
- **Content-Type:** `application/json`
- **Authentication:** JWT Bearer token in Authorization header

## Authentication

### Required Headers:
```
Authorization: Bearer <jwt_token>
Content-Type: application/json
```

### JWT Payload:
```json
{
  "user_id": "string",
  "email": "string",
  "exp": 1234567890
}
```

## Endpoint Specifications

### 1. List All Tasks

**Endpoint:** `GET /api/{user_id}/tasks`

**Description:** Retrieve all tasks for the authenticated user.

**Path Parameters:**
- `user_id` (string, required): Must match authenticated user's ID

**Query Parameters:** None (for Phase 2)

**Request Headers:**
```
Authorization: Bearer <jwt_token>
```

**Success Response (200):**
```json
{
  "success": true,
  "data": [
    {
      "id": 1,
      "user_id": "user_123",
      "title": "Buy groceries",
      "description": "Milk, eggs, bread",
      "completed": false,
      "created_at": "2026-01-26T10:30:00Z",
      "updated_at": "2026-01-26T10:30:00Z"
    },
    {
      "id": 2,
      "user_id": "user_123",
      "title": "Finish homework",
      "description": null,
      "completed": true,
      "created_at": "2026-01-25T14:20:00Z",
      "updated_at": "2026-01-26T09:15:00Z"
    }
  ],
  "count": 2
}
```

**Error Responses:**
```json
// 401 Unauthorized
{
  "success": false,
  "error": "Authentication required",
  "code": "AUTH_REQUIRED"
}

// 403 Forbidden (user_id mismatch)
{
  "success": false,
  "error": "Access denied",
  "code": "FORBIDDEN"
}
```

### 2. Create Task

**Endpoint:** `POST /api/{user_id}/tasks`

**Description:** Create a new task for the authenticated user.

**Path Parameters:**
- `user_id` (string, required): Must match authenticated user's ID

**Request Headers:**
```
Authorization: Bearer <jwt_token>
Content-Type: application/json
```

**Request Body:**
```json
{
  "title": "Buy groceries",
  "description": "Milk, eggs, bread"
}
```

**Request Body Schema:**
```typescript
{
  title: string;        // required, 1-200 chars
  description?: string; // optional, max 1000 chars
}
```

**Success Response (201):**
```json
{
  "success": true,
  "data": {
    "id": 3,
    "user_id": "user_123",
    "title": "Buy groceries",
    "description": "Milk, eggs, bread",
    "completed": false,
    "created_at": "2026-01-26T15:45:00Z",
    "updated_at": "2026-01-26T15:45:00Z"
  },
  "message": "Task created successfully"
}
```

**Error Responses:**
```json
// 400 Bad Request (validation)
{
  "success": false,
  "error": "Title is required",
  "code": "VALIDATION_ERROR",
  "field": "title"
}

// 400 Bad Request (title too long)
{
  "success": false,
  "error": "Title must be 200 characters or less",
  "code": "VALIDATION_ERROR",
  "field": "title"
}

// 401 Unauthorized
{
  "success": false,
  "error": "Authentication required",
  "code": "AUTH_REQUIRED"
}
```

### 3. Get Single Task

**Endpoint:** `GET /api/{user_id}/tasks/{id}`

**Description:** Retrieve a specific task by ID.

**Path Parameters:**
- `user_id` (string, required): Must match authenticated user's ID
- `id` (integer, required): Task ID

**Request Headers:**
```
Authorization: Bearer <jwt_token>
```

**Success Response (200):**
```json
{
  "success": true,
  "data": {
    "id": 1,
    "user_id": "user_123",
    "title": "Buy groceries",
    "description": "Milk, eggs, bread",
    "completed": false,
    "created_at": "2026-01-26T10:30:00Z",
    "updated_at": "2026-01-26T10:30:00Z"
  }
}
```

**Error Responses:**
```json
// 404 Not Found
{
  "success": false,
  "error": "Task not found",
  "code": "NOT_FOUND"
}

// 403 Forbidden (task belongs to different user)
{
  "success": false,
  "error": "Access denied",
  "code": "FORBIDDEN"
}
```

### 4. Update Task

**Endpoint:** `PUT /api/{user_id}/tasks/{id}`

**Description:** Update an existing task.

**Path Parameters:**
- `user_id` (string, required): Must match authenticated user's ID
- `id` (integer, required): Task ID

**Request Headers:**
```
Authorization: Bearer <jwt_token>
Content-Type: application/json
```

**Request Body:**
```json
{
  "title": "Buy groceries and fruits",
  "description": "Milk, eggs, bread, apples, bananas"
}
```

**Request Body Schema:**
```typescript
{
  title?: string;       // optional, 1-200 chars
  description?: string; // optional, max 1000 chars
}
```
*Note: At least one field must be provided*

**Success Response (200):**
```json
{
  "success": true,
  "data": {
    "id": 1,
    "user_id": "user_123",
    "title": "Buy groceries and fruits",
    "description": "Milk, eggs, bread, apples, bananas",
    "completed": false,
    "created_at": "2026-01-26T10:30:00Z",
    "updated_at": "2026-01-26T16:20:00Z"
  },
  "message": "Task updated successfully"
}
```

**Error Responses:**
```json
// 400 Bad Request (no fields)
{
  "success": false,
  "error": "At least one field must be provided",
  "code": "VALIDATION_ERROR"
}

// 404 Not Found
{
  "success": false,
  "error": "Task not found",
  "code": "NOT_FOUND"
}
```

### 5. Delete Task

**Endpoint:** `DELETE /api/{user_id}/tasks/{id}`

**Description:** Permanently delete a task.

**Path Parameters:**
- `user_id` (string, required): Must match authenticated user's ID
- `id` (integer, required): Task ID

**Request Headers:**
```
Authorization: Bearer <jwt_token>
```

**Success Response (200):**
```json
{
  "success": true,
  "message": "Task deleted successfully",
  "data": {
    "id": 1,
    "deleted": true
  }
}
```

**Error Responses:**
```json
// 404 Not Found
{
  "success": false,
  "error": "Task not found",
  "code": "NOT_FOUND"
}

// 403 Forbidden
{
  "success": false,
  "error": "Access denied",
  "code": "FORBIDDEN"
}
```

### 6. Toggle Task Completion

**Endpoint:** `PATCH /api/{user_id}/tasks/{id}/complete`

**Description:** Toggle task between completed and incomplete status.

**Path Parameters:**
- `user_id` (string, required): Must match authenticated user's ID
- `id` (integer, required): Task ID

**Request Headers:**
```
Authorization: Bearer <jwt_token>
```

**Request Body:** None

**Success Response (200):**
```json
{
  "success": true,
  "data": {
    "id": 1,
    "user_id": "user_123",
    "title": "Buy groceries",
    "description": "Milk, eggs, bread",
    "completed": true,
    "created_at": "2026-01-26T10:30:00Z",
    "updated_at": "2026-01-26T16:45:00Z"
  },
  "message": "Task status updated"
}
```

**Error Responses:**
```json
// 404 Not Found
{
  "success": false,
  "error": "Task not found",
  "code": "NOT_FOUND"
}
```

## Global Error Codes

| Code | HTTP Status | Description |
|------|-------------|-------------|
| AUTH_REQUIRED | 401 | No JWT token provided |
| INVALID_TOKEN | 401 | JWT token is invalid or expired |
| FORBIDDEN | 403 | User doesn't own the resource |
| NOT_FOUND | 404 | Resource doesn't exist |
| VALIDATION_ERROR | 400 | Request validation failed |
| SERVER_ERROR | 500 | Internal server error |

## CORS Configuration
```python
# Backend: main.py
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://your-app.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## Rate Limiting
Not implemented in Phase 2 (optional for future)

## API Testing Checklist
- [ ] All endpoints return correct status codes
- [ ] Authentication is enforced on all endpoints
- [ ] User data isolation is working
- [ ] Validation errors return proper messages
- [ ] Error responses follow standard format
- [ ] CORS allows frontend origin
- [ ] Response times < 200ms