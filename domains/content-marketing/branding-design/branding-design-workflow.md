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
  - name: figma MCP (Hermes-Katalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/figma"
    version_notes: "Hermes"
  - name: canva MCP (Hermes-Katalog)
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

## Zweck

Creative Briefs; Figma read-only default.

## Wann nutzen

- Klar umrissene branding-design-Aufgabe mit Briefing.

**Wann nicht**

- Ohne Quellen/Briefing oder gegen Plattform-ToS.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| required_tools | Primär | Laut Frontmatter |

## System-Prompt / Instruktionen

```text
Role: brand design strategist.
Brief: SMP, tone, mandatories, deliverable sizes.
Figma MCP read-only unless FREIGABE FIGMA.
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

## Arbeitsablauf

1. Werte
2. Deliverables
3. Optional Figma audit
4. SMP/Ton
5. Colors/Fonts
6. Moodboard
7. Brief

## Qualitätskriterien / Definition of Done

- [ ] Outputs erstellt
- [ ] Freigaben eingehalten
- [ ] Quellen/Annahmen geloggt
- [ ] Kein Auto-Publish

## Sicherheit & Freigaben

- Credentials nur im Connector.
- Send/Publish nur nach Freigabe.

## Fallstricke

- Wettbewerber kopieren
- Zu viele Fonts
- Ohne Größen
- Figma write
- Canva statt CI

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Rebrand Brief
- **Input:** 3 Werte
- **Prompt:**

```text
creative_brief
```

- **Erwartetes Ergebnis:**

```text
SMP one line
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Figma audit
- **Input:** file id
- **Prompt:**

```text
read-only summary
```

- **Erwartetes Ergebnis:**

```text
no edits
```
