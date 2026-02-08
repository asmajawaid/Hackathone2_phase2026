---
id: 0002
title: frontend-plan
stage: plan
date: 2026-02-05
surface: agent
model: claude-opus-4-5-20251101
feature: 001-frontend-spec
branch: 001-frontend-spec
user: unknown
command: /sp.plan
labels: ["frontend", "plan", "todo-app", "nextjs", "authentication", "design-system"]
links:
  spec: "D:/Hckathone2_Phase2/specs/001-frontend-spec/spec.md"
  ticket: null
  adr: null
  pr: null
files:
 - D:/Hckathone2_Phase2/specs/001-frontend-spec/plan.md
 - D:/Hckathone2_Phase2/specs/001-frontend-spec/research.md
 - D:/Hckathone2_Phase2/specs/001-frontend-spec/data-model.md
 - D:/Hckathone2_Phase2/specs/001-frontend-spec/quickstart.md
 - D:/Hckathone2_Phase2/specs/001-frontend-spec/contracts/task-api.yaml
tests:
 - none
---

## Prompt

# 🎯 FRONTEND PLAN PROMPT (CONCISE)

```markdown
Based on the frontend specification (@specs/ui/*.md, @speckit.specify), create a detailed technical plan (speckit.plan) for implementing Phase 2 Todo Application frontend.

## CONTEXT
- Backend: ALREADY BUILT and running on http://localhost:8000
- Frontend: Next.js 16+ App Router, TypeScript, Tailwind CSS, Better Auth
- Design: Latte colors, Glass morphism, Gradients
- Goal: Connect frontend to working backend

---

## PLAN STRUCTURE

### 1. EXECUTIVE SUMMARY
- Project: Evolution of Todo - Phase 2 Frontend
- Timeline: 2 weeks
- Phases: Setup → Design System → Auth → Features → Integration
- Risk level: Low (backend ready)
- Success criteria: All 5 CRUD features + auth working

### 2. ARCHITECTURE OVERVIEW

**Frontend Stack:**
- Next.js 16+ App Router (Server Components default)
- TypeScript for type safety
- Tailwind CSS with custom design system
- Better Auth for authentication
- Native fetch for API calls

**Route Structure:**
```
/ → Landing (public)
/signin → Sign in (public)
/signup → Sign up (public)
/dashboard/tasks → Main app (protected)
```

**Component Hierarchy:**
```
Root Layout
├── (auth) Layout
│   ├── SignIn Page
│   └── SignUp Page
└── (dashboard) Layout (Protected)
    └── Tasks Page
        ├── TaskList
        │   └── TaskCard (multiple)
        ├── Modal (TaskForm)
        └── EmptyState
```

**Data Flow:**
```
User Action → useTasks Hook → API Client → Backend
         ↓
   Optimistic Update
         ↓
