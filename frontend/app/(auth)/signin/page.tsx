import { SignInForm } from '@/components/auth/SignInForm';
import Link from 'next/link';

export default function SigninPage() {
  return (
    <div className="flex flex-col items-center justify-center">
      <SignInForm />
      <div className="mt-6 text-center">
        <p className="text-latte-text">
          Don't have an account?{' '}
          <Link href="/signup" className="text-latte-lavender hover:underline">
            Sign up
          </Link>
        </p>
      </div>
    </div>
  );
}