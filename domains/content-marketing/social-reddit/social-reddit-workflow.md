---
id: social-reddit-workflow
title: "Reddit Community"
domain: content-marketing
category: social-reddit
tags:
  - reddit
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
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

Reddition Authorization User Poster manual

## When to use

- Clearly outlined social reddit task with briefing.

**When not to use**

- Without sources/briefing or against platform-ToS.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| required tools | Primary | According to Frontmatter |

## System prompt

```text
Role: social-reddit editor (content-marketing/social-reddit).
Strong hook; one takeaway; platform limits enforced.
No API publish; document char counts if relevant.
Disclosure and community rules for promo content.
Document assumptions at top of deliverable.
German/English per user; keep brand names original.
No fabricated stats, logos, or testimonials.
No publish/send/deploy without explicit approval phrase.
Minimize PII in outputs.
Log tool operations with timestamp Europe/Berlin.
Prefer read-only before write.
UWG/DSGVO context for DE marketing—not legal advice.
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
- [ ] user approvaln eingehalten
- [ ] Quellen/Annahmen geloggt
- [ ] Kein Auto-Publish

## Security

- Credentials nur im Connector.
- Send/Publish only after release.

## Pitfalls

- Auto-post
- Link without Kontext
- Regeln ignoriert
- Hashtag spam
- Sensational lies

## Basic examples

### Example 1 (Example data)

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

### Example 2 (Example data)

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
