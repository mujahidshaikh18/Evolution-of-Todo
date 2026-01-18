# Next.js 16 Development & Deployment Guide

## Core Principles
- Use App Router architecture
- Maintain consistent import/export patterns
- Ensure Vercel deployment compatibility from the start
- Follow Next.js 16 best practices

## Project Structure
```
frontend/
├── app/
│   ├── layout.tsx
│   ├── page.tsx
│   ├── dashboard/
│   │   └── page.tsx
│   └── auth/
│       ├── signin/
│       │   └── page.tsx
│       └── signup/
│       └── page.tsx
├── components/
│   ├── TaskList.tsx
│   ├── TaskCard.tsx
│   ├── AddTaskModal.tsx
│   ├── EditTaskModal.tsx
│   └── Navbar.tsx
├── lib/
│   ├── auth.ts
│   ├── api-client.ts
│   └── types.ts
├── public/
├── package.json
├── tsconfig.json
└── next.config.js
```

## Import/Export Patterns
- Use relative imports consistently: `../lib/auth`, `../../components/Navbar`
- Avoid path aliases (`@/`) to prevent deployment issues
- Ensure file names match export names exactly
- Maintain consistent casing across all imports

## Vercel Deployment Best Practices
- Use standard build command: `next build`
- Ensure all dependencies are properly declared in package.json
- Test locally with `next build` before deploying
- Use compatible Node.js version (24.x)
- Include proper vercel.json configuration

## UI Consistency
- Maintain the cyberpunk/neon aesthetic
- Use consistent color scheme (green/black theme)
- Preserve all existing UI components and layouts
- Keep the same navigation and user experience

## Code Quality Standards
- Follow TypeScript best practices
- Maintain proper error handling
- Include proper loading states
- Ensure accessibility compliance
- Write comprehensive comments for complex logic

## Testing Approach
- Verify all routes work locally
- Test authentication flow
- Validate API integration
- Confirm responsive design
- Run build command to catch errors early

## Common Pitfalls to Avoid
- Path alias issues with Vercel deployment
- Case sensitivity mismatches
- Missing dependencies in package.json
- Incorrect import paths
- Turbopack vs webpack compatibility issues