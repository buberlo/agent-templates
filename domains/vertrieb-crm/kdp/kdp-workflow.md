---
id: kdp-workflow
title: "Amazon KDP & Buch-Metadaten"
domain: vertrieb-crm
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
    version_notes: "Stars hier nicht per API gezogen."
inputs:
  - "ASIN/ISBN, Kategorie, Zielmarkt (amazon.de)"
  - "Manuskript-Metadaten (Titel, Untertitel, Keywords)"
  - "Nur read-only Marktanalyse oder Metadata-Draft"
outputs:
  - "Kategorie- und Keyword-Vorschlag mit Wettbewerber-ASINs"
  - "Cover/Description-Checkliste (kein Upload)"
  - "Royalty-Szenario grob (Preis × Seitenformat)"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

**KDP-Publishing vorbereiten**: Metadaten, Kategorien und Wettbewerbs-ASINs recherchieren—Upload und Preisänderung bleiben beim Autor in KDP.

## Wann nutzen

- Neues Buch: Kategorie-Baum und Backend-Keywords planen.
- Titel/Subtitle A/B-Entwürfe vor ISBN-Registrierung.
- Comp-ASINs für Amazon-Werbeanzeigen recherchieren.

**Wann nicht**

- Urheberrechtsverletzende Inhalte oder AI-Disclosure-Pflicht ignorieren.
- Automatisiertes KDP-Login oder Massenupload.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| HasData/amazon-mcp | Comp-Bücher lesen | Read-only |
| Manuell KDP-Richtlinien | Compliance | Kein MCP-Ersatz |

## System-Prompt / Instruktionen

```text
Role: KDP metadata strategist (vertrieb-crm/kdp).
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

## Arbeitsablauf

1. Genre, Format und Marktplatz klären.
2. Comp-ASINs über erlaubte Quellen sammeln.
3. Kategoriepfade und Keyword-Slots ausfüllen (Draft).
4. Titel/Untertitel/Description-Entwürfe.
5. Royalty-Hinweis grob rechnen.
6. Policy-Check (AI, Inhalt, Marken).
7. Pack zur manuellen KDP-Eingabe übergeben.

## Qualitätskriterien / Definition of Done

- [ ] Comp-ASINs mit Abrufquelle
- [ ] Keyword-Byte-Limits beachtet (DE)
- [ ] Kein KDP-Upload/Preis-API
- [ ] AI-Disclosure-Hinweis wenn relevant

## Sicherheit & Freigaben

- Inhalte und Accounts nur beim Autor.
- MCP-ToS wie Amazon-Workflow.

## Fallstricke

- Keyword-Stuffing im Untertitel → Ablehnung.
- Falsche Kategorie → schlechte Organics.
- Comp-BSR ohne Kategorie-Kontext missverständlich.
- Taschenbuchmaße und Cover-Bleed verwechseln.
- Übersetzung ohne lokales Lektorat.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Nonfiction Produktivität DE, 7 Keywords
- **Input:** Working title, Ziel amazon.de
- **Prompt:**

```text
5 comp ASINs, 7 keyword slots DE, title+subtitle draft.
```

- **Erwartetes Ergebnis:**

```text
comps.csv 5 rows | keywords in byte-safe phrases | no upload
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Series Buch 2 Metadaten
- **Input:** Series name, Book 1 ASIN
- **Prompt:**

```text
Consistency check title pattern; ads keyword ideas from book1 comps.
```

- **Erwartetes Ergebnis:**

```text
Series bracket format suggested | 10 ad keywords | series order warning in notes
```