---
id: social-x-twitter-workflow
title: "X Posts & Threads"
domain: content-marketing
category: social-x-twitter
tags:
  - x
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

X Posts & Threads drafts of synddtte Flora

## When to use

- Clearly outlined social x-twitter task with briefing.

**When not to use**

- Japan without the sources/briefing or a platform-tos.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
Recommended to the Recommended

## System prompt

```text
Role: social-x-twitter editor (content-marketing/social-x-twitter).
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
Send/Publish only after release nitrogen.

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
