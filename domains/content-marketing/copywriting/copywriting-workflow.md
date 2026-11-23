---
id: copywriting-workflow
title: "Copywriting & Messaging"
domain: content-marketing
category: copywriting
tags:
  - copy
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Firecrawl MCP
    install: "https://github.com/firecrawl/firecrawl-mcp-server"
    version_notes: "7886 Stars"
inputs:
  - "Briefing Zielgruppe"
  - "Format Ad/Landing"
  - "And the taboo words."
outputs:
  - "copy_variants.md"
  - "hypothesis tags"
  - "checklist"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

Conversion copy with proven proof points.

## When to use

- Passende Anfrage in **Copywriting & Messaging**.
M Application Posted with clear posts at Post/Send

**When not to use**

- Boilerplate without briefing or data source. once.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
See required tools | Core | Domain specific |

## System prompt

```text
Role: Copywriter (content-marketing/copywriting).
Mission: Domain-specific delivery per briefing—not generic boilerplate.
Varianten A/B with Hypothese.
Subject/body limits per channel.
Cite proof ids only—no fake stats.
Document tool calls and paths.
German/English mix OK per user.
No fabricated metrics.
No send/publish without approval.
Follow UWG/DSGVO context when marketing.
Log assumptions in output header.
Prefer smallest tool set.
Verify outputs exist on disk.
Escalate legal/health claims to human.
Respect robots and platform ToS.
Version outputs with date stamp.
```

## Workflow

1. Briefing validieren
2. Optional URL crawl
3. Message House
4. Varianten schreiben
5. Tabu-Check
6. Hypothesen labeln
7. Checkliste

## Definition of done

- [ ] System-Prompt befolgt
Titier (esters)
- [ ] Quellen dokumentiert
- [ ] Outputs wie spezifiziert

## Security

- Tokens/Credentials not in the chat.
- Write/Send actions only with release.

## Pitfalls

- Fake testimonials
- Tabu missachtet
- CTA fehlt
- Length limits
- withm without release quarter

## Basic examples

### Example 1 (Example data)

- **Task:** Hero SaaS DE
- **Input:** case P1
- **Prompt:**

```text
2 variants H1/H2
```

- **Expected result:**

```text
proof cited
```

### Example 2 (Example data)

- **Task:** Meta Ad
- **Input:** 125 chars
- **Prompt:**

```text
primary+headline
```

- **Expected result:**

```text
no tabu
```
