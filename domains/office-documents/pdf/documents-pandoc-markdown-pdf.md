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
  - "Markdown sources (one or more files)"
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

**Technical and internal documentation** from Markdown into consistent, printable PDFs—with reproducible Pandoc commands, the Typst engine, and optional pre-rendered diagrams.

## When to use

- Manuals, policies, or proposals already exist as Markdown in the repo.
- CI verlangt fixeds Layout (Titelseite, TOC, Fusszeile with Versionsstand).
- no WYSIWYG-Editor required; Build should in CI or per Agent-Shell laufen.

**When not to use**

- Komplexe Excel-Modelle or interaktive Forms.
- Legally final certificates without human approval of the PDFs.
- Reine DOCX-Editing with Track Changes (→ word-docx-Templates).

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| Pandoc | MD → PDF/DOCX | Einheitlicher Conversionspfad |
| Typst | PDF-Engine | Schneller as LaTeX; gut for Tabellen |
| mermaid-cli | Diagramme | no Runtime-Diagramme im PDF |
| pypdf / pdfinfo | QA | Verify page count and file size |

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
2. List Mermaid blocks; run `mmdc -i diagram.mmd -o assets/diagram.svg` in batches.
3. Dry-run: `pandoc --print-default-data-file` only at Template-Debugging.
4. `pandoc ... -o handbuch_v1.pdf` with vereinbartem Typst-Template.
5. `pdfinfo handbuch_v1.pdf` → document pages and size.
6. Spot-check TOC and footer in rendered PDF (user or pdftoppm page 1).
7. Optional `review.docx` for content comments; PDF remains canonical.

## Definition of done

- [ ] no fehlenden Bild- or Include-Referenzen im Build-Log
- [ ] Schrift and Raender entsprechen CI-Template
- [ ] PDF under agreed size and page count limits
- [ ] Version status in footer/metadata matches `meta.yaml`
- [ ] All Pandoc commands documented in thread

## Security

- Send confidential content only over encrypted channels.
- No API keys, tokens, or customer data in example code blocks in the PDF.
- Legally binding approval rests with the author, not the agent.

## Pitfalls

- Mermaid im PDF without Vorrender → leere Kaesten or Build-Abbruch.
- Typst template with wrong paper size (US Letter vs. A4).
- `include`-pathe at Pandoc Multi-Root-Projekten brechen still.
- Git LFS-Bilder not ausgecheckt → 0-Byte-Assets im PDF.
- LaTeX and Typst gemischt in a Repo without documented Engine-Wahl.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Build internal handbook as PDF from three chapter MDs.
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

### Example 2 (Example data (self-written))
- **Task:** Review DOCX alongside PDF for marketing feedback.
- **Input:** `policy.md`, same `meta.yaml`.
- **Prompt:**

```text
PDF canonical via typst; additionally export policy_review.docx with reference.docx styles. No content edits.
```

- **Expected result:**

```text
policy.pdf (canonical), policy_review.docx (comments only), build.log with both pandoc invocations listed.
```