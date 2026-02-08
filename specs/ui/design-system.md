# Evolution of Todo - Phase 2 Design System Documentation

## Design System Overview

**Name:** Latte Glass Design System
**Version:** 1.0.0
**Theme:** Light, warm, modern with glass morphism
**Inspiration:** Catppuccin Latte + Glass morphism trends

## Color Palette

### Base Colors (Backgrounds & Surfaces)
```typescript
// tailwind.config.ts
colors: {
  latte: {
    // Primary backgrounds
    base: '#eff1f5',      // Main page background
    mantle: '#e6e9ef',    // Slightly darker bg (cards)
    crust: '#dce0e8',     // Input backgrounds

    // Text colors
    text: '#4c4f69',      // Primary text
    subtext1: '#5c5f77',  // Secondary text
    subtext0: '#6c6f85',  // Tertiary text (placeholders)

    // Surface elevations
    surface0: '#ccd0da',  // Elevated elements
    surface1: '#bcc0cc',  // Hover states
    surface2: '#acb0be',  // Pressed/active states

    // Overlays (borders, dividers)
    overlay0: '#9ca0b0',  // Light dividers
    overlay1: '#8c8fa1',  // Medium borders
    overlay2: '#7c7f93',  // Strong borders

    // Accent colors (vibrant)
    lavender: '#7287fd',  // Primary brand
    blue: '#1e66f5',      // Links, info
    sapphire: '#209fb5',  // Secondary actions
    sky: '#04a5e5',       // Highlights
    teal: '#179299',      // Success alt
    green: '#40a02b',     // Success
    yellow: '#df8e1d',    // Warning
    peach: '#fe640b',     // Accent warm
    maroon: '#e64553',    // Error alt
    red: '#d20f39',       // Error, danger
    mauve: '#8839ef',     // Purple accent
    pink: '#ea76cb',      // Pink accent
    flamingo: '#dd7878',  // Coral accent
    rosewater: '#dc8a78', // Rose accent
  }
}
```

### Color Usage Guidelines

| Purpose | Color | Usage |
|---------|-------|-------|
| Page background | `latte-base` | Main app background |
| Card background | `latte-mantle` | Task cards, modals |
| Input background | `latte-crust` | Form inputs |
| Primary text | `latte-text` | Headings, body text |
| Secondary text | `latte-subtext1` | Labels, captions |
| Placeholder text | `latte-subtext0` | Input placeholders |
| Borders | `latte-overlay1` | Default borders |
| Primary CTA | `latte-lavender` | Main action buttons |
| Links | `latte-blue` | Hyperlinks |
| Success | `latte-green` | Success messages, checkmarks |
| Error | `latte-red` | Error messages, delete |
| Warning | `latte-yellow` | Warnings, cautions |

## Glass Morphism

### Glass Card Base
```css
.glass-card {
  background: rgba(230, 233, 239, 0.4);  /* latte-mantle with 40% opacity */
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid rgba(156, 160, 176, 0.2);  /* latte-overlay0 */
  box-shadow: 0 8px 32px 0 rgba(124, 127, 147, 0.15);
  border-radius: 16px;
}
```

### Tailwind Utility Classes
```typescript
// Add to tailwind.config.ts
extend: {
  backdropBlur: {
    xs: '2px',
    sm: '4px',
    DEFAULT: '8px',
    md: '12px',
    lg: '16px',
    xl: '24px',
    '2xl': '40px',
  },
  boxShadow: {
    'glass': '0 8px 32px 0 rgba(124, 127, 147, 0.15)',
    'glass-lg': '0 8px 32px 0 rgba(124, 127, 147, 0.25)',
  }
}
```

### Glass Component Classes
```css
/* Base glass card */
.glass {
  @apply bg-latte-mantle/40 backdrop-blur-md border border-latte-overlay0/20 shadow-glass rounded-2xl;
}

/* Glass on hover */
.glass-hover {
  @apply hover:bg-latte-mantle/50 hover:border-latte-overlay0/30 hover:shadow-glass-lg;
}

/* Strong glass (modals) */
.glass-strong {
  @apply bg-latte-mantle/60 backdrop-blur-xl border border-latte-overlay1/30 shadow-glass-lg;
}

/* Subtle glass (inputs) */
.glass-subtle {
  @apply bg-latte-crust/50 backdrop-blur-sm border border-latte-overlay0/20;
}
```

## Gradients

