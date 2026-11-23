---
id: it-meshcentral-remote-session
domain: it-betrieb-support
title: "Remote-Support mit MeshCentral"
category: remote-support
tags:
  - meshcentral
  - remote
  - support
target_agents:
  - hermes
  - generic
required_tools:
  - name: meshcentral
    install: "docker: meshcentral/meshcentral"
    version_notes: "1.1.x; TLS reverse proxy"
  - name: meshagent
    install: "von MC Server"
    version_notes: "Windows/macOS/Linux Agent"
inputs:
  - "Geräte-ID"
  - "Ticket-Nr."
  - "Zeitfenster"
outputs:
  - "Session-Protokoll"
  - "Optional Screenshot"
risk_level: high
version: "1.0.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

Endnutzer-Geräte unter Einwilligung fernsteuern und IT-Probleme live lösen.

## Wann nutzen

- Desktop-Software, VPN, Drucker Remote.
- Nicht ohne dokumentierte Nutzereinwilligung.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| MeshCentral | RMM/Remote | Self-hosted, Agent |
| nginx | TLS termination | Öffentlicher Zugang |
| Vault | Session-Keys | Keine Klartext-Keys |

## System-Prompt / Instruktionen

```text
Remote support via MeshCentral only with user consent logged.
Record ticket ID in session notes; no file exfiltration.
Prefer view-only first; ask before installing software.
Disconnect when done; confirm user satisfaction.
```

## Arbeitsablauf

1. Ticket validieren; Nutzer informieren.
2. Einladungslink oder bestehender Agent.
3. Diagnose; nur freigegebene Aktionen.
4. Kurzdokumentation im Ticket.
5. Session beenden; Audit-Log prüfen.

## Qualitätskriterien / Definition of Done

- [ ] Nutzereinwilligung im Ticket
- [ ] Problem gelöst oder eskaliert
- [ ] Keine unbefugten Dateizugriffe

## Sicherheit & Freigaben

- MFA auf MeshCentral Admin.
- Sessions nicht außerhalb SLA-Zeiten.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

_Siehe vorheriger Abschnitt; bei Migration ergänzt._

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Validierung
- **Input:** n/a
- **Prompt:** `validate output`
- **Erwartetes Ergebnis:** OK

## Beispiele (Legacy)

**Eingabe:** Ticket #8842, Windows-Laptop VPN defekt
**Erwartetes Ergebnis:** VPN-Profil repariert, Session 18 min
