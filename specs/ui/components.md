# Evolution of Todo - Phase 2 Component Specifications

## Component Library Overview

All UI components must follow the Latte Glass Design System and be built as reusable, composable React components with TypeScript.

## Component 1: GlassCard

**Purpose:** Reusable glass morphism card container

**Props:**
```typescript
interface GlassCardProps {
  children: React.ReactNode;
  className?: string;
  hover?: boolean;  // Enable hover effect
  onClick?: () => void;
}
```

**Implementation:**
```tsx
export function GlassCard({
  children,
  className = '',
  hover = true,
  onClick
}: GlassCardProps) {
  return (
    <div
      className={cn(
        "bg-latte-mantle/40 backdrop-blur-md rounded-2xl",
        "border border-latte-overlay0/20 shadow-glass",
        "p-6 transition-all duration-300",
        hover && "hover:bg-latte-mantle/50 hover:shadow-glass-lg hover:-translate-y-1",
        onClick && "cursor-pointer",
        className
      )}
      onClick={onClick}
    >
      {children}
    </div>
  );
}
```

**Usage:**
```tsx
<GlassCard hover={true}>
  <h3>Card Title</h3>
  <p>Card content</p>
</GlassCard>
```

**Variants:**
- Default: Standard glass card
- Strong: Increased opacity for modals
- Subtle: Reduced opacity for backgrounds

## Component 2: Button

**Purpose:** Primary action buttons with variants

**Props:**
```typescript
interface ButtonProps {
  children: React.ReactNode;
  variant?: 'primary' | 'secondary' | 'ghost' | 'danger';
  size?: 'sm' | 'md' | 'lg';
  disabled?: boolean;
  loading?: boolean;
  onClick?: () => void;
  type?: 'button' | 'submit' | 'reset';
  className?: string;
}
```

**Implementation:**
```tsx
export function Button({
  children,
  variant = 'primary',
  size = 'md',
  disabled = false,
  loading = false,
  onClick,
  type = 'button',
  className = ''
}: ButtonProps) {
  const baseStyles = "font-semibold rounded-lg transition-all duration-200 disabled:opacity-50 disabled:cursor-not-allowed";

  const variants = {
    primary: "bg-gradient-lavender text-white shadow-lg shadow-latte-lavender/30 hover:shadow-xl hover:shadow-latte-lavender/50 hover:scale-105 active:scale-95",
    secondary: "bg-latte-surface0 text-latte-text border border-latte-overlay1 hover:bg-latte-surface1",
    ghost: "text-latte-lavender hover:bg-latte-lavender/10",
    danger: "bg-latte-red text-white shadow-lg shadow-latte-red/30 hover:shadow-xl hover:shadow-latte-red/50"
  };

  const sizes = {
    sm: "px-4 py-2 text-sm",
    md: "px-6 py-3 text-base",
    lg: "px-8 py-4 text-lg"
  };

  return (
    <button
      type={type}
      className={cn(baseStyles, variants[variant], sizes[size], className)}
      onClick={onClick}
      disabled={disabled || loading}
    >
      {loading ? <Spinner /> : children}
    </button>
  );
}
```

**Variants:**
- Primary: Gradient button for main actions
- Secondary: Outlined button for secondary actions
- Ghost: Minimal button for tertiary actions
- Danger: Red button for destructive actions

## Component 3: Input

**Purpose:** Form input with validation

**Props:**
```typescript
interface InputProps {
  label?: string;
  placeholder?: string;
  value: string;
  onChange: (value: string) => void;
  type?: 'text' | 'email' | 'password' | 'number';
  error?: string;
  disabled?: boolean;
  required?: boolean;
  maxLength?: number;
  className?: string;
}
```

**Implementation:**
```tsx
export function Input({
  label,
  placeholder,
  value,
  onChange,
  type = 'text',
  error,
  disabled = false,
  required = false,
  maxLength,
  className = ''
}: InputProps) {
  return (
    <div className={cn("space-y-2", className)}>
      {label && (
        <label className="block text-sm font-medium text-latte-text">
          {label} {required && <span className="text-latte-red">*</span>}
        </label>
      )}
      <input
        type={type}
        value={value}
        onChange={(e) => onChange(e.target.value)}
        placeholder={placeholder}
        disabled={disabled}
        maxLength={maxLength}
        className={cn(
          "w-full bg-latte-crust/50 backdrop-blur-sm rounded-lg",
          "border px-4 py-3 text-latte-text",
          "placeholder:text-latte-subtext0",
          "transition-all duration-200",
          "focus:outline-none focus:ring-2",
          error
            ? "border-latte-red focus:border-latte-red focus:ring-latte-red/20"
            : "border-latte-overlay0/30 focus:border-latte-lavender focus:ring-latte-lavender/20",
          disabled && "opacity-50 cursor-not-allowed"
        )}
      />
      {error && (
        <p className="text-sm text-latte-red">{error}</p>
      )}
      {maxLength && (
        <p className="text-xs text-latte-subtext1 text-right">
          {value.length}/{maxLength}
        </p>
      )}
    </div>
  );
}
```

