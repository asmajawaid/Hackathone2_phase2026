# Phase 2 BACKEND Implementation Plan

## 1. Backend Architecture Overview

### High-level Architecture Diagram
```
[Frontend Request] → [Auth Middleware] → [API Routes] → [Service Layer] → [Repository Layer] → [SQLModel/DB]
         ↓                ↓                  ↓              ↓                ↓                   ↓
[JWT Token] ←→ [Validate JWT] ←→ [Validate User] ←→ [Business Logic] ←→ [Data Access] ←→ [PostgreSQL]
```

### Component Boundaries
- **API Layer**: FastAPI routes handling HTTP requests/responses
- **Service Layer**: Business logic and transaction management
- **Repository Layer**: Data access operations and queries
- **Model Layer**: SQLModel entity definitions and validation
- **Infrastructure**: Authentication, error handling, configuration

### Data Flow
1. Request arrives with JWT in Authorization header
2. Auth middleware validates JWT and extracts user context
3. API route validates request data using Pydantic models
4. Service layer executes business logic with user context
5. Repository layer performs database operations
6. Response formatted and returned with appropriate status

### Trust Boundaries
- **External Boundary**: JWT validation at middleware level
- **API Boundary**: Request validation before processing
- **Data Boundary**: User isolation enforced at repository level
- **System Boundary**: Error handling prevents information leakage

## 2. Module Breakdown

### main application entry (`main.py`)
- FastAPI application instance
- Global configuration setup
- Middleware registration
- Route inclusion

### Configuration & Environment (`config.py`)
- Environment variable loading
- Database URL configuration
- JWT secret configuration
- CORS settings
- Logging configuration

### Database Connection (`database.py`)
- SQLModel engine setup
- Session management
- Connection pooling configuration
- Database initialization

### Models (`models.py`)
- SQLModel User and Task definitions
- Field constraints and validation
- Relationship definitions
- Index specifications

### Repositories (`repositories/`)
- User repository (CRUD operations)
- Task repository (CRUD operations with user filtering)
- Generic repository base class
- Query builders

### Services (`services/`)
- Task service (business logic)
- Authentication service (JWT handling)
- User service (user operations)
- Error handling utilities

### Routes (`routes/`)
- Task API endpoints
- Health check endpoint
- Error handling middleware
- Request/response validation

### Middleware (`middleware/`)
- JWT authentication middleware
- CORS middleware
- Request logging middleware
- Error handling middleware

### Error Handling (`errors.py`)
- Custom exception classes
- Error response formatting
- HTTP status code mappings
- Validation error handling

### Testing Infrastructure (`tests/`)
- Test configuration
- Database fixtures
- Mock authentication
- API test utilities

## 3. Dependency Graph

### Module Dependencies
```
main.py → config.py
main.py → database.py
main.py → middleware/
main.py → routes/

config.py → [None]

database.py → config.py

models.py → [None]

repositories/ → models.py
repositories/ → database.py

services/ → repositories/
services/ → models.py
services/ → errors.py

routes/ → services/
routes/ → models.py
routes/ → middleware/

middleware/ → config.py
middleware/ → services/

errors.py → [None]
```

### Order of Initialization
1. `config.py` - Load environment variables
2. `database.py` - Initialize database connection
3. `models.py` - Define models
4. `repositories/` - Set up data access layer
5. `services/` - Implement business logic
6. `middleware/` - Configure request handling
7. `routes/` - Register API endpoints
8. `main.py` - Initialize FastAPI app

### Shared Utilities
- `utils/` - Common helper functions
- `schemas/` - Pydantic request/response models
- `constants/` - Application constants

## 4. Execution Phases (Backend Only)

### Phase A: Project Bootstrap & Configuration
**Inputs**: Backend specifications
**Outputs**: Project structure, basic FastAPI app, configuration management
- Initialize FastAPI application
- Set up environment configuration
- Configure logging
- Create project directory structure
- Install dependencies (FastAPI, SQLModel, etc.)

**Validation Criteria**:
- App starts without errors
- Environment variables loaded correctly
- Basic health endpoint responds

### Phase B: Database & Models
**Inputs**: Database specification from backend specs
**Outputs**: SQLModel definitions, database connection, migration setup
- Define User and Task SQLModel classes
- Set up database engine and session
- Configure connection pooling
- Implement Alembic migration setup
- Create initial migration

**Validation Criteria**:
- Models match specification exactly
- Database connection established
- Migrations can be applied
- All constraints and indexes implemented

