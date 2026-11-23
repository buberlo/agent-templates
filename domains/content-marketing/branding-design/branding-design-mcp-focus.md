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
  - name: figma MCP (Hermes-Katalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/figma"
    version_notes: "Hermes"
  - name: canva MCP (Hermes-Katalog)
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

## Zweck

Route design tasks to one MCP path.

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

## Arbeitsablauf

1. Klassifizieren
2. Ein MCP
3. Ergebnis
4. Sequenz optional
5. Skills wenn MCP off
6. Routing doc
7. Verweis Haupt-Workflow

## Qualitätskriterien / Definition of Done

- [ ] Outputs erstellt
- [ ] Freigaben eingehalten
- [ ] Quellen/Annahmen geloggt
- [ ] Kein Auto-Publish

## Sicherheit & Freigaben

- Credentials nur im Connector.
- Send/Publish nur nach Freigabe.

## Fallstricke

- Token overflow
- Font mismatch
- Figma write
- Doppel MCP
- Export falsche px

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Figma audit
- **Input:** file
- **Prompt:**

```text
figma on
```

- **Erwartetes Ergebnis:**

```text
routing says figma
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Canva 1080
- **Input:** colors paste
- **Prompt:**

```text
canva on
```

- **Erwartetes Ergebnis:**

```text
figma off
```