## Component 4: Modal

**Purpose:** Dialog/modal overlay

**Props:**
```typescript
interface ModalProps {
  isOpen: boolean;
  onClose: () => void;
  title?: string;
  children: React.ReactNode;
  size?: 'sm' | 'md' | 'lg';
}
```

**Implementation:**
```tsx
export function Modal({
  isOpen,
  onClose,
  title,
  children,
  size = 'md'
}: ModalProps) {
  if (!isOpen) return null;

  const sizes = {
    sm: "max-w-md",
    md: "max-w-lg",
    lg: "max-w-2xl"
  };

  return (
    <div
      className="fixed inset-0 bg-latte-text/20 backdrop-blur-sm flex items-center justify-center z-50 animate-fade-in"
      onClick={onClose}
    >
      <div
        className={cn(
          "bg-latte-mantle/60 backdrop-blur-xl rounded-2xl",
          "border border-latte-overlay1/30 shadow-glass-lg",
          "w-full p-6 animate-scale-in",
          sizes[size]
        )}
        onClick={(e) => e.stopPropagation()}
      >
        {title && (
          <div className="flex items-center justify-between mb-4">
            <h2 className="text-2xl font-semibold text-latte-text">{title}</h2>
            <button
              onClick={onClose}
              className="text-latte-subtext1 hover:text-latte-text transition-colors"
            >
              ✕
            </button>
          </div>
        )}
        {children}
      </div>
    </div>
  );
}
```

## Component 5: TaskCard

**Purpose:** Display individual task with actions

**Props:**
```typescript
interface TaskCardProps {
  task: Task;
  onToggle: (id: number) => void;
  onEdit: (task: Task) => void;
  onDelete: (id: number) => void;
}
```

**Implementation:**
```tsx
export function TaskCard({ task, onToggle, onEdit, onDelete }: TaskCardProps) {
  return (
    <GlassCard hover={true}>
      <div className="flex items-start gap-4">
        {/* Checkbox */}
        <button
          onClick={() => onToggle(task.id)}
          className={cn(
            "w-6 h-6 rounded-md border-2 flex items-center justify-center",
            "transition-all duration-200",
            task.completed
              ? "bg-latte-green border-latte-green"
              : "border-latte-overlay1 hover:border-latte-lavender"
          )}
        >
          {task.completed && <Check className="w-4 h-4 text-white" />}
        </button>
        {/* Content */}
        <div className="flex-1">
          <h3 className={cn(
            "text-lg font-semibold text-latte-text mb-1",
            task.completed && "line-through opacity-60"
          )}>
            {task.title}
          </h3>
          {task.description && (
            <p className="text-sm text-latte-subtext1 line-clamp-2">
              {task.description}
            </p>
          )}
          <p className="text-xs text-latte-subtext0 mt-2">
            {new Date(task.created_at).toLocaleDateString()}
          </p>
        </div>

        {/* Actions */}
        <div className="flex gap-2">
          <Button variant="ghost" size="sm" onClick={() => onEdit(task)}>
            Edit
          </Button>
          <Button variant="ghost" size="sm" onClick={() => onDelete(task.id)}>
            Delete
          </Button>
        </div>
      </div>
    </GlassCard>
  );
}
```

## Component 6: TaskForm

**Purpose:** Form for adding/editing tasks

**Props:**
```typescript
interface TaskFormProps {
  initialData?: Partial<Task>;
  onSubmit: (data: { title: string; description?: string }) => void;
  onCancel: () => void;
  isLoading?: boolean;
}
```

**Implementation:**
```tsx
export function TaskForm({ initialData, onSubmit, onCancel, isLoading }: TaskFormProps) {
  const [title, setTitle] = useState(initialData?.title || '');
  const [description, setDescription] = useState(initialData?.description || '');
  const [errors, setErrors] = useState<Record<string, string>>({});

  const validate = () => {
    const newErrors: Record<string, string> = {};
    if (!title.trim()) newErrors.title = 'Title is required';
    if (title.length > 200) newErrors.title = 'Title must be 200 characters or less';
    if (description.length > 1000) newErrors.description = 'Description must be 1000 characters or less';
    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = () => {
    if (validate()) {
      onSubmit({ title, description: description || undefined });
    }
  };

  return (
    <div className="space-y-4">
      <Input
        label="Title"
        value={title}
        onChange={setTitle}
        error={errors.title}
        required
        maxLength={200}
        placeholder="What do you need to do?"
      />

      <div>
        <label className="block text-sm font-medium text-latte-text mb-2">
          Description
        </label>
        <textarea
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          maxLength={1000}
          rows={4}
          placeholder="Add more details..."
          className="w-full bg-latte-crust/50 backdrop-blur-sm rounded-lg border border-latte-overlay0/30 px-4 py-3 text-latte-text placeholder:text-latte-subtext0 focus:outline-none focus:border-latte-lavender focus:ring-2 focus:ring-latte-lavender/20"
        />
        <p className="text-xs text-latte-subtext1 text-right">
          {description.length}/1000
        </p>
      </div>

      <div className="flex justify-end gap-2 pt-4">
        <Button variant="secondary" onClick={onCancel}>
          Cancel
        </Button>
        <Button variant="primary" onClick={handleSubmit} disabled={isLoading}>
          {initialData ? 'Update Task' : 'Add Task'}
        </Button>
      </div>
    </div>
  );
}
```

