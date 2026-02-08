'use client';

import { useSession } from '@/lib/auth';
import { useTasks } from '@/hooks/useTasks';
import { TaskList } from '@/components/tasks/TaskList';
import { Modal } from '@/components/ui/Modal';
import { TaskForm } from '@/components/tasks/TaskForm';
import { EmptyState } from '@/components/tasks/EmptyState';
import { Button } from '@/components/ui/Button';
import { Plus } from 'lucide-react';
import { useState } from 'react';

export default function TasksPage() {
  const { data: session } = useSession();
  const userId = session?.user?.id;

  const {
    tasks,
    loading,
    error,
    createTask,
    updateTask,
    deleteTask,
    toggleComplete,
  } = useTasks(userId || '');

  const [isModalOpen, setIsModalOpen] = useState(false);
  const [editingTask, setEditingTask] = useState<any>(null);
  const [formLoading, setFormLoading] = useState(false);

  if (!userId) {
    return null; // User will be redirected by layout
  }

  const handleOpenModal = (task?: any) => {
    setEditingTask(task || null);
    setIsModalOpen(true);
  };

  const handleCloseModal = () => {
    setIsModalOpen(false);
    setEditingTask(null);
    setFormLoading(false);
  };

  const handleSubmit = async (taskData: { title: string; description?: string }) => {
    setFormLoading(true);
    try {
      if (editingTask) {
        await updateTask(editingTask.id, taskData);
      } else {
        await createTask(taskData);
      }
      handleCloseModal();
    } catch (err) {
      console.error('Error saving task:', err);
    } finally {
      setFormLoading(false);
    }
  };

  const handleDelete = async (id: number) => {
    if (window.confirm('Are you sure you want to delete this task?')) {
      try {
        await deleteTask(id);
      } catch (err) {
        console.error('Error deleting task:', err);
      }
    }
  };

  return (
    <div>
      <div className="flex justify-between items-center mb-6">
        <h2 className="text-2xl font-bold text-latte-text">My Tasks</h2>
        <Button
          variant="primary"
          onClick={() => handleOpenModal()}
          icon={<Plus size={18} />}
        >
          Add Task
        </Button>
      </div>

      {tasks.length === 0 && !loading ? (
        <EmptyState onAddTaskClick={() => handleOpenModal()} />
      ) : (
        <TaskList
          tasks={tasks}
          loading={loading}
          error={error}
          onToggleComplete={toggleComplete}
          onEdit={handleOpenModal}
          onDelete={handleDelete}
        />
      )}

      <Modal
        isOpen={isModalOpen}
        onClose={handleCloseModal}
        title={editingTask ? 'Edit Task' : 'Add New Task'}
      >
        <TaskForm
          task={editingTask}
          onSubmit={handleSubmit}
          onCancel={handleCloseModal}
          loading={formLoading}
        />
      </Modal>
    </div>
  );
}