# Evolution of Todo - Phase 2 Full-Stack Web Application Constitution

## Document Version Control
- **Version**: 2.0.0
- **Original Release**: 1.0.0 (Terminal MVP)
- **Previous Version**: 1.1.0 (Enhanced Full-Stack Web App)
- **Current Version**: 2.0.0 (Complete Phase 2 Constitution)
- **Amendment Date**: January 28, 2026
- **Phase Transition**: From Terminal-Based MVP to Complete Full-Stack Web Application with Authentication

## Table of Contents
1. [Document Version Control](#document-version-control)
2. [Table of Contents](#table-of-contents)
3. [Introduction](#introduction)
4. [Section 1: Project Identity & Vision](#section-1-project-identity--vision)
5. [Section 2: Core Principles (Non-Negotiable)](#section-2-core-principles-non-negotiable)
6. [Section 3: Phase 2 Architecture Specification](#section-3-phase-2-architecture-specification)
7. [Section 4: Design System Specification](#section-4-design-system-specification)
8. [Section 5: Development Workflow (SDD Methodology)](#section-5-development-workflow-sdd-methodology)
9. [Section 6: Deliverables & Quality Gates](#section-6-deliverables--quality-gates)
10. [Section 7: Manual Setup Requirements](#section-7-manual-setup-requirements)
11. [Section 8: Enforcement & Governance](#section-8-enforcement--governance)
12. [Section 9: Reference & Resources](#section-9-reference--resources)
13. [Section 10: Success Checklist](#section-10-success-checklist)
14. [Version History](#version-history)
15. [Conclusion](#conclusion)

## Introduction

This constitution governs the Evolution of Todo project as it transitions from Phase 1 (Terminal-based MVP) to Phase 2 (Full-Stack Web Application with Authentication). The project follows Spec-Driven Development (SDD) methodology using Claude Code and Spec-Kit Plus with a technology stack of Next.js 16+, FastAPI, SQLModel, Neon PostgreSQL, and Better Auth.

All development activities must comply with the principles and specifications outlined in this document. This constitution supersedes all other development practices and methodologies.

## Section 1: Project Identity & Vision

### Project Identity
- **Project Name:** Evolution of Todo - Phase 2 Full-Stack Web Application
- **Development Methodology:** Spec-Driven Development (SDD) using Claude Code and Spec-Kit Plus
- **Tech Stack:** Next.js 16+ (App Router), FastAPI, SQLModel, Neon PostgreSQL, Better Auth, Tailwind CSS

### Vision Statement
Transform from Phase 1 console app to modern multi-user web application with secure authentication, responsive design, and intuitive user experience that scales to support multiple concurrent users.

### Success Criteria
The project will be deemed successful when:
- All 5 basic features (Add, View, Update, Delete, Mark Complete) work as a web application with authentication
- Multiple users can use the application simultaneously with isolated data
- The application meets all design system requirements (latte color palette, glass morphism, gradients)
- All automated tests pass with 80%+ coverage on backend
- The application is successfully deployed and accessible online

### Target Users
- Multiple concurrent users with isolated data
- Users seeking a modern, aesthetically pleasing task management solution
- Users who want secure, authenticated access to their personal tasks

### Timeline
Phase 2 completion deadline: As specified in the hackathon requirements

## Section 2: Core Principles (Non-Negotiable)

### Principle I: Spec-Driven Development (MANDATORY)
All development MUST follow SDD methodology:
- Specs written first → refined → then code generated from specs
- NO manual coding allowed - refine specs until Claude generates correct output
- Implementation only after spec approval
- Code generation strictly via Claude Code

### Principle II: Agentic Development Stack
Use AI agents for all development tasks following this workflow:
- Read constitution.md and speckit.specify → Create speckit.plan → Break into speckit.tasks → Generate code → Test → Update specs (NOT code) if issues
- All agents must follow this constitution
- Agent skills and subagents usage encouraged

### Principle III: Test-First Development (MANDATORY)
TDD strictly enforced for Phase 2:
- Phase 2 Testing Requirements:
  * Frontend: Jest + React Testing Library for components
  * Backend: pytest with minimum 80% coverage
  * API: Endpoint testing with proper mocking
  * E2E: Critical user flows (signup, signin, task CRUD)
- Test workflow: Write tests → User approval → Tests fail → Implement → Tests pass
- Red-Green-Refactor cycle

### Principle IV: Minimal Viable Implementation
Focus on smallest viable change meeting requirements. Phase 2 specific constraints:
- Implement ONLY 5 basic features (no intermediate/advanced features)
- Clean architecture with proper separation (frontend/backend)
- Reusable components following design system
- No over-engineering

### Principle V: Technical Constraints Compliance
Must adhere to:
- **Frontend:** Next.js 16+ (App Router), TypeScript 5.x, React 18+, Tailwind CSS
- **Backend:** FastAPI, Python 3.12+, SQLModel ORM
- **Database:** Neon Serverless PostgreSQL
- **Authentication:** Better Auth with JWT tokens
- **Styling:** Tailwind CSS with custom latte color palette, glass morphism, gradients
- **Package Manager:** npm for frontend, uv for backend
- **Deployment:** Vercel for frontend, backend hosting TBD

## Section 3: Phase 2 Architecture Specification

### 3.1 Project Structure (Monorepo)
```
hackathon-todo/
├── .spec-kit/
│   └── config.yaml
├── specs/
│   ├── overview.md
│   ├── architecture.md
│   ├── features/
│   │   ├── authentication.md
│   │   └── task-crud.md
│   ├── api/
│   │   └── rest-endpoints.md
│   ├── database/
│   │   └── schema.md
│   ├── ui/
│   │   ├── design-system.md
│   │   ├── components.md
│   │   └── pages.md
│   ├── plan.md
│   └── tasks.md
├── frontend/
│   ├── app/
│   │   ├── layout.tsx
│   │   ├── page.tsx
│   │   ├── signin/
│   │   ├── signup/
│   │   └── dashboard/
│   │       └── tasks/
│   ├── components/
│   │   ├── ui/
│   │   └── tasks/
│   ├── lib/
│   ├── public/
│   ├── styles/
│   ├── types/
│   ├── .env.local
│   ├── next.config.js
│   ├── package.json
│   └── tailwind.config.ts
├── backend/
│   ├── main.py
│   ├── models.py
│   ├── routes/
│   ├── middleware/
│   ├── db.py
│   ├── auth.py
│   ├── .env
│   ├── requirements.txt
│   └── tests/
├── .env
├── .gitignore
├── README.md
├── CLAUDE.md
├── AGENTS.md
└── constitution.md
```

### 3.2 Frontend Architecture

**Technology Stack:**
- Next.js 16+ with App Router (server components by default)
- TypeScript for type safety
- Tailwind CSS for styling
- Better Auth for authentication
- Fetch API / axios for backend communication

**Routing Structure:**
- `/` - Landing page (public)
- `/signin` - Sign in page (public)
- `/signup` - Sign up page (public)
- `/dashboard` - Main dashboard (protected)
- `/dashboard/tasks` - Task management (protected)

**Component Architecture:**
- Server Components: Default for all pages
- Client Components: Only for interactivity (forms, buttons, modals)
- Shared UI components in `/components/ui`
- Feature-specific components in `/components/tasks`

**State Management:**
- Server state: React Server Components
- Client state: React hooks (useState, useReducer)
- Form state: Controlled components
- NO global state library needed for Phase 2

### 3.3 Backend Architecture

**Technology Stack:**
- FastAPI framework
- SQLModel for ORM (combines SQLAlchemy + Pydantic)
- Pydantic for request/response validation
- python-jose for JWT handling
- psycopg2 for PostgreSQL driver

**API Structure:**
- Base path: `/api`
- User-scoped endpoints: `/api/{user_id}/tasks`
- All endpoints require JWT authentication
- RESTful conventions followed

**Middleware:**
- CORS middleware (allow frontend origin)
- JWT verification middleware
- Request logging middleware
- Error handling middleware

**Database Layer:**
- SQLModel models in `models.py`
- Database session management in `db.py`
- Connection pooling enabled
- Migrations handled via SQLModel metadata

### 3.4 Database Schema

**Users Table (managed by Better Auth):**
```sql
CREATE TABLE users (
    id TEXT PRIMARY KEY,
    email TEXT UNIQUE NOT NULL,
    name TEXT,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);
```

**Tasks Table:**
```sql
CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    user_id TEXT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    title VARCHAR(200) NOT NULL,
    description TEXT,
    completed BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    INDEX idx_user_id (user_id),
    INDEX idx_completed (completed)
);
```

### 3.5 API Specification

**Authentication Flow:**
1. User signs up via Better Auth → JWT issued
2. Frontend stores JWT (httpOnly cookie preferred)
3. Every API request includes JWT in Authorization header
4. Backend verifies JWT, extracts user_id
5. Backend filters all data by authenticated user_id

**REST Endpoints:**

| Method | Endpoint | Description | Request Body | Response |
|--------|----------|-------------|--------------|----------|
| GET | `/api/{user_id}/tasks` | List all user's tasks | None | `{ tasks: Task[] }` |
| POST | `/api/{user_id}/tasks` | Create new task | `{ title, description? }` | `{ task: Task }` |
| GET | `/api/{user_id}/tasks/{id}` | Get single task | None | `{ task: Task }` |
| PUT | `/api/{user_id}/tasks/{id}` | Update task | `{ title?, description? }` | `{ task: Task }` |
| DELETE | `/api/{user_id}/tasks/{id}` | Delete task | None | `{ success: true }` |
| PATCH | `/api/{user_id}/tasks/{id}/complete` | Toggle completion | None | `{ task: Task }` |

**Request Headers:**
```
Authorization: Bearer <jwt_token>
Content-Type: application/json
```

**Response Format:**
```json
{
  "success": true,
  "data": {...},
  "message": "Operation successful"
}
```

**Error Response:**
```json
{
  "success": false,
  "error": "Error description",
  "code": "ERROR_CODE"
}
```

### 3.6 Authentication Architecture (Better Auth + FastAPI)

**Challenge:** Better Auth runs on Next.js (JavaScript), Backend is FastAPI (Python)

**Solution:** JWT Token Bridge

**Flow:**
1. User logs in → Better Auth creates session + issues JWT
2. JWT stored as httpOnly cookie or localStorage
3. Frontend attaches JWT to every API request header
4. Backend extracts JWT, verifies signature with shared secret
5. Backend decodes JWT to get user_id
6. Backend validates user_id matches URL parameter
7. Backend filters all queries by authenticated user

**Shared Secret:**
- Environment variable: `BETTER_AUTH_SECRET`
- Must be identical in frontend and backend
- Used for JWT signing (frontend) and verification (backend)

**Security Requirements:**
- All API endpoints require valid JWT (except health checks)
- JWT expiry: 7 days (configurable)
- Token refresh mechanism implemented
- HTTPS enforced in production
- User data strictly isolated by user_id

## Section 4: Design System Specification

### 4.1 Color Palette (Latte Theme - Catppuccin Inspired)

**Base Colors:**
```typescript
latte: {
  // Backgrounds
  base: '#eff1f5',      // Main background
  mantle: '#e6e9ef',    // Secondary background
  crust: '#dce0e8',     // Tertiary background

  // Text
  text: '#4c4f69',      // Primary text
  subtext1: '#5c5f77',  // Secondary text
  subtext0: '#6c6f85',  // Tertiary text

  // Surfaces
  surface0: '#ccd0da',  // Raised elements
  surface1: '#bcc0cc',  // Hover states
  surface2: '#acb0be',  // Pressed states

  // Overlays
  overlay0: '#9ca0b0',  // Dividers
  overlay1: '#8c8fa1',  // Borders
  overlay2: '#7c7f93',  // Strong borders

  // Accents (vibrant)
  lavender: '#7287fd',
  blue: '#1e66f5',
  sapphire: '#209fb5',
  sky: '#04a5e5',
  teal: '#179299',
  green: '#40a02b',
  yellow: '#df8e1d',
  peach: '#fe640b',
  maroon: '#e64553',
  red: '#d20f39',
  mauve: '#8839ef',
  pink: '#ea76cb',
  flamingo: '#dd7878',
  rosewater: '#dc8a78',
}
```

**Usage Guidelines:**
- `base` - Main page background
- `mantle` - Card backgrounds
- `crust` - Input backgrounds
- `text` - All primary text
- `blue` - Primary actions (buttons, links)
- `green` - Success states
- `red` - Errors/destructive actions
- `lavender` - Highlights, active states

### 4.2 Glass Morphism Effects

**Standard Glass Card:**
```css
.glass-card {
  background: rgba(255, 255, 255, 0.4);
  backdrop-filter: blur(12px);
  border: 1px solid rgba(204, 208, 218, 0.5);
  box-shadow: 0 8px 32px 0 rgba(124, 127, 147, 0.2);
}
```

**Hover Enhancement:**
```css
.glass-card:hover {
  background: rgba(255, 255, 255, 0.5);
  border: 1px solid rgba(204, 208, 218, 0.7);
  box-shadow: 0 8px 32px 0 rgba(124, 127, 147, 0.3);
  transform: translateY(-2px);
}
```

**Implementation in Tailwind:**
```typescript
// Add to tailwind.config.ts
backdropBlur: {
  xs: '2px',
  sm: '4px',
  DEFAULT: '8px',
  md: '12px',
  lg: '16px',
  xl: '24px',
}
```

### 4.3 Gradient Specifications

**Gradient Presets:**
```typescript
backgroundImage: {
  'gradient-lavender': 'linear-gradient(135deg, #7287fd 0%, #8839ef 100%)',
  'gradient-ocean': 'linear-gradient(135deg, #1e66f5 0%, #04a5e5 100%)',
  'gradient-sunset': 'linear-gradient(135deg, #fe640b 0%, #dc8a78 100%)',
  'gradient-forest': 'linear-gradient(135deg, #40a02b 0%, #179299 100%)',
  'gradient-glass': 'linear-gradient(135deg, rgba(255,255,255,0.4), rgba(255,255,255,0.1))',
}
```

**Usage Guidelines:**
- `gradient-lavender` - Primary CTAs, headers
- `gradient-ocean` - Info states, navigation
- `gradient-sunset` - Warm accents, highlights
- `gradient-forest` - Success states
- `gradient-glass` - Subtle overlays on glass cards

### 4.4 Responsive Design Breakpoints
```typescript
screens: {
  'xs': '475px',
  'sm': '640px',
  'md': '768px',
  'lg': '1024px',
  'xl': '1280px',
  '2xl': '1536px',
}
```

**Mobile-First Approach:**
- Design for mobile first (xs-sm)
- Progressively enhance for tablet (md)
- Optimize for desktop (lg-xl)
- Consider ultra-wide displays (2xl)

### 4.5 Typography Scale
```typescript
fontSize: {
  'xs': ['0.75rem', { lineHeight: '1rem' }],
  'sm': ['0.875rem', { lineHeight: '1.25rem' }],
  'base': ['1rem', { lineHeight: '1.5rem' }],
  'lg': ['1.125rem', { lineHeight: '1.75rem' }],
  'xl': ['1.25rem', { lineHeight: '1.75rem' }],
  '2xl': ['1.5rem', { lineHeight: '2rem' }],
  '3xl': ['1.875rem', { lineHeight: '2.25rem' }],
  '4xl': ['2.25rem', { lineHeight: '2.5rem' }],
}
```

### 4.6 Component Design Patterns

**Glass Card Component:**
```tsx
<div className="
  bg-latte-base/40
  backdrop-blur-md
  rounded-2xl
  border border-latte-surface0/50
  shadow-lg shadow-latte-overlay0/20
  hover:shadow-xl hover:shadow-latte-overlay0/30
  transition-all duration-300
  hover:-translate-y-1
">
  {/* Content */}
</div>
```

**Gradient Button:**
```tsx
<button className="
  bg-gradient-lavender
  text-white
  px-6 py-3
  rounded-lg
  font-semibold
  shadow-lg shadow-latte-lavender/30
  hover:shadow-xl hover:shadow-latte-lavender/50
  transform transition-all duration-200
  hover:scale-105
  active:scale-95
">
  Click Me
</button>
```

**Animated Input (Glass):**
```tsx
<input className="
  bg-latte-crust/60
  backdrop-blur-sm
  border border-latte-surface0/50
  rounded-lg
  px-4 py-2
  text-latte-text
  placeholder:text-latte-subtext1
  focus:outline-none
  focus:ring-2
  focus:ring-latte-blue/50
  focus:border-transparent
  transition-all duration-200
" />
```

### 4.7 Animation & Transitions

**Micro-interactions:**
- Button hover: scale(1.05), duration 200ms
- Card hover: translateY(-4px), duration 300ms
- Input focus: border color + ring, duration 200ms
- Loading states: pulse animation
- Success feedback: scale bounce

**Easing Functions:**
```typescript
transitionTimingFunction: {
  'smooth': 'cubic-bezier(0.4, 0, 0.2, 1)',
  'bounce': 'cubic-bezier(0.68, -0.55, 0.265, 1.55)',
}
```

### 4.8 Accessibility Requirements

**WCAG 2.1 AA Compliance:**
- Color contrast ratio: minimum 4.5:1 for text
- Focus indicators: visible on all interactive elements
- Keyboard navigation: full support
- ARIA labels: on all interactive components
- Screen reader: semantic HTML

**Implementation Checklist:**
- [ ] All buttons have accessible names
- [ ] Form inputs have associated labels
- [ ] Error messages linked to inputs
- [ ] Focus visible on tab navigation
- [ ] Color not sole means of conveying information

## Section 5: Development Workflow (SDD Methodology)

### 5.1 Workflow Overview
```
┌─────────────────────────────────────────────────────────────────┐
│                    SDD WORKFLOW                                 │
├─────────────────────────────────────────────────────────────────┤
│  1. Discovery: Read constitution.md + speckit.specify          │
│  2. Planning: Generate speckit.plan with architecture breakdown│
│  3. Task Creation: Break into speckit.tasks (frontend+backend) │
│  4. Implementation: Claude Code executes tasks                 │
│  5. Testing: Run test suites (Jest, pytest)                    │
│  6. Review: Validate against constitution                       │
│  7. Iterate: Refine based on feedback                          │
└─────────────────────────────────────────────────────────────────┘
```

### 5.2 Phase 2 Specific Workflow

**Step 1: Specification Phase**

Create the following spec files:

1. **specs/overview.md**
   - Project purpose
   - Phase 2 goals
   - Success criteria
   - Tech stack overview

2. **specs/architecture.md**
   - System architecture diagram
   - Component relationships
   - Data flow
   - Authentication flow

3. **specs/features/authentication.md**
   - User stories for signup/signin
   - Acceptance criteria
   - JWT flow specification
   - Security requirements

4. **specs/features/task-crud.md**
   - User stories for 5 basic features
   - Acceptance criteria for each
   - Data validation rules
   - Error handling

5. **specs/api/rest-endpoints.md**
   - Complete API documentation
   - Request/response schemas
   - Error codes
   - Authentication requirements

6. **specs/database/schema.md**
   - Table definitions
   - Relationships
   - Indexes
   - Constraints

7. **specs/ui/design-system.md**
   - Color palette
   - Component specifications
   - Layout patterns
   - Responsive behavior

8. **specs/ui/components.md**
   - Component list
   - Props specifications
   - State management
   - Composition patterns

9. **specs/ui/pages.md**
   - Page layouts
   - Navigation flow
   - Protected routes
   - Loading states

**Step 2: Planning Phase**

Generate **speckit.plan** covering:
```markdown
# Phase 2 Technical Plan

## 1. Backend Architecture
- FastAPI application structure
- SQLModel models design
- JWT verification strategy
- API endpoint implementation order
- Error handling approach
- Testing strategy

## 2. Frontend Architecture
- Next.js App Router structure
- Component hierarchy
- Authentication flow
- API client design
- State management approach
- Routing strategy

## 3. Database Design
- Table structures
- Relationship definitions
- Index strategy
- Migration approach

## 4. Authentication Integration
- Better Auth configuration
- JWT token flow
- Frontend-backend communication
- Session management

## 5. Deployment Strategy
- Frontend: Vercel deployment
- Backend: Hosting solution
- Environment variables
- Database connection

## 6. Testing Strategy
- Unit tests (frontend + backend)
- Integration tests (API)
- E2E tests (critical flows)
- Test coverage targets

## 7. Implementation Order
Priority-ordered list of implementation phases
```

**Step 3: Task Breakdown Phase**

Generate **speckit.tasks** with atomic tasks:
```markdown
# Phase 2 Implementation Tasks

## BACKEND TASKS

### Setup & Configuration
- [ ] T-B01: Initialize FastAPI project with uv
- [ ] T-B02: Configure environment variables
- [ ] T-B03: Setup CORS middleware
- [ ] T-B04: Create project structure

### Database Layer
- [ ] T-B05: Create SQLModel User model
- [ ] T-B06: Create SQLModel Task model
- [ ] T-B07: Setup Neon database connection
- [ ] T-B08: Implement database session management

### Authentication
- [ ] T-B09: Install python-jose for JWT
- [ ] T-B10: Create JWT verification function
- [ ] T-B11: Create authentication middleware
- [ ] T-B12: Add auth dependency to routes

### API Endpoints
- [ ] T-B13: Create GET /api/{user_id}/tasks (list)
- [ ] T-B14: Create POST /api/{user_id}/tasks (create)
- [ ] T-B15: Create GET /api/{user_id}/tasks/{id} (get one)
- [ ] T-B16: Create PUT /api/{user_id}/tasks/{id} (update)
- [ ] T-B17: Create DELETE /api/{user_id}/tasks/{id} (delete)
- [ ] T-B18: Create PATCH /api/{user_id}/tasks/{id}/complete (toggle)

### Testing
- [ ] T-B19: Write pytest tests for auth middleware
- [ ] T-B20: Write pytest tests for task endpoints
- [ ] T-B21: Setup test database
- [ ] T-B22: Achieve 80%+ test coverage

## FRONTEND TASKS

### Setup & Configuration
- [ ] T-F01: Initialize Next.js 16 with TypeScript
- [ ] T-F02: Configure Tailwind CSS with latte theme
- [ ] T-F03: Setup project structure
- [ ] T-F04: Configure environment variables

### Design System
- [ ] T-F05: Create tailwind.config.ts with latte colors
- [ ] T-F06: Add glass morphism utilities
- [ ] T-F07: Add gradient utilities
- [ ] T-F08: Create base CSS animations

### UI Components
- [ ] T-F09: Create GlassCard component
- [ ] T-F10: Create Button component (with variants)
- [ ] T-F11: Create Input component (with validation)
- [ ] T-F12: Create Modal component
- [ ] T-F13: Create Loading component

### Authentication
- [ ] T-F14: Install and configure Better Auth
- [ ] T-F15: Create signup page with glass design
- [ ] T-F16: Create signin page with glass design
- [ ] T-F17: Implement JWT storage
- [ ] T-F18: Create protected route wrapper

### API Client
- [ ] T-F19: Create API client with JWT injection
- [ ] T-F20: Add error handling to API client
- [ ] T-F21: Create TypeScript types for API responses

### Task Features
- [ ] T-F22: Create TaskList component
- [ ] T-F23: Create TaskCard component (glass design)
- [ ] T-F24: Create AddTaskForm component
- [ ] T-F25: Create EditTaskModal component
- [ ] T-F26: Create DeleteConfirmation component
- [ ] T-F27: Implement task completion toggle

### Pages
- [ ] T-F28: Create landing page with gradient hero
- [ ] T-F29: Create dashboard layout
- [ ] T-F30: Create tasks page with CRUD operations
- [ ] T-F31: Add loading states to all pages
- [ ] T-F32: Add error boundaries

### Testing
- [ ] T-F33: Setup Jest and React Testing Library
- [ ] T-F34: Write tests for UI components
- [ ] T-F35: Write tests for API client
- [ ] T-F36: Write E2E tests for auth flow
- [ ] T-F37: Write E2E tests for task CRUD

## INTEGRATION TASKS
- [ ] T-I01: Connect frontend to backend API
- [ ] T-I02: Test authentication flow end-to-end
- [ ] T-I03: Test all CRUD operations end-to-end
- [ ] T-I04: Verify responsive design on all devices
- [ ] T-I05: Performance optimization

## DEPLOYMENT TASKS
- [ ] T-D01: Deploy backend (document process)
- [ ] T-D02: Deploy frontend to Vercel
- [ ] T-D03: Configure environment variables in production
- [ ] T-D04: Test production deployment
- [ ] T-D05: Create demo video (< 90 seconds)

## DOCUMENTATION TASKS
- [ ] T-DOC01: Update README.md with setup instructions
- [ ] T-DOC02: Document API endpoints
- [ ] T-DOC03: Document design system
- [ ] T-DOC04: Create CLAUDE.md files
- [ ] T-DOC05: Create AGENTS.md
```

**Task Format Requirements:**
- Each task must be completable in < 4 hours
- Clear input/output defined
- Dependencies listed
- Artifacts to create/modify specified
- Links back to spec sections

**Step 4: Implementation Phase**

For each task:
1. Read the task specification
2. Use Claude Code to implement
3. Verify against acceptance criteria
4. Run tests
5. If tests fail → update spec (not code)
6. Commit with task ID in message

**Implementation Order:**
1. Backend setup + database
2. Backend authentication
3. Backend API endpoints
4. Backend tests
5. Frontend setup + design system
6. Frontend authentication
7. Frontend task components
8. Frontend integration
9. Frontend tests
10. Deployment

**Step 5: Testing Phase**

**Backend Testing:**
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=. --cov-report=html

# Run specific test file
pytest tests/test_tasks.py
```

**Frontend Testing:**
```bash
# Run all tests
npm test

# Run with coverage
npm test -- --coverage

# Run specific test
npm test -- TaskCard
```

**Manual Testing Checklist:**
- [ ] User can sign up
- [ ] User can sign in
- [ ] User can add task
- [ ] User can view all tasks
- [ ] User can update task
- [ ] User can delete task
- [ ] User can mark task complete/incomplete
- [ ] User only sees their own tasks
- [ ] UI is responsive on mobile
- [ ] UI is responsive on tablet
- [ ] UI is responsive on desktop
- [ ] Glass effects render correctly
- [ ] Gradients display properly
- [ ] Animations are smooth
- [ ] Loading states work
- [ ] Error messages are clear

### 5.3 Agent & Skills Integration

**Using Custom Agents:**

If you have created custom agents or skills:
```markdown
# Agent Usage in Phase 2

## Custom Agents Available
- [List your custom agents here]
- [Specify their capabilities]
- [Define when to invoke them]

## Agent Skills Available
- [List your custom skills here]
- [Specify their purpose]
- [Define usage patterns]

## Agent Communication Protocol
- [How agents communicate]
- [Data formats used]
- [Error handling between agents]

## Agent Orchestration
- [Which agent runs first]
- [Dependencies between agents]
- [Fallback mechanisms]
```

**Example Agent Invocation:**
```bash
# If you have a "spec-generator" agent
claude-code invoke spec-generator --feature="task-crud" --output="specs/features/"

# If you have a "test-writer" agent
claude-code invoke test-writer --component="TaskCard" --output="frontend/__tests__/"
```

### 5.4 Spec-Kit Plus MCP Integration

**Setting up MCP Server:**

1. Create MCP server for Spec-Kit Plus commands
2. Register with Claude Code
3. Commands become available as prompts

**MCP Commands Available:**
```bash
# Initialize project
/speckit-init <project-name>

# Create specification
/speckit-specify

# Generate plan
/speckit-plan

# Break down into tasks
/speckit-tasks

# Implement task
/speckit-implement <task-id>

# Validate specs
/speckit-validate
```

## Section 6: Deliverables & Quality Gates

### 6.1 Phase 2 Deliverables

**Required Files:**
- [ ] constitution.md (this file)
- [ ] AGENTS.md (agent instructions)
- [ ] CLAUDE.md (root + frontend + backend)
- [ ] README.md (comprehensive setup guide)
- [ ] All spec files in `/specs` folder
- [ ] speckit.plan
- [ ] speckit.tasks

**Required Functionality:**
- [ ] User signup working
- [ ] User signin working
- [ ] Add task working
- [ ] View all tasks working
- [ ] Update task working
- [ ] Delete task working
- [ ] Mark task complete/incomplete working
- [ ] User data isolated (can't see other users' tasks)

**Required Design:**
- [ ] Latte color palette applied throughout
- [ ] Glass morphism effects on cards
- [ ] Gradients on CTAs and headers
- [ ] Responsive on mobile (< 640px)
- [ ] Responsive on tablet (640px - 1024px)
- [ ] Responsive on desktop (> 1024px)
- [ ] Smooth animations (200-300ms)

**Required Tests:**
- [ ] Backend: 80%+ test coverage
- [ ] Frontend: Component tests for UI
- [ ] API: All endpoints tested
- [ ] E2E: Auth flow tested
- [ ] E2E: CRUD operations tested

**Required Deployment:**
- [ ] Frontend deployed on Vercel
- [ ] Backend deployed and accessible
- [ ] Demo video created (< 90 seconds)
- [ ] GitHub repo public
- [ ] All environment variables documented

### 6.2 Quality Gates
**Before Moving to Next Task:**
- [ ] Spec approved
- [ ] Code generated via Claude Code
- [ ] Tests passing
- [ ] Manual verification done
- [ ] Committed with proper message

**Before Declaring Phase 2 Complete:**
- [ ] All tasks checked off
- [ ] All deliverables present
- [ ] All quality gates passed
- [ ] Demo video created
- [ ] Submitted via hackathon form

## Section 7: Manual Setup Requirements

### 7.1 Prerequisites
**Required Accounts:**

**Neon Database**
1. Go to: https://neon.tech
2. Sign up (free tier)
3. Create project: "hackathon-todo"
4. Copy connection string

**Vercel**
1. Go to: https://vercel.com
2. Sign up with GitHub
3. Connect your repository

**GitHub**
1. Repository must be public
2. Enable GitHub Pages (optional)

### 7.2 Database Setup (Neon)
**Step-by-step:**
1. Create account at neon.tech
2. Create new project: "hackathon-todo"
3. Select region closest to you
4. Copy connection string:
   ```
   postgres://username:password@ep-xxx-xxx.region.neon.tech/dbname?sslmode=require
   ```
5. Save to backend .env file:
   ```
   DATABASE_URL="postgresql://..."
   ```
6. Test connection:
   ```bash
   cd backend
   python -c "from db import engine; print(engine)"
   ```

### 7.3 Authentication Setup (Better Auth)
**Backend:**
1. Generate secret:
   ```bash
   openssl rand -base64 32
   ```
2. Add to backend `.env`:
   ```
   BETTER_AUTH_SECRET="your-generated-secret"
   ```

**Frontend:**
1. Add to frontend `.env.local`:
   ```
   BETTER_AUTH_SECRET="same-secret-as-backend"
   BETTER_AUTH_URL="http://localhost:3000"
   NEXT_PUBLIC_API_URL="http://localhost:8000"
   ```

2. For production `.env.production`:
   ```
   BETTER_AUTH_SECRET="your-generated-secret"
   BETTER_AUTH_URL="https://your-app.vercel.app"
   NEXT_PUBLIC_API_URL="https://your-backend.com"
   ```

### 7.4 Environment Variables Checklist
**Backend (.env):**
```bash
DATABASE_URL="postgresql://..."
BETTER_AUTH_SECRET="..."
CORS_ORIGINS="http://localhost:3000,https://your-app.vercel.app"
```

**Frontend (.env.local):**
```bash
BETTER_AUTH_SECRET="..."
BETTER_AUTH_URL="http://localhost:3000"
NEXT_PUBLIC_API_URL="http://localhost:8000"
```

## Section 8: Enforcement & Governance

### 8.1 Constitution Authority

This constitution is the **supreme governing document** for Phase 2 development:
- Supersedes all other documentation
- All agents must comply
- Developers must comply
- No exceptions unless documented

### 8.2 Violation Handling

**If spec-driven development is bypassed:**
1. Stop development immediately
2. Delete manually-written code
3. Create proper spec
4. Regenerate via Claude Code

**If design system is violated:**
1. Identify non-compliant components
2. Update to match design system
3. Document reason for deviation (if legitimate)

**If testing is skipped:**
1. Block deployment
2. Write required tests
3. Achieve minimum coverage
4. Verify all tests pass

### 8.3 Amendment Process

**To amend this constitution:**
1. Create amendment proposal document
2. Specify what changes and why
3. Create migration plan
4. Get approval
5. Update version number
6. Document amendment date
7. Update all dependent specs

### 8.4 Version Control

**Version Format:** MAJOR.MINOR.PATCH

- **MAJOR:** Phase changes (1.x.x → 2.x.x)
- **MINOR:** Significant updates (2.1.x → 2.2.x)
- **PATCH:** Small fixes (2.1.1 → 2.1.2)

**Current Version:** 2.0.0
**Ratified Date:** 2026-01-28
**Last Amended:** 2026-01-28

## Section 9: Reference & Resources

### 9.1 Tech Stack Documentation

**Frontend:**
- Next.js: https://nextjs.org/docs
- React: https://react.dev
- Tailwind CSS: https://tailwindcss.com/docs
- Better Auth: https://better-auth.com/docs

**Backend:**
- FastAPI: https://fastapi.tiangolo.com
- SQLModel: https://sqlmodel.tiangolo.com
- Pydantic: https://docs.pydantic.dev

**Database:**
- Neon: https://neon.tech/docs
- PostgreSQL: https://www.postgresql.org/docs

**Tools:**
- Claude Code: https://claude.ai/code
- Spec-Kit Plus: [Your spec-kit documentation]

### 9.2 Hackathon Resources

- Hackathon Docs: [Link to full hackathon document]
- Submission Form: https://forms.gle/KMKEKaFUD6ZX4UtY8
- Zoom Meetings: Sunday 8:00 PM
- Deadline: [Phase 2 deadline date]

### 9.3 Design Resources

**Latte Color Palette:**
- Catppuccin Latte: https://catppuccin.com/palette
- Color contrast checker: https://webaim.org/resources/contrastchecker/

**Glass Morphism:**
- Glass UI Generator: https://ui.glass/generator/
- CSS Tricks Guide: https://css-tricks.com/glassmorphism/

**Gradients:**
- CSS Gradient: https://cssgradient.io/
- Gradient Hunt: https://gradienthunt.com/

## Section 10: Success Checklist

**Before submitting Phase 2:**

**Functionality:**
- [ ] All 5 basic features implemented and working
- [ ] Authentication (signup/signin) working
- [ ] User data properly isolated
- [ ] No bugs in critical paths

**Code Quality:**
- [ ] All code generated via Claude Code (no manual coding)
- [ ] All specs properly documented
- [ ] Test coverage > 80% (backend)
- [ ] Component tests present (frontend)

**Design:**
- [ ] Latte color palette consistently applied
- [ ] Glass morphism effects visible and attractive
- [ ] Gradients used appropriately
- [ ] Fully responsive (mobile, tablet, desktop)
- [ ] Animations smooth and purposeful
- [ ] Accessible (WCAG 2.1 AA)

**Documentation:**
- [ ] README.md comprehensive and accurate
- [ ] All CLAUDE.md files present
- [ ] AGENTS.md documented (if using custom agents)
- [ ] API endpoints documented
- [ ] Setup instructions clear

**Deployment:**
- [ ] Frontend deployed on Vercel
- [ ] Backend deployed and accessible
- [ ] Database connected and working
- [ ] Environment variables properly set
- [ ] Production build tested

**Submission:**
- [ ] GitHub repository public
- [ ] Demo video created (< 90 seconds)
- [ ] Submission form filled
- [ ] WhatsApp number provided

---

## Version History

**Version 2.0.0**
- Complete Phase 2 constitution overhaul
- Ratified: 2026-01-28
- Scope: Full-stack web application with authentication

**Version 1.1.0**
- Enhanced Full-Stack Web Application specifications
- Ratified: 2026-01-26
- Scope: Added detailed architecture, security, and deployment requirements

**Version 1.0.0**
- Initial Terminal MVP constitution
- Ratified: 2026-01-25
- Scope: Terminal-based task management

---

## Conclusion

This constitution defines the complete governance, architecture, design, and development methodology for Phase 2 of the Evolution of Todo project. All development activities must strictly adhere to these principles and specifications. This document serves as the single source of truth for all technical and architectural decisions throughout the Phase 2 development lifecycle.

The success of this project depends on unwavering commitment to the Spec-Driven Development methodology and the architectural constraints outlined in this constitution. Deviation from these principles will result in immediate project halt until proper specifications are created and approved.

**Version**: 2.0.0 | **Ratified**: 2026-01-28 | **Last Amended**: 2026-01-28