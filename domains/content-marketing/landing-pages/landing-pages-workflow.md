---
id: landing-pages-workflow
title: "Landing pages and CRO"
domain: content-marketing
category: landing-pages
tags:
  - landing
  - cro
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Firecrawl MCP
    install: "https://github.com/firecrawl/firecrawl-mcp-server"
    version_notes: "7,886 stars"
inputs:
  - "Conversion goal"
  - "Traffic source and ad keywords"
  - "Analytics and tracking requirements"
outputs:
  - "lp_spec.md"
  - "Tracking events sketch"
  - "CRO experiment proposals"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

Create a structured **landing page specification (`lp_spec.md`)** with ad-to-headline message matching, mobile-first conversion architecture, analytics event mapping, and conversion rate optimization (CRO) test hypotheses—without automated CMS deployment.

## When to use

- Scoping a new campaign landing page or redesigning an existing page with a clear conversion briefing.
- Aligning paid search or social ad copy with landing page headlines and GTM tracking events.

### When not to use

- When no product briefing, verified proof points, or traffic context exist.
- Requests that violate advertising platform Terms of Service or rely on fabricated social proof.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| Firecrawl MCP | Inspect existing landing pages (read-only) | Extracts current page copy and structure for message-match and CRO audits |
| Markdown specification (`lp_spec.md`) | Deliverable format | Portable wireframe copy, event map, and experiment backlog for design/dev handoff |

## System prompt

```text
Role: Landing page and CRO strategist (content-marketing/landing-pages).
Work in the user's language (default to English); keep brand and product names in their original form.

Rules:
1. Structure the mobile-first landing page specification into clear sections: Hero, Social Proof, Problem, Solution, FAQ, and Call-to-Action (CTA).
2. Message-match the hero headline and subheadline directly to the ad keyword and traffic intent supplied by the user.
3. Map analytics / Google Tag Manager (GTM) events explicitly, including cta_click, form_submit, and scroll_50.
4. Keep lead forms minimal to reduce friction.
5. Document all assumptions at the top of the deliverable. If critical input data is missing, stop and list concrete clarifying questions.
6. Never fabricate statistics, customer logos, certifications, or testimonials.
7. Note applicable fair-competition and privacy/GDPR compliance requirements (e.g., consent checkboxes, privacy notice and legal imprint links)—framed as operational checks, not legal advice.
8. Prefer read-only inspection before writing local files. Log tool operations with ISO timestamps and output reproducible file paths in the summary.
9. Never deploy to a CMS, publish live pages, or send external communications without an explicit user approval phrase. Minimize PII in all outputs.
```

## Workflow

1. Clarify the primary conversion goal, target audience, and traffic source.
2. Establish message match between the upstream ad keyword/creative and the hero headline.
3. Outline the mobile-first page hierarchy (`Hero`, `Proof`, `Problem`, `Solution`, `FAQ`, `CTA`).
4. Draft conversion copy blocks using only verified product facts and proof points.
5. Specify a minimal-friction form layout and required privacy consent elements.
6. Map tracking events (`cta_click`, `form_submit`, `scroll_50`) and formulate CRO A/B test hypotheses.
7. Write the specification to `lp_spec.md` for human review without deploying to any live CMS.

## Definition of done

- [ ] `lp_spec.md`, tracking events sketch, and CRO test hypotheses are created
- [ ] Explicit user approval gates are respected (no auto-publish or CMS deploy)
- [ ] All sources, verified claims, and assumptions are logged at the top of the deliverable
- [ ] No fabricated testimonials, logos, or statistics are included

## Security

- Store API keys and MCP credentials exclusively in the connector environment, never in specification files.
- Never publish, deploy to a CMS, or modify live web properties without explicit user approval.

## Pitfalls

- Designing overly long forms with unnecessary required fields that depress completion rates.
- Writing a generic hero headline that fails to match the incoming ad keyword.
- Omitting mandatory privacy policy, cookie consent, or legal notice links required in the target jurisdiction.
- Including heavy autoplay videos that degrade mobile Core Web Vitals.
- Launching a landing page specification without mapped `cta_click` and `form_submit` tracking events.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Create a demo request landing page specification with event tracking (example data).
- **Input:** Ad keyword `TMS` (Transport Management System), conversion goal: book a live demo.
- **Prompt:**
```text
Generate lp_spec.md and a GTM tracking events sketch for a B2B demo landing page targeting the keyword "TMS". Do not deploy to any CMS.
```
- **Expected result:**
```text
lp_spec.md created with message-matched "TMS" hero headline, mobile-first sections, minimal 3-field demo form, and GTM event definitions for cta_click, form_submit, and scroll_50.
```

### Example 2 (Example data (self-written))

- **Task:** Propose CRO experiments for a landing page with low form completion (example data).
- **Input:** Existing landing page funnel showing high scroll depth but low form completion rate.
- **Prompt:**
```text
Propose 3 prioritized CRO A/B tests to improve form completion and name the primary evaluation metrics.
```
- **Expected result:**
```text
3 structured CRO test hypotheses (e.g., reducing form fields from 7 to 3, sticky mobile CTA bar, inline social proof near submit button) with primary metric form_submit conversion rate and guardrail bounce rate named.
```
