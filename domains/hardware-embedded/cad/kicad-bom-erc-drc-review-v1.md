---
id: kicad-bom-erc-drc-review-v1
title: "KiCad BOM, ERC, and DRC pre-fab review"
domain: hardware-embedded
category: cad
tags:
  - kicad
  - bom
  - erc
  - drc
  - pcb
  - manufacturing
target_agents:
  - hermes
  - grokbot
  - claude-code
  - cursor
  - codex
  - generic-mcp-agents
required_tools:
  - name: KiCad CLI (kicad-cli)
    install: "https://docs.kicad.org/9.0/en/cli/cli.html"
    version_notes: "Ships with KiCad 9.0; sch erc, pcb drc, and sch export bom are used here."
  - name: kicad-mcp
    install: "https://github.com/lamaalrajih/kicad-mcp"
    version_notes: "MIT license; requires KiCad 9.0 or higher, Python 3.10+, and uv; finds projects via KICAD_SEARCH_PATHS."
  - name: filesystem MCP server
    install: "https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem"
    version_notes: "Read-only access to erc.json, drc.json, bom.csv, and the report folder."
inputs:
  - "Path to the KiCad project (.kicad_pro, .kicad_sch, .kicad_pcb) and board revision"
  - "Target fab rules and the severity threshold the user treats as blocking"
  - "Optional BOM field requirements such as MPN and Manufacturer"
outputs:
  - "fab-readiness.md with summary, violation table, and BOM exception list"
  - "Exported erc.json, drc.json, and bom.csv artifacts with paths"
risk_level: medium
example_count: 2
version: "1.0.0"
updated: "2026-11-28"
---

## Purpose

Run a headless pre-fabrication check on a KiCad 9.0 project: schematic ERC, PCB DRC, and a grouped BOM export, then triage every finding by severity and produce a fab-readiness report. The human fixes the design in KiCad and decides when to order; this template never edits .kicad_sch or .kicad_pcb files and never uploads to a fab.

## When to use

- Before placing a first PCB order or a revision reorder, when the schematic and layout are nominally complete.
- When a teammate hands off a KiCad project and you need a fast check of ERC, DRC, and BOM quality.
- When the BOM lacks MPN or Manufacturer fields and the assembly house needs a clean file.
- When DNP parts or value changes must be confirmed before the fab and assembly quotes are requested.

### When not to use

- As a substitute for a human design review of analog, RF, or high-voltage sections.
- When the project is not saved in a KiCad 9.0-compatible format or the CLI is not installed.
- For panelization, impedance, or stackup decisions that need the fab's own DFM feedback.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| KiCad CLI (kicad-cli) | ERC, DRC, BOM export | Repeatable headless runs with JSON output and exit codes |
| kicad-mcp | Project discovery and BOM/DRC tracking | Reads projects via KICAD_SEARCH_PATHS and keeps history |
| filesystem MCP | Report and artifact access | Read-only reads of erc.json, drc.json, bom.csv |
| KiCad GUI (human) | Fixes and final approval | Only the human edits .kicad_sch and .kicad_pcb |

## System prompt

```text
You review KiCad 9.0 projects for a pre-fabrication readiness pass, reading .kicad_sch and .kicad_pcb files without modifying them.
You run kicad-cli sch erc with --severity-all --exit-code-violations --format json -o erc.json and capture the exit code before any other step.
You run kicad-cli pcb drc with --severity-all --exit-code-violations --format json -o drc.json and separate errors from warnings by the severity field.
You export the BOM with kicad-cli sch export bom --exclude-dnp --group-by Value,Footprint -o bom.csv and then compare it with the schematic symbol fields.
You flag BOM rows that lack an MPN or Manufacturer field, rows marked DNP, and rows where the footprint or value differs from the schematic symbol.
You classify every ERC and DRC violation as error, warning, or exclusion, and you rank them by whether they block fabrication or only need review.
You treat unconnected pins, power-pin conflicts, and missing footprints as blocking until the human confirms they are intentional.
You write the fab-readiness report to fab-readiness.md with a summary table, a violation table with file and coordinate references, and a BOM exception list.
You never edit .kicad_sch or .kicad_pcb files, never run a fab upload, and never approve an order on the user's behalf.
You quote exact violation counts and the board coordinates or schematic sheet and reference designator from the JSON report in every finding so the human can jump to the issue in KiCad.
You ask the human to fix each blocking item in KiCad and re-run the same kicad-cli commands before you mark the board ready.
You keep the exported JSON, CSV, and Markdown artifacts in the project folder and list their paths at the end of the report.
You state clearly when a violation needs a design decision, such as a footprint change, rather than silently guessing a fix.
You refuse to fabricate missing MPN data and instead list the exact reference designators that need a manufacturer part number.
```

## Workflow

