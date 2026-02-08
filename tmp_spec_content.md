# 🎯 FRONTEND SPEC PROMPT (CONCISE)

```markdown
Create a complete frontend specification file (speckit.specify) for Phase 2 Todo Application.

## CONTEXT
- Backend is ALREADY BUILT and working
- Backend API URL: http://localhost:8000
- All endpoints require JWT: Authorization: Bearer <token>
- Tech Stack: Next.js 16+ (App Router), TypeScript, Tailwind CSS, Better Auth

## BACKEND ENDPOINTS (ALREADY WORKING)
```
GET    /api/{user_id}/tasks              → List tasks
POST   /api/{user_id}/tasks              → Create task
PUT    /api/{user_id}/tasks/{id}         → Update task
DELETE /api/{user_id}/tasks/{id}         → Delete task
PATCH  /api/{user_id}/tasks/{id}/complete → Toggle completion
```

Backend Response Format:
```json
{
  "success": true,
  "data": {...},
  "message": "..."
}
```

---

## SPECIFICATION REQUIREMENTS

### 1. PROJECT IDENTITY
- Project: Evolution of Todo - Phase 2 Frontend
- Framework: Next.js 16+ App Router
- Design: Latte colors + Glass morphism + Gradients
- Authenticatiog.ts
└── .env.local
```

### 3. ENVIRONMENT VARIABLES
```bash
BETTER_AUTH_SECRET="copy-same-from-backend"
BETTER_AUTH_URL="http://localhost:3000"
NEXT_PUBLIC_API_URL="http://localhost:8000"
DATABASE_URL="postgresql://neon-connection"
```

### 4. DEPENDENCIES
```bash
npm install better-auth clsx tailwind-merge lucide-react
```

### 5. TAILWIND CONFIG
Include:
- Latte color palette (base, mantle, crust, text, subtext0/1, lavender, blue, green, red, etc.)
- Backdrop blur utilities (xs, sm, md, lg, xl)
- Gradients (gradient-lavender, gradient-ocean, gradient-sunset, gradient-forest)
- Glass shadows (glass, glass-lg)
- Animations (fade-in, slide-up, scale-in, pulse-soft)
- Responsive breakpoints (xs, sm, md, lg, xl, 2xl)

### 6. DESIGN SYSTEM GLOBALS.CSS
Include:
- Inter font
- Glass card utility (.glass)
- Input glass (.input-glass)
- Button base (.btn-base)
- Custom scrollbar
- Focus visible styles
- Selection styles

### 7. TYPESCRIPT TYPES (lib/types.ts)
Define interfaces for:
- Task
- TaskCreateInput
- TaskUpdateInput
- ApiSuccessResponse<T>
- ApiErrorResponse
- User
- Session
- All component props (GlassCardProps, ButtonProps, InputProps, ModalProps, TaskCardProps, etc.)

### 8. AUTH SETUP (lib/auth.ts)
```typescript
import { createAuthClient } from "better-auth/react"

export const authClient = createAuthClient({
  baseURL: process.env.BETTER_AUTH_URL
})

export const { signIn, signUp, signOut, useSession, getSession } = authClient
```

### 9. API CLIENT (lib/api.ts)
Functions needed:
- getTasks(userId)
- createTask(userId, input)
- updateTask(userId, taskId, input)
- deleteTask(userId, taskId)
- toggleComplete(userId, taskId)

All should:
- Get JWT from session
- Add to Authorization header
- Handle errors
- Return typed data

### 10. CUSTOM HOOK (hooks/useTasks.ts)
Export useTasks() hook with:
- tasks: Task[]
- loading: boolean
- error: string | null
- fetchTasks()
- createTask(input)
- updateTask(id, input)
- deleteTask(id)
- toggleComplete(id)

Features:
- Auto-fetch on mount
- Optimistic UI updates
- Error handling

### 11. UI COMPONENTS

**GlassCard:**
- Props: children, className, hover, onClick
- Glass morphism effect
- Hover animation (translate-y, shadow)

**Button:**
- Variants: primary (gradient-lavender), secondary, ghost, danger
- Sizes: sm, md, lg
- Loading state with spinner
- Icon support

**Input:**
- Label, placeholder, value, onChange
- Error display
- Character counter
- Glass styling
- Focus states

**Modal:**
- Backdrop with blur
- Glass card design
- ESC to close
- Click outside to close
- Size variants (sm, md, lg)

**Spinner:**
- Sizes: xs, sm, md, lg
- Spin animation

### 12. TASK COMPONENTS

**TaskCard:**
- Display task (title, description, date)
- Checkbox for completion toggle
- Edit/Delete buttons (show on hover)
- Glass card design
- Strikethrough when completed

**TaskList:**
- Grid layout (responsive: 1, 2, 3 cols)
- Loading skeletons
- Empty state
- Error state

**TaskForm:**
- Title input (required, max 200)
- Description textarea (optional, max 1000)
- Character counters
- Validation
- Submit/Cancel buttons
- Works for both add and edit

**EmptyState:**
- Icon
- Message: "No tasks yet"
- Encouraging text

### 13. PAGES

