---
id: web-exa-perplexity-briefing
title: "Recherche-Briefing mit Exa und Zitaten"
domain: recherche-wissen
category: web-recherche
tags:
  - exa
  - briefing
  - citations
target_agents:
  - grokbot
  - generic-mcp-agents
  - hermes
required_tools:
  - name: Exa MCP
    install: "https://github.com/exa-labs/exa-mcp-server"
    version_notes: "Search + crawl"
  - name: Firecrawl MCP
    install: "https://github.com/firecrawl/firecrawl-mcp-server"
    version_notes: "Verify sources"
  - name: Hermes grounded-citations
    install: "https://hermes-agent.nousresearch.com/docs/reference/skills-catalog"
    version_notes: "Citation discipline"
inputs:
  - "Entscheidungsfrage"
  - "Zeitfenster und Sprache"
outputs:
  - "briefing.md"
  - "sources.bib oder URL-Liste"
risk_level: low
version: "1.1.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

**Entscheidungsbriefings** aus aktuellen Webquellen—Frage → Exa/Firecrawl → belegte Aussagen mit URLs, keine erfundenen Fakten.

## Wann nutzen

- Vendor-Auswahl, Policy-Updates, Markt-Snapshots.
- Vor Meeting oder Investment-Memo.
- Zeitgebundene Frage (letzte 12 Monate).

**Wann nicht**

- Rechts- oder Medizinberatung allein aus Web.
- Geheimprojekte mit exfiltration-Risiko ohne Freigabe.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Exa MCP | Suche | Agent-orientiert |
| Firecrawl | Volltext | Verifikation |
| grounded-citations | Disziplin | Keine halluz. Links |
| Brave | Optional | Zweitmeinung |

## System-Prompt / Instruktionen

```text
You produce decision briefings grounded in fetched sources—not Perplexity-only when user has Exa+Firecrawl.

Inputs: decision question, time window (e.g. since 2025-01-01), language, output briefing.md, max sources 12.

Process:
- Decompose question into 3-5 subquestions.
- Exa search per subquestion; collect candidates.
- Firecrawl verify: each key claim needs at least one fetched paragraph supporting it.
- Mark UNVERIFIED when paywall blocked.

Briefing structure:
- Executive summary (5 bullets)
- Findings per subquestion with [n] footnotes
- Risks and contradictions between sources
- Recommended next steps (human decisions)
- Source table: url | title | date | trust note

grounded-citations skill rules: no fabricated URLs; if unsure omit claim.

Contradictions: present both sides with citations.

Approvals: share briefing externally, send to board requires user yes.

No investment advice language—informational only.

Output files: briefing.md, sources.md

Avoid copying entire articles—fair-use excerpts only.

If API perplexity requested as secondary, label model-generated synthesis separately from fetched facts.
Timestamp access date on every url.
Downrank content farms and SEO spam in source table.
```

## Arbeitsablauf

1. Frage und Zeitfenster fixieren.
2. Subfragen ableiten.
3. Exa pro Subfrage (max 5 Treffer).
4. Firecrawl auf Kern-URLs.
5. Claims ↔ Quellen mappen.
6. briefing.md schreiben.
7. Nutzer Review UNVERIFIED markieren.

## Qualitätskriterien / Definition of Done

- [ ] Jede Kernaussage mit [n] oder UNVERIFIED
- [ ] sources.md vollständig
- [ ] Widersprüche dokumentiert
- [ ] Zeitraum eingehalten
- [ ] Kein externer Versand ohne Freigabe

## Sicherheit & Freigaben

- Keine internen Codenamen in Suchqueries ohne Freigabe.
- API keys geschützt.
- Board-Briefings manuell freigeben.

## Fallstricke

- Exa-Snippet ohne Firecrawl-Check.
- Alte Blogposts als „aktuell“.
- Ein Quellen-Bias.
- Footnotes ohne URL.
- Perplexity-Zitat ohne Primary fetch.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** EU AI Act Vendor Shortlist.
- **Input:** Frage 3 Vendors, since 2024-08.
- **Prompt:**

```text
Exa+Firecrawl briefing; 10 sources max; footnoted claims; briefing.md + sources.md.
```

- **Erwartetes Ergebnis:**

```text
briefing.md with [1]-[n]; sources.md urls with dates; UNVERIFIED lines if paywall.
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Behauptung ohne Quelle streichen.
- **Input:** Draft claim „Market share 80%“.
- **Prompt:**

```text
Remove or mark UNVERIFIED any claim without firecrawl excerpt.
```

- **Erwartetes Ergebnis:**

```text
Claim removed or labeled UNVERIFIED in revised briefing.md.
```