## Page Structure

The application follows this page structure:
```
app/
├── (auth)/
│   ├── layout.tsx          # Auth layout
│   ├── signin/
│   │   └── page.tsx        # Sign in page
│   └── signup/
│       └── page.tsx        # Sign up page
├── (dashboard)/
│   ├── layout.tsx          # Protected dashboard layout
│   └── tasks/
│       └── page.tsx        # Task management page
├── layout.tsx              # Root layout
├── page.tsx                # Landing page
└── globals.css             # Global styles
```

### Page 1: Landing Page (`/`)

**Purpose:** Welcome page with auth CTA

**Layout:**
```
┌────────────────────────────────────────────┐
│  [Logo]                  [Sign In] Button  │
├────────────────────────────────────────────┤
│                                            │
│          Hero Section with Gradient        │
│                                            │
│    "Organize Your Life with TodoApp"      │
│                                            │
│         [Get Started] Button               │
│                                            │
├────────────────────────────────────────────┤
│          Features (3 glass cards)          │
└────────────────────────────────────────────┘
```

**Components:**
- Gradient hero section
- Glass feature cards
- CTA buttons with gradients

**Responsive:**
- Mobile: Stacked layout
- Tablet: 2-column features
- Desktop: 3-column features

### Page 2: Sign Up Page (`/signup`)

**Purpose:** User registration

**Layout:**
```
┌─────────────────────────────────────────────┐
│                                             │
│              Sign Up Form                    │
│                                             │
│  [Name]                                     │
│  [Email]                                    │
│  [Password]                                 │
│  [Confirm Password]                         │
│                                             │
│  [Sign Up Button] [Already have account?]   │
│                                             │
└─────────────────────────────────────────────┘
```

**Form Fields:**
- Name (optional)
- Email (required, validated)
- Password (required, validated)

**Validation:**
- Real-time validation
- Error messages inline
- Submit disabled until valid

**Flow:**
1. User fills form
2. Client-side validation
3. Submit to Better Auth
4. On success → redirect to `/dashboard/tasks`
5. On error → show message

### Page 3: Sign In Page (`/signin`)

**Purpose:** User authentication

**Layout:** Similar to sign up, but with:
- Email field
- Password field
- "Forgot password?" link (optional for Phase 2)
- "Don't have account? Sign up" link

**Flow:**
1. User enters credentials
2. Submit to Better Auth
3. Receive JWT token
4. Store token (httpOnly cookie)
5. Redirect to `/dashboard/tasks`

### Page 4: Tasks Dashboard (`/dashboard/tasks`)

**Purpose:** Main task management interface

**Layout:**
```
┌─────────────────────────────────────────────┐
│  Header with Gradient Background            │
│  [Logo] [User Menu]                        │
├─────────────────────────────────────────────┤
│  [Add Task Button]                          │
│                                             │
│  Task Grid (Responsive)                     │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐     │
│  │ Task 1  │  │ Task 2  │  │ Task 3  │     │
│  │         │  │         │  │         │     │
│  └─────────┘  └─────────┘  └─────────┘     │
│                                             │
└─────────────────────────────────────────────┘
```

**Features:**
- Header with gradient
- Add task button (opens modal)
- Task grid (responsive)
- Each task card shows:
  - Checkbox (toggle completion)
  - Title
  - Description (truncated)
  - Edit button
  - Delete button

**States:**
- Loading: Skeleton cards
- Empty: Empty state message
- Error: Error message with retry
- Success: Task grid

**Interactions:**
- Click "+ Add Task" → Open TaskForm modal
- Click checkbox → Toggle completion (optimistic UI)
- Click "Edit" → Open TaskForm modal with data
- Click "Delete" → Show confirmation modal

**Responsive:**
- Mobile: 1 column
- Tablet: 2 columns
- Desktop: 3-4 columns

## Route Protection

**Protected Routes:**
```tsx
// app/(dashboard)/layout.tsx
import { redirect } from 'next/navigation';
import { getSession } from '@/lib/auth';

export default async function DashboardLayout({ children }) {
  const session = await getSession();

  if (!session) {
    redirect('/signin');
  }

  return <>{children}</>;
}
```

**Public Routes:**
- `/` (landing page)
- `/signin` (sign in page)
- `/signup` (sign up page)