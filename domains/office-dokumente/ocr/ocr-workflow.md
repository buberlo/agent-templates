---
id: ocr-workflow
domain: office-dokumente
title: "OCR für Scans und Bild-PDFs"
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
  - "Scan-PDF oder Bilder"
  - "Sprache (deu+eng)"
  - "Freigabe für Drittanbieter-OCR"
outputs:
  - "Text pro Seite"
  - "confidence-Warnungen"
risk_level: medium
version: "1.1.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

**Text aus Scans** extrahieren mit Skill- oder Tesseract-Pfad, kritische Felder **am Bild gegenlesen**—besonders Zahlen und Namen.

## Wann nutzen

- Rechnungs- und Vertrags-Scans als durchsuchbaren Text.
- Kein natives Textlayer im PDF.
- Ergebnis ist Entwurf für Mensch oder ERP, nicht Auto-Buchung.

**Wann nicht**

- Handschrift ohne spezialisiertes Modell.
- Rechtlich bindende Einreichung ohne Mensch.
- Inhalte mit strengem Cloud-Verbot ohne lokales OCR.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Hermes pdf OCR | Integriert | Skill-Pfad |
| tesseract | Lokal | Air-gapped |
| pdftoppm | Rasterize | Vor Tesseract |
| pdf-Skill | Verify | Gegenlesen Struktur |

## System-Prompt / Instruktionen

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

## Arbeitsablauf

1. `pdfinfo` / pypdf: Textlayer prüfen.
2. Bei Scan: Seiten zu PNG (300 DPI).
3. OCR Skill oder `tesseract png stdout`.
4. Confidence-Report pro Seite.
5. Kritische Felder extrahieren + Crop speichern.
6. Nutzer Stichprobe Betrag vs. Bild.
7. Textdatei mit [?]-Markierungen liefern.

## Qualitätskriterien / Definition of Done

- [ ] NATIVE_TEXT vs OCR dokumentiert
- [ ] Niedrig-Confidence-Seiten gelistet
- [ ] Beträge/Datum stichprobenartig geprüft oder als OPEN markiert
- [ ] Kein Cloud-OCR ohne Freigabe
- [ ] Engine-Log vorhanden

## Sicherheit & Freigaben

- Vertrags- und Gesundheits-Scans vertraulich.
- Keine öffentlichen OCR-APIs ohne Vertrag.
- Einreichung nur nach menschlicher Freigabe.

## Fallstricke

- 72 DPI reicht nicht für Kommazahlen.
- deu ohne englische Begriffe in Rechnungen.
- Tabellen als Fließtext ohne Spalten.
- Doppelte Seiten im Scan.
- Such-PDF schlecht indexiert bei schiefem Raster.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Lieferantenrechnung Scan → Text.
- **Input:** `invoice_scan.pdf` 2 Seiten, deu.
- **Prompt:**

```text
OCR beide Seiten; extract total and invoice date; flag conf<85%; save page crops.
```

- **Erwartetes Ergebnis:**

```text
invoice_scan.txt; critical_field_table: TOTAL 1.234,56 EUR date 2026-11-15; page2 conf warning if any.
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Bereits Text-PDF.
- **Input:** `digital.pdf` mit Selectable text.
- **Prompt:**

```text
Detect native text; if present skip OCR and extract fields only.
```

- **Erwartetes Ergebnis:**

```text
NATIVE_TEXT; extracted fields from text layer; no tesseract run logged.
```