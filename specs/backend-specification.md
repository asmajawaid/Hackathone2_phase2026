# Backend Specification: Phase 2 Full-Stack Web Application

## 1. Backend System Overview Spec

### Responsibilities of Backend
- Handle all task management operations (CRUD) for authenticated users
- Authenticate and authorize API requests using JWT tokens
- Manage database operations for users and tasks
- Provide REST API endpoints under `/api/v1/`
- Enforce user data isolation by user_id
- Handle error responses consistently across all endpoints
- Implement rate limiting and security measures

### API Boundaries
- Public endpoints: Health check and authentication-related endpoints
- Private endpoints: All task management endpoints require valid JWT
- Database layer: SQLModel ORM manages all database interactions
- External services: JWT verification against Better Auth shared secret

### Trust Boundaries
- **Authentication Layer**: JWT tokens verified using Better Auth shared secret
- **Frontend Boundary**: All requests from frontend must include valid JWT
- **Database Boundary**: Direct database access restricted to backend services
- **External Services**: JWT verification happens locally without external calls

### High-Level Request Flow
1. Frontend sends API request with JWT in Authorization header
2. Auth middleware extracts and validates JWT using shared secret
3. Middleware verifies user_id in token matches user_id in URL path
4. Request routed to appropriate endpoint handler
5. Service layer performs business logic and database operations
6. Response formatted according to API specification
7. Response returned to frontend with appropriate status code

## 2. Authentication & Authorization Spec

### JWT Verification Process
- Backend verifies JWT signature using BETTER_AUTH_SECRET environment variable
- Token payload contains user identity information
- Verification happens synchronously in auth middleware
- Invalid tokens result in 401 Unauthorized response

### Better Auth Shared Secret Usage
- Shared secret stored in BETTER_AUTH_SECRET environment variable
- Same secret must be configured in both frontend (Better Auth) and backend
- Secret used for both token signing (frontend) and verification (backend)
- Secret must be 32+ characters and cryptographically random

### Token Expiry Rules
- JWT tokens expire after 24 hours (configurable)
- Expired tokens result in 401 Unauthorized response
- Frontend responsible for refreshing tokens before expiry
- No automatic token refresh mechanism in backend

### User Isolation Enforcement
- All database queries filtered by authenticated user_id
- Users cannot access tasks belonging to other users
- URL path parameter {user_id} must match authenticated user_id
- 403 Forbidden returned if user attempts to access another user's data

### Middleware Behavior
- Auth middleware intercepts all protected endpoints
- Extracts JWT from Authorization: Bearer <token> header
- Verifies token signature and validity
- Attaches authenticated user context to request
- Blocks requests with invalid/missing tokens

### Error Responses for Auth Failures
- Invalid token: 401 Unauthorized with error message
- Missing token: 401 Unauthorized with error message
- Expired token: 401 Unauthorized with error message
- User mismatch: 403 Forbidden with error message

## 3. Database Specification

### SQLModel Models

#### User Model
```python
class User(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    email: str = Field(sa_column=Column("email", String, unique=True, nullable=False))
    name: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow, sa_column_kwargs={"onupdate": datetime.utcnow})
```

#### Task Model
```python
class TaskStatus(str, Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"

class TaskPriority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class Task(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    user_id: UUID = Field(foreign_key="users.id", ondelete="CASCADE")
    title: str = Field(sa_column=Column(String(200), nullable=False))
    description: Optional[str] = None
    status: TaskStatus = Field(default=TaskStatus.PENDING)
    priority: TaskPriority = Field(default=TaskPriority.MEDIUM)
    completed: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow, sa_column_kwargs={"onupdate": datetime.utcnow})

    # Indexes
    __table_args__ = (
        Index("idx_user_status", "user_id", "status"),
        Index("idx_user_created", "user_id", "created_at"),
    )
```

### Field Constraints
- User ID: UUID, primary key, not null
- Email: String(255), unique, not null
- Task ID: UUID, primary key, not null
- Title: String(200), not null
- Description: Text, nullable
- Status: Enum values (pending, in_progress, completed), default: pending
- Priority: Enum values (low, medium, high), default: medium
- Created/Updated timestamps: DateTime, defaults to current UTC time

