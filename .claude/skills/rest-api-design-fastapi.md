# Skill: REST API Design (FastAPI)

## Purpose
This skill provides structured guidance for designing RESTful APIs using FastAPI, ensuring consistency, best practices, and adherence to REST principles. It helps developers create well-architected, maintainable, and scalable APIs that follow industry standards.

## Scope
**Included:**
- REST API endpoint design following HTTP methods and status codes conventions
- Request/response schema design using Pydantic models
- API documentation generation with OpenAPI/Swagger
- Authentication and authorization patterns
- Error handling and response formatting
- API versioning strategies
- Input validation and serialization

**Excluded:**
- Database implementation details
- Frontend integration specifics
- Deployment configurations
- Infrastructure setup
- Specific business logic implementation

## Responsibilities
- Design RESTful endpoints that follow HTTP standards and semantic conventions
- Create appropriate request/response models using Pydantic
- Implement proper HTTP status codes for different scenarios
- Design consistent API naming conventions and URL structures
- Ensure proper input validation and error responses
- Generate comprehensive API documentation
- Apply security best practices for authentication and authorization
- Design API for scalability and performance considerations

## Inputs
- Feature specifications or user stories requiring API endpoints
- Domain models and business requirements
- Security requirements and authentication methods
- Existing API contracts or integration requirements
- Performance and scalability constraints
- Compliance or regulatory requirements

## Outputs
- Well-structured FastAPI route definitions
- Pydantic models for request/response validation
- OpenAPI/Swagger documentation
- API design guidelines and best practices documentation
- Error handling strategies and response formats
- Authentication and authorization implementation patterns
- API testing endpoints and documentation

## Constraints
- Must follow REST architectural principles
- API endpoints must be idempotent where appropriate
- Response times must meet performance requirements
- All endpoints must include proper authentication where required
- Input validation must be comprehensive and secure
- API versioning must be implemented if specified
- Must comply with security best practices

## Failure Cases
- Inconsistent HTTP method usage (e.g., using GET for state-changing operations)
- Improper status code responses leading to client confusion
- Insufficient input validation causing security vulnerabilities
- Poor error message design exposing internal system details
- Missing authentication/authorization checks
- Inadequate API documentation making integration difficult
- Violating REST principles (e.g., not using proper resource naming)

## Usage Context
This skill should be applied during:
- API design phase of new features
- Refactoring existing API endpoints for better consistency
- Creating API specifications before implementation
- Reviewing API designs for best practices compliance
- Training team members on API design standards
- Establishing API design guidelines for the project

## Update Notes
- v1.0 (2026-01-07): Initial skill definition created for REST API Design with FastAPI, focusing on design principles, responsibilities, and usage guidelines for the Todo Application project.