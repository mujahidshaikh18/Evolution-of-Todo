import './globals.css'

export const metadata = {
  title: 'Todo App - Phase II',
  description: 'Full-Stack Web Application with Next.js and FastAPI',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en" className="dark">
      <body className={'bg-black text-green-400 matrix-bg font-mono'}>{children}</body>
    </html>
  )
}