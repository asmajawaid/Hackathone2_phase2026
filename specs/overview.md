# Evolution of Todo - Phase 2 Full-Stack Web Application - Overview

## Project Identity
- **Project name:** Evolution of Todo - Phase 2
- **Version:** 2.0.0
- **Phase:** Full-Stack Web Application
- **Development period:** January 2026 - February 2026
- **Deadline:** As specified in hackathon requirements

## Vision Statement
Transform Phase 1 console app into modern multi-user web application with secure authentication, responsive design, and intuitive user experience that implements the 5 basic todo features as a web interface.

## Objectives
- **Primary:** Deliver working web application with authentication
- **Secondary:** Demonstrate SDD methodology mastery
- **Tertiary:** Create reusable design system

## Success Criteria
**Measurable success metrics:**
- All 5 basic features functional (Add, View, Update, Delete, Mark Complete)
- Authentication working (signup/signin)
- User data isolated
- Design system implemented (latte color palette, glass morphism, gradients)
- Tests passing (80%+ coverage backend)
- Deployed on Vercel
- Demo video created (< 90 seconds)

## Scope

### In Scope:
- 5 basic features (Add, View, Update, Delete, Mark Complete)
- User authentication (signup/signin)
- RESTful API
- Persistent database storage (PostgreSQL)
- Responsive UI with glass design
- JWT-based auth

### Out of Scope (for Phase 2):
- Intermediate features (priorities, tags, search, filter, sort)
- Advanced features (recurring tasks, reminders)
- AI chatbot integration
- Multi-language support

## Technical Architecture

### Frontend Architecture
- **Framework:** Next.js 16+ (App Router)
- **Language:** TypeScript 5.x
- **Runtime:** Node.js/React 18+
- **Styling:** Tailwind CSS with custom design system
- **Authentication:** Better Auth with JWT
- **Communication:** Fetch API / axios for backend communication
- **Architecture Pattern:**
  - Server Components: Default for all pages (data fetching, initial rendering)
  - Client Components: Only for interactivity (forms, buttons, modals, state management)
  - Protected routes via middleware
- **State Management:**
  - Server state: React Server Components
  - Client state: React hooks (useState, useReducer)
  - Form state: Controlled components
  - NO global state library needed for Phase 2

### Backend Architecture
- **Framework:** FastAPI
- **ORM:** SQLModel (SQLAlchemy + Pydantic)
- **Authentication:** JWT verification middleware
- **API Pattern:** RESTful with user-scoped endpoints
- **Validation:** Pydantic models
- **Error Handling:** Custom exception handlers

### Database Architecture
- **Type:** PostgreSQL (Neon Serverless)
- **ORM:** SQLModel
- **Tables:** users, tasks
- **Relationships:** tasks.user_id → users.id (foreign key)
- **Indexes:** user_id, completed status

### Authentication Flow
```
┌──────────┐                                           ┌──────────┐
│  User    │                                           │ Frontend │
└────┬─────────────────────────────────────────────────┴─────────┘
     │    (only user's tasks)
     │
     ▼
┌──────────┐
│  Backend │
└──────────┘
```

### Data Flow
Request/Response lifecycle for each operation

### Component Diagram
Frontend component hierarchy:
```
App
├── (auth)
│   ├── layout.tsx
│   ├── signin/page.tsx
│   └── signup/page.tsx
├── (dashboard)
│   ├── layout.tsx (protected)
│   └── tasks/page.tsx
└── components
    ├── ui/
    │   ├── GlassCard.tsx
    │   ├── Button.tsx
    │   ├── Input.tsx
    │   └── Modal.tsx
    └── tasks/
        ├── TaskList.tsx
        ├── TaskCard.tsx
        ├── TaskForm.tsx
        └── TaskActions.tsx
```

### API Architecture
- **Base path:** `/api`
- **Versioning:** Not needed for Phase 2
- **User-scoped:** All endpoints under `/api/{user_id}/`
- **Authentication:** JWT required for all endpoints

### Security Architecture
- **JWT token-based auth**
- **Shared secret between frontend/backend**
- **User data isolation via user_id filtering**
- **CORS configured for frontend origin**
- **Input validation on all endpoints**
- **SQL injection prevention via ORM**

### Deployment Architecture
- **Frontend:** Vercel (serverless)
- **Backend:** Railway/Render/Fly.io (containerized)
- **Database:** Neon (serverless PostgreSQL)
- **Environment variables:** Secure storage