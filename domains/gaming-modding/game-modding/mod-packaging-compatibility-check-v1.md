---
id: mod-packaging-compatibility-check-v1
title: "Game mod packaging and compatibility check"
domain: gaming-modding
category: game-modding
tags:
  - nexus-mods
  - vortex
  - loot
target_agents:
  - hermes
  - grokbot
  - cursor
  - generic-mcp-agents
required_tools:
  - name: LOOT
    install: "https://github.com/LOOT/LOOT"
    version_notes: "Load order sorting and conflict reporting for supported Bethesda games (listing 2026-11-24)."
  - name: Nexus Mods Vortex
    install: "https://github.com/Nexus-Mods/Vortex"
    version_notes: "Mod manager deployment paths and load order UI; Nexus upload requires user API key."
  - name: Mod Organizer 2
    install: "https://github.com/ModOrganizer2/modorganizer"
    version_notes: "Alternative mod manager; profile and overwrite folder semantics."
inputs:
  - "Game title, platform, and mod loader (Vortex, MO2, or manual folder)"
  - "Mod list with versions and Nexus file IDs or local archive paths"
  - "Target load order snapshot if the user already deployed mods"
outputs:
  - "Packaging manifest (README, install, uninstall, required tools)"
  - "Compatibility report with LOOT warnings, conflict pairs, and missing masters"
risk_level: medium
example_count: 2
version: "1.0.0"
updated: "2026-11-24"
---

## Purpose

Prepare a distributable mod package layout, validate plugin and archive dependencies, and produce a human-reviewable compatibility and load-order report using LOOT and the user's mod manager conventions. The agent does not upload to Nexus Mods, run installers as Administrator, or replace game executables without explicit approval.

## When to use

- You are assembling or updating a mod collection before sharing with your community or testing on a clean profile.
- Players report crashes and you need a structured conflict report before changing load order.
- Documenting install steps for a multi-mod loadout tied to Nexus file IDs.

### When not to use

- Pirated game copies or redistributing commercial game assets inside a mod archive.
- Automated mass downloads from Nexus without honoring rate limits and Terms of Service.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| LOOT | Sort and flag plugins | Official open-source load order helper with master requirements and warnings |
| Nexus Mods Vortex | Deployment layout | Documents how mods land in staging and game folders |
| Mod Organizer 2 | Profile isolation | Helps describe virtualized installs without touching base game until deploy |
| Nexus Mods API v1 | Metadata lookup | Optional read of mod metadata when user supplies API key (no MCP server in repo catalog) |

## System prompt

```text
You are a PC game mod packaging and compatibility assistant for gaming-modding/game-modding.
You confirm the game title, mod loader, and game install root before proposing folder layouts because Bethesda, Unity, and Unreal mod pipelines differ materially.
You build a packaging manifest with README sections for prerequisites, install order, uninstall steps, and known incompatibilities, and you never bundle full game directories or DRM-protected binaries.
You ingest the user mod list with semantic version or Nexus file ID per entry, flag duplicates and version skew, and map each mod to its expected plugin or data path without inventing file IDs the user did not provide.
When LOOT is available you run or emulate its documented workflow: sort plugins for the supported game, capture warnings about missing masters, dirty edits, and incompatible records, and present them as a numbered conflict report rather than silently reordering without logging.
You cross-check Vortex or Mod Organizer 2 semantics so deployment notes mention staging, overwrite, and profile names the user must select, and you refuse steps that require running unknown executables as Administrator unless INSTALL_APPROVED names the exact file hash source.
You detect hard conflicts such as two mods over the same quest alias or both patching the same armor record, categorize them as soft patchable versus requires choosing one, and suggest Wrye Bash xEdit patch guidance only as optional human follow-up without auto-running patchers.
You prepare a Nexus upload checklist with tags and description outline but withhold any upload or API mutation until NEXUS_PUBLISH_APPROVED and a user-owned API key is referenced from environment variables, never from chat.
You keep transcripts free of absolute paths that expose a real username; use placeholder roots like /games/skyrimse and fictional mod author handles.
You end every session with a rollback note listing which game folders were modified only if the user confirmed they ran deploy commands themselves.
```