### Enums
- TaskStatus: pending, in_progress, completed
- TaskPriority: low, medium, high

### Indexing Rules
- Index on (user_id, status) for efficient filtering by user and status
- Index on (user_id, created_at) for chronological ordering by user
- Primary key indexes automatically created

### Foreign Key Behavior
- Task.user_id references User.id with CASCADE delete
- When user is deleted, all their tasks are automatically deleted
- Referential integrity enforced at database level

### Migration Strategy (Alembic)
- Alembic manages schema migrations
- Automatic migration generation from model changes
- Downgrade capability for rollback scenarios
- Environment-specific configurations (dev, staging, prod)

### Neon-Specific Considerations
- Serverless PostgreSQL with connection pooling
- Connection string uses Neon-specific format
- Branch databases for development/staging environments
- Automatic connection management by SQLModel

## 4. API Endpoint Specifications

### GET /api/v1/{user_id}/tasks
- **Method**: GET
- **Path**: `/api/v1/{user_id}/tasks`
- **Auth Requirement**: Valid JWT, user_id in token must match path parameter
- **Request Schema**: Query parameters (optional):
  - limit: int (default 20, max 100)
  - offset: int (default 0)
  - status: TaskStatus (optional filter)
  - sort: str (created_at, updated_at, priority - default created_at)
  - order: str (asc, desc - default desc)
- **Response Schema**:
  ```json
  {
    "success": true,
    "data": {
      "tasks": [
        {
          "id": "uuid",
          "title": "string",
          "description": "string or null",
          "status": "pending|in_progress|completed",
          "priority": "low|medium|high",
          "completed": "boolean",
          "created_at": "ISO datetime",
          "updated_at": "ISO datetime"
        }
      ],
      "pagination": {
        "total": "int",
        "limit": "int",
        "offset": "int",
        "has_more": "boolean"
      }
    },
    "message": "Tasks retrieved successfully"
  }
  ```
- **Validation Rules**:
  - user_id must be valid UUID
  - limit between 1-100
  - offset >= 0
- **Error Cases**:
  - 401: Invalid/missing JWT
  - 403: User_id mismatch
  - 422: Invalid query parameters
- **Ownership Checks**: Only return tasks belonging to authenticated user

### POST /api/v1/{user_id}/tasks
- **Method**: POST
- **Path**: `/api/v1/{user_id}/tasks`
- **Auth Requirement**: Valid JWT, user_id in token must match path parameter
- **Request Schema**:
  ```json
  {
    "title": "string (required, max 200 chars)",
    "description": "string or null (max text length)",
    "status": "pending|in_progress|completed (optional, default pending)",
    "priority": "low|medium|high (optional, default medium)"
  }
  ```
- **Response Schema**:
  ```json
  {
    "success": true,
    "data": {
      "task": {
        "id": "uuid",
        "title": "string",
        "description": "string or null",
        "status": "pending|in_progress|completed",
        "priority": "low|medium|high",
        "completed": "boolean",
        "created_at": "ISO datetime",
        "updated_at": "ISO datetime"
      }
    },
    "message": "Task created successfully"
  }
  ```
- **Validation Rules**:
  - Title required, 1-200 characters
  - Description max length as per database
  - Status and priority must be valid enum values
  - user_id must match authenticated user
- **Error Cases**:
  - 401: Invalid/missing JWT
  - 403: User_id mismatch
  - 422: Validation errors
- **Ownership Checks**: Create task for authenticated user only

### GET /api/v1/{user_id}/tasks/{id}
- **Method**: GET
- **Path**: `/api/v1/{user_id}/tasks/{id}`
- **Auth Requirement**: Valid JWT, user_id in token must match path parameter
- **Request Schema**: None (path parameters only)
- **Response Schema**:
  ```json
  {
    "success": true,
    "data": {
      "task": {
        "id": "uuid",
        "title": "string",
        "description": "string or null",
        "status": "pending|in_progress|completed",
        "priority": "low|medium|high",
        "completed": "boolean",
        "created_at": "ISO datetime",
        "updated_at": "ISO datetime"
      }
    },
    "message": "Task retrieved successfully"
  }
  ```
