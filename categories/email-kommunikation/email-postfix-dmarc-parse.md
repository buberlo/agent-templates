---
id: email-postfix-dmarc-parse
title: "DMARC-Reports auswerten"
category: email-kommunikation
tags:
  - dmarc
  - postfix
  - email-security
target_agents:
  - hermes
  - generic
required_tools:
  - name: parsedmarc
    install: "pip: parsedmarc"
    version_notes: "Aggregate XML"
  - name: postfix
    install: "system"
    version_notes: "SPF/DKIM Alignment prüfen"
inputs:
  - "DMARC XML ZIP"
  - "Domain"
  - "Berichtszeitraum"
outputs:
  - "HTML/JSON Report"
  - "Handlungsempfehlungen"
risk_level: low
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Wöchentliche DMARC-Aggregate auswerten und Spoofing/Alignment-Probleme erkennen.

## Wann nutzen

- Nach SPF/DKIM-Umstellung, vor p=reject.
- Nicht für forensische Einzelmail-Analyse (dafür Message-Header).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| parsedmarc | XML parse | Standard-Tool |
| OpenDKIM | DKIM verify | Serverseitig |
| Grafana | optional Dashboard | Trends |

## System-Prompt / Instruktionen

```text
Parse DMARC aggregate reports with parsedmarc.
Flag sources failing SPF or DKIM alignment.
Recommend p=quarantine/reject only when pass rate > threshold.
Do not expose full IP lists in public tickets.
```

## Arbeitsablauf

1. Reports aus Mailbox/Ordner sammeln.
2. parsedmarc → JSON/HTML.
3. Ausreißer-IPs identifizieren.
4. Empfehlungen an Mail-Admin.
5. Trend vs. Vorwoche.

## Qualitätskriterien / Definition of Done

- [ ] Alle Reports im Zeitraum verarbeitet
- [ ] Fail-Rate pro Quelle
- [ ] Nächste Policy-Stufe begründet

## Sicherheit & Freigaben

- Reports können Wettbewerbsinfos enthalten.
- Keine Weiterleitung an Dritte.

## Beispiele

**Eingabe:** 4 XML für `example.de`, Woche 47
**Erwartetes Ergebnis:** `dmarc_w47.html`, 2 unkonfigurierte Sender
