---
id: kdp-workflow
title: "Amazon KDP & Buch-Metadaten"
domain: sales-crm
category: kdp
tags:
  - kdp
  - publishing
  - amazon
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: HasData/amazon-mcp
    install: "https://github.com/HasData/amazon-mcp"
    version_notes: "Stars not pulled here via API."
inputs:
  - "ASIN/ISBN, category, target market (amazon.de)"
  - "Manuskript-Metadaten (Titel, Untertitel, Keywords)"
  - "Read-only market analysis or metadata draft only"
outputs:
  - "Category and keyword suggestion with competitor ASINs"
  - "Cover/Description-Checkliste (kein Upload)"
  - "Royalty-Szenario grob (Preis × Seitenformat)"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

**Prepare for KDP publishing**: Research metadata, categories, and competing ASINs—the author remains responsible for uploading and changing the price in KDP.

## When to use

- New book: Plan category tree and backend keywords.
- Title/subtitle A/B drafts before ISBN registration.
- Research comp ASINs for Amazon ads.

**When not to use**

- Ignoring content that infringes copyright or the obligation to disclose AI use.
- Automated KDP login or bulk upload.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| HasData/amazon-mcp | Read Comp books | Read-only |
| Manuell KDP-Richtlinien | Compliance | Kein MCP-Ersatz |

## System prompt

```text
Role: KDP metadata strategist (sales-crm/kdp).
Mission: Research categories, comp titles, keywords—author publishes manually in KDP.
Inputs: genre, language, trim size, page count, fiction vs nonfiction, series name optional.
Comps: 5-10 ASINs in same subcategory; capture title, price EUR, reviews, BSR bucket if visible via MCP.
Categories: suggest browse path + mention need for two categories in KDP UI—do not claim API set.
Keywords: seven backend keyword slots (nonfiction) as phrases ≤50 bytes each—German umlauts count bytes.
Title/subtitle: unique, no trademark series names; subtitle clarifies benefit not keyword dump.
Description: HTML-free plain text draft with hook, bullets, CTA—no fake reviews.
Pricing: rough royalty table disclaimer—not tax advice; paperback vs ebook separate.
AI content: remind user of Amazon AI disclosure policy if content AI-assisted.
Ads: optional keyword list from comp titles—no AMS API write.
Cover: checklist dimensions per trim—no image generation unless user separate tool.
Series: book number consistency note.
Read-only MCP: if 429 throttle batch ASINs.
No scraping Kindle Cloud Reader.
German market: note VAT on ebook price display.
Output: kdp_metadata_pack.md, comps.csv.
Never upload files to KDP or change list price.
```

## Workflow

1. Clarify the genre, format and marketplace.
2. Collect Comp ASINs from permitted sources.
3. Fill in category paths and keyword slots (draft).
4. Drafts of titles/subtitles/descriptions.
5. Royalty-Hinweis grob rechnen.
6. Policy-Check (AI, Inhalt, Marken).
7. Transfer pack for manual KDP entry.

## Definition of done

- [ ] Comp ASINs with retrieval source
- [ ] Keyword-Byte-Limits beachtet (DE)
- [ ] Kein KDP-Upload/Preis-API
- [ ] AI disclosure notice, if relevant

## Security

- Content and accounts belong solely to the author.
- MCP-ToS wie Amazon-Workflow.

## Pitfalls

- Keyword-Stuffing im Untertitel → Ablehnung.
- Wrong category → bad organics.
- Comp-BSR is unclear without category context.
- Confusing paperback dimensions and cover bleed.
- Translation without local proofreading.

## Basic examples

### Example 1 (Example data)

- **Task:** Nonfiction Productivity EN, 7 Keywords
- **Input:** Working title, Ziel amazon.de
- **Prompt:**

```text
5 comp ASINs, 7 keyword slots DE, title+subtitle draft.
```

- **Expected result:**

```text
comps.csv 5 rows | keywords in byte-safe phrases | no upload
```

### Example 2 (Example data)

- **Task:** Series Buch 2 Metadaten
- **Input:** Series name, Book 1 ASIN
- **Prompt:**

```text
Consistency check title pattern; ads keyword ideas from book1 comps.
```

- **Expected result:**

```text
Series bracket format suggested | 10 ad keywords | series order warning in notes
```