---
id: web-exa-perplexity-briefing
title: "Recherche-Briefing mit Exa und Perplexity"
category: web-recherche
tags:
  - exa
  - perplexity
  - briefing
target_agents:
  - grokbot
  - generic
required_tools:
  - name: exa
    install: "API: exa.ai"
    version_notes: "Neural search API"
  - name: perplexity
    install: "API: perplexity.ai"
    version_notes: "sonar-pro für Zitate"
inputs:
  - "Fragestellung"
  - "Zeitraum"
  - "Sprache"
outputs:
  - "Briefing MD"
  - "Quellenliste mit URLs"
risk_level: low
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Aktuelle Fakten zu einem Thema sammeln, bewerten und als Entscheidungsbriefing aufbereiten.

## Wann nutzen

- Vor Investitionen, Vendor-Auswahl, Policy-Updates.
- Nicht als alleinige Rechts- oder Medizinberatung.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Exa | Semantische Suche | Hochwertige Treffer |
| Perplexity | Synthese | Zitierte Antworten |
| Zotero | optional | Quellen verwalten |

## System-Prompt / Instruktionen

```text
Research with Exa search then Perplexity synthesis.
Every factual claim must cite URL and retrieval date.
Separate facts from inference; mark low-confidence items.
German output unless user specifies English.
```

## Arbeitsablauf

1. Frage in Teilfragen zerlegen.
2. Exa: 15–30 Quellen sammeln.
3. Deduplizieren; Paywall-Quellen markieren.
4. Perplexity/ manuell strukturieren.
5. Executive Summary + Detailanhang.

## Qualitätskriterien / Definition of Done

- [ ] Mindestens 5 unabhängige Primärquellen
- [ ] Widersprüche explizit benannt
- [ ] Datum der Recherche im Dokument

## Sicherheit & Freigaben

- API-Keys aus Umgebungsvariablen.
- Keine internen Codenamen in externen Suchanfragen.

## Beispiele

**Eingabe:** "EU AI Act Auswirkungen auf SaaS 2026"
**Erwartetes Ergebnis:** `briefing_ai_act.md` mit 12 Quellen
