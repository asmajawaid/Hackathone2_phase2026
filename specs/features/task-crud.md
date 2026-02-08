# Evolution of Todo - Phase 2 Task CRUD Operations Specification

## Feature Overview
Complete task management system allowing users to create, read, update, delete, and toggle completion status of their todo items.

## User Stories

### US-TASK-01: Add Task
```
As a user
I want to add a new task
So that I can track things I need to do
```

**Acceptance Criteria:**
- [ ] User can click "Add Task" button in dashboard
- [ ] Modal/form appears with glass effect
- [ ] Required field: title (1-200 characters)
- [ ] Optional field: description (max 1000 characters)
- [ ] Client-side validation before submission
- [ ] On success: task appears in list immediately
- [ ] On error: validation message displayed
- [ ] Form clears after successful submission

### US-TASK-02: View Tasks
```
As a user
I want to see all my tasks
So that I know what I need to do
```

**Acceptance Criteria:**
- [ ] Tasks displayed in grid/list on `/dashboard/tasks`
- [ ] Each task shows: title, description (truncated), status, created date
- [ ] Glass card design for each task
- [ ] Completed tasks visually distinct (opacity, strikethrough)
- [ ] Empty state message if no tasks
- [ ] Loading state while fetching
- [ ] Smooth fade-in animation for tasks

### US-TASK-03: Update Task
```
As a user
I want to edit a task
So that I can correct or update information
```

**Acceptance Criteria:**
- [ ] User can click "Edit" button on task card
- [ ] Modal appears pre-filled with current data
- [ ] Can update title and/or description
- [ ] Same validation as create
- [ ] On success: task updates in list immediately
- [ ] On error: validation message displayed
- [ ] Can cancel without saving

### US-TASK-04: Delete Task
```
As a user
I want to delete a task
So that I can remove items I no longer need
```

**Acceptance Criteria:**
- [ ] User can click "Delete" button on task card
- [ ] Confirmation modal appears (prevent accidents)
- [ ] On confirm: task removed from list immediately
- [ ] On cancel: modal closes, no action taken
- [ ] Fade-out animation on deletion
- [ ] Cannot undo (for Phase 2)

### US-TASK-05: Mark Complete/Incomplete
```
As a user
I want to toggle task completion
So that I can track my progress
```

**Acceptance Criteria:**
- [ ] Checkbox or toggle button on task card
- [ ] Click toggles between complete/incomplete
- [ ] Visual feedback: strikethrough, color change, icon
- [ ] Updates immediately (optimistic UI)
- [ ] If API fails, revert to previous state
- [ ] Smooth transition animation

## Technical Requirements

### API Endpoints:
```
GET    /api/{user_id}/tasks           # List all tasks
POST   /api/{user_id}/tasks           # Create task
GET    /api/{user_id}/tasks/{id}      # Get single task
PUT    /api/{user_id}/tasks/{id}      # Update task
DELETE /api/{user_id}/tasks/{id}      # Delete task
PATCH  /api/{user_id}/tasks/{id}/complete  # Toggle completion
```

### Request/Response Schemas:
```typescript
// Create Task Request
{
  title: string;        // required, 1-200 chars
  description?: string; // optional, max 1000 chars
}

// Update Task Request
{
  title?: string;       // optional, 1-200 chars
  description?: string; // optional, max 1000 chars
}

// Task Response
{
  id: number;
  user_id: string;
  title: string;
  description: string | null;
  completed: boolean;
  created_at: string;   // ISO 8601
  updated_at: string;   // ISO 8601
}

// List Tasks Response
{
  success: true;
  data: Task[];
  count: number;
}

// Error Response
{
  success: false;
  error: string;
  code: string;
}
```

## Data Model

### Task Table:
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
```

### SQLModel Definition:
```python
class Task(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: str = Field(foreign_key="users.id", index=True)
    title: str = Field(max_length=200)
    description: Optional[str] = None
    completed: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
```

## Validation Rules
- **Title:**
  - Required
  - Min 1 character
  - Max 200 characters
  - Trim whitespace
  - Cannot be only whitespace

- **Description:**
  - Optional
  - Max 1000 characters
  - Trim whitespace

## Business Rules
1. User can only access their own tasks
2. Task IDs must belong to the authenticated user
3. Deleted tasks cannot be recovered (Phase 2)
4. Updated tasks get new `updated_at` timestamp
5. Completed status is boolean (no partial completion)

## Error Handling

### Validation Errors:
- Empty title: "Title is required"
- Title too long: "Title must be 200 characters or less"
- Description too long: "Description must be 1000 characters or less"

### Authorization Errors:
- Task not found or doesn't belong to user: 404 "Task not found"
- No JWT token: 401 "Authentication required"
- Invalid JWT: 401 "Invalid authentication token"

### Server Errors:
- Database error: 500 "Unable to save task. Please try again."
- Network error: "Connection failed. Please check your internet."

## UI/UX Requirements

### Task Card Design:
- Glass morphism background
- Gradient accent on hover
- Title in large font (text-lg)
- Description truncated to 2 lines with "..."
- Completion checkbox/toggle prominent
- Edit/Delete buttons visible on hover
- Smooth hover scale animation (1.02)
- Shadow elevation on hover

### Add/Edit Form Design:
- Modal with glass background
- Gradient header
- Input fields with glass effect
- Character counter for title/description
- Clear visual feedback for validation errors
- Submit button with gradient
- Cancel button (ghost style)
- Loading spinner on submit

### Empty State:
- Illustration or icon
- Message: "No tasks yet. Create your first task!"
- Prominent "Add Task" button with gradient

### Loading State:
- Skeleton cards with pulse animation
- Or spinner with glass background

## Performance Requirements
- Task list should load in < 1 second
- API responses < 200ms
- Optimistic UI updates (no waiting for API)
- Smooth animations (60fps)