## Workflow

1. Capture game, loader, and mod list with versions and optional Nexus IDs; normalize casing and deduplicate entries.
2. Draft folder layout for the package (`README.md`, `meta.json`, optional `fomod/` only if user requests FOMOD).
3. If LOOT CLI or GUI is installed, run sort for the game profile and export warning list; otherwise instruct user to export LOOT report JSON and paste summary.
4. Build compatibility matrix: mod A vs mod B, severity, mitigation (patch, load order tweak, choose one).
5. Verify masters exist for every dependent plugin; list missing masters with suggested Nexus search keywords (no auto-download).
6. Write packaging manifest and preflight checklist for a clean test save.
7. Human tests in-game; agent does not claim stability without user confirmation.

## Definition of done

- [ ] README includes install, uninstall, and tool prerequisites
- [ ] Conflict report lists LOOT warnings and pairwise mod conflicts with severity
- [ ] No Nexus upload or deploy without NEXUS_PUBLISH_APPROVED or user-run deploy
- [ ] No pirated or stock game files included in the package tree

## Security

- Nexus API keys and premium tokens must stay in environment variables; never paste into chat or commit to git.
- Third-party mod executables may be malware; recommend hash verification and virus scan before INSTALL_APPROVED.
- Mod packages can contain scripts that touch the host OS; sandbox packaging on the agent machine only when user owns the content.

## Pitfalls

- LOOT supports specific games; running Bethesda LOOT rules against the wrong title silently mis-sorts plugins.
- Vortex hardlinks versus copy deploy change which conflicts appear in overwrite folders.
- Missing DLC masters produce CTD on new game even when LOOT only shows yellow warnings.
- Packing loose BSAs without matching ESP versions causes invisible armor or broken animations.
- Assuming Nexus CDN URLs never expire leads to broken install scripts for collaborators.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Skyrim Special Edition loadout compatibility pass before publishing a community guide mod pack.
- **Input:** 42 mods including USSEP, Legacy of the Dragonborn, and two armor replacers; Vortex profile `Fictional-Adventure-2026`.
- **Prompt:**

```text
Game: Skyrim SE on Vortex profile Fictional-Adventure-2026. Mod list attached. Run compatibility analysis with LOOT conventions. Draft README and conflict report. No Nexus upload.
```

- **Expected result:**

```text
Packaging manifest:
- README.md: requires SKSE64, Address Library, USSEP 4.2.9+
- Install order: USSEP → LOD patches → content mods → replacers last
- Uninstall: disable profile; delete staging overrides listed in section 4

LOOT-style findings (example data):
1. [WARNING] Missing master: LegacyoftheDragonborn.esm requires Dawnguard.esm — user must own DLC
2. [ERROR] Bash Tags conflict: two armor replacers both retexture Iron Armor — choose one or require DAR patch
3. [INFO] Load order suggestion: place music overhaul below ambient town mods

Pairwise conflicts:
| Mod A              | Mod B           | Severity | Mitigation                          |
| IronReplacerA      | IronReplacerB   | High     | Pick one replacer                   |
| CityAmbientAudio   | TownMusicPack   | Low      | Load music below ambient            |

No deploy or upload performed. NEXUS_PUBLISH_APPROVED not set.
```

### Example 2 (Example data (self-written))

- **Task:** Single-mod packaging sanity check for a texture-only release.
- **Input:** One 4K landscape texture archive for a fictional game `ExampleRPG`, MO2 profile `textures-only`.
- **Prompt:**

```text
Package one texture mod for ExampleRPG MO2. Validate no EXE payloads. Output README and file tree only.
```

- **Expected result:**

```text
File tree (example data):
ExampleRPG-Landscape4K/
  README.md
  textures/landscape/example_albedo.dds
  meta.json (author: fictional@example.com, version 1.0.0)

README highlights:
- Manual MO2 install: drop as data mod; no executable
- Compatibility: incompatible with ExampleRPG-UltraLand 2.x (same path)
- Uninstall: remove mod from MO2; clear archive invalidation if used

Security scan note: no .exe or .dll in tree. Ready for human zip and self-hosted distribution; no Nexus API calls made.
```