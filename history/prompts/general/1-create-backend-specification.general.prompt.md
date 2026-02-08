---
id: 1
title: Create Backend Specification
stage: spec
date: 2026-01-26
surface: agent
model: claude-opus-4-5-20251101
feature: backend
branch: master
user: user
command: /sp.specify
labels: [backend, specification, fastapi, sqlmodel, auth]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - specs/backend-specification.md
tests:
  - none
---

## Prompt

/sp.specify

Context:
You are operating under a strict Spec-Driven Development (SDD) constitution.
This project is "Evolution of Todo – Phase 2 Full-Stack Web Application".
Phase 1 is archived. We are now defining Phase 2 BACKEND specifications only.

Authoritative document:
- constitution.md v1.1.0 (Full-Stack Web App Constitution)

MANDATORY RULES:
- NO implementation
- NO code
- NO assumptions outside constitution
- Specs must be implementation-ready for FastAPI + SQLModel
- Use small, verifiable chunks
- Backend-first
- JWT authentication via Better Auth bridge
- User isolation by user_id is mandatory

Objective:
Generate backend specifications ONLY for Phase 2, broken into clear, structured spec chunks suitable for SpecKit Plus and Claude Code execution.

Scope (Backend ONLY):
- FastAPI application architecture
- Authentication & JWT verification
- Task CRUD API
- Database schema (SQLModel)
- Dependency injection
- Middleware
- Error handling
- Testing specifications

Technology Constraints (must follow exactly):
- Python 3.12+
- FastAPI (async)
- SQLModel ORM
- Neon PostgreSQL
- Alembic migrations
- Better Auth JWT verification
- REST API under /api/v1/
- pytest + httpx for testing

--------------------------------------------------
SPEC CHUNK STRUCTURE REQUIRED
--------------------------------------------------

Produce specs in the following chunks (IN ORDER):

### 1. Backend System Overview Spec
- Responsibilities of backend
- API boundaries
- Trust boundaries (auth, frontend, DB)
- High-level request flow

### 2. Authentication & Authorization Spec
- JWT verification process
- Better Auth shared secret usage
- Token expiry rules
- User isolation enforcement
- Middleware behavior
- Error responses for auth failures

### 3. Database Specification
- SQLModel models
- Field constraints
- Enums (status, priority)
- Indexing rules
- Foreign key behavior
- Migration strategy (Alembic)
- Neon-specific considerations

### 4. API Endpoint Specifications
For each endpoint define:
- Method & path
- Auth requirement
- Request schema
- Response schema
- Validation rules
- Error cases
- Ownership checks

Endpoints required:
- GET /api/v1/{user_id}/tasks
- POST /api/v1/{user_id}/tasks
- GET /api/v1/{user_id}/tasks/{id}
- PUT /api/v1/{user_id}/tasks/{id}
- DELETE /api/v1/{user_id}/tasks/{id}
- PATCH /api/v1/{user_id}/tasks/{id}/complete

### 5. Service Layer Specification
- Separation of concerns
- Task service responsibilities
- Transaction handling
- Async behavior

### 6. Error Handling Specification
- Standard error response format
- HTTP status code mapping
- Validation errors
- Auth errors
- Database errors

### 7. Middleware Specification
- Auth middleware
- CORS handling
- Logging
- Request lifecycle

### 8. Testing Specification (Backend)
- Unit tests
- API integration tests
- Auth mocking strategy
- Database test isolation
- Coverage requirements (≥85%)

--------------------------------------------------
AGENT & SKILL USAGE
--------------------------------------------------

Explicitly tag which agent would ow

## Response snapshot

I've created a comprehensive backend specification for the Phase 2 Full-Stack Web Application following the required structure. The specification includes all 8 required sections:

1. Backend System Overview Spec
2. Authentication & Authorization Spec
3. Database Specification
4. API Endpoint Specifications (covering all 6 required endpoints)
5. Service Layer Specification
6. Error Handling Specification
7. Middleware Specification
8. Testing Specification (Backend)

The specification adheres to all the technology constraints (Python 3.12+, FastAPI, SQLModel, Neon PostgreSQL, Alembic, Better Auth JWT verification, REST API under /api/v1/, pytest + httpx) and focuses exclusively on backend functionality as required. All user isolation requirements by user_id are incorporated, and the JWT authentication via Better Auth bridge is properly specified.

## Outcome

- ✅ Impact: Complete backend specification document created with all required sections
- 🧪 Tests: Testing specification included with ≥85% coverage requirements
- 📁 Files: specs/backend-specification.md created
- 🔁 Next prompts: Ready for planning phase (/sp.plan)
- 🧠 Reflection: Specification follows SDD methodology and is implementation-ready

## Evaluation notes (flywheel)

- Success: All required specification sections completed according to constitution
- Success: Technology constraints properly applied throughout
- Success: User isolation and authentication requirements clearly specified
- Success: API endpoints fully specified with request/response schemas
- Success: Error handling and middleware specifications comprehensive
- Success: Testing requirements meet coverage targets