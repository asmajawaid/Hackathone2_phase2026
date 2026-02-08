import type { Metadata } from 'next';
import { Inter } from 'next/font/google';
import './globals.css'; // Import CSS from the same directory

const inter = Inter({ subsets: ['latin'] });

export const metadata: Metadata = {
  title: 'Todo App - Phase 2',
  description: 'Modern todo application with glass morphism design',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className={inter.className}>{children}</body>
    </html>
  );
}