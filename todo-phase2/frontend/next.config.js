/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,

  // Required for React 19 + modern caching behavior
  reactCompiler: true,

  // Vercel + Next 16 defaults, explicitly declared
  output: 'standalone',

  // Better error surfacing in production
  logging: {
    fetches: {
      fullUrl: true
    }
  }
}

module.exports = nextConfig