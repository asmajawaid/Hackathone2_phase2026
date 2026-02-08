import { Plus } from 'lucide-react';
import { Button } from '@/components/ui/Button';

interface EmptyStateProps {
  onAddTaskClick?: () => void;
}

export const EmptyState: React.FC<EmptyStateProps> = ({ onAddTaskClick }) => {
  return (
    <div className="glass-card flex flex-col items-center justify-center p-12 text-center">
      <div className="bg-latte-lavender/10 p-4 rounded-full mb-4">
        <Plus className="text-latte-lavender" size={32} />
      </div>
      <h3 className="text-xl font-semibold text-latte-text mb-2">No tasks yet</h3>
      <p className="text-latte-subtext1 mb-4">
        You don't have any tasks. Add one to get started!
      </p>
      {onAddTaskClick && (
        <Button variant="primary" onClick={onAddTaskClick}>
          Add Your First Task
        </Button>
      )}
    </div>
  );
};