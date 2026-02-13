<<<<<<< HEAD
import './globals.css';
import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'TASK.MATRIX',
  description: 'Cyberpunk-themed task management application',
  icons: {
    icon: '/favicon.ico',
  },
};
=======
import './globals.css'

export const metadata = {
  title: 'Todo App - Phase II',
  description: 'Full-Stack Web Application with Next.js and FastAPI',
}
>>>>>>> be27deab3d3f566b1231b8e6365d105beb813b09

export default function RootLayout({
  children,
}: {
<<<<<<< HEAD
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
=======
  children: React.ReactNode
}) {
  return (
    <html lang="en" className="dark">
      <body className={'bg-black text-green-400 matrix-bg font-mono'}>{children}</body>
    </html>
  )
>>>>>>> be27deab3d3f566b1231b8e6365d105beb813b09
}