- **Validation Rules**:
  - user_id must be valid UUID
  - task id must be valid UUID
  - task must belong to authenticated user
- **Error Cases**:
  - 401: Invalid/missing JWT
  - 403: User_id mismatch or task doesn't belong to user
  - 404: Task not found
  - 422: Invalid UUID format
- **Ownership Checks**: Verify task belongs to authenticated user

### PUT /api/v1/{user_id}/tasks/{id}
- **Method**: PUT
- **Path**: `/api/v1/{user_id}/tasks/{id}`
- **Auth Requirement**: Valid JWT, user_id in token must match path parameter
- **Request Schema**:
  ```json
  {
    "title": "string (optional, 1-200 chars)",
    "description": "string or null (optional)",
    "status": "pending|in_progress|completed (optional)",
    "priority": "low|medium|high (optional)"
  }
  ```
- **Response Schema**:
  ```json
  {
    "success": true,
    "data": {
      "task": {
        "id": "uuid",
        "title": "string",
        "description": "string or null",
        "status": "pending|in_progress|completed",
        "priority": "low|medium|high",
        "completed": "boolean",
        "created_at": "ISO datetime",
        "updated_at": "ISO datetime"
      }
    },
    "message": "Task updated successfully"
  }
  ```
- **Validation Rules**:
  - user_id and task id must be valid UUIDs
  - At least one field must be provided for update
  - Values must pass validation (length, enum values)
  - Task must belong to authenticated user
- **Error Cases**:
  - 401: Invalid/missing JWT
  - 403: User_id mismatch or task doesn't belong to user
  - 404: Task not found
  - 422: Validation errors
- **Ownership Checks**: Verify task belongs to authenticated user before update

### DELETE /api/v1/{user_id}/tasks/{id}
- **Method**: DELETE
- **Path**: `/api/v1/{user_id}/tasks/{id}`
- **Auth Requirement**: Valid JWT, user_id in token must match path parameter
- **Request Schema**: None
- **Response Schema**:
  ```json
  {
    "success": true,
    "data": {},
    "message": "Task deleted successfully"
  }
  ```
- **Validation Rules**:
  - user_id and task id must be valid UUIDs
  - Task must belong to authenticated user
- **Error Cases**:
  - 401: Invalid/missing JWT
  - 403: User_id mismatch or task doesn't belong to user
  - 404: Task not found
  - 422: Invalid UUID format
- **Ownership Checks**: Verify task belongs to authenticated user before deletion

### PATCH /api/v1/{user_id}/tasks/{id}/complete
- **Method**: PATCH
- **Path**: `/api/v1/{user_id}/tasks/{id}/complete`
- **Auth Requirement**: Valid JWT, user_id in token must match path parameter
- **Request Schema**: None (toggles completion status)
- **Response Schema**:
  ```json
  {
    "success": true,
    "data": {
      "task": {
        "id": "uuid",
        "title": "string",
        "description": "string or null",
        "status": "pending|in_progress|completed",
        "priority": "low|medium|high",
        "completed": "boolean",
        "created_at": "ISO datetime",
        "updated_at": "ISO datetime"
      }
    },
    "message": "Task completion toggled successfully"
  }
  ```
- **Validation Rules**:
  - user_id and task id must be valid UUIDs
  - Task must belong to authenticated user
  - Toggles completed field (true ↔ false)
- **Error Cases**:
  - 401: Invalid/missing JWT
  - 403: User_id mismatch or task doesn't belong to user
  - 404: Task not found
  - 422: Invalid UUID format
- **Ownership Checks**: Verify task belongs to authenticated user before toggle

## 5. Service Layer Specification

### Separation of Concerns
- **Controller Layer**: Handles HTTP requests/responses, validation
- **Service Layer**: Business logic, transaction management, cross-cutting concerns
- **Repository Layer**: Database operations, SQL queries, model interactions

