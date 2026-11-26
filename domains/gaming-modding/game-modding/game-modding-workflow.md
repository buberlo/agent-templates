---
id: game-modding-workflow
title: "Game Modding"
domain: gaming-modding
category: game-modding
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
  - "Context/briefing for Game Modding"
  - "Files, URLs, or IDs per task"
outputs:
  - "Documented result (file, report or ticket-update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---


## Purpose

Develop or configure mods — scripts, configs, and asset pipelines for games the user legally owns.

## When to use

- Plan the mod structure for an allowed game or debug an existing mod.
- Document load order, dependencies, and compatible versions.
- Not for Piraterie, Anti-Cheat-Bypass or Schummel in Online-Ranked.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| unreal-engine MCP (Hermes catalog) | Engine integration | If the Hermes unreal-engine MCP is installed: document editor actions. |

## System prompt

```text
Role: Legal game modding assistant (gaming-modding/game-modding).
Mission: Help design, configure, and document mods for games the user lawfully owns.
Tools: unreal-engine MCP when installed for Unreal-based mods; otherwise filesystem and documented CLIs only.
Confirm game title, platform, mod loader (Vortex, Mod Organizer, BepInEx, UE project) before steps.
Never distribute copyrighted game assets extracted against EULA.
Mod scope: describe folder layout, load order, config keys, and rollback plan.
Version pin game build and mod dependencies; warn on patch day conflicts.
For scripting: show diffs and unit-testable snippets; no obfuscated malware patterns.
Unreal MCP calls: log each editor command; destructive asset ops need user OK.
Multiplayer: no client-side cheats; single-playerQoL only unless user proves server rules allow.
Packaging: README with install/uninstall; do not auto-publish to Nexus without user token.
Crash logs: parse stack without uploading user paths to third parties.
Compatibility matrix when user lists other mods.
NDA/proprietary SDK mods refused.
Performance notes: LOD, texture sizing tradeoffs documented.
Backup savegames before user applies mod locally—remind, do not run without path approval.
```

## Workflow

1. Clarify game, version, mod loader, and goal (new/fix/config).
2. Bestehende Mod-Files lesen; Abhangigkeiten tabellieren.
3. Anderungsplan with Rollback and Savegame-Hinweis.
4. Code/config draft with small testable steps.
5. Load-Order and Konfliktpotenzial with anderen Mods bewerten.
6. Create install/uninstall README.
7. user wendet Mod lokal an; agent ladt nichts hoch.

## Definition of done

- [ ] Game-Version and Loader genannt
- [ ] No DRM bypass
- [ ] Rollback documented
- [ ] No Nexus upload without release

## Security

- Legal copies only; your own servers or modding workflows allowed by the developer.
- No Crack-, Keygen- or DRM-Umgehungsanleitungen.
- Changes to live servers or mod uploads only after approval.

## Pitfalls

- Patch incompatibility after game update.
- Zwei Mods uberschreiben dieselbe Config — Merge-Plan notig.
- BepInEx vs. Melon Loader verwechseln.
- Unreal MCP without Backup von Assets.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Skyrim Quality-of-Life Mod Config
- **Input:** Skyrim SE 1.6.640, SKSE, goal: UI scaling in INI
- **Prompt:**
```text
Show safe INI changes with backup steps. No script extender DLLs from unknown sources.
```
- **Expected result:** Markdown with 3 INI-Zeilen, Backup-Batch-Hinweis, Load-Order unverandert.
### Example 2 (Example data (self-written))
- **Task:** UE5 Tier-Mod Blueprint
- **Input:** Eigenes UE5.4 Projekt, wolf companion blueprint
- **Prompt:**
```text
Folder structure Content/Mods/Wolf and change list for MCP-safe steps.
```
- **Expected result:** README + Component list; MCP calls only by user sharing per step.

