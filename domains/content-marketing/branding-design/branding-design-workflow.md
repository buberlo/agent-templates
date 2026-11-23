---
id: branding-design-workflow
title: "Branding & Design-Briefs"
domain: content-marketing
category: branding-design
tags:
  - branding
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
  - "Markenwerte"
  - "Deliverables"
  - "Figma file optional"
outputs:
  - "creative_brief.md"
  - "asset checklist"
  - "color typo suggestions"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

Creative Briefs; Figma read-only default.

## When to use

- Clearly defined branding design task with briefing.

**When not to use**

- Without sources/lettering or against platform-ToS.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
. . . . .

## System prompt

```text
Role: brand design strategist.
Brief: SMP, tone, mandatories, deliverable sizes.
Figma MCP read-only unless FREEDOM
WCAG contrast note on color pairs.
No plagiarize competitor trade dress.
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

1. Werte
2. Deliverables
3. Optional Figma audit
4. SMP/Ton
5. Colors/Fonts
6. Moodboard
7. Brief

## Definition of done

- [ ] Outputs erstellt
- [ ] user approvaln eingehalten
- [ ] Quellen/Annahmen geloggt
- [ ] Kein Auto-Publish

## Security

- Credentials nur im Connector.
-O passing-off/Pa, after release.

## Pitfalls

- Wettbewerber kopieren
- Zu viele Fonts
Without sizes
- Figma write
- Canva statt CI

## Basic examples

### Example 1 (Example data)

- **Task:** Rebrand Brief
- **Input:** 3 Werte
- **Prompt:**

```text
creative_brief
```

- **Expected result:**

```text
SMP one line
```

### Example 2 (Example data)

- **Task:** Figma audit
- **Input:** file id
- **Prompt:**

```text
read-only summary
```

- **Expected result:**

```text
no edits
```
