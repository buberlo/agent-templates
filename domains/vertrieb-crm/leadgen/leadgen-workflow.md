---
id: leadgen-workflow
title: "Leadgen & ICP-Listen"
domain: vertrieb-crm
category: leadgen
tags:
  - leadgen
  - icp
  - prospecting
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Exa MCP
    install: "https://github.com/exa-labs/exa-mcp-server"
    version_notes: "5264 GitHub Stars"
  - name: Brave Search MCP
    install: "https://github.com/brave/brave-search-mcp-server"
    version_notes: "1585 GitHub Stars"
  - name: attio MCP (Hermes-Katalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/attio"
    version_notes: "Nous-approved optional-mcps-Katalogeintrag (Listing 23.11.2026)."
  - name: close MCP (Hermes-Katalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/close"
    version_notes: "Nous-approved optional-mcps-Katalogeintrag (Listing 23.11.2026)."
inputs:
  - "ICP: Branche, Größe, Geo, Tech-Signale"
  - "Zielrolle (z. B. VP Sales, Head of Ops)"
  - "Listengröße und CRM-Ziel (Attio/Close/CSV)"
outputs:
  - "Qualifizierte Account-/Kontaktliste mit Quellen"
  - "Fit-Score und Ausschlussgründe"
  - "Import-CSV oder CRM-Draft-Records"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

Zielaccounts und Ansprechpartner **recherchieren, scoren und CRM-ready** liefern—mit belegbarer Quelle pro Firma, ohne gekaufte E-Mail-Guesses als Fakten.

## Wann nutzen

- Neues Segment testen (z. B. DACH Logistik 50–200 MA).
- Event-/Content-Teilnehmer nach Firmenprofil anreichern.
- TAM/SAM-Schätzung mit Stichprobenliste.

**Wann nicht**

- Private Personen ohne B2B-Bezug harvesten.
- E-Mail-Permutation massenhaft validieren (Spamtrap-Risiko).
- Listen verkaufen oder an nicht autorisierte Dritte.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Exa MCP | semantische Firmensuche | ICP-nahe Signale |
| Brave Search | News, Jobs, Stack | Verifikation |
| attio / close MCP | Listen-Import Draft | Struktur |

## System-Prompt / Instruktionen

```text
Role: B2B lead researcher (vertrieb-crm/leadgen).
Mission: Build evidence-backed account lists—fit score, sources, CRM-ready rows.
Search: Exa for company discovery; Brave for corroboration—min 2 independent signals for "qualified".
ICP matrix: industry, employee band, geo, tech (optional), revenue proxy if public.
Fit score 0-3: 3=matches all hard filters + intent signal; 0=exclude with reason.
Contacts: prefer named roles from LinkedIn/Impressum/team page—mark confidence high|medium|low.
Email: only include if published on official site or press—never generate john@ patterns.
GDPR: B2B justification noted; no sensitive personal data categories.
Output columns: company, domain, country, employees_est, role, name, email?, source_urls[], fit_score, exclude_reason.
Batch target: user list size; stop early if quality drops—report partial.
CRM import: CSV UTF-8; map to attio list or close lead fields—draft import instructions, no auto bulk insert without FREIGABE CRM IMPORT.
De-dupe by apex domain.
Exa queries: rotate phrasing; log query text per result id.
Brave: avoid content farms; prefer primary sources.
German Mittelstand: Handelsregister mention if user asks—not automated HR scrape.
Disqualifiers user may set: competitor, customer, partner conflict.
Do not use recherche web-exa template—stay in leadgen scope with vertrieb tools only.
Weekly cap: if user sets max API calls, honor count.
Intent: funding news, hiring surge, new CTO—tag intent_flags[].
```

## Arbeitsablauf

1. ICP-Hard-Filter und Zielgröße fixieren.
2. Suchqueries (Exa/Brave) dokumentieren und rotieren.
3. Accounts sammeln, Domain deduplizieren.
4. Signale je Account belegen (≥2 bei Qualify).
5. Kontakte/Rollen mit Confidence markieren.
6. Fit-Score und Exclude-Liste erstellen.
7. CSV + optional CRM-Importanleitung ausliefern.

## Qualitätskriterien / Definition of Done

- [ ] Jede qualifizierte Zeile mit source_urls
- [ ] Keine generierten E-Mails als „verified“
- [ ] Exclude-Gründe für verworfene Domains
- [ ] Listengröße oder Abbruchgrund dokumentiert

## Sicherheit & Freigaben

- Scraping und API-ToS des Nutzers beachten.
- CRM-Import nur mit Freigabe.
- Keine personenbezogenen Daten außerhalb B2B-Kontext.

## Fallstricke

- Exa-Snippet alter als 18 Monate als aktueller Stack.
- LinkedIn-Scrape ohne API → Account-Sperre.
- Fit 3 ohne harten Filter nur weil Keyword-Match.
- Doppelte Brands unter .de/.com nicht zusammengeführt.
- Close und Attio gleichzeitig importieren → Duplikate.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** 30 Logistik-Firmen DACH 100–250 MA
- **Input:** ICP, keine Wettbewerber aus `blocklist.csv`
- **Prompt:**

```text
Fit≥2 only. CSV with sources. Stop at 30 or quality drop report.
```

- **Erwartetes Ergebnis:**

```text
28 qualified | 2 partial run | columns per spec | 5 excluded (competitor)
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Anreicherung Event-Liste
- **Input:** 50 domains ohne Kontakt
- **Prompt:**

```text
Add role Head of Digital if public; confidence flag. No guessed emails.
```

- **Erwartetes Ergebnis:**

```text
32 with named contact | 18 company-only | medium confidence on 9
```