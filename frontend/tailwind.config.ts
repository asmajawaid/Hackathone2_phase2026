import type { Config } from 'tailwindcss';

const config: Config = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
    './app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        latte: {
          // Backgrounds
          base: '#eff1f5',
          mantle: '#e6e9ef',
          crust: '#dce0e8',

          // Text
          text: '#4c4f69',
          subtext1: '#5c5f77',
          subtext0: '#6c6f85',

          // Surfaces
          surface0: '#ccd0da',
          surface1: '#bcc0cc',
          surface2: '#acb0be',

          // Overlays
          overlay0: '#9ca0b0',
          overlay1: '#8c8fa1',
          overlay2: '#7c7f93',

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
        },
      },
      backgroundImage: {
        'gradient-lavender': 'linear-gradient(135deg, #7287fd 0%, #8839ef 100%)',
        'gradient-ocean': 'linear-gradient(135deg, #1e66f5 0%, #04a5e5 100%)',
        'gradient-sunset': 'linear-gradient(135deg, #fe640b 0%, #dc8a78 100%)',
        'gradient-forest': 'linear-gradient(135deg, #40a02b 0%, #179299 100%)',
        'gradient-glass': 'linear-gradient(135deg, rgba(255,255,255,0.4), rgba(255,255,255,0.1))',
      },
      backdropBlur: {
        xs: '2px',
        sm: '4px',
        md: '12px',
        lg: '16px',
        xl: '24px',
      },
      boxShadow: {
        glass: '0 8px 32px 0 rgba(124, 127, 147, 0.2)',
        'glass-lg': '0 12px 48px 0 rgba(124, 127, 147, 0.3)',
      },
      screens: {
        'xs': '475px',
        'sm': '640px',
        'md': '768px',
        'lg': '1024px',
        'xl': '1280px',
        '2xl': '1536px',
      },
      fontSize: {
        'xs': ['0.75rem', { lineHeight: '1rem' }],
        'sm': ['0.875rem', { lineHeight: '1.25rem' }],
        'base': ['1rem', { lineHeight: '1.5rem' }],
        'lg': ['1.125rem', { lineHeight: '1.75rem' }],
        'xl': ['1.25rem', { lineHeight: '1.75rem' }],
        '2xl': ['1.5rem', { lineHeight: '2rem' }],
        '3xl': ['1.875rem', { lineHeight: '2.25rem' }],
        '4xl': ['2.25rem', { lineHeight: '2.5rem' }],
      },
      transitionTimingFunction: {
        'smooth': 'cubic-bezier(0.4, 0, 0.2, 1)',
        'bounce': 'cubic-bezier(0.68, -0.55, 0.265, 1.55)',
      },
    },
  },
  plugins: [],
};
export default config;