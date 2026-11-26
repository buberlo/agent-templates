---
id: game-dev-workflow
title: "Game Development"
domain: software-development
category: game-dev
tags:
  - gamedev
  - unity
  - godot
target_agents:
  - hermes
  - claude-code
  - cursor
  - generic-mcp-agents
required_tools:
  - name: godot
    install: "Godot 4 CLI"
    version_notes: "godot --headless --quit-after 1"
  - name: git
    install: "LFS for assets if needed"
    version_notes: "large binary policy"
inputs:
  - "Engine (Godot/Unity) and scene"
  - "Feature scope (gameplay/UI)"
outputs:
  - "Scene/script changes"
  - "Headless smoke or test scene"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Purpose

Implement gameplay and UI logic in Godot/Unity — **headless smoke**, asset discipline, performance clues.

## When to use

- Mechanic prototype, Bug in GDScript/C#.
- Prepare export pipeline.

**When not:** AAA asset production without artist pipeline.

## Tool stack

| Tool | Role | Justification |
|------|-------|------------|
| Godot CLI | CI smoke | headless |
| git LFS | assets | if required by policy |
| engine tests | GUT/NUnit | project |

## System prompt

```text
Game dev workflow (software-development/game-dev).

Prefer data-driven parameters (Resource/ScriptableObject) over magic numbers.
Physics and input in _physics_process vs _process appropriately.
Profile expensive _process loops; avoid per-frame allocations.
Scene isolation: minimal repro scene for bugs.
Godot: godot --headless --path . --script res://tests/smoke.gd if project has.
Unity: batchmode tests if user provides command.
No copyrighted assets generated; placeholder shapes only.
Multiplayer: defer without netcode spec.
Document scene tree changes for designers.
Version pin engine in export preset notes.
```

## Workflow

1. Engine version and project.godot/ProjectSettings.
2. Szene/Script lokalisieren.
3. Implement with a clear node hierarchy.
4. Headless smoke or Test-Szene.
5. Profiler note if there is an FPS issue.
6. git commit without accidental large binaries.
7. Export notes in README.

## Definition of done

Smoke runs headless or documented editor step
- [ ] No illegalen Assets
- [ ] Input/Physics korrekt getrennt

## Security

- Online features with moderation not without Spec.

## Pitfalls

- Godot headless requires display tricks — project config.
- Git without LFS — repo explode.
- Singleton order race.
- Unit vs integration in engine fuzzy.
- Mobile perf on desktop only tested.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Jump cooldown Godot.
- **Input:** player.tscn.
- **Prompt:**

```text
Add 0.3s cooldown; export var; smoke test script.
```

- **Expected result:**

```bash
godot --headless --path . --script res://tests/player_jump.gd
# OK
```

### Example 2 (Example data (self-written))
- **Task:** UI lag fix.
- **Input:** inventory scroll.
- **Prompt:**

```text
Virtualize list or pool items; note profiler before/after targets.
```

- **Expected result:**

```text
Instancing pooled rows; target <2ms _process
```