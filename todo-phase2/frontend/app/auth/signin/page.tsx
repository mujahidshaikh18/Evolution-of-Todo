'use client';

import { useState } from 'react';
import { useRouter } from 'next/navigation';
import { authService } from '../../../lib/auth';
import Navbar from '../../../components/Navbar';

export default function SigninPage() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const router = useRouter();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    try {
      // Call the backend auth API
      const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://127.0.0.1:8000';
      const response = await fetch(`${API_BASE_URL}/auth/login`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          email,
          password
        })
      });

      if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        throw new Error(errorData.detail || 'Signin failed. Please try again.');
      }

      const tokenData = await response.json();

      // Decode the token get orignal id
      const base64Url = tokenData.access_token.split('.')[1];
      const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
      const decodedToken = JSON.parse(window.atob(base64));

      const userDetail = {
        id: decodedToken.sub, 
        email: email,
        name: email.split('@')[0]
      };

      // Store the token and user data
      authService.setSession(tokenData.access_token, userDetail);

      // Redirect to dashboard
      router.push('/dashboard');
      router.refresh(); // Refresh to update the UI
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Signin failed. Please try again.');
      console.error('Signin error:', err);
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
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M11 16l-4-4m0 0l4-4m-4 4h14m-5 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h7a3 3 0 013 3v1" />
              </svg>
            </div>
            <h2 className="mt-6 text-3xl font-bold neon-text">
              ACCESS.GATE
            </h2>
            <p className="mt-2 text-green-400 font-mono">
              VERIFY.CREDENTIALS - ENTER.SYSTEM
            </p>
          </div>
          <form className="mt-8 space-y-6" onSubmit={handleSubmit}>
            <input type="hidden" name="remember" defaultValue="true" />

            <div className="space-y-4">
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
                SIGN.IN
              </button>
            </div>

            <div className="text-center text-sm text-green-400 font-mono">
              NO.ACCESS.KEY?{' '}
              <a href="/auth/signup" className="font-medium text-green-300 hover:text-green-200 transition-colors">
                INIT.NEW
              </a>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
}
