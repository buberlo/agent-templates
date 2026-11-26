---
id: pdf-mcp-focus
title: "PDF: MCP- and Skill-Fokus"
domain: office-documents
category: pdf
tags:
  - pdf
  - pypdf
  - ocr
  - skill
target_agents:
  - hermes
  - claude-code
  - openclaw
  - generic-mcp-agents
required_tools:
  - name: Anthropic document skills (pdf)
    install: "https://github.com/anthropics/skills"
    version_notes: "Validate + Render path"
  - name: Hermes-Skill pdf
    install: "https://hermes-agent.nousresearch.com/docs/reference/skills-catalog"
    version_notes: "Bundled productivity/pdf"
  - name: pypdf
    install: "pip: pypdf"
    version_notes: "Merge, extract, forms"
  - name: MarkItDown
    install: "https://github.com/microsoft/markitdown"
    version_notes: "PDF → Markdown at Bedarf"
inputs:
  - "PDF-files or pathe"
  - "Operation (read, merge, form, ocr, edit)"
  - "approval for irreversible changes"
outputs:
  - "Bearbeitete PDF or strukturierter Text"
  - "Verification log (pages, hash, spot check)"
risk_level: low
example_count: 3
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

**PDF-Operationen** over official Document-Skills and Hermes pdf plan: read, merge, Forms, OCR—immer with **Verify-step** (Text, Render, spot check), not blind trust.

## When to use

- Agent should PDF-Toolkit (Skill/MCP) gezielt auswaehlen statt generisch to scrapen.
- Merge, Form fill or OCR on scans with human final review.
- After DOCX generation, render PDF as a verification artifact (same workflow as the Anthropic tutorial).

**When not to use**

- Finale Government-submission without menschliche Sichtpruefe.
- Password-protected PDFs without user-provided credentials.
- Full layout editor replacement (InDesign level).

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| Anthropic pdf-Skill | Create, verify, pypdf | Official Verify-path |
| Hermes pdf-Skill | OCR, merge, edit | Bundled, offline-faehig |
| pypdf | Scriptbare Basis | Schnelle Extraktion/Merge |
| pdftoppm / Render | Visuelle QA | Text allein reicht not |
| MarkItDown | MD-Export | Weiterverarbeitung in Wikis |

## System prompt

```text
You operate on PDFs using listed skills and pypdf—not arbitrary web converters.

Inputs: file path(s), task mode (read_text | merge | fill_form | ocr_scan | extract_pages), fields map for forms, output path, approval for overwrite.

Before write:
- pypdf PdfReader: page count, encryption status, form fields if any.
- If scan-only PDF, route to OCR path; never guess numbers from low-DPI renders.

Read: extract text per page; flag empty pages; for tables prefer structured export if skill offers it.

Merge: preserve bookmarks when possible; log order of inputs; verify output page count equals sum minus blanks removed.

Forms: fill only fields user supplied; never invent SSN, tax IDs, or signatures.
After fill, re-read field values programmatically and render page images for visual check.

OCR: run skill OCR; produce side-by-side diff sample for numbers and legal references (case numbers).

Verify loop (mandatory on deliverable):
- Re-open output with pypdf; compare sha256 if user tracks integrity.
- Render at least first and last page to PNG for user spot check when layout matters.

Skills vs MCP: load only pdf-related tools; do not enable full office MCP set unless needed.

Approvals: submit, email, upload, or delete originals only with explicit user consent.

Output: paths, page counts, warnings (OCR low confidence), and commands used.

Never bypass DRM or cracked password tools.

If Markdown export requested, use MarkItDown and note structure loss for complex layouts.
Log pypdf version in troubleshoot notes when merge fails on encrypted inputs.
```

## Workflow

1. Inbound-PDF with pypdf inventory (pages, encryption, form fields).
2. Enable the skill/MCP matching the task (pdf scope only).
3. Execute operation (read/merge/fill/ocr) on test copy under `out/`.
4. Programmatic field review or text extraction.
5. `pdftoppm -f 1 -l 2 out/result.pdf out/qa` for visual spot check.
6. User-approval at submissions-PDFs document.
7. Hand over final artifact with path and page count.

## Definition of done

- [ ] Output PDF opens and page count matches expectation
- [ ] form fields programmatisch against should-values geprueft
- [ ] OCR: spot-check critical numbers against scan
- [ ] no Upload/Versand without documented approval
- [ ] Tool-Aufrufe and Skill-Namen im Log

## Security

- OCR errors in amounts and case numbers: human visual inspection before submission.
- no Tokens in Skill-Argumenten or Custom-MCP-CLI.
- Do not delete original PDFs without explicit confirmation.

## Pitfalls

- Gruener Validator without PNG/PDF-Render erkennt Tabellen-Overflow not.
- OCR confuses 0/O and 1/l in IBANs and case numbers.
- Merging without uniform page size creates invisible scaling errors.
- to viele MCPs aktiv → Token-Overhead before the ersten Aktion.
- Signierte PDFs after Editing invalid—neu signieren is separater Prozess.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Drei submissions-PDFs in fixed Reihenfolge merge.
- **Input:** `anlage_a.pdf` (2 S.), `anlage_b.pdf` (5 S.), `antrag.pdf` (3 S.).
- **Prompt:**

```text
Merge in order antrag, anlage_a, anlage_b to packet.pdf. Verify 10 pages. List pypdf commands.
```

- **Expected result:**

```text
packet.pdf: 10 pages; merge log with input order; pypdf reader confirms page count.
```

### Example 2 (Example data (self-written))
- **Task:** Scan-PDF OCR and Betrag from Seite 1 extract.
- **Input:** `rechnung_scan.pdf` (image-only).
- **Prompt:**

```text
OCR with Hermes pdf skill; extract invoice total and date; flag low-confidence chars; no submission.
```

- **Expected result:**

```text
extracted.txt with TOTAL and DATE lines; confidence warnings on any digit under threshold; PNG qa page for user review.
```

### Example 3 (Example data (self-written))
- **Task:** from DOCX gerendertes Briefing-PDF with pdf-Skill zurueckread (Verify from Anthropic-Tutorial).
- **Input:** `briefing.pdf` from beforeigem DOCX-Render.
- **Prompt:**

```text
Use Anthropic pdf skill / pypdf PdfReader: report page count and first heading text from briefing.pdf.
```

- **Expected result:** Page count and text excerpt documented; same verification workflow as DOCX pipeline.
- **Source:** https://aifrontierpost.com/articles/anthropic-official-agent-skills-tutorial/