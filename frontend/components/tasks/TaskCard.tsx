import { TaskCardProps } from '@/lib/types';
import clsx from 'clsx';
const cn = clsx;
import { CheckCircle2, Circle, Pencil, Trash2 } from 'lucide-react';

export const TaskCard: React.FC<TaskCardProps> = ({
  task,
  onToggleComplete,
  onEdit,
  onDelete,
}) => {
  return (
    <div className={cn(
      'glass-card p-4 flex items-start gap-3',
      task.completed && 'opacity-70'
    )}>
      <button
        onClick={() => onToggleComplete(task.id)}
        className="mt-1 flex-shrink-0"
        aria-label={task.completed ? 'Mark as incomplete' : 'Mark as complete'}
      >
        {task.completed ? (
          <CheckCircle2 className="text-latte-green" size={24} />
        ) : (
          <Circle className="text-latte-surface1" size={24} />
        )}
      </button>

      <div className="flex-1 min-w-0">
        <h3 className={cn(
          'font-medium text-latte-text break-words',
          task.completed && 'line-through'
        )}>
          {task.title}
        </h3>

        {task.description && (
          <p className={cn(
            'text-latte-subtext1 text-sm mt-1 break-words',
            task.completed && 'line-through'
          )}>
            {task.description}
          </p>
        )}

        <p className="text-xs text-latte-subtext0 mt-2">
          {new Date(task.updatedAt).toLocaleDateString()}
        </p>
      </div>

      <div className="flex gap-2 ml-auto flex-shrink-0">
        <button
          onClick={() => onEdit(task)}
          className="text-latte-subtext1 hover:text-latte-text transition-colors"
          aria-label="Edit task"
        >
          <Pencil size={18} />
        </button>
        <button
          onClick={() => onDelete(task.id)}
          className="text-latte-subtext1 hover:text-latte-red transition-colors"
          aria-label="Delete task"
        >
          <Trash2 size={18} />
        </button>
      </div>
    </div>
  );
};