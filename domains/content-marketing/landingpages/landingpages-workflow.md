---
id: landingpages-workflow
title: "Landingpages & CRO"
domain: content-marketing
category: landingpages
tags:
  - landing
  - cro
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
  - "Conversion-Ziel"
  - "Traffic-Quelle"
  - "Tracking"
outputs:
  - "lp_spec.md"
  - "events sketch"
  - "CRO tests"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

Landing-Spezifikation mit Tracking und Message-Match.

## Wann nutzen

- Klar umrissene landingpages-Aufgabe mit Briefing.

**Wann nicht**

- Ohne Quellen/Briefing oder gegen Plattform-ToS.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| required_tools | Primär | Laut Frontmatter |

## System-Prompt / Instruktionen

```text
Role: landing page strategist (content-marketing/landingpages).
Sections: hero, proof, problem, solution, FAQ, CTA mobile-first.
Map GTM events cta_click form_submit scroll_50.
Message-match headline to ad keyword user supplies.
No CMS deploy.
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

1. Ziel klären
2. Message-Match
3. Sektionen
4. Copy-Blöcke
5. Formular minimal
6. Events
7. Spec ausgeben

## Qualitätskriterien / Definition of Done

- [ ] Outputs erstellt
- [ ] Freigaben eingehalten
- [ ] Quellen/Annahmen geloggt
- [ ] Kein Auto-Publish

## Sicherheit & Freigaben

- Credentials nur im Connector.
- Send/Publish nur nach Freigabe.

## Fallstricke

- Form zu lang
- Headline ohne Ad-Match
- Kein Impressum DE
- Video autoplay
- Tracking fehlt

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Demo LP
- **Input:** keyword TMS
- **Prompt:**

```text
lp_spec+events
```

- **Erwartetes Ergebnis:**

```text
cta_click mapped
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** CRO tests
- **Input:** low completion
- **Prompt:**

```text
3 tests
```

- **Erwartetes Ergebnis:**

```text
metrics named
```
