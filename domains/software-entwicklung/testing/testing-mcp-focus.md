---
id: testing-mcp-focus
title: "Testing: MCP/Skill-Fokus"
domain: software-entwicklung
category: testing
tags:
  - testing
  - mcp
  - playwright
target_agents:
  - hermes
  - claude-code
  - cursor
  - generic-mcp-agents
required_tools:
  - name: Playwright MCP
    install: "https://github.com/microsoft/playwright-mcp"
    version_notes: "Debug; CLI für CI"
  - name: Chrome DevTools MCP
    install: "https://github.com/ChromeDevTools/chrome-devtools-mcp"
    version_notes: "Performance traces"
  - name: playwright CLI
    install: "npx playwright"
    version_notes: "Verify step in skill"
inputs:
  - "App URL (staging)"
  - "Skill TDD steps"
outputs:
  - "Skill↔MCP matrix"
  - "Exported playwright spec"
risk_level: low
example_count: 3
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

**Playwright MCP** für interaktives Debuggen; Skill verlangt **CLI-Verify** (`npx playwright test`) vor Merge — MCP nicht als einzige Testquelle.

## Wann nutzen

- UI-Flow explorieren, danach Spec generieren.
- Performance-Spike mit Chrome DevTools MCP.

**Wann nicht:** Reine API-Tests — pytest only.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Playwright MCP | Explore | Snapshots teuer |
| playwright CLI | Verify | CI parity |
| TDD Skill | Reihenfolge | red-green-refactor |

## System-Prompt / Instruktionen

```text
Testing MCP/Skill focus (software-entwicklung/testing).

Skill phases: explore (MCP optional) -> write spec file -> verify (CLI mandatory) -> commit.
Limit Playwright MCP turns; prefer codegen export to tests/e2e/*.spec.ts then CLI.
Chrome DevTools MCP only for perf/network diagnosis step, not default every test.
MCP snapshot token cost: warn when task is extract-only HTML.
Hermes TDD skill: failing test commit before implementation.
Never mark DoD complete without npx playwright test exit 0 locally or CI link.
Matrix: Step Explore | MCP browser; Step Verify | CLI only.
Disable Playwright MCP during CI agent job if duplicate.
Do not store credentials in MCP session prompts.
```

## Arbeitsablauf

1. Skill-Matrix Explore vs Verify definieren.
2. Optional MCP: navigate staging login (read-only data).
3. Spec aus MCP/codegen in Repo schreiben.
4. `npx playwright test` — Skill Verify.
5. Bei Fail: trace `npx playwright show-trace`.
6. Unit-Tests parallel `npm test`.
7. PR mit Testplan.

## Qualitätskriterien / Definition of Done

- [ ] CLI playwright grün
- [ ] MCP nur wo dokumentiert
- [ ] Keine Secrets in Specs

## Sicherheit & Freigaben

- Staging-URLs only default.
- MCP-Screenshots können PII — nicht öffentlich posten.

## Fallstricke

- Nur MCP — keine CI-Reproduzierbarkeit.
- Riesige A11y-Snapshots — Kontext voll.
- DevTools MCP auf Prod.
- Spec aus veralteter UI.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Matrix Checkout-Flow.
- **Input:** staging shop.
- **Prompt:**

```text
MCP explore cart; write spec; npx playwright test verify.
```

- **Erwartetes Ergebnis:**

```text
tests/e2e/cart.spec.ts added
npx playwright test → 3 passed
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** MCP vermeiden bei API-only.
- **Input:** REST service.
- **Prompt:**

```text
pytest only skill; no Playwright MCP enabled.
```

- **Erwartetes Ergebnis:**

```bash
pytest -q
# MCP count 0
```

### Beispiel 3 (Praxisbeispiel)

- **Aufgabe:** Performance regression.
- **Input:** langsame Dashboard-Ladezeit.
- **Prompt:**

```text
Chrome DevTools MCP trace one navigation; suggest test via CLI measureNavigationTiming.
```

- **Erwartetes Ergebnis:**

```text
LCP 4.2s flagged; add playwright performance assertion in spec
```