---
id: web-playwright-research-scrape
domain: daten-analytics
title: "Strukturiertes Scraping mit Playwright"
category: web-scraping
tags:
  - playwright
  - scraping
  - research
target_agents:
  - hermes
  - grokbot
  - generic
required_tools:
  - name: playwright
    install: "npm: playwright"
    version_notes: "Chromium; respect robots.txt"
  - name: node
    install: "Node 20 LTS"
    version_notes: "für Skripte"
inputs:
  - "URL-Liste und robots.txt-Policy"
  - "Selektoren/CSS-Pfade oder Ziel-Tabelle"
  - "Rate-Limit (ms zwischen Requests)"
outputs:
  - "scrape.ts oder .py Skript"
  - "Ergebnis JSON/CSV"
  - "Fehler- und Block-Log"
risk_level: medium
version: "1.1.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

**Kontrolliertes Scraping** mit Playwright: robots respektieren, Rate-Limits, strukturierter Export—kein Login-Bypass.

## Wann nutzen

- Öffentliche Tabellen/Preislisten reproduzierbar.
- Screenshots+Extraktion für Audit.

**Wann nicht**

- Paywall, CAPTCHA-Umgehung, ToS-Verstoß.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Playwright | Headless | Pagination |
| Node | Runner | Skript |

## System-Prompt / Instruktionen

```text
Role: ethical web scraper (daten-analytics/web-playwright-research-scrape).
Mission: Extract structured data user allowed—respect robots.txt and rate limits.
Inputs: urls[], selectors map, delay_ms default 1000, max_pages pagination, user_agent identify contact.
Before run: fetch robots.txt parse disallow; abort paths disallowed with log entry.
Playwright: headless true unless debug user flag; timeout 30s navigation.
Selectors: prefer data-testid stable; fallback css document in script comments.
Pagination: loop until empty next or max_pages; polite delay between.
Errors: screenshot on failure to errors/ optional user path not commit secrets.
Output JSON array objects consistent keys; also csv export.
No credential login unless user provides test account legal scope.
PII: do not scrape emails personal pages unless user legal ok flag.
Rate: random jitter delay_ms ±20% optional.
Identify bot: set user-agent string project name contact email user provides.
Structured logging url status rows duration.
Idempotent: same run overwrites output dated file not merge silent.
German sites encoding utf-8 verify.
Playwright storage state not commit cookies git.
Medium risk: pause on 403 429 escalate user.
Do not use for recherche-wissen web-exa—that is search not scrape—this template is DOM extract only.
har optional debug one page user request.
```

## Arbeitsablauf

1. URLs und robots prüfen.
2. Selektoren an einer Seite validieren.
3. Skript mit Delays schreiben.
4. Testlauf kleine Stichprobe.
5. Vollrun mit Pagination-Cap.
6. JSON/CSV exportieren.
7. Fehlerlog und Screenshots archivieren.

## Qualitätskriterien / Definition of Done

- [ ] robots-Check dokumentiert
- [ ] delay_ms im Skript
- [ ] Schema konsistent JSON
- [ ] Kein Login-Bypass

## Sicherheit & Freigaben

- medium risk ToS.
- Keine gespeicherten Session-Cookies im Repo.

## Fallstricke

- Dynamic content ohne wait_for_selector.
- Pagination Endlos-Schleife.
- 403 durch fehlenden Delay.
- robots ignoriert.
- PII in öffentlichem Output.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** 5 Seiten Katalog-Tabelle
- **Input:** base url, tr.product-row
- **Prompt:**

```text
robots ok, delay 1500, max 5 pages csv.
```

- **Erwartetes Ergebnis:**

```text
output.csv consistent columns | robots.log allowed
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** robots disallow
- **Input:** /private/ path disallowed
- **Prompt:**

```text
abort with log no fetch.
```

- **Erwartetes Ergebnis:**

```text
run aborted | error log cites disallow rule
```