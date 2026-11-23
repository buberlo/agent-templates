---
id: game-dev-workflow
title: "Game Development"
domain: software-entwicklung
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
  - "Engine (Godot/Unity) und Szene"
  - "Feature scope (gameplay/UI)"
outputs:
  - "Scene/script changes"
  - "Headless smoke or test scene"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Gameplay- und UI-Logik in Godot/Unity umsetzen — **headless smoke**, Asset-Disziplin, Performance-Hinweise.

## Wann nutzen

- Mechanic prototype, Bug in GDScript/C#.
- Export-Pipeline vorbereiten.

**Wann nicht:** AAA-Asset-Produktion ohne Artist-Pipeline.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Godot CLI | CI smoke | headless |
| git LFS | assets | wenn policy |
| engine tests | GUT/NUnit | project |

## System-Prompt / Instruktionen

```text
Game dev workflow (software-entwicklung/game-dev).

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

## Arbeitsablauf

1. Engine version und project.godot/ProjectSettings lesen.
2. Szene/Script lokalisieren.
3. Implementieren mit klarer Node-Hierarchie.
4. Headless smoke oder Test-Szene.
5. Profiler-Hinweis wenn FPS-issue.
6. git commit ohne accidental large binaries.
7. Export notes in README.

## Qualitätskriterien / Definition of Done

- [ ] Smoke läuft headless oder Editor-Steps dokumentiert
- [ ] Keine illegalen Assets
- [ ] Input/Physics korrekt getrennt

## Sicherheit & Freigaben

- Online-Features mit Moderation nicht ohne Spec.

## Fallstricke

- Godot headless braucht Display tricks — project config.
- Git ohne LFS — repo explode.
- Singleton order race.
- Unit vs integration in engine fuzzy.
- Mobile perf on desktop only tested.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Jump cooldown Godot.
- **Input:** player.tscn.
- **Prompt:**

```text
Add 0.3s cooldown; export var; smoke test script.
```

- **Erwartetes Ergebnis:**

```bash
godot --headless --path . --script res://tests/player_jump.gd
# OK
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** UI lag fix.
- **Input:** inventory scroll.
- **Prompt:**

```text
Virtualize list or pool items; note profiler before/after targets.
```

- **Erwartetes Ergebnis:**

```text
Instancing pooled rows; target <2ms _process
```