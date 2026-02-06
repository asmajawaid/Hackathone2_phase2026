import { InputProps } from '@/lib/types';
import clsx from 'clsx';
const cn = clsx;

export const Input: React.FC<InputProps> = ({
  label,
  placeholder,
  value,
  onChange,
  error,
  className = '',
  type = 'text',
}) => {
  const baseClasses = 'w-full bg-white/30 backdrop-blur-sm border border-white/30 rounded-xl px-4 py-3 focus:border-latte-lavender focus:ring-2 focus:ring-latte-lavender/20 transition-all duration-200';
  const errorClasses = error ? 'border-latte-red focus:border-latte-red focus:ring-latte-red/20' : '';

  const classes = cn(baseClasses, errorClasses, className);

  return (
    <div className="w-full">
      {label && (
        <label className="block text-latte-text mb-2 font-medium">
          {label}
        </label>
      )}
      <input
        type={type}
        placeholder={placeholder}
        value={value}
        onChange={(e) => onChange(e.target.value)}
        className={classes}
      />
      {error && (
        <p className="text-latte-red mt-1 text-sm">{error}</p>
      )}
    </div>
  );
};