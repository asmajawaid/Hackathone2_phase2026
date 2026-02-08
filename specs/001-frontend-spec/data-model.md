# Data Model: Phase 2 Todo Application Frontend

## Entities

### User
Represents a registered user with authentication credentials and personal data

**Fields**:
- id: string (primary identifier from authentication system)
- email: string (unique, required for login)
- name: string (optional, display name)
- createdAt: timestamp (account creation date)
- updatedAt: timestamp (last update date)

**Validation Rules**:
- Email must be valid format
- Email must be unique
- Name (if provided) must be 1-100 characters

### Task
Represents a todo item with properties like title, description, completion status, creation date, and associated user ID

**Fields**:
- id: number (unique identifier for the task)
- userId: string (foreign key linking to user)
- title: string (required, maximum 200 characters)
- description: string (optional, maximum 1000 characters)
- completed: boolean (default: false)
- createdAt: timestamp (task creation date)
- updatedAt: timestamp (last update date)

**Validation Rules**:
- Title must be 1-200 characters
- Title cannot be only whitespace
- Description (if provided) must be 0-1000 characters
- Completed must be boolean
- userId must correspond to a valid user

### Session
Represents an authenticated user session managed by Better Auth

**Fields**:
- token: string (JWT token for API authentication)
- userId: string (associated user)
- expiresAt: timestamp (session expiration)

**Validation Rules**:
- Token must be valid JWT format
- Session must not be expired
- UserId must correspond to a valid user

## Relationships
- User (1) → (Many) Task (one user can have many tasks)
- Session (1) → (1) User (one session corresponds to one user)

## State Transitions

### Task State Transitions
- Active → Completed (when user marks task as complete)
- Completed → Active (when user unmarks task as complete)

### Session State Transitions
- Unauthenticated → Authenticated (when user signs in)
- Authenticated → Unauthenticated (when user signs out or session expires)