Backend Response → Update State → Re-render
```

### 3. IMPLEMENTATION PHASES

**Phase A: Project Setup (Day 1)**
- Initialize Next.js with TypeScript
- Install dependencies (better-auth, lucide-react, clsx, tailwind-merge)
- Create folder structure
- Setup .env.local with backend URL
- Configure next.config.js

**Phase B: Design System (Day 2)**
- Configure tailwind.config.ts (latte colors, gradients, animations)
- Create globals.css (glass utilities, fonts, scrollbar)
- Define TypeScript types (lib/types.ts)
- Create utility functions (lib/utils.ts - cn, formatDate, validation)

**Phase C: Core UI Components (Day 3-4)**
- GlassCard.tsx (glass morphism container)
- Button.tsx (4 variants: primary, secondary, ghost, danger)
- Input.tsx (with validation, error display, counter)
- Modal.tsx (backdrop blur, ESC/outside click to close)
- Spinner.tsx (loading indicator)
- Skeleton.tsx (loading placeholders)

**Phase D: Auth Setup (Day 5)**
- Configure Better Auth (lib/auth.ts)
- Create API route (app/api/auth/[...]/route.ts)
- Setup middleware.ts (route protection)
- Create SignUpForm component
- Create SignInForm component
- Create signup page (app/(auth)/signup/page.tsx)
- Create signin page (app/(auth)/signin/page.tsx)
- Test auth flow end-to-end

**Phase E: API Client (Day 6)**
- Create lib/api.ts
- Implement getHeaders() with JWT
- Implement getTasks(userId)
- Implement createTask(userId, input)
- Implement updateTask(userId, taskId, input)
- Implement deleteTask(userId, taskId)
- Implement toggleComplete(userId, taskId)
- Test all endpoints with Postman/Thunder Client

**Phase F: Custom Hooks (Day 7)**
- Create hooks/useTasks.ts
- Implement state (tasks, loading, error)
- Implement fetchTasks (auto-fetch on mount)
- Implement createTask (optimistic UI)
- Implement updateTask (optimistic UI)
- Implement deleteTask (optimistic UI)
- Implement toggleComplete (optimistic UI)

**Phase G: Task Components (Day 8-9)**
- TaskCard.tsx (display, checkbox, edit/delete buttons)
- TaskList.tsx (grid, loading, empty, error states)
- TaskForm.tsx (add/edit form with validation)
- EmptyState.tsx (when no tasks)
- DeleteConfirmation.tsx (optional modal)

**Phase H: Pages (Day 10)**
- Landing page (app/page.tsx - hero, features, CTA)
- Dashboard layout (app/(dashboard)/layout.tsx - navbar, protected)
- Tasks page (app/(dashboard)/tasks/page.tsx - integrate all)

**Phase I: Integration & Testing (Day 11-12)**
- Connect all components
- Test full CRUD flow
- Test auth flow (signup → signin → logout)
- Test responsive design (mobile, tablet, desktop)
- Test error handling
- Fix bugs

**Phase J: Polish & Deployment (Day 13-14)**
- Add animations
- Optimize performance
- Test on real devices
- Deploy to Vercel
- Test production build
- Create demo video
- Submit to hackathon

### 4. TECHNICAL SETUP

**Install Dependencies:**
```bash
npx create-next-app@latest frontend --typescript --tailwind --app
cd frontend
npm install better-auth clsx tailwind-merge lucide-react
```

**Environment Variables (.env.local):**
```bash
BETTER_AUTH_SECRET="copy-from-backend"
BETTER_AUTH_URL="http://localhost:3000"
NEXT_PUBLIC_API_URL="http://localhost:8000"
DATABASE_URL="postgresql://neon-connection"
```

**Tailwind Config (Key Parts):**
```typescript
colors: {
  latte: {
    base: '#eff1f5',
    mantle: '#e6e9ef',
    text: '#4c4f69',
    lavender: '#7287fd',
    // ... all other colors
  }
},
backdropBlur: { xs: '2px', sm: '4px', md: '12px', lg: '16px', xl: '24px' },
backgroundImage: {
  'gradient-lavender': 'linear-gradient(135deg, #7287fd 0%, #8839ef 100%)',
  // ... other gradients
},
animation: {
  'fade-in': 'fade-in 250ms ease-out',
  'scale-in': 'scale-in 250ms ease-out',
  // ... other animations
}
```

### 5. KEY IMPLEMENTATION PATTERNS

**Server vs Client Components:**
- Server: All pages, layouts by default
- Client: Forms, buttons, interactive components (use 'use client')

**Auth Flow:**
```
1. User submits signup form
2. Call signUp.email({ email, password })
3. Better Auth creates user + session
4. JWT token stored in httpOnly cookie
5. Redirect to /dashboard/tasks
6. Middleware checks token on protected routes
```

**API Client Pattern:**
```typescript
// Get JWT from session
const session = await getSession()
const headers = {
  'Authorization': `Bearer ${session.token}`,
  'Content-Type': 'application/json'
}

// Make request
const response = await fetch(`${API_URL}/api/${userId}/tasks`, { headers })
const data = await response.json()
```

**Optimistic UI Pattern:**
```typescript
// Delete task example
const deleteTask = async (id) => {
  // Save current state
  const previous = tasks

  // Update UI immediately
  setTasks(tasks.filter(t => t.id !== id))

  try {
    // Call API
    await api.deleteTask(userId, id)
  } catch (error) {
    // Revert on error
    setTasks(previous)
    showError('Delete failed')
  }
}
```

**Form Validation Pattern:**
```typescript
const validate = () => {
  const errors = {}
  if (!title.trim()) errors.title = 'Title is required'
  if (title.length > 200) errors.title = 'Max 200 characters'
  setErrors(errors)
  return Object.keys(errors).length === 0
}
```

### 6. COMPONENT SPECIFICATIONS

**GlassCard:**
```tsx
<div className="bg-white/40 backdrop-blur-md border border-white/30 shadow-glass rounded-2xl p-6">
  {children}
</div>
```

**Button (Primary):**
```tsx
<button className="bg-gradient-lavender text-white px-6 py-3 rounded-xl shadow-lg hover:scale-105 transition-all">
  {children}
