# Skill: Database Modeling (SQLModel + Neon)

## Purpose
This skill provides structured guidance for designing and implementing database schemas using SQLModel and Neon, ensuring consistency, performance, and maintainability. It helps developers create well-architected data models that follow best practices for relational databases and modern cloud database platforms.

## Scope
**Included:**
- Entity relationship modeling and design
- SQLModel class definitions and schema generation
- Database connection and session management
- Migration strategies and versioning
- Indexing and performance optimization
- Data validation and constraints
- Neon-specific configuration and optimization
- Relationship mapping (one-to-many, many-to-many, etc.)

**Excluded:**
- Business logic implementation
- API endpoint creation
- Frontend data handling
- Deployment scripts
- Specific application workflow implementation
- Database backup and recovery procedures

## Responsibilities
- Design normalized database schemas that follow relational database principles
- Create SQLModel classes that accurately represent business entities
- Define appropriate relationships between entities (foreign keys, constraints)
- Implement proper indexing strategies for performance optimization
- Ensure data integrity through validation and constraints
- Design migration strategies for schema evolution
- Optimize queries and database interactions for performance
- Configure Neon-specific settings for optimal performance and security

## Inputs
- Domain models and business requirements
- Entity relationship diagrams or specifications
- Performance requirements and expected data volumes
- Security and compliance requirements
- Existing database schemas (for migrations)
- Integration requirements with other systems
- Data access patterns and query requirements

## Outputs
- SQLModel class definitions representing database tables
- Database schema diagrams and documentation
- Migration scripts for schema changes
- Index and performance optimization recommendations
- Connection and session management patterns
- Data validation and constraint definitions
- Neon configuration recommendations
- Database performance benchmarks and optimization reports

## Constraints
- Must follow SQL standards and relational database best practices
- Schema changes must maintain backward compatibility where possible
- Database queries must meet performance requirements
- All data must be properly validated before storage
- Database connections must be properly managed and secured
- Migration strategies must support rollback capabilities
- Must comply with Neon's specific limitations and features

## Failure Cases
- Poor normalization leading to data redundancy or inconsistency
- Missing or inappropriate indexes causing performance issues
- Improper relationship constraints leading to data integrity problems
- Inadequate validation allowing invalid data into the database
- Poor migration strategies causing data loss or downtime
- Unoptimized queries causing performance bottlenecks
- Security vulnerabilities in database access patterns
- Violation of Neon's connection or performance limits

## Usage Context
This skill should be applied during:
- Initial database schema design for new features
- Refactoring existing database models for better performance
- Creating data models from business requirements
- Reviewing database designs for best practices compliance
- Planning database migrations for schema changes
- Optimizing existing database schemas for performance
- Setting up Neon database configurations for new projects

## Update Notes
- v1.0 (2026-01-07): Initial skill definition created for Database Modeling with SQLModel and Neon, focusing on design principles, responsibilities, and usage guidelines for the Todo Application project.