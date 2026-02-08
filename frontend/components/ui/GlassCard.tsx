import { GlassCardProps } from '@/lib/types';

export const GlassCard: React.FC<GlassCardProps> = ({
  children,
  className = '',
  hover = true,
  onClick
}) => {
  const baseClasses = 'bg-white/40 backdrop-blur-md border border-white/30 shadow-glass rounded-2xl p-6';
  const hoverClasses = hover
    ? 'hover:bg-white/50 hover:border-white/50 hover:shadow-glass-lg transition-all duration-300 hover:-translate-y-1 cursor-pointer'
    : '';

  const classes = `${baseClasses} ${hoverClasses} ${className}`;

  return (
    <div className={classes} onClick={onClick}>
      {children}
    </div>
  );
};