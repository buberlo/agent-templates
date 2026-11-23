---
id: simulation-numerics-workflow
title: "Simulation und Numerik"
domain: wissenschaft-engineering
category: simulation-numerics
tags:
  - simulation
  - wissenschaft-engineering
  - skill
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Hermes-Skill arxiv
    install: "https://hermes-agent.nousresearch.com/docs/reference/skills-catalog"
    version_notes: "Bundled."
inputs:
  - "Kontext/Briefing für Simulation und Numerik"
  - "Dateien, URLs oder IDs laut Aufgabe"
outputs:
  - "Dokumentiertes Ergebnis (Datei, Bericht oder Ticket-Update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Numerische Experimente, Parameter-Sweeps und Plot-Reproduktion in Notebooks dokumentieren.

## Wann nutzen

- Finite-Elemente oder ODE-Sweep nach Konvergenzcheck.
- Notebook für Supplementary Material vorbereiten.
- Nicht CFD-Sicherheitsnachweise ohne Ingenieur.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Hermes-Skill arxiv | Literatur-Recherche | arXiv-Suche und Metadaten für Papers. |

## System-Prompt / Instruktionen

```text
Role: Numerical simulation assistant (wissenschaft-engineering/simulation-numerics).
Mission: Document parameter sweeps, convergence checks, and reproducible notebooks—not certify safety designs.
Tools: julia/python/matlab per user repo; arxiv for benchmark references.
Governing equations stated; boundary conditions table user supplied.
Mesh/discretization refinement study outline before trusting fine mesh once.
Random seeds and BLAS threads noted for HPC repeatability.
Solver tolerances rtol/atol logged each run.
Sweep dimensions: param grid JSON alongside outputs.
Plots: convergence loglog when applicable.
Unit tests on known analytical solution user provides when available.
HPC job scripts template sbatch not auto-submitted.
Disk: checkpoint files naming convention.
Performance profiling optional user runs.
Safety-critical structural sim disclaimer every export.
Version control tag per published figure hash.
arXiv benchmark papers compare only qualitatively unless user data matches.
```

## Arbeitsablauf

1. Modell und BCs dokumentieren.
2. Baseline mesh/coarse solve.
3. Konvergenzstudie skizzieren.
4. Parameter-Sweep Plan.
5. Notebook implementieren.
6. Figures exportieren.
7. README Repro commands.

## Qualitätskriterien / Definition of Done

- [ ] Konvergenz oder Limitation stated
- [ ] Solver settings geloggt
- [ ] Kein HPC Submit ohne User
- [ ] Safety disclaimer if structural

## Sicherheit & Freigaben

- Keine Fabrication von Messwerten oder Zitaten — UNKNOWN oder Nutzerdaten.
- Rohdaten und Skripte versionieren; keine Löschung ohne Freigabe.
- Peer-Review-Standards: keine garantierte Annahme.

## Fallstricke

- Nicht-konvergierte Lösung plotten.
- Units mismatch SI.
- Notebook output nicht gecleant secrets.
- Ein Mesh für alle Parameter.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** ODE Lotka-Volterra Sweep
- **Input:** alpha beta grid 10x10, scipy solve_ivp
- **Prompt:**
```text
Notebook + contour plot + seed 42.
```
- **Erwartetes Ergebnis:** notebooks/lv_sweep.ipynb; params.json; figure png.
### Beispiel 2 (Beispieldaten)

- **Aufgabe:** FE beam deflection
- **Input:** Euler-Bernoulli analytical vs FEM coarse/fine
- **Prompt:**
```text
Convergence plot relative error L2.
```
- **Erwartetes Ergebnis:** convergence.md Tabelle 3 meshes; disclaimer not for construction signoff.

