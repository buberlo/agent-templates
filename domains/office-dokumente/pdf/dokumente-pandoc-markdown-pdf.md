---
id: dokumente-pandoc-markdown-pdf
domain: office-dokumente
title: "Markdown in PDF mit Pandoc und Typst"
category: pdf
tags:
  - pandoc
  - pdf
  - markdown
  - typst
target_agents:
  - hermes
  - claude-code
  - cursor
  - generic
required_tools:
  - name: pandoc
    install: "apt/brew: pandoc 3.x"
    version_notes: "PDF-Engine typst oder lualatex"
  - name: typst
    install: "https://github.com/typst/typst"
    version_notes: "Pandoc --pdf-engine=typst"
  - name: mermaid-cli
    install: "npm: @mermaid-js/mermaid-cli"
    version_notes: "Diagramme vorrendern als SVG/PNG"
inputs:
  - "Markdown-Quellen (ein oder mehrere Dateien)"
  - "YAML-Metadaten (Titel, Autor, CI-Template)"
  - "Optional: CSS/Typst-Template"
outputs:
  - "Druckfertiges PDF"
  - "Optional DOCX für Review"
risk_level: low
version: "1.1.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

**Technische und interne Dokumentation** aus Markdown in konsistente, druckbare PDFs übergeben—mit reproduzierbaren Pandoc-Befehlen, Typst-Engine und optional vorgerenderten Diagrammen.

## Wann nutzen

- Handbücher, Policies oder Angebote liegen bereits als Markdown im Repo.
- CI verlangt festes Layout (Titelseite, TOC, Fußzeile mit Versionsstand).
- Kein WYSIWYG-Editor nötig; Build soll in CI oder per Agent-Shell laufen.

**Wann nicht**

- Komplexe Excel-Modelle oder interaktive Formulare.
- Rechtlich finale Urkunden ohne menschliche Freigabe des PDFs.
- Reine DOCX-Bearbeitung mit Track Changes (→ word-docx-Templates).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Pandoc | MD → PDF/DOCX | Einheitlicher Konvertierungspfad |
| Typst | PDF-Engine | Schneller als LaTeX; gut für Tabellen |
| mermaid-cli | Diagramme | Keine Runtime-Diagramme im PDF |
| pypdf / pdfinfo | QA | Seitenzahl und Dateigröße prüfen |

## System-Prompt / Instruktionen

```text
You build print-ready PDFs from Markdown using pandoc with the typst PDF engine unless the user mandates LaTeX.

Inputs: source .md file(s) or a glob, metadata YAML (title, author, version, date), template path (.typ or reference.docx for DOCX), output basename, language (de-DE default).

Pre-flight:
- Resolve all image and include paths relative to project root; fail on broken links.
- Lint headings: single H1 or user-specified policy; no duplicate anchors if TOC enabled.
- Extract mermaid fenced blocks; render each to SVG via mmdc before pandoc run; replace blocks with image refs.

Build:
- pandoc --from gfm+yaml_metadata_block --to pdf --pdf-engine=typst -o out.pdf --metadata-file meta.yaml sources.md
- Table of contents when >3 level-1 headings or user requests --toc.
- Embed fonts only if CI template provides paths; do not bundle copyrighted fonts without license note.

Post-build verify:
- File exists, non-zero size, page count within agreed limit.
- Spot-check first page title and last page footer against metadata.version.
- Optional DOCX: pandoc -o review.docx for stakeholder comments only; PDF remains deliverable.

Security: strip secrets from code samples; redact env vars in listings.
Never email or upload PDFs without user approval channel.

Document every command in order. On failure, paste pandoc stderr and stop.

Keep chapter files modular; use @include or concat list in pandoc invocation.
If German hyphenation issues appear, note typst lang: "de" in template meta.
Prefer vector SVG for diagrams; PNG only when user requires raster.

Do not claim legal compliance of content—layout only.
```

## Arbeitsablauf

1. `meta.yaml` und alle `*.md` auf relative Bildpfade prüfen.
2. Mermaid-Blöcke listen; `mmdc -i diagram.mmd -o assets/diagram.svg` batchweise.
3. Dry-run: `pandoc --print-default-data-file` nur bei Template-Debugging.
4. `pandoc ... -o handbuch_v1.pdf` mit vereinbartem Typst-Template.
5. `pdfinfo handbuch_v1.pdf` → Seiten, Größe dokumentieren.
6. Stichprobe TOC und Fußzeile im gerenderten PDF (Nutzer oder pdftoppm Seite 1).
7. Optional `review.docx` für inhaltliche Kommentare; PDF unverändert canonical.

## Qualitätskriterien / Definition of Done

- [ ] Keine fehlenden Bild- oder Include-Referenzen im Build-Log
- [ ] Schrift und Ränder entsprechen CI-Template
- [ ] PDF unter vereinbarter Größen- und Seitenzahl-Limite
- [ ] Versionsstand in Fußzeile/Metadaten stimmt mit `meta.yaml`
- [ ] Alle Pandoc-Befehle im Thread dokumentiert

## Sicherheit & Freigaben

- Vertrauliche Inhalte nur über verschlüsselte Kanäle versenden.
- Keine API-Keys, Tokens oder Kundendaten in Beispiel-Codeblöcken im PDF.
- Rechtlich bindende Freigabe liegt beim Autor, nicht beim Agenten.

## Fallstricke

- Mermaid im PDF ohne Vorrender → leere Kästen oder Build-Abbruch.
- Typst-Template mit falscher Papiergröße (US Letter vs. A4).
- `include`-Pfade bei Pandoc Multi-Root-Projekten brechen still.
- Git LFS-Bilder nicht ausgecheckt → 0-Byte-Assets im PDF.
- LaTeX und Typst gemischt in einem Repo ohne dokumentierte Engine-Wahl.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Internes Handbuch aus drei Kapitel-MDs als PDF bauen.
- **Input:** `chapters/{01-intro,02-api,03-ops}.md`, `meta.yaml` (title: „Platform Runbook“, version: 1.2).
- **Prompt:**

```text
Render all chapter md files to handbuch_v1.pdf with pandoc typst engine and TOC. Pre-render two mermaid diagrams in ch02. Document commands.
```

- **Erwartetes Ergebnis:**

```bash
mmdc -i chapters/diagram-seq.mmd -o assets/diagram-seq.svg
pandoc chapters/*.md --from gfm+yaml_metadata_block --pdf-engine=typst --metadata-file meta.yaml --toc -o handbuch_v1.pdf
pdfinfo handbuch_v1.pdf | grep Pages
# → Pages: 42
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Review-DOCX parallel zum PDF für Marketing-Feedback.
- **Input:** `policy.md`, gleiches `meta.yaml`.
- **Prompt:**

```text
PDF canonical via typst; additionally export policy_review.docx with reference.docx styles. No content edits.
```

- **Erwartetes Ergebnis:**

```text
policy.pdf (canonical), policy_review.docx (comments only), build.log with both pandoc invocations listed.
```