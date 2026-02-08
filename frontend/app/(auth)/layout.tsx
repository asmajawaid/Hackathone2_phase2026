import { GlassCard } from '@/components/ui/GlassCard';

export default function AuthLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <div className="min-h-screen bg-gradient-to-br from-latte-lavender to-latte-blue flex items-center justify-center p-4">
      {children}
    </div>
  );
}