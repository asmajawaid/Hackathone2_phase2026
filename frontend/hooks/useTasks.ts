import { useState, useEffect } from 'react';
import { Task } from '../lib/types';
import { getTasks, createTask, updateTask, deleteTask, toggleComplete } from '../lib/api';

export const useTasks = (userId: string) => {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);

  // Fetch tasks on mount
  useEffect(() => {
    fetchTasks();
  }, [userId]);

  const fetchTasks = async () => {
    setLoading(true);
    setError(null);
    try {
      const fetchedTasks = await getTasks(userId);
      setTasks(fetchedTasks);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to fetch tasks');
    } finally {
      setLoading(false);
    }
  };

  const createTaskHandler = async (input: { title: string; description?: string }) => {
    setLoading(true);
    setError(null);
    try {
      // Optimistic update
      const newTask: Task = {
        id: Date.now(), // Temporary ID until server response
        userId,
        title: input.title,
        description: input.description,
        completed: false,
        createdAt: new Date().toISOString(),
        updatedAt: new Date().toISOString(),
      };
      setTasks(prev => [...prev, newTask]);

      const createdTask = await createTask(userId, input);
      setTasks(prev => prev.map(t => t.id === newTask.id ? createdTask : t));
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to create task');
      // Revert optimistic update if needed
      setTasks(prev => prev.filter(t => t.id !== Date.now()));
    } finally {
      setLoading(false);
    }
  };

  const updateTaskHandler = async (id: number, input: { title?: string; description?: string }) => {
    setLoading(true);
    setError(null);
    try {
      // Optimistic update
      setTasks(prev => prev.map(t =>
        t.id === id ? { ...t, ...input, updatedAt: new Date().toISOString() } : t
      ));

      const updatedTask = await updateTask(userId, id, input);
      setTasks(prev => prev.map(t => t.id === id ? updatedTask : t));
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to update task');
      // Revert optimistic update if needed
      fetchTasks(); // Refresh from server
    } finally {
      setLoading(false);
    }
  };

  const deleteTaskHandler = async (id: number) => {
    setLoading(true);
    setError(null);
    try {
      // Optimistic update
      setTasks(prev => prev.filter(t => t.id !== id));

      await deleteTask(userId, id);
      // No need to update state as we already filtered it out
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to delete task');
      // Revert optimistic update if needed
      fetchTasks(); // Refresh from server
    } finally {
      setLoading(false);
    }
  };

  const toggleCompleteHandler = async (id: number) => {
    setLoading(true);
    setError(null);
    try {
      // Optimistic update
      setTasks(prev => prev.map(t =>
        t.id === id ? { ...t, completed: !t.completed, updatedAt: new Date().toISOString() } : t
      ));

      const updatedTask = await toggleComplete(userId, id);
      setTasks(prev => prev.map(t => t.id === id ? updatedTask : t));
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to toggle task completion');
      // Revert optimistic update if needed
      fetchTasks(); // Refresh from server
    } finally {
      setLoading(false);
    }
  };

  return {
    tasks,
    loading,
    error,
    fetchTasks,
    createTask: createTaskHandler,
    updateTask: updateTaskHandler,
    deleteTask: deleteTaskHandler,
    toggleComplete: toggleCompleteHandler,
  };
};