---
id: forensik-workflow
title: "Forensik (nur autorisiert)"
domain: security
category: forensik
tags:
  - forensics
  - incident
  - authorized
target_agents:
  - hermes
  - generic-mcp-agents
required_tools:
  - name: chain-of-custody
    install: "Org forensics SOP"
    version_notes: "Hash before analyze"
  - name: read-only images
    install: "E01/DD per legal"
    version_notes: "No mount write"
inputs:
  - "Legal/HR authorization"
  - "Evidence IDs and hashes"
outputs:
  - "Chain-of-custody notes"
  - "Timeline template (no destructive steps)"
risk_level: high
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Forensik **Rahmen**: Chain of Custody, Timeline, Reporting — keine Schritt-für-Schritt-Datenrettung oder Malware-Detonation in diesem Template.

## Wann nutzen

- IR-Team braucht strukturierte Agent-Hilfe für Dokumentation.
- Nach Autorisierung durch Legal/Security.

**Wann nicht:** Ohne Custody-Formular oder bei personal devices without policy.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| SOP | Process | org-specific |
| Hash tools | Integrity | sha256 before open |
| Human examiner | Analysis | off-template |

## System-Prompt / Instruktionen

```text
Forensics framework ONLY (security/forensik).

Do not instruct live disk writes, malware execution, memory scraping tools, or circumvention of encryption on seized media.
Require: case id, authorizing officer, evidence list with sha256, storage location, and retention schedule.
Outputs allowed: chain-of-custody log template, timeline columns (UTC, host, artifact, analyst, hash), interview question bank (high level).
If evidence hash mismatch, stop and escalate; do not analyze.
Minimize PII in chat; reference evidence ids only.
Coordinate with incident response; preserve originals; work on forensic copies per SOP.
Jurisdiction and privacy law reminder in summary.
No cloud exfiltration of disk images to public AI services.
Handoff to certified forensic analyst for tooling steps.
```

## Arbeitsablauf

1. Authorization und Case-ID prüfen.
2. Evidence-Liste mit SHA256 eintragen.
3. Custody-Log: wer, wann, wohin.
4. Timeline-Template anlegen (leer, strukturiert).
5. Kopie vs. Original laut SOP bestätigen.
6. Menschlicher Analyst übernimmt Tooling.
7. Agent nur Dokumentation fortsetzen.

## Qualitätskriterien / Definition of Done

- [ ] Custody vollständig
- [ ] Keine destruktiven/analyse-Befehle generiert
- [ ] Hashes vor Analyse dokumentiert

## Sicherheit & Freigaben

- **high risk**; Legal-Freigabe Pflicht.
- Beweismittel nicht in Cloud-LLM hochladen.

## Fallstricke

- Mount read-write — Spuren zerstört.
- Fehlende Uhrzeit-Sync in Timeline.
- Analyst-Tool-Output ohne Hash-Referenz.
- GDPR bei Mitarbeiter-Geräten.
- Chain-of-custody Lücken invalidate court use.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Custody log für USB-STICK-7.
- **Input:** sha256 `abc...`, Case FIR-2026-03.
- **Prompt:**

```text
Create custody table and timeline headers only; no acquisition commands.
```

- **Erwartetes Ergebnis:**

```text
Custody: received FIR-2026-03 by Analyst M; hash abc...; sealed bag ID 7
Timeline columns ready UTC|Host|Event|Ref
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Hash mismatch.
- **Input:** re-hash differs.
- **Prompt:**

```text
Apply mismatch policy.
```

- **Erwartetes Ergebnis:**

```text
STOP analysis; escalate integrity failure; do not mount image
```