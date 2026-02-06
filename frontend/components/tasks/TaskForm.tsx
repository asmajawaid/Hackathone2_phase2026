import { useState, useEffect } from 'react';
import { Input } from '@/components/ui/Input';
import { Button } from '@/components/ui/Button';
import { Task } from '@/lib/types';

interface TaskFormProps {
  task?: Task;
  onSubmit: (taskData: { title: string; description?: string }) => void;
  onCancel: () => void;
  loading?: boolean;
}

export const TaskForm: React.FC<TaskFormProps> = ({
  task,
  onSubmit,
  onCancel,
  loading = false,
}) => {
  const [formData, setFormData] = useState({
    title: '',
    description: '',
  });
  const [errors, setErrors] = useState<Record<string, string>>({});

  useEffect(() => {
    if (task) {
      setFormData({
        title: task.title,
        description: task.description || '',
      });
    } else {
      setFormData({
        title: '',
        description: '',
      });
    }
  }, [task]);

  const handleChange = (field: keyof typeof formData, value: string) => {
    setFormData(prev => ({ ...prev, [field]: value }));
    // Clear error when user starts typing
    if (errors[field]) {
      setErrors(prev => {
        const newErrors = { ...prev };
        delete newErrors[field];
        return newErrors;
      });
    }
  };

  const validate = (): boolean => {
    const newErrors: Record<string, string> = {};

    if (!formData.title.trim()) {
      newErrors.title = 'Title is required';
    } else if (formData.title.length > 200) {
      newErrors.title = 'Title must be 200 characters or less';
    }

    if (formData.description && formData.description.length > 1000) {
      newErrors.description = 'Description must be 1000 characters or less';
    }

    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = (e?: React.FormEvent) => {
    e?.preventDefault();

    if (!validate()) return;

    onSubmit({
      title: formData.title.trim(),
      description: formData.description.trim() || undefined,
    });
  };

  return (
    <div className="space-y-4">
      <Input
        label="Title"
        placeholder="Task title"
        value={formData.title}
        onChange={(value) => handleChange('title', value)}
        error={errors.title}
      />

      <Input
        label="Description"
        placeholder="Task description (optional)"
        value={formData.description}
        onChange={(value) => handleChange('description', value)}
        error={errors.description}
      />

      <div className="flex gap-3 pt-2">
        <Button
          variant="primary"
          loading={loading}
          className="flex-1"
          onClick={() => handleSubmit()}
        >
          {task ? 'Update Task' : 'Add Task'}
        </Button>
        <Button
          variant="secondary"
          onClick={onCancel}
        >
          Cancel
        </Button>
      </div>
    </div>
  );
};