### Gradient Definitions
```typescript
// Add to tailwind.config.ts
backgroundImage: {
  // Primary gradients
  'gradient-lavender': 'linear-gradient(135deg, #7287fd 0%, #8839ef 100%)',
  'gradient-ocean': 'linear-gradient(135deg, #1e66f5 0%, #04a5e5 100%)',
  'gradient-sunset': 'linear-gradient(135deg, #fe640b 0%, #dc8a78 100%)',
  'gradient-forest': 'linear-gradient(135deg, #40a02b 0%, #179299 100%)',

  // Glass gradients (for overlays)
  'gradient-glass-light': 'linear-gradient(135deg, rgba(255,255,255,0.4), rgba(255,255,255,0.1))',
  'gradient-glass-dark': 'linear-gradient(135deg, rgba(76,79,105,0.3), rgba(76,79,105,0.1))',

  // Radial gradients
  'gradient-radial': 'radial-gradient(circle, var(--tw-gradient-stops))',
  'gradient-radial-lavender': 'radial-gradient(circle, #7287fd 0%, #8839ef 100%)',
}
```

### Gradient Usage
- **Buttons:** `gradient-lavender` for primary CTAs
- **Headers:** `gradient-ocean` for page headers
- **Accents:** `gradient-sunset` for warm highlights
- **Success:** `gradient-forest` for success states
- **Overlays:** `gradient-glass-light` on glass cards

## Typography

### Font Family
```typescript
// tailwind.config.ts
fontFamily: {
  sans: ['Inter', 'system-ui', 'sans-serif'],
  mono: ['JetBrains Mono', 'monospace'],
}
```

### Font Scale
```typescript
fontSize: {
  'xs': ['0.75rem', { lineHeight: '1rem' }],      // 12px
  'sm': ['0.875rem', { lineHeight: '1.25rem' }],  // 14px
  'base': ['1rem', { lineHeight: '1.5rem' }],     // 16px
  'lg': ['1.125rem', { lineHeight: '1.75rem' }],  // 18px
  'xl': ['1.25rem', { lineHeight: '1.75rem' }],   // 20px
  '2xl': ['1.5rem', { lineHeight: '2rem' }],      // 24px
  '3xl': ['1.875rem', { lineHeight: '2.25rem' }], // 30px
  '4xl': ['2.25rem', { lineHeight: '2.5rem' }],   // 36px
  '5xl': ['3rem', { lineHeight: '1' }],           // 48px
}
```

### Font Weights
- **Regular:** 400 (body text)
- **Medium:** 500 (labels)
- **Semibold:** 600 (headings)
- **Bold:** 700 (emphasis)

### Usage Guidelines
| Element | Font Size | Weight | Color |
|---------|-----------|--------|-------|
| H1 | 3xl-4xl | Semibold | latte-text |
| H2 | 2xl-3xl | Semibold | latte-text |
| H3 | xl-2xl | Semibold | latte-text |
| Body | base | Regular | latte-text |
| Caption | sm | Regular | latte-subtext1 |
| Label | sm | Medium | latte-subtext1 |
| Button | base | Semibold | white |

## Spacing Scale
```typescript
spacing: {
  '0': '0px',
  '1': '0.25rem',   // 4px
  '2': '0.5rem',    // 8px
  '3': '0.75rem',   // 12px
  '4': '1rem',      // 16px
  '5': '1.25rem',   // 20px
  '6': '1.5rem',    // 24px
  '8': '2rem',      // 32px
  '10': '2.5rem',   // 40px
  '12': '3rem',     // 48px
  '16': '4rem',     // 64px
  '20': '5rem',     // 80px
}
```

## Border Radius
```typescript
borderRadius: {
  'none': '0',
  'sm': '0.25rem',  // 4px
  'DEFAULT': '0.5rem', // 8px
  'md': '0.75rem',  // 12px
  'lg': '1rem',     // 16px
  'xl': '1.5rem',   // 24px
  '2xl': '2rem',    // 32px
  'full': '9999px', // Fully rounded
}
```

## Shadows
```typescript
boxShadow: {
  'sm': '0 1px 2px 0 rgba(124, 127, 147, 0.05)',
  'DEFAULT': '0 1px 3px 0 rgba(124, 127, 147, 0.1), 0 1px 2px -1px rgba(124, 127, 147, 0.1)',
  'md': '0 4px 6px -1px rgba(124, 127, 147, 0.1), 0 2px 4px -2px rgba(124, 127, 147, 0.1)',
  'lg': '0 10px 15px -3px rgba(124, 127, 147, 0.1), 0 4px 6px -4px rgba(124, 127, 147, 0.1)',
  'xl': '0 20px 25px -5px rgba(124, 127, 147, 0.1), 0 8px 10px -6px rgba(124, 127, 147, 0.1)',
  'glass': '0 8px 32px 0 rgba(124, 127, 147, 0.15)',
  'glass-lg': '0 8px 32px 0 rgba(124, 127, 147, 0.25)',
}
```

## Animations & Transitions

### Transition Durations
```typescript
transitionDuration: {
  '75': '75ms',
  '100': '100ms',
  '150': '150ms',
  '200': '200ms',
  '300': '300ms',
  '500': '500ms',
  '700': '700ms',
  '1000': '1000ms',
}
```

