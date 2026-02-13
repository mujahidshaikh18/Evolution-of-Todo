import './globals.css';
import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'TASK.MATRIX',
  description: 'Cyberpunk-themed task management application',
  icons: {
    icon: '/favicon.ico',
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className="matrix-bg">
        <div className="relative z-10">
          <main className="min-h-screen">
            {children}
          </main>
        </div>
      </body>
    </html>
  );
}