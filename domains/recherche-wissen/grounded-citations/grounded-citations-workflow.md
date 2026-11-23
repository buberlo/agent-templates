---
id: grounded-citations-workflow
domain: recherche-wissen
title: "Belegpflicht und Quellenzitate"
category: grounded-citations
tags:
  - citations
  - sources
  - verify
target_agents:
  - hermes
  - grokbot
  - generic
required_tools:
  - name: Hermes grounded-citations
    install: "https://hermes-agent.nousresearch.com/docs/reference/skills-catalog"
    version_notes: "Bundled"
  - name: Firecrawl MCP
    install: "https://github.com/firecrawl/firecrawl-mcp-server"
    version_notes: "URL verify"
inputs:
  - "Textentwurf oder Frage"
  - "Quellenformat (APA, inline URL)"
outputs:
  - "Überarbeiteter Text mit Zitaten"
  - "Quellenprüf-Log"
risk_level: low
version: "1.1.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

**Antworten an prüfbare Quellen binden**—jede Kernbehauptung mit URL, Datum oder Paper-ID, UNVERIFIED sonst.

## Wann nutzen

- Agenten-Output für Kunden oder Wiki.
- Fact-check nach Web-Recherche.
- Kombination mit akademisch oder news-monitoring.

**Wann nicht**

- Kreative Fiktion.
- Interne Hypothesen ohne Veröffentlichungsbedarf.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| grounded-citations | Skill-Regeln | Disziplin |
| Firecrawl | Fetch | Quote check |
| arxiv | Paper IDs | Akademisch |

## System-Prompt / Instruktionen

```text
You rewrite or produce text where every factual claim is grounded or marked UNVERIFIED—Hermes grounded-citations discipline.

Inputs: draft text or question, citation style (inline [url] | footnote | APA rough), allow UNVERIFIED sections yes/no.

For each sentence with number, date, law, product feature, or quote:
- Attach source url + access date OR paper id OR mark UNVERIFIED.
- Fetch with firecrawl when url already provided by user to confirm wording.

Quotes: max 25 words unless user has license; use quotation marks.

Remove fabricated references—if no source found after one search pass, downgrade claim to UNVERIFIED or delete.

Source log table: claim_id | source | status OK|UNVERIFIED|CONFLICT.

Contradictions: keep both with citations.

Approvals: publish grounded text externally requires user yes.

No legal/medical authority voice.

Output: grounded.md, source_log.csv.

Do not cite Wikipedia as sole primary for regulated topics—use primary linked there.

When user supplies only chat context, never invent urls.

Refresh access date to ISO on edit.
```

## Arbeitsablauf

1. Claims aus Entwurf extrahieren.
2. Pro Claim Quelle suchen oder Nutzer-URL fetchen.
3. Status OK/UNVERIFIED setzen.
4. Text mit Zitaten neu schreiben.
5. source_log.csv pflegen.
6. Konflikte Abschnitt einfügen.
7. Freigabe vor Publish.

## Qualitätskriterien / Definition of Done

- [ ] Keine Behauptung ohne Tag
- [ ] source_log vollständig
- [ ] Keine erfundenen URLs
- [ ] Quotes gekürzt
- [ ] Publish-Freigabe dokumentiert

## Sicherheit & Freigaben

- Keine internen URLs in öffentliche Texte ohne Freigabe.
- Paywall-Volltext nicht verbreiten.
- Quellen-Log kann sensibel sein.

## Fallstricke

- Link rot aber behauptet OK.
- arXiv als Journal.
- Ein Blog als einzige Quelle.
- UNVERIFIED vergessen zu labeln.
- Zitat aus Snippet nicht im Artikel.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Marketing-Absatz fact-checken.
- **Input:** 5 Sätze mit Statistiken.
- **Prompt:**

```text
Ground each stat or UNVERIFIED; firecrawl user urls; source_log.csv.
```

- **Erwartetes Ergebnis:**

```text
grounded.md; 2 UNVERIFIED; source_log 5 rows.
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Fake URL entfernen.
- **Input:** Draft cites https://example-fake.domain/study
- **Prompt:**

```text
Verify urls; remove fabricated links.
```

- **Erwartetes Ergebnis:**

```text
Fake url removed; claim UNVERIFIED or deleted.
```