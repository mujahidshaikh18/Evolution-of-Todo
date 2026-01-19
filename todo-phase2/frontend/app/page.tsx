'use client';

import { useEffect } from 'react';
import { useRouter } from 'next/navigation';
import { authService } from '@/lib/auth';
import Navbar from '@/components/Navbar';

export default function HomePage() {
  const router = useRouter();

  useEffect(() => {
    // Delay the redirect to show the loading message
    const timer = setTimeout(() => {
      // Redirect to dashboard if user is authenticated, otherwise to signup
      if (authService.isAuthenticated()) {
        router.push('/dashboard');
      } else {
        router.push('/auth/signup');
      }
    }, 1000); // Wait 1 second before redirecting

    return () => clearTimeout(timer);
  }, [router]);

  return (
    <div className="min-h-screen bg-black matrix-bg pt-16"> {/* Added pt-16 to account for fixed navbar */}
      <Navbar />
      <div className="flex flex-col items-center justify-center min-h-[calc(100vh-4rem)] px-4 py-12">
        <div className="max-w-md w-full text-center">
          <div className="mx-auto w-24 h-24 bg-black rounded-full flex items-center justify-center mb-8 border border-green-500">
            <svg className="w-12 h-12 text-green-400" fill="none" stroke="#00ff41" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
            </svg>
          </div>
          <h1 className="text-5xl font-extrabold neon-text mb-4">
            TASK.MATRIX
          </h1>
          <p className="text-xl text-green-400 mb-8 font-mono">
            PRODUCTIVITY.PROTOCOL.ACTIVE
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <div className="animate-pulse text-green-400 font-mono">SYSTEM.REDIRECT.PENDING...</div>
          </div>
        </div>
      </div>
    </div>
  );
}