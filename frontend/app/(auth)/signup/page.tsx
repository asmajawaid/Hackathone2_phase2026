import { SignUpForm } from '@/components/auth/SignUpForm';
import Link from 'next/link';

export default function SignupPage() {
  return (
    <div className="flex flex-col items-center justify-center">
      <SignUpForm />
      <div className="mt-6 text-center">
        <p className="text-latte-text">
          Already have an account?{' '}
          <Link href="/signin" className="text-latte-lavender hover:underline">
            Sign in
          </Link>
        </p>
      </div>
    </div>
  );
}