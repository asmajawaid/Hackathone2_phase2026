import clsx from 'clsx';
const cn = clsx;

interface SpinnerProps {
  size?: 'xs' | 'sm' | 'md' | 'lg';
  className?: string;
}

export const Spinner: React.FC<SpinnerProps> = ({
  size = 'md',
  className = ''
}) => {
  const sizeClasses = {
    xs: 'w-4 h-4 border-2',
    sm: 'w-5 h-5 border-2',
    md: 'w-8 h-8 border-4',
    lg: 'w-12 h-12 border-4',
  };

  const classes = cn(
    'animate-spin rounded-full border-latte-lavender border-t-transparent',
    sizeClasses[size],
    className
  );

  return <div className={classes}></div>;
};