---
id: model-routing-workflow
title: "Model-Routing"
domain: ki-ops
category: model-routing
tags:
  - routing
  - ki-ops
  - models
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: AI Gateway / Router
    install: "Vercel AI Gateway, LiteLLM, oder Provider-Router"
    version_notes: "Fallback-Kette"
inputs:
  - "Tasks mit Latenz/Kosten/Qualität"
  - "Modellliste und Limits"
outputs:
  - "Routing-Tabelle"
  - "Fallback-Policy"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

**Modelle pro Aufgabe routen**: billig/schnell für Klassifikation, stark für Code — mit Fallback bei Ausfall und Kosten-Obergrenze.

## Wann nutzen

- Multi-Model-Agent-Plattform im Team.
- Kosten-Explosion bei einem Modell.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Router config | Policy | zentral |
| Small model | Triage | günstig |
| Large model | Hard tasks | Qualität |

## System-Prompt / Instruktionen

```text
Role: model routing architect (ki-ops/model-routing).
Mission: Table task_class primary model fallback max_cost_per_request log metrics.

Task classes: triage classify extract summarize code review codegen long context research.
Triage always small model route label confidence if below 0.7 escalate large.
Code: prefer model strong at code use same for review different temperature 0.
Long context only if token count exceeds small model window measure before route.
Fallback chain primary secondary after timeout 60s or 429 twice.
Cost cap: abort or downgrade if estimated input output cost exceeds user daily cap variable.
Privacy: eu data residency route eu endpoints only list models compliant.
Log: route decision model id latency tokens cost per request id.
Human override user says USE MODEL X lock session ignore router.
Eval: monthly sample 50 tasks compare router vs always-large cost quality delta.
No routing secret keys in client—gateway holds keys.
Stream: same route sticky within conversation turn multi-step tools.
German quality: note models weak at legal de escalate if user domain legal.
A/B: optional canary 10 percent new model compare eval harness ki-ops/evals-benchmarks.
```

## Arbeitsablauf

1. Aufgabenklassen definieren.
2. Modelle mit Stärken/Schwächen tabellieren.
3. Primär/Fallback pro Klasse setzen.
4. Kosten- und Timeout-Regeln.
5. Router-Config schreiben (LiteLLM/Gateway).
6. Logging-Felder festlegen.
7. Monatlicher Eval-Sample planen.

## Qualitätskriterien / Definition of Done

- [ ] Jede Task-Klasse hat Primary+Fallback
- [ ] Kosten-Cap dokumentiert
- [ ] Residency-Regel wenn EU

## Sicherheit & Freigaben

- Keys nur im Gateway.

## Fallstricke

- Immer Large → Kosten.
- Fallback nie getestet → Ausfall.
- Triage-Fehler kaskadiert.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Support triage + answer
- **Input:** tickets
- **Prompt:**

```text
Route classify small answer large if billing.
```

- **Erwartetes Ergebnis:**

```text
routing table | fallback on 429
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** EU PII
- **Input:** customer data
- **Prompt:**

```text
Use cheapest US model.
```

- **Erwartetes Ergebnis:**

```text
block or eu-only models | residency note
```