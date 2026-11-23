---
id: documents-pandoc-markdown-pdf
title: "Markdown in PDF with Pandoc and Typst"
domain: office-documents
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
    version_notes: "PDF-Engine typst or lualatex"
  - name: typst
    install: "https://github.com/typst/typst"
    version_notes: "Pandoc --pdf-engine=typst"
  - name: mermaid-cli
    install: "npm: @mermaid-js/mermaid-cli"
    version_notes: "Diagramme vorrendern as SVG/PNG"
inputs:
  - "Markdown-Quellen (ein or mehrere files)"
  - "YAML-Metadaten (Titel, Autor, CI-Template)"
  - "Optional: CSS/Typst-Template"
outputs:
  - "Druckfertiges PDF"
  - "Optional DOCX for Review"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

**Technische and interne Dokumentation** from Markdown in konsistente, druckbare PDFs viageben—with reproducible Pandoc-commands, Typst-Engine and optional vorgerenderten Diagrammen.

## When to use

- Handbuecher, Policies or Angebote liegen bereits as Markdown im Repo.
- CI verlangt fixeds Layout (Titelseite, TOC, Fusszeile with Versionsstand).
- no WYSIWYG-Editor required; Build should in CI or per Agent-Shell laufen.

**When not to use**

- Komplexe Excel-Modelle or interaktive Forms.
- Rechtlich finale Urkunden without menschliche approval the PDFs.
- Reine DOCX-Editing with Track Changes (→ word-docx-Templates).

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| Pandoc | MD → PDF/DOCX | Einheitlicher Conversionspfad |
| Typst | PDF-Engine | Schneller as LaTeX; gut for Tabellen |
| mermaid-cli | Diagramme | no Runtime-Diagramme im PDF |
| pypdf / pdfinfo | QA | pageszahl and filegroesse verify |

## System prompt

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

## Workflow

1. `meta.yaml` and all `*.md` on relative Bildpfade verify.
2. Mermaid-Bloecke listen; `mmdc -i diagram.mmd -o assets/diagram.svg` batchweise.
3. Dry-run: `pandoc --print-default-data-file` only at Template-Debugging.
4. `pandoc ... -o handbuch_v1.pdf` with vereinbartem Typst-Template.
5. `pdfinfo handbuch_v1.pdf` → pages, Groesse document.
6. Stichprobe TOC and Fusszeile im gerenderten PDF (User or pdftoppm Seite 1).
7. Optional `review.docx` for inhaltliche Kommentare; PDF unveraendert canonical.

## Definition of done

- [ ] no fehlenden Bild- or Include-Referenzen im Build-Log
- [ ] Schrift and Raender entsprechen CI-Template
- [ ] PDF unter vereinbarter Groessen- and pageszahl-Limite
- [ ] Versionsstand in Fusszeile/Metadaten stimmt with `meta.yaml`
- [ ] all Pandoc-Befehle im Thread dokumentiert

## Security

- Vertrauliche Inhalte only over verschluesselte Kanaele versenden.
- no API-Keys, Tokens or Kundendaten in Example-Codebloecken im PDF.
- Rechtlich bindende approval liegt when Autor, not when Agenten.

## Pitfalls

- Mermaid im PDF without Vorrender → leere Kaesten or Build-Abbruch.
- Typst-Template with falscher Papiergroesse (US Letter vs. A4).
- `include`-pathe at Pandoc Multi-Root-Projekten brechen still.
- Git LFS-Bilder not ausgecheckt → 0-Byte-Assets im PDF.
- LaTeX and Typst gemischt in a Repo without documented Engine-Wahl.

## Basic examples

### Example 1 (Example data)

- **Task:** Internes Handbuch from drei Kapitel-MDs as PDF bauen.
- **Input:** `chapters/{01-intro,02-api,03-ops}.md`, `meta.yaml` (title: „Platform Runbook“, version: 1.2).
- **Prompt:**

```text
Render all chapter md files to handbuch_v1.pdf with pandoc typst engine and TOC. Pre-render two mermaid diagrams in ch02. Document commands.
```

- **Expected result:**

```bash
mmdc -i chapters/diagram-seq.mmd -o assets/diagram-seq.svg
pandoc chapters/*.md --from gfm+yaml_metadata_block --pdf-engine=typst --metadata-file meta.yaml --toc -o handbuch_v1.pdf
pdfinfo handbuch_v1.pdf | grep Pages
# → Pages: 42
```

### Example 2 (Example data)

- **Task:** Review-DOCX parallel zum PDF for Marketing-Feedback.
- **Input:** `policy.md`, gleiches `meta.yaml`.
- **Prompt:**

```text
PDF canonical via typst; additionally export policy_review.docx with reference.docx styles. No content edits.
```

- **Expected result:**

```text
policy.pdf (canonical), policy_review.docx (comments only), build.log with both pandoc invocations listed.
```