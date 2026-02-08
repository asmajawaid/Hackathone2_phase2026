# Skill: Authentication & JWT Flow

## Purpose
This skill provides structured guidance for implementing secure authentication systems using JWT (JSON Web Tokens), ensuring consistent, secure, and maintainable authentication flows. It helps developers create robust authentication mechanisms that follow industry security standards and best practices.

## Scope
**Included:**
- JWT token generation, validation, and refresh mechanisms
- User authentication and authorization flows
- Password hashing and verification
- Session management and token lifecycle
- Security headers and protection against common attacks
- Role-based access control (RBAC)
- Token expiration and renewal strategies
- Secure storage and transmission of tokens

**Excluded:**
- Specific UI implementation for login/logout forms
- Third-party authentication providers (OAuth, SSO)
- Database schema design for user management
- Password reset email functionality
- Biometric authentication methods
- Hardware security token integration

## Responsibilities
- Implement secure JWT token generation with appropriate claims
- Design token validation and verification mechanisms
- Create secure password hashing and verification processes
- Establish proper token refresh and expiration strategies
- Implement role-based access control for protected resources
- Apply security best practices to prevent common vulnerabilities
- Design error handling for authentication failures
- Ensure secure transmission and storage of authentication data

## Inputs
- User credentials (username/email and password)
- Security requirements and compliance standards
- User role definitions and access control requirements
- Token expiration policies and refresh strategies
- Existing user database schema
- Integration requirements with other services
- Performance and scalability constraints

## Outputs
- Secure JWT-based authentication endpoints
- Token validation and middleware implementations
- User registration and login functionality
- Role-based access control mechanisms
- Secure password management utilities
- Authentication error handling strategies
- Security headers and protection implementations
- Documentation for authentication flows

## Constraints
- Must follow JWT RFC standards and security best practices
- All passwords must be properly hashed using secure algorithms
- Token transmission must use HTTPS in production
- Implementation must protect against common attacks (CSRF, XSS, etc.)
- Token storage must be secure on both client and server
- Must comply with applicable security and privacy regulations
- Authentication flows must be performant and scalable

## Failure Cases
- Weak password hashing algorithms leading to security vulnerabilities
- Improper token validation allowing unauthorized access
- Exposed secrets or hardcoded credentials in code
- Insufficient protection against brute force attacks
- Inadequate session management leading to token hijacking
- Missing validation of token claims causing security bypasses
- Improper error handling revealing sensitive information
- Weak random token generation making tokens predictable

## Usage Context
This skill should be applied during:
- Implementation of user authentication systems
- Design of secure API access patterns
- Creation of role-based permission systems
- Migration from legacy authentication to JWT
- Security review of existing authentication mechanisms
- Integration of authentication with new features
- Compliance review for security requirements

## Update Notes
- v1.0 (2026-01-07): Initial skill definition created for Authentication & JWT Flow, focusing on security best practices, responsibilities, and usage guidelines for the Todo Application project.