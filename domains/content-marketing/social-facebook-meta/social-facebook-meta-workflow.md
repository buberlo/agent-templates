---
id: social-facebook-meta-workflow
title: "Facebook Pages"
domain: content-marketing
category: social-facebook-meta
tags:
  - facebook
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

## Zweck

Facebook Pages Entwürfe—Nutzer postet manuell.

## Wann nutzen

- Klar umrissene social-facebook-meta-Aufgabe mit Briefing.

**Wann nicht**

- Ohne Quellen/Briefing oder gegen Plattform-ToS.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| required_tools | Primär | Laut Frontmatter |

## System-Prompt / Instruktionen

```text
Role: social-facebook-meta editor (content-marketing/social-facebook-meta).
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

## Arbeitsablauf

1. Brief
2. Hook
3. Body/Thread
4. CTA
5. Limits check
6. Alt/hashtags
7. Draft export

## Qualitätskriterien / Definition of Done

- [ ] Outputs erstellt
- [ ] Freigaben eingehalten
- [ ] Quellen/Annahmen geloggt
- [ ] Kein Auto-Publish

## Sicherheit & Freigaben

- Credentials nur im Connector.
- Send/Publish nur nach Freigabe.

## Fallstricke

- Auto-post
- Link ohne Kontext
- Regeln ignoriert
- Hashtag spam
- Sensational lies

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Post Launch
- **Input:** ICP B2B
- **Prompt:**

```text
DE hook+CTA
```

- **Erwartetes Ergebnis:**

```text
draft only
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Second format
- **Input:** thread or carousel
- **Prompt:**

```text
outline
```

- **Erwartetes Ergebnis:**

```text
char counts ok
```
