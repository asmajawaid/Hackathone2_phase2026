'use client';

import { useState } from 'react';
import { Input } from '@/components/ui/Input';
import { Button } from '@/components/ui/Button';
import { authClient } from '@/lib/auth';
import { useRouter } from 'next/navigation';

export const SignInForm = () => {
  const [formData, setFormData] = useState({
    email: '',
    password: '',
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

    if (!formData.email.trim()) {
      newErrors.email = 'Email is required';
    } else if (!/\S+@\S+\.\S+/.test(formData.email)) {
      newErrors.email = 'Email is invalid';
    }

    if (!formData.password) {
      newErrors.password = 'Password is required';
    }

    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = async (e?: React.FormEvent) => {
    e?.preventDefault();

    if (!validate()) return;

    setLoading(true);
    try {
      const result = await authClient.signIn.email({
        email: formData.email,
        password: formData.password,
      });

      if (result.error) {
        setErrors({ general: result.error.message || "Sign in failed. Please try again." 
          
        });
      } else {
        // Redirect to dashboard after successful signin
        router.push('/dashboard/tasks');
      }
    } catch (error) {
      console.error('Signin error:', error);
      setErrors({ general: 'An unexpected error occurred' });
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="glass-card max-w-md w-full p-8">
      <h2 className="text-2xl font-bold text-center mb-6 text-latte-text">Welcome Back</h2>

      {errors.general && (
        <div className="mb-4 p-3 bg-latte-red/10 border border-latte-red rounded-lg text-latte-red">
          {errors.general}
        </div>
      )}

      <div className="space-y-4">
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

        <Button
          variant="primary"
          loading={loading}
          className="w-full mt-4"
          onClick={handleSubmit}
        >
          Sign In
        </Button>
      </div>
    </div>
  );
};