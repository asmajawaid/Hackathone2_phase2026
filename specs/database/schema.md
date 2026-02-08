# Evolution of Todo - Phase 2 Database Schema Documentation

## Database Overview
- **Type:** PostgreSQL 15+
- **Hosting:** Neon Serverless
- **ORM:** SQLModel
- **Migration:** SQLModel metadata (auto-create tables)
- **Connection Pooling:** Enabled

## Connection Configuration
```python
# Backend: db.py
from sqlmodel import create_engine, Session, SQLModel
from typing import Generator
import os

DATABASE_URL = os.getenv("DATABASE_URL")

# Add connection pool settings
engine = create_engine(
    DATABASE_URL,
    echo=True,  # Set to False in production
    pool_size=5,
    max_overflow=10,
    pool_pre_ping=True,  # Verify connections before using
)

def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session

# Create tables
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
```

## Tables

### Table 1: users

**Purpose:** Store user account information (managed by Better Auth)

**Schema:**
```sql
CREATE TABLE users (
    id TEXT PRIMARY KEY,
    email TEXT UNIQUE NOT NULL,
    name TEXT,
    password_hash TEXT NOT NULL,
    email_verified BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE UNIQUE INDEX idx_users_email ON users(email);
```

**SQLModel Definition:**
```python
from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional

class User(SQLModel, table=True):
    __tablename__ = "users"

    id: str = Field(primary_key=True)
    email: str = Field(unique=True, index=True)
    name: Optional[str] = None
    password_hash: str
    email_verified: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
```

**Indexes:**
- Primary key on `id`
- Unique index on `email`

**Constraints:**
- `email` must be unique
- `email` cannot be null
- `password_hash` cannot be null

### Table 2: tasks

**Purpose:** Store todo tasks for all users

**Schema:**
```sql
CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    user_id TEXT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    title VARCHAR(200) NOT NULL,
    description TEXT,
    completed BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);
CREATE INDEX idx_tasks_user_id ON tasks(user_id);
CREATE INDEX idx_tasks_completed ON tasks(completed);
CREATE INDEX idx_tasks_user_completed ON tasks(user_id, completed);
```

**SQLModel Definition:**
```python
from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional

class Task(SQLModel, table=True):
    __tablename__ = "tasks"

    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: str = Field(foreign_key="users.id", index=True)
    title: str = Field(max_length=200)
    description: Optional[str] = None
    completed: bool = Field(default=False, index=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
```

**Indexes:**
- Primary key on `id`
- Index on `user_id` (for filtering by user)
- Index on `completed` (for filtering by status)
- Composite index on `(user_id, completed)` (for common queries)

**Constraints:**
- `user_id` references `users.id`
- `ON DELETE CASCADE` (when user deleted, tasks deleted)
- `title` cannot be null
- `title` max 200 characters

## Relationships
```
users (1) ──────< (many) tasks
│                        │
└─ id                    └─ user_id (FK)
```

**Relationship Rules:**
1. One user can have many tasks
2. Each task belongs to exactly one user
3. When user is deleted, all their tasks are deleted (CASCADE)

## Data Types

| Column | SQL Type | Python Type | Description |
|--------|----------|-------------|-------------|
| id (users) | TEXT | str | UUID or string ID from Better Auth |
| id (tasks) | SERIAL | int | Auto-incrementing integer |
| email | TEXT | str | Email address |
| name | TEXT | Optional[str] | User's display name |
| password_hash | TEXT | str | Hashed password |
| user_id | TEXT | str | Foreign key to users.id |
| title | VARCHAR(200) | str | Task title |
| description | TEXT | Optional[str] | Task details |
| completed | BOOLEAN | bool | Completion status |
| email_verified | BOOLEAN | bool | Email verification status |
| created_at | TIMESTAMP | datetime | Creation timestamp |
| updated_at | TIMESTAMP | datetime | Last update timestamp |

## Sample Data
```sql
-- Sample user
INSERT INTO users (id, email, name, password_hash, email_verified)
VALUES (
    'user_abc123',
    'john@example.com',
    'John Doe',
    '$2b$12$hashedhashed...',
    FALSE
);

-- Sample tasks
INSERT INTO tasks (user_id, title, description, completed)
VALUES
    ('user_abc123', 'Buy groceries', 'Milk, eggs, bread', FALSE),
    ('user_abc123', 'Finish homework', NULL, TRUE),
    ('user_abc123', 'Call mom', 'Wish her happy birthday', FALSE);
```

## Common Queries

**Get all tasks for a user:**
```sql
SELECT * FROM tasks
WHERE user_id = 'user_abc123'
ORDER BY created_at DESC;
```

**Get incomplete tasks for a user:**
```sql
SELECT * FROM tasks
WHERE user_id = 'user_abc123' AND completed = FALSE
ORDER BY created_at DESC;
```

**Toggle task completion:**
```sql
UPDATE tasks
SET completed = NOT completed, updated_at = NOW()
WHERE id = 1 AND user_id = 'user_abc123';
```

**Delete user and all tasks (cascade):**
```sql
DELETE FROM users WHERE id = 'user_abc123';
-- All tasks for this user automatically deleted
```

## Performance Considerations

**Indexes:**
- `idx_tasks_user_id`: Speeds up "get all user tasks" queries
- `idx_tasks_completed`: Speeds up "filter by completion status"
- `idx_tasks_user_completed`: Composite index for combined queries

**Query Optimization:**
- Always filter by `user_id` first (indexed)
- Use `completed` index for status filters
- Avoid SELECT * in production (specify columns)

## Migration Strategy

**Phase 2 (Simple):**
```python
# On app startup:
from db import create_db_and_tables

@app.on_event("startup")
def on_startup():
    create_db_and_tables()
```

**Future Phases (Alembic):**
- Use Alembic for migrations
- Version control schema changes
- Safe production migrations

## Backup & Recovery
- Neon handles automatic backups
- Point-in-time recovery available
- Export data via pg_dump if needed

## Security

**Best Practices:**
- Never store plain-text passwords
- Use parameterized queries (ORM handles this)
- Limit database user permissions
- Use SSL for connections (Neon enforces)

**Environment Variables:**
DATABASE_URL=postgresql://user:pass@host.neon.tech/dbname?sslmode=require