### Phase C: Authentication & JWT Middleware
**Inputs**: Authentication specification from backend specs
**Outputs**: JWT verification, auth middleware, user context extraction
- Implement JWT verification using python-jose
- Create authentication middleware
- Set up Better Auth secret handling
- Implement user context attachment
- Test token validation

**Validation Criteria**:
- Valid JWTs are accepted
- Invalid JWTs are rejected with 401
- User context attached to requests
- Token expiration handled

### Phase D: Task Service Layer
**Inputs**: Service specification from backend specs
**Outputs**: Business logic for task operations, user isolation
- Implement TaskService with CRUD operations
- Enforce user isolation in all operations
- Handle transaction boundaries
- Implement async operations
- Add validation logic

**Validation Criteria**:
- All CRUD operations work correctly
- User isolation enforced properly
- Transactions handled appropriately
- Async operations function as expected

### Phase E: API Routes
**Inputs**: API endpoint specifications from backend specs
**Outputs**: FastAPI routes implementing all required endpoints
- Create GET /api/v1/{user_id}/tasks
- Create POST /api/v1/{user_id}/tasks
- Create GET /api/v1/{user_id}/tasks/{id}
- Create PUT /api/v1/{user_id}/tasks/{id}
- Create DELETE /api/v1/{user_id}/tasks/{id}
- Create PATCH /api/v1/{user_id}/tasks/{id}/complete
- Implement request/response validation

**Validation Criteria**:
- All endpoints match specification
- Request/response schemas validated
- Authentication required where specified
- Error responses match specification

### Phase F: Error Handling & Validation
**Inputs**: Error handling specification from backend specs
**Outputs**: Comprehensive error handling, validation, response formatting
- Implement custom exception handlers
- Format error responses per specification
- Add request validation
- Handle all specified error cases
- Implement validation error formatting

**Validation Criteria**:
- All error cases handled correctly
- Response format matches specification
- Validation errors formatted properly
- HTTP status codes match specification

### Phase G: Testing (Unit + API)
**Inputs**: Testing specification from backend specs
**Outputs**: Complete test suite with ≥85% coverage
- Unit tests for service layer
- API integration tests for all endpoints
- Authentication testing
- Database isolation tests
- Coverage validation (≥85%)

**Validation Criteria**:
- Unit test coverage ≥90% for services
- API test coverage ≥85% for routes
- All authentication scenarios tested
- Database isolation verified
- Total coverage ≥85%

## 5. Agent Responsibility Mapping

### architect → System Structure & Dependencies
- Design overall architecture
- Define module boundaries
- Establish dependency graph
- Plan initialization order
- Review component interactions

### backend → Services, Routes, Middleware
- Implement service layer logic
- Create API routes
- Develop middleware components
- Handle business logic implementation
- Ensure proper separation of concerns

### database → Models, Migrations, Indexing
- Create SQLModel definitions
- Implement repository patterns
- Set up Alembic migrations
- Configure database indexes
- Handle relationship definitions

### test → Testing Strategy & Coverage
- Develop unit test suite
- Create API integration tests
- Implement test data factories
- Ensure coverage requirements met
- Validate error handling tests

## 6. Testing Alignment

### Test-First Enforcement Points
- Service layer: Unit tests written before implementation
- API routes: Contract tests defined before endpoints
- Authentication: Security tests defined before middleware
- Error handling: Error scenario tests before implementation

### Test Development Sequence
1. **Phase A**: Basic app startup tests
2. **Phase B**: Model validation and database connection tests
3. **Phase C**: Authentication middleware tests
4. **Phase D**: Service layer unit tests
5. **Phase E**: API integration tests
6. **Phase F**: Error handling tests
7. **Phase G**: Complete coverage validation

### Coverage Checkpoints
- After Phase D: Service layer ≥90% coverage
- After Phase E: API layer ≥85% coverage
- After Phase G: Overall ≥85% coverage

## 7. Constraints & Guards

### Out of Scope
- Frontend development
- Deployment configuration
- Monitoring setup
- Advanced caching layers
- WebSocket implementations
- Third-party integrations
- Admin panel development

### Rules Preventing Over-Engineering
- Maximum 5 basic features (task CRUD + authentication)
- No additional entities beyond User and Task
- No complex business logic beyond specifications
- No microservice architecture (single service)
- No advanced queueing systems
- No complex reporting features

### Constitution Compliance Checks
- All API endpoints under `/api/v1/{user_id}/tasks`
- JWT verification using Better Auth shared secret
- User isolation by user_id enforced everywhere
- SQLModel ORM used for all database operations
- FastAPI async patterns used throughout
- Neon PostgreSQL configuration applied
- Test coverage ≥85% maintained
- Spec-Driven Development followed strictly