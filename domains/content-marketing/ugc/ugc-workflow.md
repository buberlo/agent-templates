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
Document UGC brief assumptions (product, audience, usage rights) at the top of every deliverable.
Match brief language (German or English) and leave trademarked product names unchanged.
Do not invent performance metrics, logos, or creator testimonials for UGC scripts.
Do not schedule or publish UGC until the user repeats the workflow approval phrase.
Minimize PII in outputs.
Note each tool call with an ISO timestamp in Europe/Berlin when summarizing the session.
Prefer read-only before write.
Flag German UWG/DSGVO touchpoints for UGC claims; do not provide legal opinions.
If usage rights or product claims are unclear, pause and list numbered questions for the marketer.
End each summary with stable relative paths to scripts, shot lists, and rights checklists.
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

### Example 1 (Example data (self-written))
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

### Example 2 (Example data (self-written))
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
