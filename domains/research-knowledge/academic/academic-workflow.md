---
id: academic-workflow
title: "Akademische Literatursuche"
domain: research-knowledge
category: academic
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
  - "Suchthema or Paper-ID"
  - "Zitationsstil optional"
outputs:
  - "Paper list with metadata"
  - "Reading with IDs"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

**Find and access papers** (arXiv, IDs)—Abstract, PDF link, quoteable metadata, **no invented DOI**.

## When to use

- Related work for project or thesis.
- Paper-ID vom User vertiefen.
- Seminar preparation with source-bound notes.

**When not**

- Peer-Review-Garantie or Gutachten.
- Paywall-Journals without Zugang (nur Metadaten).
- Plagiatsfreie Ghostwriting-Zusage.

## Tool stack

| Tool | Role | Justification |
|------|-------|------------|
| Hermes arxiv | Suche | Bundled |
| grounded-citations | Quellenpflicht | Halluzinationsschutz |
| Semantic Scholar | Optional API | Metadaten |
| Zotero | Optional | Export User |

## System prompt

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

## Workflow

1. clarify keywords and exclusions.
2. arxiv-Suche iterieren (breit → eng).
3. ID-Liste deduplizieren.
4. Abstracts ziehen.
5. notes.md pro Paper.
6. papers.bib generieren.
7. User priorisiert Leseliste.

## Definition of done

- [ ] Alle IDs in search_log
- [ ] No fake DOI
- [ ] bib keys konsistent
- [ ] Withdrawn papers markiert
- [ ] Synthesis linked to ID list

## Security

- No DRM-PDFs crack.
- copyright bei distribution observe.
- No invented Ergebnisse.

## Pitfalls

- arXiv without Journal als peer-reviewed verkauft.
- Falsche arXiv-ID erraten.
- Zu breite Query → Noise.
- Bibtex without escaped titles.
- Alte Preprints ignoriert neuere Version.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Related Work Transformer Efficiency.
- **Input:** Keywords efficient attention, max 10 papers.
- **Prompt:**

```text
arxiv search; notes.md + papers.bib; log queries.
```

- **Expected result:**

```text
10 entries; search_log 3 queries; bib with arXiv ids.
```

### Example 2 (Example data (self-written))
- **Task:** Einzelnes Paper.
- **Input:** arXiv:2401.12345.
- **Prompt:**

```text
Fetch metadata and abstract; one-page note; no invented journal.
```

- **Expected result:**

```text
notes/2401.12345.md; MISSING journal if absent in metadata.
```