'use client';

import { authService } from '@/lib/auth';
import { User } from '@/lib/types';
import Link from 'next/link';
import { useEffect, useState } from 'react';

interface NavbarProps {
  onLogout?: () => void;
}

const Navbar: React.FC<NavbarProps> = ({ onLogout }) => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [user, setUser] = useState<User | null>(null);

  useEffect(() => {
    // Only run on client side
    if (typeof window !== 'undefined') {
      setIsAuthenticated(authService.isAuthenticated());
      setUser(authService.getUser());
    }
  }, []);

  const handleLogout = () => {
    authService.logout();
    setIsAuthenticated(false);
    setUser(null);
    if (onLogout) {
      onLogout();
    }
  };

  return (
    <nav className="bg-black border-b border-green-500 fixed top-0 left-0 right-0 z-50">
      <div className="container mx-auto px-4 py-3">
        <div className="flex justify-between items-center">
          <Link href="/" className="text-2xl font-bold flex items-center gap-2 neon-text">
            <svg className="w-8 h-8" fill="none" stroke="#00ff41" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
            </svg>
            <span>TODO.HACK</span>
          </Link>

          <div className="flex items-center space-x-4">
            {isAuthenticated ? (
              <div className="flex items-center space-x-4">
                <div className="hidden md:block px-3 py-1 rounded-full text-sm border border-green-500 neon-text">
                  <span>USER: {user?.name || user?.email}</span>
                </div>
                <button
                  onClick={handleLogout}
<<<<<<< HEAD
                  className="border border-green-500 bg-black text-green-400 shadow-[0_0_5px_#00ff41,_0_0_10px_#00ff41] transition-all duration-300 hover:bg-black/100 hover:shadow-[0_0_10px_#00ff41,_0_0_20px_#00ff41] py-2 px-4 rounded font-mono"
=======
                  className="neon-button py-2 px-4 rounded font-mono"
>>>>>>> be27deab3d3f566b1231b8e6365d105beb813b09
                >
                  <svg className="w-4 h-4 inline mr-1" fill="none" stroke="#00ff41" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" />
                  </svg>
                  LOGOUT
                </button>
              </div>
            ) : (
              <div className="flex space-x-2">
                <Link
                  href="/auth/signin"
<<<<<<< HEAD
                  className="border border-green-500 bg-black text-green-400 shadow-[0_0_5px_#00ff41,_0_0_10px_#00ff41] transition-all duration-300 hover:bg-black/100 hover:shadow-[0_0_10px_#00ff41,_0_0_20px_#00ff41] py-2 px-4 rounded font-mono"
=======
                  className="neon-button py-2 px-4 rounded font-mono"
>>>>>>> be27deab3d3f566b1231b8e6365d105beb813b09
                >
                  SIGN IN
                </Link>
                <Link
                  href="/auth/signup"
<<<<<<< HEAD
                  className="border border-green-500 bg-black text-green-400 shadow-[0_0_5px_#00ff41,_0_0_10px_#00ff41] transition-all duration-300 hover:bg-black/100 hover:shadow-[0_0_10px_#00ff41,_0_0_20px_#00ff41] py-2 px-4 rounded font-mono"
=======
                  className="neon-button py-2 px-4 rounded font-mono"
>>>>>>> be27deab3d3f566b1231b8e6365d105beb813b09
                >
                  SIGN UP
                </Link>
              </div>
            )}
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;