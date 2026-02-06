import { ButtonProps } from '@/lib/types';
import clsx from 'clsx';
const cn = clsx;
import { Spinner } from './Spinner';

export const Button: React.FC<ButtonProps> = ({
  children,
  variant = 'primary',
  size = 'md',
  loading = false,
  icon,
  onClick,
  className = '',
  disabled = false,
}) => {
  const variantClasses = {
    primary: 'bg-gradient-lavender text-white shadow-lg hover:shadow-xl active:shadow-md',
    secondary: 'bg-latte-surface0 text-latte-text border border-latte-surface1 hover:bg-latte-surface1',
    ghost: 'bg-transparent text-latte-text hover:bg-latte-surface0',
    danger: 'bg-latte-red text-white hover:bg-red-600',
  };

  const sizeClasses = {
    sm: 'px-3 py-2 text-sm',
    md: 'px-6 py-3',
    lg: 'px-8 py-4 text-lg',
  };

  const disabledClass = disabled ? 'opacity-50 cursor-not-allowed' : '';

  const classes = cn(
    'font-semibold rounded-xl transition-all duration-200 flex items-center justify-center gap-2',
    'focus:outline-none focus:ring-2 focus:ring-latte-lavender focus:ring-opacity-50',
    variantClasses[variant],
    sizeClasses[size],
    disabledClass,
    className
  );

  return (
    <button
      className={classes}
      onClick={onClick}
      disabled={disabled || loading}
    >
      {loading && <Spinner size="sm" />}
      {icon && !loading && <span>{icon}</span>}
      {children}
    </button>
  );
};