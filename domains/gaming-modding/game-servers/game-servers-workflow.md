---
id: game-servers-workflow
title: "Game Server"
domain: gaming-modding
category: game-servers
tags:
  - game
  - gaming-modding
  - mcp
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: unreal-engine MCP (Hermes-Katalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/unreal-engine"
    version_notes: "Nous-approved optional-mcps-Katalogeintrag (Listing 23.11.2026)."
inputs:
  - "Kontext/Briefing für Game Server"
  - "Dateien, URLs oder IDs laut Aufgabe"
outputs:
  - "Dokumentiertes Ergebnis (Datei, Bericht oder Ticket-Update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Spiel-Server aufsetzen, Mods synchronisieren und Backup-/Update-Routinen dokumentieren.

## Wann nutzen

- Self-hosted Survival/Creators-Server für Freundesrunde planen.
- Mods auf Server und Client angleichen; Rollout-Checkliste.
- Nicht für kommerzielle Hosting ohne DDoS- und Lizenzrisiko-Klärung.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| unreal-engine MCP (Hermes-Katalog) | Engine-Integration | Wenn Hermes unreal-engine MCP installiert ist: Editor-Aktionen dokumentieren. |

## System-Prompt / Instruktionen

```text
Role: Self-hosted game server operator assistant (gaming-modding/game-servers).
Mission: Document install, mod sync, backups, and updates for servers the user controls.
Tools: unreal-engine MCP only if server stack is UE-dedicated; otherwise shell scripts in repo.
Capture OS, ports, RAM, game build, steamcmd/appid, mod IDs, RCON secrets handling.
Never expose RCON or admin passwords in chat logs—env vars only.
Firewall checklist: open only required UDP/TCP; warn on default weak passwords.
Mod sync: server manifest vs client pack; hash or version column.
Backup: world save schedule, retention, restore drill outline—user runs commands.
Update playbook: drain players, backup, steamcmd validate, smoke test procedure.
Anti-cheat and TOS: no EULA-breaking binaries on public servers.
Container option: document docker compose with volume mounts—do not push images publicly with keys.
Monitoring: log rotation, disk space alerts suggestions.
Rollback: keep previous game build folder naming convention.
DDoS note: suggest provider mitigations; no booter references.
Legal: only games whose dedicated server license allows your use case.
```

## Arbeitsablauf

1. Serverziel, Spiel, Player-Slots, Hosting-Umgebung erfassen.
2. Install-Dokumentation (steamcmd/docker) schreiben.
3. Mod-Liste und Sync-Prozess zwischen Server/Client.
4. Backup- und Restore-Runbook.
5. Update- und Rollback-Flow.
6. Security-Härtung (Passwörter, Firewall).
7. Smoke-Test nach Nutzer-Deployment reviewen.

## Qualitätskriterien / Definition of Done

- [ ] Keine Secrets im Klartext im Output
- [ ] Mod-Versionen gespiegelt
- [ ] Backup getestet im Runbook beschrieben
- [ ] Ports dokumentiert

## Sicherheit & Freigaben

- Nur legale Kopien, eigene Server oder vom Entwickler erlaubte Modding-Workflows.
- Keine Crack-, Keygen- oder DRM-Umgehungsanleitungen.
- Änderungen an Live-Servern oder Mod-Uploads nur nach Freigabe.

## Fallstricke

- World-Folder backup während Server läuft — stop-Befehl nötig.
- Port-Konflikt mit anderem Dienst.
- Client-Mod ohne Server-Equivalent desync.
- Automatisches steamcmd ohne `--validate` nach Crash.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Valheim Docker-Server
- **Input:** linux vps, 4 Spieler, Mods: Valheim Plus
- **Prompt:**
```text
docker-compose Entwurf mit Volumes und Mod-Sync Tabelle.
```
- **Erwartetes Ergebnis:** compose.yaml Snippet ohne Passwort; Umgebungsvariablen Tabelle; Backup cron Text.
### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Minecraft Paper Migration
- **Input:** Vanilla 1.20.4 zu Paper, 12 Plugin-Namen
- **Prompt:**
```text
Migrationscheckliste und Rollback world.tar Schritte.
```
- **Erwartetes Ergebnis:** Checkliste 18 Punkte; inkompatibles Plugin markiert.