</button>
```

**Input:**
```tsx
<input className="w-full bg-white/30 backdrop-blur-sm border border-white/30 rounded-xl px-4 py-3 focus:border-latte-lavender focus:ring-2 focus:ring-latte-lavender/20" />
```

### 7. RESPONSIVE BREAKPOINTS

```
xs:  475px  → Mobile (portrait)
sm:  640px  → Mobile (landscape)
md:  768px  → Tablet
lg:  1024px → Desktop
xl:  1280px → Large desktop
2xl: 1536px → Extra large
```

**Grid Layout:**
- Mobile (< sm): 1 column
- Tablet (md): 2 columns
- Desktop (lg+): 3 columns

### 8. ERROR HANDLING STRATEGY

**API Errors:**
```typescript
try {
  const data = await api.getTasks(userId)
  setTasks(data)
} catch (error) {
  if (error.status === 401) {
    // Redirect to signin
    router.push('/signin')
  } else {
    setError(error.message || 'Failed to load tasks')
  }
}
```

**Form Errors:**
- Display inline below input
- Red text color (latte-red)
- Clear on input change

**Toast Notifications (Optional):**
- Success: Green with checkmark
- Error: Red with X icon
- Position: top-right
- Auto-dismiss: 3 seconds

### 9. TESTING CHECKLIST

**Manual Testing:**
- [ ] User can signup
- [ ] User can signin
- [ ] Invalid credentials rejected
- [ ] Protected routes redirect
- [ ] User can add task
- [ ] User can view tasks
- [ ] User can edit task
- [ ] User can delete task
- [ ] User can toggle completion
- [ ] User only sees own tasks
- [ ] UI responsive on mobile
- [ ] UI responsive on tablet
- [ ] UI responsive on desktop
- [ ] Glass effects visible
- [ ] Gradients render correctly
- [ ] Animations smooth
- [ ] Loading states work
- [ ] Error messages clear
- [ ] User can logout

**Browser Testing:**
- [ ] Chrome
- [ ] Firefox
- [ ] Safari
- [ ] Edge

### 10. DEPLOYMENT PLAN

**Vercel Deployment:**
```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel

# Set environment variables in Vercel dashboard
BETTER_AUTH_SECRET=...
BETTER_AUTH_URL=https://your-app.vercel.app
NEXT_PUBLIC_API_URL=https://your-backend.com
DATABASE_URL=postgresql://...

# Deploy to production
vercel --prod
```

**Pre-deployment Checklist:**
- [ ] All environment variables set
- [ ] Build succeeds locally (`npm run build`)
- [ ] No TypeScript errors
- [ ] No console errors
- [ ] All features tested
- [ ] Responsive verified
- [ ] Performance optimized

### 11. PERFORMANCE OPTIMIZATION

**Code Splitting:**
- Use dynamic imports for modals
- Lazy load heavy components

**Image Optimization:**
- Use next/image for all images
- Provide width/height
- Use modern formats (WebP)

**Caching:**
- API responses cached in React state
- Don't refetch on every render

**Bundle Size:**
- Minimize dependencies
- Tree-shake unused code
- Check bundle analyzer

### 12. ACCESSIBILITY

**Keyboard Navigation:**
- Tab through all interactive elements
- Enter to submit forms
- ESC to close modals

**Screen Readers:**
- Semantic HTML (nav, main, section)
- ARIA labels on icons
- Alt text on images

**Focus Indicators:**
- Visible focus ring (lavender)
- 2px ring with offset

**Color Contrast:**
- Text: 4.5:1 minimum
- Buttons: 3:1 minimum
- Test with WebAIM tool

### 13. RISK MITIGATION

**Risk: Auth Integration Complex**
- Mitigation: Follow Better Auth docs exactly
- Test auth flow first before building features

**Risk: CORS Issues**
- Mitigation: Backend already configured CORS
- Verify allowed origins include localhost:3000

**Risk: JWT Expiry**
- Mitigation: 7-day expiry (configured)
- Redirect to signin on 401

**Risk: Responsive Issues**
- Mitigation: Mobile-first approach
- Test on real devices early

**Risk: Performance**
- Mitigation: Use Server Components
- Optimize early, not last minute

### 14. SUCCESS CRITERIA

**Functional:**
- ✅ All 5 CRUD features working
- ✅ Auth (signup, signin, logout) working
- ✅ User data isolated
- ✅ No critical bugs

**Design:**
- ✅ Latte colors applied
- ✅ Glass morphism effects visible
- ✅ Gradients used appropriately
- ✅ Fully responsive
- ✅ Smooth animations

**Performance:**
- ✅ Page load < 3s
- ✅ Lighthouse score > 90
- ✅ No console errors

**Process:**
- ✅ All via Claude Code
- ✅ Specs documented
- ✅ Code organized
- ✅ Dep
```

## Response snapshot

Created comprehensive frontend implementation plan with all required components, architecture overview, and technical specifications for the Phase 2 Todo Application.

## Outcome

- ✅ Impact: Complete frontend plan created with architecture, components, and implementation phases
- 🧪 Tests: none
- 📁 Files: specs/001-frontend-spec/plan.md, specs/001-frontend-spec/research.md, specs/001-frontend-spec/data-model.md, specs/001-frontend-spec/quickstart.md, specs/001-frontend-spec/contracts/task-api.yaml
- 🔁 Next prompts: /sp.tasks to break plan into implementation tasks
- 🧠 Reflection: Comprehensive frontend plan establishes clear architecture for connecting Next.js frontend to backend API with proper authentication and design system implementation

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
