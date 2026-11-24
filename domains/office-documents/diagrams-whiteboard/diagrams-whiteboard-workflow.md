---
id: diagrams-whiteboard-workflow
title: "Diagramme and Whiteboards document"
domain: office-documents
category: diagrams-whiteboard
tags:
  - mermaid
  - excalidraw
  - diagrams
target_agents:
  - cursor
  - claude-code
  - generic
required_tools:
  - name: mermaid-cli
    install: "npm: @mermaid-js/mermaid-cli"
    version_notes: "mmdc SVG/PNG"
  - name: draw.io
    install: "https://github.com/jgraph/drawio-desktop or CLI export"
    version_notes: "Optional"
inputs:
  - "Architektur- or Prozessbeschreibung"
  - "Targetformat (SVG, PNG, embed in MD)"
outputs:
  - "Diagrammdateien"
  - "Quelltext (mmd/drawio)"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

**Prozess- and Architekturdiagramme** as versionierbare Quellen (Mermaid, draw.io) create and for Docs/PDF exportieren.

## When to use

- Workshop-resultse in Wiki-faehige Diagramme viafuehren.
- CI-Docs with eingebetteten SVGs.
-Agent iterates to the text-source instead of pixels.

**When not to use**

- UX-High-Fidelity in Figma.
- GIS or CAD (→ hardware/wissenschaft).
- Live-Whiteboard-Sync without Export-Snapshot.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| Mermaid | Text-Diagramme | Git-diff-freundlich |
| mmdc | Render | SVG for Pandoc |
| draw.io | Komplexe Layouts | Optional |
| Excalidraw | Skizzen | JSON-Export when vorhanden |

## System prompt

```text
You create maintainable diagrams from user descriptions—prefer Mermaid for flow/sequence/C4 unless layout needs draw.io.

You are a careful assistant for this workflow. You work read-first by default and you must not run destructive or production changes until the user confirms the approval gate named in their request.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.


Inputs: diagram type, nodes and edges list, style (light/dark), output paths (diagram.mmd, diagram.svg), language DE labels if requested.
Mermaid rules:
- Unique node ids; avoid reserved words; quote labels with special chars.
- Max ~25 nodes per diagram—split into linked diagrams if larger.
- Run mmdc -i diagram.mmd -o diagram.svg before claiming done.
draw.io: only when user needs freeform; keep .drawio source in repo; export svg/png.
Whiteboard import: if user pastes Excalidraw JSON, clean and export svg—do not trace screenshots unless no source.
Accessibility: title/desc in svg metadata when embedding in docs.
Approvals: publish diagrams with customer names requires user yes.
Output: source file, rendered svg, render command log.
Never invent infrastructure the user did not describe—use TBD nodes.
Version filenames with v1 v2 when iterating major layout changes.
Validate mermaid syntax with mmdc stderr empty.
For C4 use official mermaid C4 blocks when applicable.
Keep legend for color semantics when more than 3 colors.```

## Workflow

1. Knoten/Kanten from Briefing tabellarisch.
2. Mermaid source write.
3. `mmdc` rendern; at Fehler Syntax fixen.
4. SVG in MD einbinden testen.
5. Optional draw.io for Layout-Korrektur.
6. Review with User (Screenshot or SVG).
7. Quellen ins Repo committen.

## Definition of done

- [ ] mmdc exit 0
- [ ] Source in Repo versioniert
- [ ] Lesbare Labels (DE/EN konsistent)
- [ ] Grosse Diagramme aufgeteilt
- [ ] Kundennamen only with approval

## Security

- Interne Architektur not oeffentlich posten without approval.
- no echten Hostnames in oeffentlichen Demos.
- Whiteboard-Screenshots can PII enthalten.

## Pitfalls

- Mermaid-Knoten with Klammern without Quotes.
- SVG riesig durch eingebettete Fonts.
- draw.io without CLI-Export manuell vergessen.
- Sequenzdiagramm with falschem activate/deactivate.
- Dark-Theme in Print-PDF unleserlich.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Onboarding-Prozess Flowchart.
- **Input:** 8 steps of Registrierung bis Go-Live.
- **Prompt:**

```text
Mermaid flowchart TD; render deploy_flow.svg; German labels.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.deploy_flow.mmd, deploy_flow.svg; mmdc log success.
```

### Example 2 (Example data (self-written))
- **Task:** Sequenz Auth-Service.
- **Input:** 4 Akteure, 6 Messages.
- **Prompt:**

```text
Mermaid sequenceDiagram; export auth_seq.svg.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.auth_seq.mmd/svg; actors User, API, IdP, DB documented.
```