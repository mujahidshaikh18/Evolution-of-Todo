'use client';

import { useState } from 'react';
import { useRouter } from 'next/navigation';
import { authService } from '@/lib/auth';
import Navbar from '@/components/Navbar';

export default function SignupPage() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [name, setName] = useState('');
  const [error, setError] = useState('');
  const router = useRouter();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    try {
      // Call the backend auth API
      const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/auth/register`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          email,
          password,
          name: name || email.split('@')[0]
        })
      });

      if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        throw new Error(errorData.detail || 'Signup failed. Please try again.');
      }

      const userData = await response.json();

      // Now login to get JWT token
      const loginResponse = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/auth/login`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          email,
          password
        })
      });

      if (!loginResponse.ok) {
        const errorData = await loginResponse.json().catch(() => ({}));
        throw new Error(errorData.detail || 'Login failed after registration. Please try again.');
      }

      const tokenData = await loginResponse.json();

      // Store the token and user data
      authService.setSession(tokenData.access_token, userData);

      // Redirect to dashboard
      router.push('/dashboard');
      router.refresh(); // Refresh to update the UI
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Signup failed. Please try again.');
      console.error('Signup error:', err);
    }
  };

  return (
    <div className="min-h-screen bg-black matrix-bg pt-16"> {/* Added pt-16 to account for fixed navbar */}
      <Navbar />
      <div className="flex min-h-[calc(100vh-4rem)] items-center justify-center py-12 px-4 sm:px-6 lg:px-8">
        <div className="w-full max-w-md bg-gray-900 rounded border border-green-500 p-8">
          <div className="text-center">
            <div className="mx-auto h-16 w-16 bg-black rounded-full flex items-center justify-center border border-green-500">
              <svg className="h-8 w-8 text-green-400" fill="none" stroke="#00ff41" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
              </svg>
            </div>
            <h2 className="mt-6 text-3xl font-bold neon-text">
              INIT_ACCOUNT
            </h2>
            <p className="mt-2 text-green-400 font-mono">
              ACCESS.GRANTED - START.ORGANIZING
            </p>
          </div>
          <form className="mt-8 space-y-6" onSubmit={handleSubmit}>
            <input type="hidden" name="remember" defaultValue="true" />

            <div className="space-y-4">
              <div>
                <label htmlFor="name" className="block text-sm font-medium text-green-400 mb-1 font-mono">
                  FULL.NAME
                </label>
                <input
                  id="name"
                  name="name"
                  type="text"
                  required
                  className="relative block w-full appearance-none rounded border border-green-500 px-4 py-3 bg-black text-green-400 placeholder-green-600 focus:z-10 focus:border-green-400 focus:outline-none focus:ring-green-500 sm:text-sm transition-colors font-mono"
                  placeholder="JOHN DOE"
                  value={name}
                  onChange={(e) => setName(e.target.value)}
                />
              </div>

              <div>
                <label htmlFor="email-address" className="block text-sm font-medium text-green-400 mb-1 font-mono">
                  EMAIL.ADDRESS
                </label>
                <input
                  id="email-address"
                  name="email"
                  type="email"
                  autoComplete="email"
                  required
                  className="relative block w-full appearance-none rounded border border-green-500 px-4 py-3 bg-black text-green-400 placeholder-green-600 focus:z-10 focus:border-green-400 focus:outline-none focus:ring-green-500 sm:text-sm transition-colors font-mono"
                  placeholder="JOHN@EXAMPLE.COM"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                />
              </div>

              <div>
                <label htmlFor="password" className="block text-sm font-medium text-green-400 mb-1 font-mono">
                  PASSWORD
                </label>
                <input
                  id="password"
                  name="password"
                  type="password"
                  autoComplete="current-password"
                  required
                  className="relative block w-full appearance-none rounded border border-green-500 px-4 py-3 bg-black text-green-400 placeholder-green-600 focus:z-10 focus:border-green-400 focus:outline-none focus:ring-green-500 sm:text-sm transition-colors font-mono"
                  placeholder="••••••••"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                />
              </div>
            </div>

            {error && (
              <div className="rounded border border-red-500 bg-gray-800 p-4">
                <div className="flex">
                  <div className="flex-shrink-0">
                    <svg className="h-5 w-5 text-red-400" fill="currentColor" viewBox="0 0 20 20">
                      <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clipRule="evenodd" />
                    </svg>
                  </div>
                  <div className="ml-3">
                    <h3 className="text-sm font-medium text-red-400 font-mono">{error}</h3>
                  </div>
                </div>
              </div>
            )}

            <div>
              <button
                type="submit"
                className="group relative w-full flex justify-center py-3 px-4 border border-transparent text-sm font-mono rounded border-green-500 bg-black text-green-400 hover:bg-gray-800 focus:outline-none focus:ring-2 focus:ring-green-500 transition-all duration-200"
              >
                SIGN.UP
              </button>
            </div>

            <div className="text-center text-sm text-green-400 font-mono">
              ALREADY.MEMBER?{' '}
              <a href="/auth/signin" className="font-medium text-green-300 hover:text-green-200 transition-colors">
                SIGN.IN
              </a>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
}