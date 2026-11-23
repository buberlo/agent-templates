---
id: social-buffer-schedule-campaign
title: "Buffer Kampagnenplanung"
domain: content-marketing
category: social-media-strategie
tags:
  - buffer
  - scheduling
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: buffer
    install: "API: buffer.com"
    version_notes: "OAuth"
  - name: ffmpeg
    install: "apt ffmpeg"
    version_notes: "trim"
inputs:
  - "Kalender CSV"
  - "Kanäle"
  - "UTM"
outputs:
  - "queue_report.csv"
  - "validation.md"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

Buffer CSV validieren und queuen—Draft bei medium risk.

## Wann nutzen

- Klar umrissene social-media-strategie-Aufgabe mit Briefing.

**Wann nicht**

- Ohne Quellen/Briefing oder gegen Plattform-ToS.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| required_tools | Primär | Laut Frontmatter |

## System-Prompt / Instruktionen

```text
Role: Buffer scheduler (social-buffer-schedule-campaign).
Validate media per channel; UTMs on all links.
Default draft queue unless FREIGABE.
ffmpeg probe video length reels <=60s.
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

1. CSV validieren
2. UTM global
3. Medien prüfen
4. Textlimits
5. Buffer queue
6. Report
7. Read-back

## Qualitätskriterien / Definition of Done

- [ ] Outputs erstellt
- [ ] Freigaben eingehalten
- [ ] Quellen/Annahmen geloggt
- [ ] Kein Auto-Publish

## Sicherheit & Freigaben

- Credentials nur im Connector.
- Send/Publish nur nach Freigabe.

## Fallstricke

- TZ Berlin
- IG crop
- Wrong profile
- No https
- API limit

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** 10 posts
- **Input:** draft mode
- **Prompt:**

```text
queue_report
```

- **Erwartetes Ergebnis:**

```text
all draft
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** 90s video
- **Input:** trim 58s
- **Prompt:**

```text
error or trim
```

- **Erwartetes Ergebnis:**

```text
logged
```
