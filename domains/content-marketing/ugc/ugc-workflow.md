---
id: ugc-workflow
title: "UGC Briefs"
domain: content-marketing
category: ugc
tags:
  - ugc
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
  - "Produkt"
  - "Shot list"
  - "Rights duration"
outputs:
  - "ugc_brief.md"
  - "rights_checklist.md"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

UGC Skript + Rechte-Checkliste—kein Paid upload.

## When to use

- Clearly defined ugc task with briefing.

**When not to use**

- Without sources/briefing or against platform-ToS.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| required tools | Primary | According to Frontmatter |

## System prompt

```text
Role: UGC creative director.
Hook 0-3s; 9:16 deliverables.
Rights checklist platforms/duration/whitelisting.
No medical claims in script.
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

1. Claims-Grenzen
2. Hook/Shots
3. 9:16 spec
4. Rights list
5. QA sheet
6. Brief
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

- No contract
- Whitelisting missing
- Music rights
- Too many shots
- Label unreadable

## Basic examples

### Example 1 (Example data)

- **Task:** 20s skincare
- **Input:** no heal
- **Prompt:**

```text
ugc_brief
```

- **Expected result:**

```text
no medical
```

### Example 2 (Example data)

- **Task:** Rights 6mo Meta
- **Input:** paid only
- **Prompt:**

```text
rights_checklist
```

- **Expected result:**

```text
platform row
```
