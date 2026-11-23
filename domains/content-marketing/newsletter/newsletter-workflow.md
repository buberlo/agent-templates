---
id: newsletter-workflow
title: "Newsletter Content"
domain: content-marketing
category: newsletter
tags:
  - newsletter
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Hermes-Skill google-workspace / gws CLI
    install: "https://hermes-agent.nousresearch.com/docs/reference/skills-catalog"
    version_notes: "Bundled"
inputs:
  - "Thema"
  - "Opt-in Kontext"
  - "CTA"
outputs:
  - "issue_draft.md"
  - "html_skeleton"
  - "utm csv"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

Newsletter drafts with UTM and Unsub placeholders—no Send.

## When to use

- Clearly defined newsletter task with briefing.

**When not to use**

- Without sources/briefing or against platform-ToS.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| required tools | Primary | According to Frontmatter |

## System prompt

```text
Role: newsletter editor.
Subject <=45 chars; preview complements subject.
UTM on all links: source=newsletter medium=email.
Footer [ESP_UNSUB] mandatory in skeleton.
No SMTP send.
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

1. Theme
2. Subject/Preview
3. Blocks+UTM
4. HTML skeleton
5. Plain text
6. Segment-Hinweis
7. Release

## Definition of done

- [ ] Outputs erstellt
- [ ] user approvaln eingehalten
- [ ] Quellen/Annahmen geloggt
- [ ] Kein Auto-Publish

## Security

- Credentials nur im Connector.
- Send/Publish only after release.

## Pitfalls

- Preview leer
- Link without https
- Sie/du mix
- Bild-only
- Falsche Liste

## Basic examples

### Example 1 (Example data)

- **Task:** Issue KW48
- **Input:** 3 links
- **Prompt:**

```text
DE Sie utm
```

- **Expected result:**

```text
[ESP_UNSUB] present
```

### Example 2 (Example data)

- **Task:** Plain text
- **Input:** tech segment
- **Prompt:**

```text
full urls
```

- **Expected result:**

```text
no images
```