### Task Service Responsibilities
- Create new tasks with proper ownership assignment
- Retrieve tasks with user isolation enforcement
- Update task properties with validation
- Delete tasks with cascade handling
- Toggle task completion status
- Apply pagination and filtering logic
- Handle transaction boundaries for complex operations

### Transaction Handling
- Each service method operates within a single database transaction
- Transactions automatically committed on success
- Transactions automatically rolled back on exception
- Nested transactions handled appropriately with savepoints if needed

### Async Behavior
- All service methods are asynchronous (async/await)
- Database operations use async SQLAlchemy/SQLModel methods
- Concurrent requests handled safely with async operations
- Proper event loop management for I/O operations

## 6. Error Handling Specification

### Standard Error Response Format
```json
{
  "success": false,
  "error": "Human-readable error message",
  "code": "ERROR_CODE_CONSTANT",
  "details": {
    "timestamp": "ISO datetime",
    "path": "request path",
    "method": "request method"
  }
}
```

### HTTP Status Code Mapping
- 200: Successful GET, PUT, PATCH operations
- 201: Successful POST operation
- 204: Successful DELETE operation
- 400: Bad request (malformed JSON, invalid data format)
- 401: Unauthorized (invalid/missing JWT)
- 403: Forbidden (user_id mismatch, insufficient permissions)
- 404: Not found (resource doesn't exist)
- 409: Conflict (resource conflict, e.g., duplicate email)
- 422: Unprocessable entity (validation errors)
- 429: Too many requests (rate limiting)
- 500: Internal server error (unexpected errors)

### Validation Errors
- Return 422 status with detailed field-specific errors
- Error format includes field names and validation messages
- Multiple validation errors returned in single response
- Validation happens before any database operations

### Auth Errors
- Return 401 for invalid/missing/expired tokens
- Return 403 for user_id mismatches or insufficient permissions
- Include descriptive error messages without exposing internal details

### Database Errors
- Map database-specific errors to appropriate HTTP status codes
- Handle constraint violations with 409 Conflict
- Handle connection errors with 500 Internal Server Error
- Log database errors for debugging while returning generic messages to clients

## 7. Middleware Specification

### Auth Middleware
- Extracts JWT from Authorization header
- Verifies token signature using BETTER_AUTH_SECRET
- Validates token expiration
- Extracts user_id from token payload
- Compares token user_id with URL path parameter
- Attaches user context to request object
- Returns 401/403 for invalid authentication

### CORS Handling
- Configured with specific allowed origins
- Supports credentials for secure token transmission
- Allows required headers (Authorization, Content-Type)
- Implements preflight request handling
- Production configuration restricts origins appropriately

### Logging
- Logs all incoming requests with method, path, and timestamp
- Logs response status codes and execution time
- Logs authentication failures for security monitoring
- Includes correlation IDs for request tracing
- Respects privacy by excluding sensitive data from logs

### Request Lifecycle
1. Request received by FastAPI
2. CORS preflight handling (if applicable)
3. Authentication middleware
4. Request validation
5. Endpoint handler execution
6. Response formatting
7. Logging
8. Response sent to client

## 8. Testing Specification (Backend)

### Unit Tests
- Test individual service layer functions in isolation
- Mock database dependencies using in-memory SQLite
- Verify business logic correctness
- Test error handling paths
- Coverage target: ≥85% for service layer

### API Integration Tests
- Test complete API endpoints with real database (test instance)
- Verify request/response schemas
- Test authentication and authorization flows
- Validate error responses
- Coverage target: ≥85% for API layer

### Auth Mocking Strategy
- Create helper functions to generate valid test JWTs
- Mock Better Auth verification for testing
- Test both valid and invalid authentication scenarios
- Verify user isolation in multi-user test scenarios

### Database Test Isolation
- Use separate test database instance
- Transaction rollback after each test
- Test data factories for consistent test data setup
- Isolate tests to prevent interference between test cases

### Coverage Requirements
- Overall coverage: ≥85%
- Service layer: ≥90%
- API layer: ≥85%
- Critical paths: 100% (authentication, data isolation)
- Generate coverage reports with each test run