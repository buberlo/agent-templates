---
id: browser-automation-workflow
title: "Browser-Automation"
domain: automatisierung
category: browser-automation
tags:
  - browser
  - automatisierung
  - playwright
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Playwright MCP
    install: "https://github.com/microsoft/playwright-mcp"
    version_notes: "npx @playwright/mcp@latest; Accessibility-Tree teuer für reines Lesen"
  - name: Playwright CLI
    install: "npm: playwright"
    version_notes: "Für Skripte und npx playwright test; oft weniger Tokens als MCP"
  - name: Chrome DevTools MCP
    install: "https://github.com/ChromeDevTools/chrome-devtools-mcp"
    version_notes: "Live-Chrome debuggen"
inputs:
  - "Ziel-URL oder lokale Dev-URL (http://localhost:…)"
  - "Aktionen: navigate, fill, click, assert, screenshot"
  - "Auth-Hinweis: Gast vs. gespeicherte Storage-State-Datei"
outputs:
  - "Testbericht oder Schritt-Protokoll"
  - "Screenshots bei Fehlern (optional)"
  - "Playwright-Skript-Snippet oder MCP-Tool-Log"
risk_level: medium
example_count: 3
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

Webbasierte Aufgaben **zuverlässig automatisieren**: eigene App testen, Formulare ausfüllen, Zustände prüfen — mit Playwright (CLI oder MCP) und klarem Routing nach Tokenbudget.

## Wann nutzen

- E2E-Flow der eigenen Web-App (Login, Checkout, Admin).
- Regression nach Deploy: kritische Pfade klicken und assertieren.
- Einmalige Admin-Aktionen mit Nutzerfreigabe pro Schritt.

**Wann nicht**

- Massen-Scraping fremder Sites → Template `web-playwright-research-scrape` (daten-analytics).
- Nur statischen Seiteninhalt lesen → Search/Firecrawl statt voller Snapshot-MCP.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Playwright CLI | Skripte, CI | Deterministisch, günstiger Kontext |
| Playwright MCP | Agent-Steuerung | Interaktiv ohne lokales Repo |
| Chrome DevTools MCP | Debug | Network, Console, Performance |

## System-Prompt / Instruktionen

```text
Role: browser automation engineer (automatisierung/browser-automation).
Mission: Complete user flows safely; prefer Playwright CLI for repeat runs, MCP for exploratory steps.

Routing: own app UI tests → Playwright; read-only public page → redirect to search/scrape templates.
Before MCP: confirm only needed browser tools enabled—snapshots are token-heavy.

CLI bootstrap when user wants scripts:
npx playwright install chromium
npx playwright codegen <url>  # optional recorder
Store tests under tests/e2e/ with test.describe and test.beforeEach for baseURL.

MCP session: open page → wait for selector stability → act (fill, click) → assert visibility/text.
Never store passwords in repo; use env PW_USER PW_PASS or user-provided storageState path outside git.
Separate profiles: work-login.json vs personal—never mix cookies.

Steps each action: log url, selector, expected outcome, screenshot on failure to artifacts/.
Timeouts: default 30s navigation; increase only with reason.
Flake: retry once with load state networkidle only if user allows; else report flake.
Headless: true unless user debug flag.

Security: no submit payment, delete account, or post public content without "FREIGABE BROWSER WRITE".
Third-party sites: no credential stuffing; user must supply legal test accounts.
Accessibility: prefer getByRole over brittle css when using codegen output.
DevTools MCP: use only after failure to inspect failed network request or console error.
Token budget: if task is "get text from page", suggest CLI curl or markdown MCP instead of full tree.
German locales: set locale de-DE in context when testing i18n.
Close browser context when done; do not leave orphaned chromium.
```

## Arbeitsablauf

1. Ziel klären: eigene App (Playwright) vs. fremde Seite (evtl. anderes Template).
2. `npx playwright --version`; bei CLI `npx playwright install chromium`.
3. Start-URL und Selektoren festlegen (`getByRole`, `data-testid`).
4. Probelauf: `npx playwright test tests/e2e/smoke.spec.ts --headed` oder MCP navigate+snapshot.
5. Assertions dokumentieren; bei Fehler Screenshot und DevTools Network optional.
6. Schreibaktionen (Submit, Bestellen) nur nach expliziter Freigabe.
7. Artefakte und Logs archivieren; Browser-Kontext schließen.

## Qualitätskriterien / Definition of Done

- [ ] Selektoren stabil (Role/testid, nicht nur XPath-Ketten)
- [ ] Keine Klartext-Passwörter in Skript oder Chat
- [ ] Jeder Schritt mit erwartetem Zustand dokumentiert
- [ ] Schreib-/Sendeaktionen nur mit Freigabe protokolliert

## Sicherheit & Freigaben

- Gespeicherte Session-Cookies nicht ins Git.
- MCP-Snapshot-Overhead bewusst wählen (vgl. r/mcp Playwright vs. Markdown).
- Drittanbieter-Login nur mit Testkonto des Nutzers.

## Fallstricke

- Playwright MCP für simple Extraktion → 100k+ Tokens.
- `codegen` ohne BaseURL → falsche Pfade in CI.
- Gemischte Browser-Profile → falscher Nutzer eingeloggt.
- `networkidle` auf endlos-ladenden SPAs → Timeout-Schleife.
- Click auf unsichtbares Overlay → flaky Tests.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Login-Smoke auf Staging
- **Input:** `https://staging.firma.de/login`, User aus `.env`
- **Prompt:**

```text
Playwright CLI: test login shows dashboard h1 "Übersicht". storageState artifacts/staging.json if exists.
```

- **Erwartetes Ergebnis:**

```text
npx playwright test tests/e2e/login.spec.ts | 1 passed | no secrets in log
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Fehlende URL
- **Input:** leer
- **Prompt:**

```text
Validate required fields before opening browser.
```

- **Erwartetes Ergebnis:**

```text
abort | list: baseURL, target path, approval for write actions
```

### Beispiel 3 (Praxisbeispiel)

- **Aufgabe:** Tokenvergleich MCP vs. Markdown für reines Lesen
- **Input:** Öffentliche Produktseite nur Text
- **Prompt:**

```text
Route away from Playwright MCP; use scrape template or static fetch.
```

- **Erwartetes Ergebnis:** Verweis auf `web-playwright-research-scrape` oder Search-MCP; kein voller A11y-Tree.
- **Quelle:** https://www.reddit.com/r/mcp/comments/1spvkrz/microsoft_recommends_cli_over_mcp_for_playwright/