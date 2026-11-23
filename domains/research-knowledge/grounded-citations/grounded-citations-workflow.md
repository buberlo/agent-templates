---
id: grounded-citations-workflow
title: "Requirement and source quotations"
domain: research-knowledge
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
  - "Textentwurf or Frage"
  - "Quellenformat (APA, inline URL)"
outputs:
  - "Revised text with quotations"
  - "source verification log"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

**Bind responses to verifiable sources**—any core claim with URL, date or paper ID, UNVERIFIED otherwise.

## When to use

- Agent output for customers or wiki.
- Fact-check nach Web research.
- Combination with academic or news monitoring.

**When not**

- Kreative Fiktion.
- Internal hypotheses without publication need.

## Tool stack

| Tool | Role | Justification |
|------|-------|------------|
| grounded-citations | Skill-Regeln | Disziplin |
| Firecrawl | Fetch | Quote check |
| arxiv | Paper IDs | Akademisch |

## System prompt

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

## Workflow

1. Claims aus Entwurf extrahieren.
2. Search for source per claim or fetching user URL.
3. Status OK/UNVERIFIED setzen.
4. Rewrite text with quotes.
5. source_log.csv pflegen.
6. Insert conflicts section.
7. Release before publish.

## Definition of done

- [ ] No Behauptung without Tag
- [ ] source log complete
- [ ] No invented URLs
[ ] Quotes shortened
- [ ] Publish release documented

## Security

- No internal URLs in public texts without sharing.
- Do not distribute paywall full text.
- Quellen-Log kann sensibel sein.

## Pitfalls

- Link rot aber behauptet OK.
- arXiv als Journal.
A blog as the only source.
- UNVERIFIED vergessen zu labeln.
- Quote from Snippet not in the article.

## Basic examples

### Example 1 (Example data)

- **Task:** Marketing-Absatz fact-checken.
- **Input:** 5 sets of statistics.
- **Prompt:**

```text
Ground each stat or UNVERIFIED; firecrawl user urls; source_log.csv.
```

- **Expected result:**

```text
grounded.md; 2 UNVERIFIED; source_log 5 rows.
```

### Example 2 (Example data)

- **Task:** Fake URL entfernen.
- **Input:** Draft cites https://example-fake.domain/study
- **Prompt:**

```text
Verify urls; remove fabricated links.
```

- **Expected result:**

```text
Fake url removed; claim UNVERIFIED or deleted.
```