'use client';

import Link from 'next/link';
import { Button } from '@/components/ui/Button';

export default function HomePage() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-latte-lavender to-latte-blue flex flex-col items-center justify-center p-4">
      <div className="max-w-4xl w-full text-center">
        <h1 className="text-4xl md:text-6xl font-bold text-white mb-6">
          Organize Your Life
        </h1>
        <p className="text-xl md:text-2xl text-latte-surface0 mb-10">
          A beautiful, modern todo application with glass morphism design
        </p>

        <div className="flex flex-col sm:flex-row gap-4 justify-center">
          <Link href="/signup">
            <Button variant="primary" size="lg">
              Get Started
            </Button>
          </Link>
          <Link href="/signin">
            <Button variant="secondary" size="lg">
              Sign In
            </Button>
          </Link>
        </div>

        <div className="mt-16 grid grid-cols-1 md:grid-cols-3 gap-6">
          <div className="glass-card p-6">
            <h3 className="text-xl font-semibold text-latte-lavender mb-2">Task Management</h3>
            <p className="text-latte-subtext1">Create, update, and manage your tasks efficiently</p>
          </div>
          <div className="glass-card p-6">
            <h3 className="text-xl font-semibold text-latte-lavender mb-2">Secure Auth</h3>
            <p className="text-latte-subtext1">Protect your data with secure authentication</p>
          </div>
          <div className="glass-card p-6">
            <h3 className="text-xl font-semibold text-latte-lavender mb-2">Beautiful UI</h3>
            <p className="text-latte-subtext1">Enjoy a modern glass morphism interface</p>
          </div>
        </div>
      </div>
    </div>
  );
}