1. Confirm the project path, KiCad version, and board revision, then set KICAD_SEARCH_PATHS for kicad-mcp.
2. List the project files with kicad-mcp and confirm that the .kicad_sch and .kicad_pcb pair match the requested revision.
3. Run kicad-cli sch erc with --severity-all --exit-code-violations --format json -o erc.json and record the exit status.
4. Run kicad-cli pcb drc with --severity-all --exit-code-violations --format json -o drc.json and record the exit status.
5. Export the BOM with kicad-cli sch export bom --exclude-dnp --group-by Value,Footprint -o bom.csv.
6. Triage ERC and DRC findings into blocking, review, and accepted-exclusion groups with file and coordinate references.
7. Audit BOM rows for missing MPN, missing Manufacturer, DNP status, and value or footprint mismatch against the schematic.
8. Write fab-readiness.md with the summary table, violation table, BOM exception list, and artifact paths; list every item the human must fix in KiCad.
9. Hand the report to the human, who fixes the design and decides when to order; do not edit source files or contact a fab.

## Definition of done

- [ ] ERC, DRC, and BOM commands ran with the recorded exit status
- [ ] Every violation is grouped as blocking, review, or accepted exclusion
- [ ] BOM exception list names missing MPN, DNP, and value or footprint mismatch rows
- [ ] fab-readiness.md lists all artifact paths and human fixes
- [ ] No .kicad_sch or .kicad_pcb file was edited and no fab was contacted

## Security

- Keep project files, BOM pricing, and fab quotes in the project folder; do not paste them into public chats.
- Run kicad-cli and kicad-mcp with the least access needed; the agent only reads artifacts.
- Never upload the project, Gerbers, or BOM to a fab portal; the human owns that action.
- Treat MPN and supplier data as confidential when the BOM includes negotiated pricing.

## Pitfalls

- A clean ERC does not prove the circuit works; unconnected pins marked as no-connect can hide a real wiring mistake.
- DRC rules differ from the fab's capabilities, so a passing board can still fail at the fab if the rule set is stale.
- BOM grouping by Value,Footprint merges parts that need distinct MPNs and hides a substitution risk.
- DNP parts may still appear in the assembly file if --exclude-dnp is missing, which inflates the quote.
- Stale erc.json or drc.json from an earlier revision can make a changed board look ready.
- Footprint names that differ only by a suffix can pass a string check while the pad geometry differs.
- Footprint mismatches between schematic and board stay hidden unless DRC runs with --schematic-parity.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Review fictional Acme Sensor Board rev C before ordering 25 boards.
- **Input:** KiCad project at /work/acme-sensor-revC with one ERC error and one DRC clearance error.
- **Prompt:**

```text
Run ERC, DRC, and the grouped BOM for acme-sensor-revC. Treat severity-error as blocking, flag missing MPN and DNP rows, and write fab-readiness.md. Do not edit the design.
```

- **Expected result:**

```text
Fab-readiness: NOT READY (3 blocking items)
ERC: 12 violations (2 error, 7 warning, 3 exclusion)
DRC: 9 violations (1 error, 6 warning, 2 exclusion)
Blocking DRC: clearance 0.15 mm at (42.10, 18.75) on F.Cu, below the 0.20 mm rule
BOM: 41 rows after --exclude-dnp (3 DNP symbols R7, C9, C10 excluded), 6 missing MPN, 2 value mismatches (R14, C22)
BOM exception: U3 footprint field SOT-23-5 differs from the footprint placed on the PCB (SOIC-8); re-run DRC with --schematic-parity to confirm
Artifacts: erc.json, drc.json, bom.csv, fab-readiness.md
Human action: fix R14 value, confirm the DNP status of R7, C9, C10, then re-run all three commands
```

### Example 2 (Example data (self-written))

- **Task:** Run a BOM-only audit of fictional Acme Power Board rev A.
- **Input:** bom.csv and the schematic symbol table for the same revision.
- **Prompt:**

```text
Audit bom.csv against the schematic symbols. List missing MPN, DNP, duplicate references, and footprint mismatches. Do not change any file.
```

- **Expected result:**

```text
BOM audit: 28 rows, 4 missing MPN, 2 DNP, 1 duplicate reference
Missing MPN: Q1, Q2, D4, J3 (all need Manufacturer and MPN fields)
DNP rows: R21 and R22 excluded from the order by --exclude-dnp
Duplicate: C8 appears twice with values 100nF and 1uF; schematic shows 100nF
Footprint check: J3 is USB-C-16P in BOM but USB-C-6P in schematic symbol
Decision: hold the order until Q1, Q2, D4, J3 and C8 are resolved
Artifacts: bom.csv and bom-audit.md in the project folder
```

## Sources

- https://docs.kicad.org/9.0/en/cli/cli.html
- https://docs.kicad.org/9.0/en/pcbnew/pcbnew.html
- https://docs.kicad.org/9.0/en/eeschema/eeschema.html
- https://github.com/lamaalrajih/kicad-mcp
