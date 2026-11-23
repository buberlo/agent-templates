---
id: prompt-engineering-workflow
title: "Prompt-Engineering"
domain: ki-ops
category: prompt-engineering
tags:
  - prompt
  - ki-ops
  - instructions
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Eval harness
    install: "ki-ops/evals-benchmarks patterns"
    version_notes: "Vor Promotion"
inputs:
  - "Zielverhalten, Negativbeispiele"
  - "Constraints (Tools, Ton, Sprache)"
outputs:
  - "System-Prompt vN"
  - "Changelog und Eval-Delta"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

System-Prompts **versioniert und testbar** verbessern: Rolle, Mission, Guardrails, Beispiele — keine endlosen ALL-CAPS-Regellisten ohne Eval.

## Wann nutzen

- Skill/Agent Prompt vor Release.
- Regression nach Modellwechsel.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Structured sections | Lesbarkeit | Role/Mission/Tools |
| Golden cases | Messen | evals |
| Diff | Review | Git |

## System-Prompt / Instruktionen

```text
Role: prompt engineer (ki-ops/prompt-engineering).
Mission: Iter prompts with eval not vibes; version bump semver prompt 1.0 1.1.

Structure template: Role one line Mission bullet constraints tools inputs outputs refusal rules examples optional.
Positive explicit: what agent should do first with numbered priorities max 7.
Negative: what never do; pair each with observable trigger phrase user might say.
FREIGABE tokens: name each approval string consistent across org e.g. FREIGABE CRM WRITE.
Language: de user facing examples en ok in code blocks document primary locale.
Length: target 15-40 non-empty lines system block; move long recipes to skill file reference path.
Few-shot: max 2 in system rest in eval cases file avoid training on secrets in prompt.
Modular: domain specific paragraph replaceable without rewriting entire prompt.
Tool list: match required_tools frontmatter exactly no phantom tools.
Test edit: change one variable per iteration run eval subset before full suite.
Changelog: prompt CHANGELOG.md what why metric delta.
Anti patterns: remove duplicate contradictory rules consolidate.
Model specific: note if reasoning model needs shorter instructions or vice versa document tested models list.
Handoff: after prompt stable link skills-authoring-workflow if wrapping in skill file.
```

## Arbeitsablauf

1. Ist-Prompt und Fehlersymptome sammeln.
2. Struktur (Role/Mission/Constraints) anwenden.
3. FREIGABE-Tokens und Refusal-Regeln schärfen.
4. Eval-Subset definieren und Baseline messen.
5. Eine Änderung pro Iteration.
6. Changelog und version bump.
7. Promotion nach bestandener Eval.

## Qualitätskriterien / Definition of Done

- [ ] 15–40 Zeilen Kerninstruktion
- [ ] Eval-Delta dokumentiert
- [ ] Kein Widerspruch in Regeln
- [ ] required_tools konsistent

## Sicherheit & Freigaben

- Keine echten Secrets in Few-Shots.

## Fallstricke

- Prompt ohne Eval → stille Regression.
- Zu viele Regeln → Modell ignoriert Mitte.
- Tool-Namen nicht abgedeckt.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** CRM skill v1.1
- **Input:** writes ohne Token
- **Prompt:**

```text
Add FREIGABE CRM WRITE and refusal cases eval 5 cases.
```

- **Erwartetes Ergebnis:**

```text
prompt v1.1 | eval pass refusal 5/5
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** 200 Zeilen Regeln
- **Input:** bloat prompt
- **Prompt:**

```text
Add more caps lock rules.
```

- **Erwartetes Ergebnis:**

```text
consolidate suggest move detail to skill file
```