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

## Zweck

Newsletter-Entwürfe mit UTM und Unsub-Platzhalter—kein Send.

## Wann nutzen

- Klar umrissene newsletter-Aufgabe mit Briefing.

**Wann nicht**

- Ohne Quellen/Briefing oder gegen Plattform-ToS.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| required_tools | Primär | Laut Frontmatter |

## System-Prompt / Instruktionen

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

## Arbeitsablauf

1. Theme
2. Subject/Preview
3. Blöcke+UTM
4. HTML skeleton
5. Plain text
6. Segment-Hinweis
7. Freigabe

## Qualitätskriterien / Definition of Done

- [ ] Outputs erstellt
- [ ] Freigaben eingehalten
- [ ] Quellen/Annahmen geloggt
- [ ] Kein Auto-Publish

## Sicherheit & Freigaben

- Credentials nur im Connector.
- Send/Publish nur nach Freigabe.

## Fallstricke

- Preview leer
- Link ohne https
- Sie/du mix
- Bild-only
- Falsche Liste

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Issue KW48
- **Input:** 3 links
- **Prompt:**

```text
DE Sie utm
```

- **Erwartetes Ergebnis:**

```text
[ESP_UNSUB] present
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Plain text
- **Input:** tech segment
- **Prompt:**

```text
full urls
```

- **Erwartetes Ergebnis:**

```text
no images
```
