'use client';

import { useSession } from '@/lib/auth';
import { useEffect } from 'react';
import { useRouter } from 'next/navigation';
import { Spinner } from '@/components/ui/Spinner';

export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  const { data: session, isPending } = useSession();
  const router = useRouter();

  useEffect(() => {
    if (!isPending && !session) {
      router.push('/signin');
    }
  }, [session, isPending, router]);

  if (isPending) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <Spinner size="lg" />
      </div>
    );
  }

  if (!session) {
    return null; // Will be redirected by useEffect
  }

  return (
    <div className="min-h-screen bg-latte-base">
      <header className="bg-gradient-ocean p-4 shadow-md">
        <div className="container mx-auto flex justify-between items-center">
          <h1 className="text-xl font-bold text-white">Todo App</h1>
          <div className="flex items-center gap-4">
            <span className="text-white">{session.user.email}</span>
            <button
              onClick={() => {
                // Sign out and redirect to home
                window.location.href = '/';
              }}
              className="text-white hover:underline"
            >
              Logout
            </button>
          </div>
        </div>
      </header>
      <main className="container mx-auto p-4">
        {children}
      </main>
    </div>
  );
}