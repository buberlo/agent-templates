---
id: email-postfix-dmarc-parse
domain: security
title: "DMARC-Reports auswerten"
category: compliance-nis2-dsgvo
tags:
  - dmarc
  - postfix
  - email-security
target_agents:
  - hermes
  - generic-mcp-agents
  - generic
required_tools:
  - name: parsedmarc
    install: "pip install parsedmarc"
    version_notes: "Aggregate XML parser"
  - name: postfix
    install: "system MTA"
    version_notes: "optional alignment check"
inputs:
  - "DMARC aggregate XML or ZIP"
  - "Domain und Berichtszeitraum"
outputs:
  - "HTML/JSON Report"
  - "Empfehlung p=quarantine/reject"
risk_level: low
version: "1.1.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

DMARC-Aggregate Reports auswerten (Spoofing, SPF/DKIM-Alignment) und Policy-Stufen **datenbasiert** empfehlen.

## Wann nutzen

- Nach SPF/DKIM-Umstellung, vor Verschärfung auf `p=reject`.
- Wöchentliche Mail-Security-Review.

**Wann nicht:** Forensik einzelner Mails (Message-Header-Analyse separat).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| parsedmarc | Parse | Standard für Aggregate |
| OpenDKIM | Server | Alignment verifizieren |
| Grafana | optional | Trends |

## System-Prompt / Instruktionen

```text
DMARC aggregate analysis (security/compliance-nis2-dsgvo).

Use parsedmarc to ingest XML/ZIP from mailbox path user provides.
Summarize: total messages, SPF pass/fail, DKIM pass/fail, alignment failures by source IP/organizer.
Threshold before recommending p=reject: user org policy or default note pass rate > 98% over 2+ weeks.
Redact full IP lists in public tickets; summarize top failing sources only.
Identify legitimate forwarders failing alignment separately from malicious spoof attempts.
Do not publish raw DMARC XML with customer domains to third-party analytics.
Compare week-over-week trend when multiple reports available.
postfix/opendkim: suggest config review pointers, not paste entire main.cf without ask.
Policy recommendation: staged p=none -> quarantine -> reject with pct ramp when noted.
GDPR: reports may contain recipient domain volumes — handle confidentially.
```

## Arbeitsablauf

1. Reports in Ordner sammeln (`/var/spool/dmarc/incoming/*.xml.gz`).
2. `parsedmarc -f /path/to/report.xml -o /tmp/dmarc_out`.
3. JSON/HTML öffnen; Fail-Rate pro Quelle tabellieren.
4. Legitime Forwarder vs. unbekannte Sending-IPs trennen.
5. Abgleich mit DNS: `dig TXT _dmarc.example.de` und SPF record.
6. Empfehlung an Mail-Admin (Policy-Stufe).
7. Trend vs. Vorwoche dokumentieren.

## Qualitätskriterien / Definition of Done

- [ ] Alle Reports im Zeitraum verarbeitet
- [ ] Fail-Rate pro Quelle benannt
- [ ] Nächste Policy-Stufe begründet

## Sicherheit & Freigaben

- Reports vertraulich; nicht an Dritte ohne AV-Vertrag.
- Keine Weiterleitung kompletter XML in öffentliche KI-Threads.

## Fallstricke

- Nur eine Woche Daten — zu früh für reject.
- Forwarder als „Angriff“ klassifiziert.
- parsedmarc Version skew bei neuen XML-Schemas.
- SPF -all nicht gesetzt trotz guter DMARC pass rate.
- Uhrzeit/Zeitzone Report-Period missverstanden.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Woche 47 für `example.de`.
- **Input:** 4 XML-Dateien.
- **Prompt:**

```text
Run parsedmarc; summarize failing sources; recommend policy step.
```

- **Erwartetes Ergebnis:**

```bash
parsedmarc -f dmarc_w47.xml -o ./out
# dmarc_w47.html — 2 unknown sources, 99.1% aligned
# recommend stay p=quarantine
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Vor reject-Freigabe.
- **Input:** 3 Wochen >98% pass.
- **Prompt:**

```text
Trend three weeks; if stable suggest p=reject with pct=25 ramp note.
```

- **Erwartetes Ergebnis:**

```text
Weeks 45-47 pass 98.4%, 98.9%, 99.2%
Suggest: p=reject; pct=25; monitor 1 week
```