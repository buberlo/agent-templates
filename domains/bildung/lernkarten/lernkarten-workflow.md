---
id: lernkarten-workflow
title: "Lernkarten"
domain: bildung
category: lernkarten
tags:
  - lernkarten
  - bildung
  - skillcli
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Hermes-Skill microsoft-office
    install: "https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-microsoft-office"
    version_notes: "Teil des offiziellen Bundled-Katalogs."
  - name: Hermes-Skill youtube-content
    install: "https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/media/media-youtube-content"
    version_notes: "Bundled-Katalog."
inputs:
  - "Quelltext (PDF, docx, YouTube-URL)"
  - "Anki-Deck-Name und Sprache"
  - "Kartenlimit pro Abschnitt"
outputs:
  - "TSV/CSV für Anki-Import"
  - "Qualitätsnotizen (Duplikate, zu breite Karten)"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

Aus Vorlesungen, Skripten oder Videos **konzise Lernkarten** (Anki-format) erzeugen—eine Frage pro Karte, mit **Quellenangabe**.

## Wann nutzen

- Prüfungsvorbereitung mit begrenztem Stoffkorpus.
- Transkript oder docx liegt vor.
- Export als Tab-getrennte Datei für Anki.

**Wann nicht**

- Rohmaterial ohne Urheberrechtsklärung.
- Medizinrechtliche Merkhilfen ohne Fachreview.
- Riesige PDFs ohne Chunking → Kontext-Overflow.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| youtube-content | Transkript | Zeitstempel als Quelle |
| microsoft-office | docx lesen | Vorlesungsskript |
| TSV | Anki-Import | Standardformat |

## System-Prompt / Instruktionen

```text
You create flashcards for bildung/lernkarten.

Inputs: source (file path|youtube url), deck_name, language, max_cards, card_style (basic|cloze), source_tag_prefix.

Rules:
- One fact per card; question answerable without long context.
- Cloze: max 2 deletions per card.
- Back side: short answer + source (page, timestamp, or heading).
- No copyrighted exam item banks copied verbatim.
- Deduplicate near-identical cards; list removed_duplicates[].
- After generation, sample 5 cards for leak (answer in question).

Output: anki_import.tsv columns: Front, Back, Tags
Tag format: source_tag_prefix::chapter

If youtube: fetch transcript via skill; cite mm:ss.
Deliver: anki_import.tsv, quality_notes.md, card_count.
```

## Arbeitsablauf

1. Quelle laden (docx oder YouTube-Transkript).
2. In Abschnitte chunken (max ~2k Wörter pro Pass).
3. Pro Abschnitt Karten generieren bis `max_cards`.
4. Duplikate entfernen; Cloze-Karten prüfen.
5. `anki_import.tsv` schreiben (UTF-8, Tabs).
6. `quality_notes.md` mit Stichprobe 5 Karten.
7. Nutzer importiert in Anki; Agent sendet keine Cloud-Syncs.

## Qualitätskriterien / Definition of Done

- [ ] Eine Karte = ein prüfbarer Fakt
- [ ] Quelle auf Rückseite
- [ ] Keine Antwort in Frage versteckt (Stichprobe)
- [ ] TSV valide für Anki Desktop Import

## Sicherheit & Freigaben

- Keine personenbezogenen Daten auf Kartenrückseiten.
- YouTube nur öffentliche Videos mit Nutzerfreigabe.
- Prüfungsleak: nur selbst formulierte Fragen.

## Fallstricke

- Karten zu lang → schlechte Retention.
- Cloze zu komplex.
- Falsche Zeitstempel bei Transkript-Sync.
- Tag-Overflow in Anki.
- Import-Kodierung falsch (Komma statt Tab).

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** 30 Karten aus Vorlesung docx Kap. 2.
- **Input:** `lecture2.docx`, DE, basic.
- **Prompt:**

```text
Max 30 cards, tag prefix BIO101::ch2, export anki_import.tsv.
```

- **Erwartetes Ergebnis:**

```text
card_count: 30
Sample front: "Was ist Mitose?"
Sample back: "Zellteilung … — Quelle: Kap. 2 §Mitose"
quality_notes: 2 duplicates removed
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** YouTube ohne URL.
- **Input:** Nur Thema "Photosynthese".
- **Prompt:**

```text
Make flashcards from YouTube.
```

- **Erwartetes Ergebnis:**

```text
Abbruch: source_url required for youtube path.
Alternative: paste transcript text or provide docx.
No TSV written.
```