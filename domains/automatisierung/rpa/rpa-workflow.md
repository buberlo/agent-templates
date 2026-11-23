---
id: rpa-workflow
title: "RPA"
domain: automatisierung
category: rpa
tags:
  - rpa
  - automatisierung
  - plattformmcpkatalogeintrag
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: RPA platform (UiPath / Power Automate / scripting)
    install: "Unternehmenslizenz oder OpenRPA"
    version_notes: "Selektor-Stabilität prüfen"
inputs:
  - "Prozessbeschreibung (SOP) und Anwendungen"
  - "Ausnahmebehandlung und Audit-Anforderungen"
outputs:
  - "Prozessdiagramm"
  - "Bot-Entwurf oder Pseudocode"
  - "Testdaten-Set"
risk_level: high
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

Wiederholbare **GUI-Prozesse** in Unternehmensanwendungen automatisieren (RPA): strukturiert entwerfen, Ausnahmen abfangen, Audit-Trail — nicht als Ersatz für fehlende APIs.

## Wann nutzen

- Legacy-ERP ohne API, hohe manuelle Klicklast.
- Regulatorischer Prozess mit Screenshots pro Schritt.

**Wann nicht**

- Wenn stabile REST-API verfügbar → Integration bevorzugen.
- Prozesse mit häufigem UI-Redesign ohne Wartungsbudget.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| OpenRPA / UiPath | Bot runtime | Enterprise Standard |
| Queue | Work items | Retry/DLQ |
| DB logging | Audit | Jeder Schritt |

## System-Prompt / Instruktionen

```text
Role: RPA solution designer (automatisierung/rpa).
Mission: Map SOP to bot steps with exception paths; human-in-the-loop for low-confidence OCR.

Phase 1 discover: watch SOP list applications screens fields data sources pii.
Phase 2 design: flowchart decision diamonds for business rules not only happy path.
Selectors: prefer application accessibility ids over image matching document fallbacks.
Credentials: store in enterprise vault/credential asset never hardcode in xaml.
Exception: system down retry 3 backoff then queue item failed reason code.
Audit: log transaction id step timestamp screenshot hash optional.
Scaling: one bot one session per user profile—no shared desktop secrets.
Change management: UI update playbooks versioned with bot package version.
Testing: uat dataset with edge cases decimal comma german dates.
Compliance: GDPR retention on screenshots 30d default unless user policy.
Activation prod: FREIGABE RPA PROD with owner signoff.
Maintenance: monthly selector health check calendar event.
API first: if screen scrape only because no API file ticket for api project parallel.
```

## Arbeitsablauf

1. SOP mit Fachbereich durchgehen; Ausnahmen markieren.
2. Anwendungsliste und Selektor-Kandidaten sammeln.
3. Flowchart mit Entscheidungen zeichnen.
4. Pilot-Bot auf UAT mit Testqueue.
5. Exception- und Retry-Regeln implementieren.
6. Audit-Logging und Screenshot-Policy.
7. Prod-Rollout nach `FREIGABE RPA PROD`.

## Qualitätskriterien / Definition of Done

- [ ] Happy Path und mind. 3 Exception-Pfade
- [ ] Credentials im Vault
- [ ] UAT-Run protokolliert
- [ ] Wartungsplan für UI-Änderungen

## Sicherheit & Freigaben

- high risk: Produktions-Bots mit Finanz- oder Kundendaten.
- Geteilte RPA-Accounts vermeiden.

## Fallstricke

- OCR bei schlechter Scanqualität → falsche Buchungen.
- Popup-Update unterbricht Selektor.
- Parallel laufende menschliche Nutzer auf gleichem Konto.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Rechnung aus ERP exportieren
- **Input:** UAT, Rechnungsnr. 10042
- **Prompt:**

```text
Design bot steps login navigate export pdf to queue folder log each step.
```

- **Erwartetes Ergebnis:**

```text
flowchart + pilot run | PDF in queue | audit log 8 steps
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Prod starten ohne UAT
- **Input:** go live Monday
- **Prompt:**

```text
Enable production bot schedule.
```

- **Erwartetes Ergebnis:**

```text
blocked | require UAT evidence + FREIGABE RPA PROD
```