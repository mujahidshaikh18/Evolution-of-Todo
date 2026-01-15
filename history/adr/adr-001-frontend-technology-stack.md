# ADR-001: Frontend Technology Stack

> **Scope**: Document decision clusters, not individual technology choices. Group related decisions that work together (e.g., "Frontend Stack" not separate ADRs for framework, styling, deployment).

- **Status:** Accepted
- **Date:** 2026-01-09
- **Feature:** phase2-web
- **Context:** Need to select a modern, scalable frontend stack that integrates well with the backend API, provides good developer experience, and supports responsive UI requirements for the todo application.

<!-- Significance checklist (ALL must be true to justify this ADR)
     1) Impact: Long-term consequence for architecture/platform/security?
     2) Alternatives: Multiple viable options considered with tradeoffs?
     3) Scope: Cross-cutting concern (not an isolated detail)?
     If any are false, prefer capturing as a PHR note instead of an ADR. -->

## Decision

Selected Next.js 16+ with App Router as the frontend framework, integrated with Tailwind CSS for styling, and deployed on Vercel. This stack provides a cohesive solution for building the responsive web application.

- Framework: Next.js 16+ (App Router)
- Language: TypeScript 5.3+
- Styling: Tailwind CSS
- Deployment: Vercel (as per constitution)
- State Management: React useState and Context (appropriate for Phase II scope)

## Consequences

### Positive

- Excellent developer experience with integrated routing via App Router
- Strong TypeScript support and type safety throughout
- Built-in server-side rendering and static generation capabilities
- Robust ecosystem and community support
- Responsive design capabilities with Tailwind CSS utility classes
- Performance optimizations out of the box
- SEO-friendly due to server-side rendering capabilities

### Negative

- Learning curve for developers unfamiliar with Next.js App Router
- Potential vendor lock-in to Vercel for optimal deployment experience
- Bundle size considerations with the full Next.js framework
- Complexity overhead for a simple todo application

## Alternatives Considered

Alternative Stack A: Create React App + traditional CSS/Sass + self-hosted
- Why rejected: Outdated architecture, lacks server-side rendering benefits, no longer maintained as actively

Alternative Stack B: Remix + styled-components + Cloudflare Pages
- Why rejected: Would violate constitution requirements for Next.js, different mental model than specified

Alternative Stack C: Pure client-side React + traditional CSS + any hosting
- Why rejected: Would impact SEO and initial load performance, lacks Next.js integrated features

## References

- Feature Spec: specs/phase2-web/spec.md
- Implementation Plan: specs/phase2-web/plan.md
- Related ADRs:
- Evaluator Evidence: specs/phase2-web/research.md