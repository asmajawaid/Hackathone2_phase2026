# Evolution of Todo - Phase 2 Authentication Feature Specification

## Feature Overview
User authentication system using Better Auth with JWT tokens for secure access to the todo application.

## User Stories

### US-AUTH-01: User Signup
```
As a new user
I want to create an account
So that I can manage my personal todo list
```

**Acceptance Criteria:**
- [ ] User can access signup page at `/signup`
- [ ] Form requires: email, password, name (optional)
- [ ] Email validation (valid format)
- [ ] Password requirements: min 8 characters, 1 uppercase, 1 number, 1 special char
- [ ] Show validation errors inline
- [ ] On success: auto-login and redirect to `/dashboard/tasks`
- [ ] On error: clear error message displayed
- [ ] Prevent duplicate email registration

### US-AUTH-02: User Signin
```
As a registered user
I want to sign in to my account
So that I can access my todo list
```

**Acceptance Criteria:**
- [ ] User can access signin page at `/signin`
- [ ] Form requires: email, password
- [ ] Show validation errors inline
- [ ] On success: redirect to `/dashboard/tasks`
- [ ] On error: "Invalid credentials" message (don't specify which field)
- [ ] Remember me option (optional for Phase 2)

### US-AUTH-03: Session Management
```
As a signed-in user
I want my session to persist
So that I don't have to login repeatedly
```

**Acceptance Criteria:**
- [ ] JWT token stored securely (httpOnly cookie preferred)
- [ ] Token expiry: 7 days
- [ ] Auto-logout on token expiry
- [ ] Protected routes redirect to `/signin` if not authenticated
- [ ] Token refresh mechanism (optional for Phase 2)

### US-AUTH-04: Logout
```
As a signed-in user
I want to logout
So that I can secure my account
```

**Acceptance Criteria:**
- [ ] Logout button visible in dashboard
- [ ] On logout: clear JWT token
- [ ] Redirect to `/signin`
- [ ] Cannot access protected routes after logout

## Technical Requirements

### Better Auth Configuration:
```typescript
// Frontend: lib/auth.ts
{
  providers: [
    emailProvider({
      sendVerificationEmail: false // Simplify for Phase 2
    })
  ],
  plugins: [
    jwtPlugin({
      secret: process.env.BETTER_AUTH_SECRET,
      expiresIn: "7d"
    })
  ],
  database: {
    type: "postgres",
    url: process.env.DATABASE_URL
  }
}
```

### Backend JWT Verification:
```python
# Backend: middleware/auth.py
from jose import jwt, JWTError
from fastapi import HTTPException, Header

async def verify_jwt(authorization: str = Header(...)):
    try:
        token = authorization.replace("Bearer ", "")
        payload = jwt.decode(
            token,
            settings.BETTER_AUTH_SECRET,
            algorithms=["HS256"]
        )
        return payload["user_id"]
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
```

## Data Models

### User Table (Better Auth managed):
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
```

## Validation Rules
- Email: RFC 5322 compliant
- Password: Min 8 chars, 1 uppercase, 1 number, 1 special
- Name: Optional, max 100 characters

## Error Handling
- Invalid email format: "Please enter a valid email"
- Weak password: "Password must be at least 8 characters with 1 uppercase, 1 number, and 1 special character"
- Email exists: "An account with this email already exists"
- Invalid credentials: "Invalid email or password"
- Token expired: Auto-redirect to signin
- Network error: "Unable to connect. Please try again."

## Security Requirements
- Passwords hashed with bcrypt (Better Auth handles)
- JWT tokens signed with HS256
- Shared secret stored in environment variables
- HTTPS enforced in production
- Rate limiting on auth endpoints (optional for Phase 2)

## UI/UX Requirements
- Glass morphism design on auth pages
- Gradient background
- Smooth transitions between fields
- Loading states during submission
- Success/error feedback
- Password visibility toggle
- Link between signup/signin pages