### Timing Functions
```typescript
transitionTimingFunction: {
  'DEFAULT': 'cubic-bezier(0.4, 0, 0.2, 1)',
  'linear': 'linear',
  'in': 'cubic-bezier(0.4, 0, 1, 1)',
  'out': 'cubic-bezier(0, 0, 0.2, 1)',
  'in-out': 'cubic-bezier(0.4, 0, 0.2, 1)',
  'bounce': 'cubic-bezier(0.68, -0.55, 0.265, 1.55)',
  'smooth': 'cubic-bezier(0.4, 0, 0.2, 1)',
}
```

### Keyframe Animations
```typescript
keyframes: {
  'fade-in': {
    '0%': { opacity: '0' },
    '100%': { opacity: '1' },
  },
  'fade-out': {
    '0%': { opacity: '1' },
    '100%': { opacity: '0' },
  },
  'slide-up': {
    '0%': { transform: 'translateY(10px)', opacity: '0' },
    '100%': { transform: 'translateY(0)', opacity: '1' },
  },
  'slide-down': {
    '0%': { transform: 'translateY(-10px)', opacity: '0' },
    '100%': { transform: 'translateY(0)', opacity: '1' },
  },
  'scale-in': {
    '0%': { transform: 'scale(0.95)', opacity: '0' },
    '100%': { transform: 'scale(1)', opacity: '1' },
  },
  'pulse-soft': {
    '0%, 100%': { opacity: '1' },
    '50%': { opacity: '0.8' },
  },
}

animation: {
  'fade-in': 'fade-in 200ms ease-out',
  'fade-out': 'fade-out 200ms ease-in',
  'slide-up': 'slide-up 300ms ease-out',
  'slide-down': 'slide-down 300ms ease-out',
  'scale-in': 'scale-in 200ms ease-out',
  'pulse-soft': 'pulse-soft 2s ease-in-out infinite',
}
```

## Responsive Breakpoints
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

### Breakpoint Usage
- **xs-sm:** Mobile phones
- **md:** Tablets
- **lg-xl:** Desktops
- **2xl:** Large desktops

## Component Patterns

### Glass Card
```tsx
<div className="
  bg-latte-mantle/40
  backdrop-blur-md
  rounded-2xl
  border border-latte-overlay0/20
  shadow-glass
  p-6
  transition-all duration-300
  hover:bg-latte-mantle/50
  hover:shadow-glass-lg
  hover:-translate-y-1
">
  {/* Content */}
</div>
```

### Gradient Button (Primary)
```tsx
<button className="
  bg-gradient-lavender
  text-white
  font-semibold
  px-6 py-3
  rounded-lg
  shadow-lg shadow-latte-lavender/30
  transition-all duration-200
  hover:shadow-xl hover:shadow-latte-lavender/50
  hover:scale-105
  active:scale-95
  disabled:opacity-50 disabled:cursor-not-allowed
">
  Click Me
</button>
```

### Glass Input
```tsx
<input className="
  w-full
  bg-latte-crust/50
  backdrop-blur-sm
  rounded-lg
  border border-latte-overlay0/30
  px-4 py-3
  text-latte-text
  placeholder:text-latte-subtext0
  transition-all duration-200
  focus:border-latte-lavender
  focus:ring-2 focus:ring-latte-lavender/20
  focus:outline-none
"/>
```

### Modal Overlay
```tsx
<div className="
  fixed inset-0
  bg-latte-text/20
  backdrop-blur-sm
  flex items-center justify-center
  z-50
  animate-fade-in
">
  <div className="
    bg-latte-mantle/60
    backdrop-blur-xl
    rounded-2xl
    border border-latte-overlay1/30
    shadow-glass-lg
    max-w-lg w-full
    p-6
    animate-scale-in
  ">
    {/* Modal content */}
  </div>
</div>
```

## Accessibility

### Focus States
```css
/* All interactive elements */
.focus-visible:focus {
  @apply outline-none ring-2 ring-latte-lavender ring-offset-2 ring-offset-latte-base;
}
```

### Color Contrast
All text must meet WCAG 2.1 AA standards:
- Normal text: 4.5:1 contrast ratio
- Large text: 3:1 contrast ratio

### Keyboard Navigation
- All interactive elements must be keyboard accessible
- Tab order must be logical
- Focus indicators must be visible

## Design Tokens Export
```typescript
// design-tokens.ts
export const tokens = {
  colors: {
    base: '#eff1f5',
    lavender: '#7287fd',
    // ... all colors
  },
  spacing: {
    xs: '0.25rem',
    sm: '0.5rem',
    // ... all spacing
  },
  typography: {
    fontFamily: 'Inter',
    sizes: {
      xs: '0.75rem',
      // ... all sizes
    }
  }
}
```