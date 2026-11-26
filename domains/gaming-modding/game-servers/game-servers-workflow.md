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
  - name: unreal-engine MCP (Hermes catalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/unreal-engine"
    version_notes: "Nous-approved optional-mcps catalog entry (listing 2026-11-23)."
inputs:
  - "Context/briefing for Game Server"
  - "Files, URLs, or IDs per task"
outputs:
  - "Documented result (file, report or ticket-update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---


## Purpose

Set up game servers, synchronize mods, and document backup and update routines.

## When to use

- Self-hosted Survival/Creators-Server for Freundesrunde planen.
- Align mods on server and client; rollout checklist.
- Not for kommerzielle Hosting without DDoS- and Lizenzrisiko-Klarung.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| unreal-engine MCP (Hermes catalog) | Engine integration | If the Hermes unreal-engine MCP is installed: document editor actions. |

## System prompt

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

## Workflow

1. Capture server goal, game, player slots, hosting environment.
2. Write install documentation (steamcmd/docker).
3. Mod-list and Sync-Prozess zwischen Server/Client.
4. Backup- and Restore-Runbook.
5. update- and Rollback-Flow.
6. Security hardening (passwords, firewall).
7. Review smoke test after user deployment.

## Definition of done

- [ ] No Secrets in Klartext in Output
- [ ] Mod-Versionen gespiegelt
- [ ] Backup getestet im Runbook beschrieben
- [ ] Ports documented

## Security

- Legal copies only; your own servers or modding workflows allowed by the developer.
- No Crack-, Keygen- or DRM-Umgehungsanleitungen.
- Changes to live servers or mod uploads only after approval.

## Pitfalls

- World-Folder backup wahrend Server lauft — stop-Befehl notig.
- Port-Konflikt with anderem Dienst.
- Client-Mod without Server-Equivalent desync.
- Automatic steamcmd without `--validate` after crash.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Valheim Docker-Server
- **Input:** linux vps, 4 Spieler, Mods: Valheim Plus
- **Prompt:**
```text
docker-compose draft with volumes and mod-sync table.
```
- **Expected result:** compose.yaml snippet without password; environment variables table; backup cron text.
### Example 2 (Example data (self-written))
- **Task:** Minecraft Paper Migration
- **Input:** Vanilla 1.20.4 zu Paper, 12 Plugin-Namen
- **Prompt:**
```text
Migration checklist and world.tar rollback steps.
```
- **Expected result:** 18-item checklist; incompatible plugin flagged.

