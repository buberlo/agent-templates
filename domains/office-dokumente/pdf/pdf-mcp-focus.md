---
id: pdf-mcp-focus
title: "PDF: MCP- und Skill-Fokus"
domain: office-dokumente
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
    version_notes: "Validate + Render Pfad"
  - name: Hermes-Skill pdf
    install: "https://hermes-agent.nousresearch.com/docs/reference/skills-catalog"
    version_notes: "Bundled productivity/pdf"
  - name: pypdf
    install: "pip: pypdf"
    version_notes: "Merge, extract, forms"
  - name: MarkItDown
    install: "https://github.com/microsoft/markitdown"
    version_notes: "PDF → Markdown bei Bedarf"
inputs:
  - "PDF-Dateien oder Pfade"
  - "Operation (lesen, merge, form, ocr, edit)"
  - "Freigabe für irreversible Änderungen"
outputs:
  - "Bearbeitete PDF oder strukturierter Text"
  - "Verify-Log (Seiten, Hash, Stichprobe)"
risk_level: low
version: "1.1.0"
updated: "2026-11-23"
example_count: 3
---

## Zweck

**PDF-Operationen** über offizielle Document-Skills und Hermes pdf planen: lesen, mergen, Formulare, OCR—immer mit **Verify-Schritt** (Text, Render, Stichbild), nicht blind vertrauen.

## Wann nutzen

- Agent soll PDF-Toolkit (Skill/MCP) gezielt auswählen statt generisch zu scrapen.
- Merge, Formularausfüllung oder OCR auf Scans mit menschlicher Endkontrolle.
- Nach DOCX-Erzeugung PDF als Prüf-Artefakt (gleicher Workflow wie Anthropic-Tutorial).

**Wann nicht**

- Finale Behörden-Einreichung ohne menschliche Sichtprüfe.
- Passwort-geschützte PDFs ohne vom Nutzer gelieferte Credentials.
- Voller Layout-Editor-Ersatz (InDesign-Niveau).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Anthropic pdf-Skill | Erzeugen, prüfen, pypdf | Offizieller Verify-Pfad |
| Hermes pdf-Skill | OCR, merge, edit | Bundled, offline-fähig |
| pypdf | Scriptbare Basis | Schnelle Extraktion/Merge |
| pdftoppm / Render | Visuelle QA | Text allein reicht nicht |
| MarkItDown | MD-Export | Weiterverarbeitung in Wikis |

## System-Prompt / Instruktionen

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

OCR: run skill OCR; produce side-by-side diff sample for numbers and legal references (Aktenzeichen).

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

## Arbeitsablauf

1. Eingangs-PDF mit pypdf inventarisieren (Seiten, Verschlüsselung, Formularfelder).
2. Skill/MCP passend zur Aufgabe aktivieren (nur pdf-Scope).
3. Operation ausführen (read/merge/fill/ocr) in Testkopie unter `out/`.
4. Programmatisches Gegenlesen der Felder bzw. Textextraktion.
5. `pdftoppm -f 1 -l 2 out/result.pdf out/qa` für visuelle Stichprobe.
6. Nutzer-Freigabe bei Einreichungs-PDFs dokumentieren.
7. Finales Artefakt mit Pfad und Seitenzahl übergeben.

## Qualitätskriterien / Definition of Done

- [ ] Ausgabe-PDF öffnet und Seitenzahl stimmt mit Erwartung
- [ ] Formularfelder programmatisch gegen Soll-Werte geprüft
- [ ] OCR: kritische Zahlen im Stichproben-Vergleich zum Scan
- [ ] Kein Upload/Versand ohne dokumentierte Freigabe
- [ ] Tool-Aufrufe und Skill-Namen im Log

## Sicherheit & Freigaben

- OCR-Fehler bei Beträgen und Aktenzeichen: menschliche Sichtprüfung vor Einreichung.
- Keine Tokens in Skill-Argumenten oder Custom-MCP-CLI.
- Original-PDFs nicht löschen ohne explizite Bestätigung.

## Fallstricke

- Grüner Validator ohne PNG/PDF-Render erkennt Tabellen-Overflow nicht.
- OCR verwechselt 0/O und 1/l in IBAN und Aktenzeichen.
- Merge ohne einheitliche Seitengröße erzeugt unsichtbare Skalierungsfehler.
- Zu viele MCPs aktiv → Token-Overhead vor der ersten Aktion.
- Signierte PDFs nach Bearbeitung ungültig—neu signieren ist separater Prozess.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Drei Einreichungs-PDFs in feste Reihenfolge mergen.
- **Input:** `anlage_a.pdf` (2 S.), `anlage_b.pdf` (5 S.), `antrag.pdf` (3 S.).
- **Prompt:**

```text
Merge in order antrag, anlage_a, anlage_b to packet.pdf. Verify 10 pages. List pypdf commands.
```

- **Erwartetes Ergebnis:**

```text
packet.pdf: 10 pages; merge log with input order; pypdf reader confirms page count.
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Scan-PDF OCR und Betrag aus Seite 1 extrahieren.
- **Input:** `rechnung_scan.pdf` (image-only).
- **Prompt:**

```text
OCR with Hermes pdf skill; extract invoice total and date; flag low-confidence chars; no submission.
```

- **Erwartetes Ergebnis:**

```text
extracted.txt with TOTAL and DATE lines; confidence warnings on any digit under threshold; PNG qa page for user review.
```

### Beispiel 3 (Praxisbeispiel)

- **Aufgabe:** Aus DOCX gerendertes Briefing-PDF mit pdf-Skill zurücklesen (Verify aus Anthropic-Tutorial).
- **Input:** `briefing.pdf` aus vorherigem DOCX-Render.
- **Prompt:**

```text
Use Anthropic pdf skill / pypdf PdfReader: report page count and first heading text from briefing.pdf.
```

- **Erwartetes Ergebnis:** Seitenzahl und Textauszug dokumentiert; gleicher Verify-Workflow wie DOCX-Pipeline.
- **Quelle:** https://aifrontierpost.com/articles/anthropic-official-agent-skills-tutorial/