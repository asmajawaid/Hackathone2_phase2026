# Quickstart Guide: Phase 2 Todo Application Frontend

## Prerequisites

- Node.js 18+ installed
- npm package manager
- Access to backend API (running on http://localhost:8000)

## Setup Instructions

### 1. Clone and Navigate
```bash
# If you have the repository
git clone <repo-url>
cd frontend  # Navigate to frontend directory
```

### 2. Install Dependencies
```bash
npm install
# Installs:
# - next (v16+)
# - react, react-dom
# - typescript
# - tailwindcss
# - better-auth
# - clsx
# - tailwind-merge
# - lucide-react
```

### 3. Environment Configuration
Create `.env.local` file in the frontend root:
```env
BETTER_AUTH_SECRET="copy-from-backend"  # Same as backend
BETTER_AUTH_URL="http://localhost:3000"
NEXT_PUBLIC_API_URL="http://localhost:8000"  # Backend API URL
DATABASE_URL="postgresql://neon-connection"  # If needed for auth
```

### 4. Run Development Server
```bash
npm run dev
# Frontend will be available at http://localhost:3000
```

## Project Structure
```
frontend/
├── app/
│   ├── (auth)/
│   │   ├── signup/page.tsx
│   │   └── signin/page.tsx
│   ├── (dashboard)/
│   │   ├── layout.tsx
│   │   └── tasks/
│   │       └── page.tsx
│   ├── layout.tsx
│   └── page.tsx
├── components/
│   ├── ui/
│   │   ├── GlassCard.tsx
│   │   ├── Button.tsx
│   │   ├── Input.tsx
│   │   ├── Modal.tsx
│   │   └── Spinner.tsx
│   └── tasks/
│       ├── TaskCard.tsx
│       ├── TaskList.tsx
│       └── TaskForm.tsx
├── lib/
│   ├── types.ts
│   ├── api.ts
│   └── auth.ts
├── hooks/
│   └── useTasks.ts
├── styles/
│   └── globals.css
├── .env.local
├── next.config.js
├── tailwind.config.ts
└── package.json
```

## Key Components

### Authentication Flow
1. Landing page (`/`) → Sign Up/Sign In
2. Protected routes redirect to `/signin` if unauthenticated
3. JWT tokens managed by Better Auth
4. API requests include Authorization header automatically

### Task Management Features
1. **View Tasks**: Dashboard shows all user's tasks in responsive grid
2. **Add Task**: Modal form with validation
3. **Update Task**: Edit existing tasks with pre-filled form
4. **Delete Task**: Confirmation modal before deletion
5. **Toggle Complete**: Checkbox to mark tasks as complete/incomplete

### UI Components
- **GlassCard**: Container with glass morphism effect
- **Button**: Gradient buttons with multiple variants
- **Input**: Glass-styled inputs with validation
- **Modal**: Glass-styled modals with backdrop blur
- **Spinner**: Loading indicators

## Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `BETTER_AUTH_SECRET` | JWT secret (must match backend) | `your-secret-key` |
| `BETTER_AUTH_URL` | Frontend auth URL | `http://localhost:3000` |
| `NEXT_PUBLIC_API_URL` | Backend API URL | `http://localhost:8000` |

## Development Commands

```bash
# Start development server
npm run dev

# Build for production
npm run build

# Start production build
npm start

# Run tests
npm test

# Lint code
npm run lint
```

## API Integration

The frontend communicates with the backend API using:
- Base URL: `http://localhost:8000` (configured via `NEXT_PUBLIC_API_URL`)
- JWT tokens automatically added to Authorization header
- All requests follow the pattern: `/api/{user_id}/tasks`

Example request:
```typescript
// Get user's tasks
const response = await fetch(`http://localhost:8000/api/${userId}/tasks`, {
  headers: {
    'Authorization': `Bearer ${jwtToken}`,
    'Content-Type': 'application/json'
  }
});
```

## Styling System

### Color Palette (Latte)
- `bg-latte-base`: Main background (#eff1f5)
- `text-latte-text`: Primary text (#4c4f69)
- `bg-latte-lavender`: Primary gradient (#7287fd)

### Glass Morphism Effects
- `bg-white/40`: Semi-transparent white background
- `backdrop-blur-md`: Medium backdrop blur
- `border border-white/30`: Subtle border
- `shadow-glass`: Custom glass shadow

### Responsive Design
- Mobile: 1 column layout (< 640px)
- Tablet: 2 column layout (640px - 1024px)
- Desktop: 3 column layout (> 1024px)