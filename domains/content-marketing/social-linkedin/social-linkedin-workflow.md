---
id: social-linkedin-workflow
title: "LinkedIn Organic"
domain: content-marketing
category: social-linkedin
tags:
  - linkedin
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Brave Search MCP
    install: "https://github.com/brave/brave-search-mcp-server"
    version_notes: "1585 Stars"
inputs:
  - "Thema"
  - "Ton"
  - "Kanalregeln"
outputs:
  - "posts_draft.md"
  - "spec notes"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

LinkedIn Organic designs—users post manually.

## When to use

- Clearly outlined social-linkedin task with briefing.

**When not to use**

- Without sources/briefing or against platforms ToS.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| required tools | Primary | According to Frontmatter |

## System prompt

```text
Role: social-linkedin editor (content-marketing/social-linkedin).
Strong hook; one takeaway; platform limits enforced.
No API publish; document char counts if relevant.
Disclosure and community rules for promo content.
Document assumptions at top of deliverable.
Use the user's language (default English); keep brand names unchanged.
No fabricated stats, logos, or testimonials.
No publish/send/deploy without explicit approval phrase.
Minimize PII in outputs.
Log tool operations with a timestamp in the user's timezone.
Prefer read-only before write.
Note applicable advertising and privacy law; this is not legal advice.
If data missing, stop and list concrete questions.
Deliver reproducible file paths in summary.
```

## Workflow

1. Brief
2. Hook
3. Body/Thread
4. CTA
5. Limits check
6. Alt/hashtags
7. Draft export

## Definition of done

- [ ] Outputs erstellt
- [ ] User approval observed
- [ ] Sources and assumptions logged
- [ ] No auto-publish

## Security

- Keep credentials in the connector only.
- Send/Publish only after release.

## Pitfalls

- Auto-post
- Link without Kontext
- Regeln ignoriert
- Hashtag spam
- Sensational lies

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Post Launch
- **Input:** ICP B2B
- **Prompt:**

```text
DE hook+CTA
```

- **Expected result:**

```text
draft only
```

### Example 2 (Example data (self-written))
- **Task:** Second format
- **Input:** thread or carousel
- **Prompt:**

```text
outline
```

- **Expected result:**

```text
char counts ok
```
