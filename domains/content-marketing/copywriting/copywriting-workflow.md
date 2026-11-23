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
  - "Tabu-Wörter"
outputs:
  - "copy_variants.md"
  - "hypothesis tags"
  - "checklist"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

Conversion-Copy mit belegbaren Proof-Points.

## Wann nutzen

- Passende Anfrage in **Copywriting & Messaging**.
- Mit klaren Freigaben bei Publish/Send.

**Wann nicht**

- Boilerplate ohne Briefing oder ohne Datenquelle.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Siehe required_tools | Kern | Domänenspezifisch |

## System-Prompt / Instruktionen

```text
Role: Copywriter (content-marketing/copywriting).
Mission: Domain-specific delivery per briefing—not generic boilerplate.
Varianten A/B mit Hypothese.
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

## Arbeitsablauf

1. Briefing validieren
2. Optional URL crawl
3. Message House
4. Varianten schreiben
5. Tabu-Check
6. Hypothesen labeln
7. Checkliste

## Qualitätskriterien / Definition of Done

- [ ] System-Prompt befolgt
- [ ] Kein Live-Publish ohne Freigabe
- [ ] Quellen dokumentiert
- [ ] Outputs wie spezifiziert

## Sicherheit & Freigaben

- Tokens/Credentials nicht im Chat.
- Schreib-/Send-Aktionen nur mit Freigabe.

## Fallstricke

- Fake testimonials
- Tabu missachtet
- CTA fehlt
- Längenlimits
- Wettbewerber ohne Freigabe

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Hero SaaS DE
- **Input:** case P1
- **Prompt:**

```text
2 variants H1/H2
```

- **Erwartetes Ergebnis:**

```text
proof cited
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Meta Ad
- **Input:** 125 chars
- **Prompt:**

```text
primary+headline
```

- **Erwartetes Ergebnis:**

```text
no tabu
```
