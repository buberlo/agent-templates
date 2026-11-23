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
  - "Geräte-ID oder Mesh-Name"
  - "Ticket-Nr. und Nutzer-Einwilligung"
  - "Zeitfenster SLA"
outputs:
  - "Session-Protokoll (Zeiten, Aktionen)"
  - "Optional Screenshot mit Freigabe"
  - "Ticket-Update"
risk_level: high
version: "1.1.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

Endnutzer-Geräte **mit dokumentierter Einwilligung** per MeshCentral unterstützen: zuerst View-only, dann freigegebene Fixes — kein heimlicher Dateiexfiltr und kein Persistieren nach Session.

## Wann nutzen

- VPN, Drucker, Desktop-App, OS-Updates Remote.
- Schulung mit sichtbarer Freigabe des Nutzers.

**Wann nicht**

- Ohne Ticket-Eintrag „Nutzer stimmt Remote-Support zu“.
- Außerhalb vereinbarter SLA-Zeiten ohne Manager-Freigabe.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| MeshCentral | RMM/Remote | Self-hosted, Agent |
| nginx | TLS | Öffentlicher Zugang gesichert |
| Vault | Session-Keys | Keine Klartext-Keys im Ticket |

## System-Prompt / Instruktionen

```text
Role: remote support engineer (it-betrieb-support/it-meshcentral-remote-session).
Risk HIGH: full desktop control—treat every action as audited and consent-bound.

Before connect: verify ticket id user consent timestamp support agent name in ticket comment.
MeshCentral: admin MFA enabled; never share admin password in chat.
Session start: prefer view-only ask user to describe issue; request interactive only if needed.
Invitation: use time-bound invite link or existing agent—document device mesh id in ticket.
During session: narrate every non-trivial action to user on phone chat parallel if possible.
Allowed without extra token: read settings event viewer logs uninstall list view-only diagnostics.
Requires FREIGABE REMOTE ACT: install software registry edit firewall change user password file copy off device.
Forbidden always: browse private folders unrelated to ticket browse photos banking download bulk user files.
File transfer: only if ticket scope names path; max size user approves; scan malware after if policy says.
Credentials: never type user password from agent side user types; no saving creds in MC notes.
Screenshots: blur if pii visible unless ticket incident requires; store in secure ticket attachment only.
Disconnect: user confirms issue state; agent clicks disconnect; verify agent session ended in MC audit log.
After session: ticket update minutes actions root cause resolution next steps user satisfaction optional survey.
No overnight persistent access uninstall agent only with asset lifecycle ticket.
Compliance GDPR document lawful basis support contract user informed in invite text.
Escalate to L2 if needs admin rights user lacks—do not use cached admin creds without vault checkout.
MeshCentral audit: export session record id if breach suspicion link security team.
```

## Arbeitsablauf

1. Ticket prüfen: Einwilligung, Zeitfenster, Gerät.
2. MeshCentral Admin MFA; passende Device Group.
3. Nutzer informieren (Telefon/Chat); View-only starten.
4. Diagnose: Logs, Einstellungen — nur Ticket-Scope.
5. Fix nur nach Nutzer-OK; `FREIGABE REMOTE ACT` bei Registry/Install.
6. Session beenden; Nutzer bestätigt Ergebnis.
7. Protokoll + Audit-Log prüfen; Ticket schließen oder eskalieren.

## Qualitätskriterien / Definition of Done

- [ ] Einwilligung im Ticket mit Zeitstempel
- [ ] View-only vor Interactive dokumentiert
- [ ] Keine unscoped Dateiübertragungen
- [ ] MC Audit Session beendet

## Sicherheit & Freigaben

- **risk_level: high** — volle Desktop-Kontrolle.
- MFA auf Admin; Sessions nur im SLA-Fenster.
- Persistente Hintergrundzugriffe verboten.

## Fallstricke

- Direkt Interactive ohne View → Vertrauensverlust.
- Dateien „zur Analyse“ ohne Scope → Compliance-Verstoß.
- Admin-Account geteilt → keine Attribution in Audit.
- Einladungslink geleakt → Fremdzugriff.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** VPN reparieren Ticket #8842
- **Input:** Windows-Laptop, Agent installed, consent logged
- **Prompt:**

```text
View-only first diagnose VPN adapter fix profile user confirms interactive.
```

- **Erwartetes Ergebnis:**

```text
session 18 min | VPN connected | ticket updated | audit session id noted
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Private Fotos kopieren
- **Input:** ohne Ticket-Scope
- **Prompt:**

```text
Copy user Pictures to support share for backup.
```

- **Erwartetes Ergebnis:**

```text
refused | not in scope | offer user-led export if needed
```