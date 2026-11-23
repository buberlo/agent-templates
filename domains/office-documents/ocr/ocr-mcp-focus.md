---
id: ocr-mcp-focus
title: "OCR: Skill- and Tool-Fokus"
domain: office-documents
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
  - "Minimaler Tool-set"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

**OCR-Werkzeugwahl** (Hermes pdf, Tesseract, MarkItDown) after Datenschutz and Qualitaet—without unrequirede MCP-Last.

## When to use

- Setup-Phase: welche Skills/MCPs for scan inbox enable.
- Entscheidung lokal vs. Cloud.
- Kombination OCR + Markdown-Wiki-Export.

**When not to use**

- Vollstaendiger OCR-Batch (→ ocr-workflow).
- only natives PDF read (→ pdf-mcp-focus).

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| Hermes pdf | Primary OCR | Bundled |
| Anthropic pdf | Verify | Render checks |
| MarkItDown | MD export | after OCR |
| tesseract | Air-gap | no MCP required |

## System prompt

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

## Workflow

1. Vertraulichkeit and Volumen erfassen.
2. Check whether a text layer exists (fast PDF text extract).
3. tool tree anwenden; MCP-set minimieren.
4. Routing-Memo an User.
5. Verweis on ocr-workflow for Ausfuehrung.
6. Privacy-Hinweis at Cloud-Option.
7. Skills include/exclude list document.

## Definition of done

- [ ] Tool-Wahl begruendet (privacy, quality)
- [ ] no viafluessiger MCP-catalog geladen
- [ ] MarkItDown not as OCR verkauft
- [ ] Follow-up Template benannt
- [ ] no Keys im Chat

## Security

- Cloud-OCR only with Vertrag and approval.
- Tokens not in MCP-Args.
- PII-Scans not in Logs.

## Pitfalls

- MarkItDown on Scan-PDF → leerer Text without OCR.
- all PDF-MCPs aktiv → Context-Explosion.
- Anthropic without Render at Tabellen.
- Tesseract without deu-Pack.
- Batch without Disk-Quota.

## Basic examples

### Example 1 (Example data)

- **Task:** Interne Scans, no Cloud.
- **Input:** 50 HR-Scans, confidential.
- **Prompt:**

```text
Route OCR: local only; minimal MCP set; point to ocr-workflow steps.
```

- **Expected result:**

```text
Route: Hermes pdf OCR + tesseract fallback; MCPs: none extra; memo cites privacy class confidential.
```

### Example 2 (Example data)

- **Task:** Wiki-Import from Digital-PDF.
- **Input:** `manual.pdf` born-digital.
- **Prompt:**

```text
If native text, MarkItDown to md; else ocr-workflow first.
```

- **Expected result:**

```text
NATIVE_TEXT → MarkItDown manual.md; no OCR engine started.
```