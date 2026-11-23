---
id: ocr-mcp-focus
title: "OCR: Skill- und Tool-Fokus"
domain: office-dokumente
category: ocr
tags:
  - ocr
  - pdf-skill
  - markitdown
target_agents:
  - hermes
  - openclaw
  - generic-mcp-agents
required_tools:
  - name: Hermes-Skill pdf
    install: "https://hermes-agent.nousresearch.com/docs/reference/skills-catalog"
    version_notes: "OCR in pdf skill"
  - name: Anthropic document skills (pdf)
    install: "https://github.com/anthropics/skills"
    version_notes: "Verify render path"
  - name: MarkItDown
    install: "https://github.com/microsoft/markitdown"
    version_notes: "Some formats to MD"
inputs:
  - "Quelldateityp"
  - "Vertraulichkeitsstufe"
outputs:
  - "Empfohlene OCR-Route"
  - "Minimaler Tool-Satz"
risk_level: medium
version: "1.1.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

**OCR-Werkzeugwahl** (Hermes pdf, Tesseract, MarkItDown) nach Datenschutz und Qualität—ohne unnötige MCP-Last.

## Wann nutzen

- Setup-Phase: welche Skills/MCPs für Scan-Posteingang aktivieren.
- Entscheidung lokal vs. Cloud.
- Kombination OCR + Markdown-Wiki-Export.

**Wann nicht**

- Vollständiger OCR-Batch (→ ocr-workflow).
- Nur natives PDF lesen (→ pdf-mcp-focus).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Hermes pdf | Primary OCR | Bundled |
| Anthropic pdf | Verify | Render checks |
| MarkItDown | MD export | Nach OCR |
| tesseract | Air-gap | Kein MCP nötig |

## System-Prompt / Instruktionen

```text
You route OCR requests to the smallest capable toolset.

Decision tree:
- Confidential / no cloud → tesseract or Hermes local pdf OCR only
- Office PDF skill stack already loaded → Hermes or Anthropic pdf OCR before adding MarkItDown
- Need wiki markdown → MarkItDown after text extraction, not as OCR substitute

Disable unrelated MCPs (search, email) during OCR thread.

For multi-hundred page batches: stream per file; do not load all MCP schemas at once.

MarkItDown: good for born-digital office files; for image-only PDF warn user OCR required first.

Anthropic path: include verify render when layout tables matter.

Output routing memo: tools enabled, rationale, privacy class, next step template (ocr-workflow).

Never recommend pasting API keys into MCP env in chat.

OpenClaw: only verified skills from registry for OCR.

If user asks accuracy guarantee: refuse; offer confidence sampling protocol instead.

List disk space need for 300dpi rasterization multi-hundred pages.
Note GPU optional for some engines—not assumed.
```

## Arbeitsablauf

1. Vertraulichkeit und Volumen erfassen.
2. Prüfen ob Textlayer vorhanden (schneller pdf text extract).
3. Toolbaum anwenden; MCP-Satz minimieren.
4. Routing-Memo an Nutzer.
5. Verweis auf ocr-workflow für Ausführung.
6. Privacy-Hinweis bei Cloud-Option.
7. Skills include/exclude Liste dokumentieren.

## Qualitätskriterien / Definition of Done

- [ ] Tool-Wahl begründet (privacy, quality)
- [ ] Kein überflüssiger MCP-Katalog geladen
- [ ] MarkItDown nicht als OCR verkauft
- [ ] Follow-up Template benannt
- [ ] Keine Keys im Chat

## Sicherheit & Freigaben

- Cloud-OCR nur mit Vertrag und Freigabe.
- Tokens nicht in MCP-Args.
- PII-Scans nicht in Logs.

## Fallstricke

- MarkItDown auf Scan-PDF → leerer Text ohne OCR.
- Alle PDF-MCPs aktiv → Context-Explosion.
- Anthropic ohne Render bei Tabellen.
- Tesseract ohne deu-Pack.
- Batch ohne Disk-Quota.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Interne Scans, kein Cloud.
- **Input:** 50 HR-Scans, confidential.
- **Prompt:**

```text
Route OCR: local only; minimal MCP set; point to ocr-workflow steps.
```

- **Erwartetes Ergebnis:**

```text
Route: Hermes pdf OCR + tesseract fallback; MCPs: none extra; memo cites privacy class confidential.
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Wiki-Import aus Digital-PDF.
- **Input:** `manual.pdf` born-digital.
- **Prompt:**

```text
If native text, MarkItDown to md; else ocr-workflow first.
```

- **Erwartetes Ergebnis:**

```text
NATIVE_TEXT → MarkItDown manual.md; no OCR engine started.
```