**Landing (/):**
- Hero section with gradient background
- "Organize Your Life" heading
- CTA button → Sign Up
- Features cards (glass design)

**Sign Up (/signup):**
- Glass form card
- Fields: name (optional), email, password, confirm password
- Validation (email format, password strength)
- Success → redirect to /dashboard/tasks
- Link to sign in

**Sign In (/signin):**
- Glass form card
- Fields: email, password
- Validation
- Success → redirect to /dashboard/tasks
- Link to sign up

**Dashboard (/dashboard/tasks):**
- Protected route (middleware)
- Navbar with gradient, logo, logout button
- "My Tasks" heading
- "+ Add Task" button → opens modal
- Task grid
- Loading state (skeletons)
- Empty state if no tasks

### 14. ROUTE PROTECTION (middleware.ts)
```typescript
import { NextResponse } from 'next/server'
import type { NextRequest } from 'next/server'

export function middleware(request: NextRequest) {
  const session = request.cookies.get('better-auth.session_token')

  if (request.nextUrl.pathname.startsWith('/dashboard')) {
    if (!session) {
      return NextResponse.redirect(new URL('/signin', request.url))
    }
  }

  return NextResponse.next()
}

export const config = {
  matcher: '/dashboard/:path*',
}
```

### 15. FEATURES TO IMPLEMENT

**Authentication:**
- User can sign up (email, password)
- User can sign in
- JWT token stored in httpOnly cookie
- Protected routes redirect to signin
- Logout clears session

**Task Management (5 Basic Features):**
1. **Add Task:** Modal with form, create via API
2. **View Tasks:** Grid layout, fetch from API
3. **Update Task:** Modal with pre-filled form, update via API
4. **Delete Task:** Confirmation modal, delete via API
5. **Mark Complete:** Checkbox toggle, patch via API

**UX Features:**
- Optimistic UI updates (instant feedback)
- Loading states (skeletons, spinners)
- Error handling (toast notifications)
- Smooth animations (fade, slide, scale)
- Responsive design (mobile, tablet, desktop)

### 16. DESIGN REQUIREMENTS

**Glass Morphism:**
- All cards: bg-white/40, backdrop-blur-md
- Borders: border-white/30
- Shadows: shadow-glass
- Hover effects: opacity increase, shadow grow

**Gradients:**
- Hero background: gradient-hero
- Primary buttons: gradient-lavender
- Navbar: gradient-ocean
- Accent elements: gradient-sunset

**Colors (Latte Palette):**
- Background: latte-base (#eff1f5)
- Cards: latte-mantle (#e6e9ef)
- Text: latte-text (#4c4f69)
- Accents: latte-lavender (#7287fd)
- Success: latte-green (#40a02b)
- Error: latte-red (#d20f39)

**Animations:**
- Page transitions: fade-in
- Modal: scale-in
- Task cards: slide-up (staggered)
- Buttons: scale on hover/active
- Loading: pulse-soft

**Responsive:**
- Mobile (<640px): 1 column, stacked layout
- Tablet (640-1024px): 2 columns
- Desktop (>1024px): 3-4 columns
- Touch-friendly: larger tap targets on mobile

### 17. VALIDATION RULES

**Email:**
- Required
- Valid format (regex)

**Password:**
- Min 8 characters
- 1 uppercase letter
- 1 number
- 1 special character

**Task Title:**
- Required
- Min 1 character
- Max 200 characters
- Cannot be only whitespace

**Task Description:**
- Optional
- Max 1000 characters

### 18. ERROR HANDLING

**API Errors:**
- Network error: "Connection failed. Please check your internet."
- 401: Redirect to signin
- 403: "Access denied"
- 404: "Task not found"
- 500: "Server error. Please try again."

**Form Errors:**
- Show inline below input
- Red text color
- Clear on input change

**Toast Notifications:**
- Success: Green checkmark icon
- Error: Red X icon
- Auto-dismiss after 3s
- Positioned top-right

### 19. PERFORMANCE

**Optimization:**
- Use Server Components by default
- Client Components only for interactivity
- Lazy load modals
- Optimize images (next/image)
- Code splitting

**Targets:**
- Page load: <3s
- First Contentful Paint: <1.5s
- Time to Interactive: <3s
- Lighthouse score: >90

### 20. ACCESSIBILITY

**WCAG 2.1 AA:**
- Color contrast: 4.5:1 minimum
- Focus indicators: visible on all interactive elements
- Keyboard navigation: full support
- ARIA labels: on all components
- Semantic HTML: proper headings, sections

### 21. TESTING (Optional for Phase 2)
- Component tests with React Testing Library
- E2E tests for auth flow
- E2E tests for CRUD operations

---

## OUTPUT FORMAT

Generate **speckit.specify** with:
- Clear sections
- User stories with acceptance criteria
- Technical specifications
- Component specifications
- Design specifications
- Validation rules
- Error handling
- Performance targets

**Focus:** Frontend ONLY. Backend is already built.

**Goal:** Developer should be able to build complete Phase 2 frontend from this spec using Claude Code.

Generate the complete speckit.specify file now.
```