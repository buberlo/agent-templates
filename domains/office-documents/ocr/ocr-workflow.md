---
id: ocr-workflow
title: "OCR for Scans and Bild-PDFs"
domain: office-documents
category: ocr
tags:
  - ocr
  - tesseract
  - pdf
target_agents:
  - hermes
  - claude-code
  - generic
required_tools:
  - name: Hermes-Skill pdf
    install: "https://hermes-agent.nousresearch.com/docs/reference/skills-catalog"
    version_notes: "Bundled OCR path"
  - name: tesseract
    install: "apt: tesseract-ocr tesseract-ocr-deu"
    version_notes: "Fallback CLI"
  - name: MarkItDown
    install: "https://github.com/microsoft/markitdown"
    version_notes: "Optional structure export"
inputs:
  - "Scan-PDF or Bilder"
  - "Sprache (deu+eng)"
  - "approval for Drittanbieter-OCR"
outputs:
  - "Text pro Seite"
  - "confidence-Warnungen"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

**Text from Scans** extract with Skill- or Tesseract-path, kritische fields **am Bild re-checked**—besonders Zahlen and Namen.

## When to use

- Rechnungs- and contract-Scans as durchsuchbaren Text.
- no natives Textlayer im PDF.
- result is Entwurf for Mensch or ERP, not Auto-Buchung.

**When not to use**

- Handschrift without spezialisiertes Modell.
- Rechtlich bindende submission without Mensch.
- Inhalte with strengem Cloud-Verbot without lokales OCR.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| Hermes pdf OCR | Integriert | Skill-path |
| tesseract | Lokal | Air-gapped |
| pdftoppm | Rasterize | before Tesseract |
| pdf skill | Verify | Structure review |

## System prompt

```text
You OCR scanned PDFs and images for office use—not legal submission without human review.

Inputs: file path, languages (deu+eng default), output format (txt per page, md, searchable pdf optional user tool), fields_of_interest list (amounts, dates, case numbers).

Pipeline:
- Detect text layer: if extractable text > threshold, skip OCR and report NATIVE_TEXT.
- Else rasterize 300 DPI min for numbers; deskew if skill offers.

OCR engines: prefer Hermes pdf skill OCR; fallback tesseract -l deu+eng; never send confidential scans to public APIs without contract.

Per page output: text + average confidence if available; flag pages below threshold.

Critical field pass: regex extract amounts/dates; compare visually to crop snippet user can open.

Side-by-side: save page PNG crops for amount_lines when billing.

Mark low-confidence digits with [?] in export—do not silently fix.

Approvals: upload scans to cloud OCR, delete originals, or email results requires user yes.

Output: combined.txt, page_confidence.csv, critical_field_table.md.

Do not store PII in public issue trackers.

Searchable PDF creation only if user provides tool and license.

Log which engine per page for audit.
Deskew and contrast normalize before tesseract when photos of paper.
```

## Workflow

1. `pdfinfo` / pypdf: Textlayer verify.
2. at Scan: pages to PNG (300 DPI).
3. OCR Skill or `tesseract png stdout`.
4. Confidence-Report pro Seite.
5. Kritische fields extract + Crop speichern.
6. User Stichprobe Betrag vs. Bild.
7. Textdatei with [?]-Markierungen liefern.

## Definition of done

- [ ] NATIVE_TEXT vs OCR dokumentiert
- [ ] Niedrig-Confidence-pages listed
- [ ] Betraege/Datum stichprobenartig geprueft or as OPEN markiert
- [ ] no Cloud-OCR without approval
- [ ] Engine-Log vorhanden

## Security

- contract- and Gesundheits-Scans vertraulich.
- no oeffentlichen OCR-APIs without Vertrag.
- submission only after menschlicher approval.

## Pitfalls

- 72 DPI reicht not for Kommazahlen.
- German without englische Begriffe in invoices.
- Tabellen as Fliesstext without Spalten.
- Doppelte pages im Scan.
- Such-PDF schlecht indexiert at schiefem Raster.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Lieferantenrechnung Scan → Text.
- **Input:** `invoice_scan.pdf` 2 pages, deu.
- **Prompt:**

```text
OCR beide pages; extract total and invoice date; flag conf<85%; save page crops.
```

- **Expected result:**

```text
invoice_scan.txt; critical_field_table: TOTAL 1.234,56 EUR date 2026-11-15; page2 conf warning if any.
```

### Example 2 (Example data (self-written))
- **Task:** Bereits Text-PDF.
- **Input:** `digital.pdf` with Selectable text.
- **Prompt:**

```text
Detect native text; if present skip OCR and extract fields only.
```

- **Expected result:**

```text
NATIVE_TEXT; extracted fields from text layer; no tesseract run logged.
```