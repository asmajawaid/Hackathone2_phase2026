'use client';

import { useState } from 'react';
import { Input } from '@/components/ui/Input';
import { Button } from '@/components/ui/Button';
import { authClient } from '@/lib/auth';
import { useRouter } from 'next/navigation';

export const SignUpForm = () => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    password: '',
    confirmPassword: '',
  });
  const [errors, setErrors] = useState<Record<string, string>>({});
  const [loading, setLoading] = useState(false);

  const router = useRouter();

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

    if (!formData.name.trim()) {
      newErrors.name = 'Name is required';
    }

    if (!formData.email.trim()) {
      newErrors.email = 'Email is required';
    } else if (!/\S+@\S+\.\S+/.test(formData.email)) {
      newErrors.email = 'Email is invalid';
    }

    if (!formData.password) {
      newErrors.password = 'Password is required';
    } else if (formData.password.length < 8) {
      newErrors.password = 'Password must be at least 8 characters';
    } else if (!/(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])/.test(formData.password)) {
      newErrors.password = 'Password must contain uppercase, lowercase, number, and special character';
    }

    if (formData.password !== formData.confirmPassword) {
      newErrors.confirmPassword = 'Passwords do not match';
    }

    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = async (e?: React.FormEvent) => {
    e?.preventDefault();

    if (!validate()) return;

    setLoading(true);
    try {
      const result = await authClient.signUp.email({
        email: formData.email,
        password: formData.password,
        name: formData.name,
      });

      if (result.error) {
        setErrors({ general: result.error.message || "Sign up failed. Please try again." });
      } else {
        // Redirect to dashboard after successful signup
        router.push('/dashboard/tasks');
      }
    } catch (error) {
      console.error('Signup error:', error);
      setErrors({ general: 'An unexpected error occurred' });
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="glass-card max-w-md w-full p-8">
      <h2 className="text-2xl font-bold text-center mb-6 text-latte-text">Create Account</h2>

      {errors.general && (
        <div className="mb-4 p-3 bg-latte-red/10 border border-latte-red rounded-lg text-latte-red">
          {errors.general}
        </div>
      )}

      <div className="space-y-4">
        <Input
          label="Name"
          placeholder="John Doe"
          value={formData.name}
          onChange={(value) => handleChange('name', value)}
          error={errors.name}
        />

        <Input
          label="Email"
          type="email"
          placeholder="email@example.com"
          value={formData.email}
          onChange={(value) => handleChange('email', value)}
          error={errors.email}
        />

        <Input
          label="Password"
          type="password"
          placeholder="••••••••"
          value={formData.password}
          onChange={(value) => handleChange('password', value)}
          error={errors.password}
        />

        <Input
          label="Confirm Password"
          type="password"
          placeholder="••••••••"
          value={formData.confirmPassword}
          onChange={(value) => handleChange('confirmPassword', value)}
          error={errors.confirmPassword}
        />

        <Button
          variant="primary"
          loading={loading}
          className="w-full mt-4"
          onClick={handleSubmit}
        >
          Sign Up
        </Button>
      </div>
    </div>
  );
};