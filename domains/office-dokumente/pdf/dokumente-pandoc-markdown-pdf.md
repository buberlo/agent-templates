---
id: dokumente-pandoc-markdown-pdf
domain: office-dokumente
title: "Markdown in PDF mit Pandoc und Typst"
category: pdf
tags:
  - pandoc
  - pdf
  - markdown
target_agents:
  - hermes
  - generic
required_tools:
  - name: pandoc
    install: "apt/brew: pandoc"
    version_notes: "3.x"
  - name: typst
    install: "cargo/apt: typst"
    version_notes: "Pandoc PDF-Engine typst"
inputs:
  - "Markdown-Quellen"
  - "CSS/Template"
  - "Metadaten YAML"
outputs:
  - "PDF"
  - "Optional DOCX"
risk_level: low
version: "1.0.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

Technische Dokumentation aus Markdown in druckfertige PDFs konvertieren.

## Wann nutzen

- Handbücher, Angebote, interne Policies.
- Nicht für komplexe Excel-Modelle.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Pandoc | Konvertierung | Universelles Format |
| Typst | PDF-Engine | Schneller als LaTeX |
| Mermaid CLI | Diagramme | Vorrender als SVG |

## System-Prompt / Instruktionen

```text
Build PDFs with pandoc --pdf-engine=typst.
Pre-render mermaid blocks to SVG; inject into MD.
Apply corporate template paths from metadata.
Table of contents when >3 headings.
```

## Arbeitsablauf

1. MD linten; Bilder lokal verlinken.
2. Mermaid → SVG Batch.
3. `pandoc -o out.pdf` mit Template.
4. Seitenzahlen/Fußzeile prüfen.
5. Optional DOCX für Kundenreview.

## Qualitätskriterien / Definition of Done

- [ ] Keine gebrochenen Bildlinks
- [ ] Einheitliche Schrift gemäß CI
- [ ] PDF < vereinbarter Größenlimit

## Sicherheit & Freigaben

- Vertrauliche Docs nur verschlüsselt versenden.
- Keine Secrets in Beispielcode im PDF.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

_Siehe vorheriger Abschnitt; bei Migration ergänzt._

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Validierung
- **Input:** n/a
- **Prompt:** `validate output`
- **Erwartetes Ergebnis:** OK

## Beispiele (Legacy)

**Eingabe:** `handbuch/*.md`, Template `corp.typ`
**Erwartetes Ergebnis:** `handbuch_v1.pdf`
