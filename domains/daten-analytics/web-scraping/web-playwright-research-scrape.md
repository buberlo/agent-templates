---
id: web-playwright-research-scrape
domain: daten-analytics
title: "Strukturierte Web-Recherche mit Playwright"
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
  - "URL-Liste"
  - "Selektoren/CSS"
  - "Rate-Limit"
outputs:
  - "JSON Datensatz"
  - "Screenshots optional"
risk_level: medium
version: "1.0.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

Öffentliche Quellen strukturiert auslesen für Wettbewerbs- oder Marktanalysen.

## Wann nutzen

- Preislisten, Dokumentationsseiten, Verzeichnisse.
- Nicht gegen ToS oder login-geschützte Bereiche ohne Berechtigung.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Playwright | Browser automation | JS-heavy Sites |
| cheerio | Parse HTML | Leichtgewicht |
| trafilatura | Main content | Artikel extrahieren |

## System-Prompt / Instruktionen

```text
Scrape only allowed URLs; honor robots.txt and rate limits.
Use playwright for dynamic pages; extract to JSON schema provided.
Store fetched_at timestamp and source URL per record.
Stop and report on CAPTCHA or 403; do not bypass paywalls.
```

## Arbeitsablauf

1. Zielschema definieren.
2. Pilot auf 5 URLs.
3. Batch mit Delay 1–2 s.
4. Validierung gegen Schema.
5. Quellenverzeichnis beilegen.

## Qualitätskriterien / Definition of Done

- [ ] Alle Pflichtfelder befüllt
- [ ] robots.txt beachtet dokumentiert
- [ ] Reproduzierbares Skript im Repo

## Sicherheit & Freigaben

- Keine Credentials in Skripten committen.
- Rechtliche Prüfung bei personenbezogenen Verzeichnissen.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

_Siehe vorheriger Abschnitt; bei Migration ergänzt._

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Validierung
- **Input:** n/a
- **Prompt:** `validate output`
- **Erwartetes Ergebnis:** OK

## Beispiele (Legacy)

**Eingabe:** 50 Produkt-URLs, Schema `product.json`
**Erwartetes Ergebnis:** `products.json`, `fetch.log`
