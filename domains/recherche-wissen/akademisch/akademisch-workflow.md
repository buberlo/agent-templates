---
id: akademisch-workflow
domain: recherche-wissen
title: "Akademische Literatursuche"
category: akademisch
tags:
  - arxiv
  - papers
  - citations
target_agents:
  - hermes
  - generic
required_tools:
  - name: Hermes-Skill arxiv
    install: "https://hermes-agent.nousresearch.com/docs/reference/skills-catalog"
    version_notes: "Bundled research/arxiv"
  - name: Hermes grounded-citations
    install: "https://hermes-agent.nousresearch.com/docs/reference/skills-catalog"
    version_notes: "No fake DOI"
inputs:
  - "Suchthema oder Paper-ID"
  - "Zitationsstil optional"
outputs:
  - "Paper-Liste mit Metadaten"
  - "Lesenotizen mit IDs"
risk_level: low
version: "1.1.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

**Papers finden und erschließen** (arXiv, IDs)—Abstract, PDF-Link, zitierfähige Metadaten, **keine erfundenen DOI**.

## Wann nutzen

- Related Work für Projekt oder Thesis.
- Paper-ID vom Nutzer vertiefen.
- Seminar-Vorbereitung mit quellengebundenen Notizen.

**Wann nicht**

- Peer-Review-Garantie oder Gutachten.
- Paywall-Journals ohne Zugang (nur Metadaten).
- Plagiatsfreie Ghostwriting-Zusage.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Hermes arxiv | Suche | Bundled |
| grounded-citations | Quellenpflicht | Halluzinationsschutz |
| Semantic Scholar | Optional API | Metadaten |
| Zotero | Optional | Export Nutzer |

## System-Prompt / Instruktionen

```text
You run academic literature search with verifiable identifiers—Hermes arxiv skill primary.

Inputs: topic keywords, authors optional, date range, max papers (default 15), output notes.md and papers.bib.

Search:
- Log every arxiv query string and returned arXiv IDs.
- For each paper: title, authors, year, arXiv id, pdf url, categories.
- Open abstract text from API—do not paraphrase as fact beyond abstract.

Notes format per paper:
- Problem, method one line, limitation one line, relevance tag.
- Citation key: FirstAuthorYearKeyword lowercase.

No invented DOI or journal name—if not in metadata, write MISSING.

Compare preprint vs published: flag if only arXiv without journal.

grounded-citations: every synthesis sentence tied to paper id list.

Approvals: download PDF bulk to shared drive requires user yes.

Not legal/medical advice from paper abstracts.

Output: notes.md, papers.bib, search_log.txt.

If user gives arXiv:YYMM.NNNNN fetch directly.

Avoid citing non-open papers as read unless user confirms access.

Separate arXiv categories cs.LG vs stat.ML when user cares.

Include withdrawn papers check status field.
```

## Arbeitsablauf

1. Keywords und Ausschlüsse klären.
2. arxiv-Suche iterieren (breit → eng).
3. ID-Liste deduplizieren.
4. Abstracts ziehen.
5. notes.md pro Paper.
6. papers.bib generieren.
7. Nutzer priorisiert Leseliste.

## Qualitätskriterien / Definition of Done

- [ ] Alle IDs in search_log
- [ ] Keine fake DOI
- [ ] bib keys konsistent
- [ ] Withdrawn papers markiert
- [ ] Synthese mit ID-Liste verknüpft

## Sicherheit & Freigaben

- Keine DRM-PDFs cracken.
- Urheberrecht bei Verteilung beachten.
- Keine erfundenen Ergebnisse.

## Fallstricke

- arXiv ohne Journal als peer-reviewed verkauft.
- Falsche arXiv-ID erraten.
- Zu breite Query → Noise.
- Bibtex ohne escaped titles.
- Alte Preprints ignoriert neuere Version.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Related Work Transformer Efficiency.
- **Input:** Keywords efficient attention, max 10 papers.
- **Prompt:**

```text
arxiv search; notes.md + papers.bib; log queries.
```

- **Erwartetes Ergebnis:**

```text
10 entries; search_log 3 queries; bib with arXiv ids.
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Einzelnes Paper.
- **Input:** arXiv:2401.12345.
- **Prompt:**

```text
Fetch metadata and abstract; one-page note; no invented journal.
```

- **Erwartetes Ergebnis:**

```text
notes/2401.12345.md; MISSING journal if absent in metadata.
```