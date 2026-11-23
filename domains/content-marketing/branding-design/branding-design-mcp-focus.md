---
id: branding-design-mcp-focus
title: "Branding: Figma vs Canva"
domain: content-marketing
category: branding-design
tags:
  - mcp
  - figma
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: figma MCP (Hermes-catalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/figma"
    version_notes: "Hermes"
  - name: canva MCP (Hermes-catalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/canva"
    version_notes: "Hermes"
inputs:
  - "Audit vs Quick asset"
  - "Policy"
outputs:
  - "routing.md"
  - "tool rationale"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

Route design tasks to one MCP path.

## When to use

Clearly intersected branding and design task with briefing.

**When not to use**

- Without sources/briefing or against platform ToS.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
Exe--thesheets-of-the-'''''''''''''''''''''''''''' all'' Plus''

## System prompt

```text
Role: branding tool router.
Design system audit → figma only.
Quick social resize → canva only.
Never both MCPs parallel.
Sequential figma then canva if needed.
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

1. Klassifizieren
2. Ein MCP
3. result
4. Sequenz optional
5. Skills wenn MCP off
6. Routing doc
7. Verweis Haupt-Workflow

## Definition of done

- [ ] Outputs erstellt
- [ ] user approvaln eingehalten
- [ ] Quellen/Annahmen geloggt
- [ ] Kein Auto-Publish

## Security

- Credentials nur im Connector.
in- off-line,

## Pitfalls

- Token overflow
- Font mismatch
- Figma write
- Doppel MCP
- Export falsche px

## Basic examples

### Example 1 (Example data)

- **Task:** Figma audit
- **Input:** file
- **Prompt:**

```text
figma on
```

- **Expected result:**

```text
routing says figma
```

### Example 2 (Example data)

- **Task:** Canva 1080
- **Input:** colors paste
- **Prompt:**

```text
canva on
```

- **Expected result:**

```text
figma off
```
