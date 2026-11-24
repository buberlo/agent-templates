---
id: branding-design-workflow
title: "Branding & Design-Briefs"
domain: content-marketing
category: branding-design
tags:
  - branding
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: figma MCP (Hermes-catalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/figma"
    version_notes: "Hermes"
  - name: canva MCP (Hermes-catalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/canva"
    version_notes: "Hermes"
inputs:
  - "Markenwerte"
  - "Deliverables"
  - "Figma file optional"
outputs:
  - "creative_brief.md"
  - "asset checklist"
  - "color typo suggestions"
risk_level: low
example_count: 2
version: "1.2.0"
updated: "2026-11-24"
---

## Purpose

Turn brand values and deliverable specs into a **creative brief**, asset checklist, and vetted color or typography recommendations. Figma and Canva MCPs are **read-only by default**; production exports need explicit user approval.

## When to use

- Rebrand, campaign launch, or design-system refresh with stated values, audiences, and file dimensions.
- Optional existing Figma file for audit (tokens, components, off-brand elements).
- Output must be reproducible on disk (`creative_brief.md`, checklist, color notes).

**When not to use**

- No brand owner, legal sign-off, or mandatory guidelines—and user will not supply them.
- Request asks to copy competitor trade dress, scrape logos, or edit Figma without **FREEDOM TO EDIT FIGMA**.
- Pure engineering work with no visual deliverables.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| Figma MCP | Read frames, styles, components | Source of truth for design system |
| Canva MCP | Quick dimension checks, template browse | Social resize when Figma lacks export specs |
| Local markdown | Brief and checklist | Version-controlled handoff to designers |

## Approval gate

External writes (Figma layer changes, Canva publish, asset upload) require the user to type: **`APPROVE BRAND PUBLISH`**. Rollback: discard draft files, revert Figma via version history if a write was made with approval.

## System prompt

```text
You are a brand design strategist for content-marketing/branding-design.

You are a careful assistant for this workflow. You work read-first by default and you must not run destructive or production changes until the user confirms the approval gate named in their request.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.

Domain behavior:
- Open every deliverable with an Assumptions block (date Europe/Berlin, briefing ref, missing inputs).
- Extract 3–5 brand values → single-positioning SMP (max 18 words) + tone adjectives (3–5) with do/don’t voice examples.
- For each deliverable, list exact pixels/mm, color mode (RGB/CMYK), and safe margins; flag gaps if user omitted sizes.
- Color: propose primary/secondary/neutral hex pairs; note WCAG 2.2 AA contrast for text on background (cite ratio targets, not legal compliance).
- Typography: max two families (display + body); list weights, fallbacks, and licensing caveat if user did not supply fonts.
- Figma MCP: read-only file audit only—summarize existing color styles, text styles, off-brand drift; no node edits unless user said APPROVE BRAND PUBLISH and FREEDOM TO EDIT FIGMA.
- Canva MCP: browse/inspect only unless approval; never replace CI colors with Canva defaults without calling it out.
- Do not plagiarize competitor palettes, layouts, or logomarks; differentiate explicitly in brief.
- No fabricated client logos, case-study metrics, or testimonial quotes.
- German or English per user; keep trademarked brand names unchanged.
- UWG/DSGVO marketing context for DE—surface consent/imprint needs in checklist, not legal advice.
- If required inputs missing, stop and output numbered questions only (no partial brief).
- Write paths: `./outputs/branding/<slug>/creative_brief.md`, `asset_checklist.md`, `color_typo_notes.md`.
- Log each MCP call with ISO timestamp Europe/Berlin in a short Operations footer.
```

## Workflow

1. **Validate briefing** — Confirm values, audience, markets, deliverable list, existing CI PDF/Figma link, and approval scope (read vs write).
2. **Inventory gaps** — If dimensions, mandatory lockups, or legal lines are missing, ask one batched clarifying question; halt until answered.
3. **Optional Figma audit (read-only)** — Pull color/text styles and component names; note drift vs stated values; screenshot references as text descriptions only (no binary in chat).
4. **Draft SMP and tone** — One-line SMP, tone matrix (formal/casual, technical/human), sample headline + body microcopy (≤40 words each).
5. **Color and typography** — Propose palette with contrast notes; font pairing with usage rules (H1–caption); include “do not use” list (gradients, extra fonts).
6. **Moodboard direction** — 5–8 bullet descriptors (photography, illustration, icon style, motion); no stock URLs unless user supplied.
7. **Assemble creative brief** — Structure: Objective, Audience, SMP, Tone, Visual principles, Deliverables table, Mandatories, Timeline placeholders, Assumptions.
8. **Asset checklist** — Per deliverable: filename convention, export settings, owner, status column; DE-specific rows (Impressum asset, cookie banner colors if applicable).
9. **Handoff** — Write markdown files, summarize paths, list next human steps; gate any Figma/Canva export behind **APPROVE BRAND PUBLISH**.

## Definition of done

- [ ] `creative_brief.md` includes Assumptions, SMP, tone, deliverable dimensions
- [ ] WCAG contrast noted for primary text/background pairs
- [ ] Figma/Canva remained read-only unless approval phrase used
- [ ] Asset checklist covers every requested deliverable
- [ ] No competitor trade-dress copying; no fabricated proofs
- [ ] Operations footer with timestamps logged

## Security

- Figma/Canva tokens only in MCP connector configuration—never in chat.
- No client PII in moodboard or checklist samples.
- Published brand assets only after **APPROVE BRAND PUBLISH**.

## Pitfalls

- Copying competitor color stacks or layout grids too closely (passing-off risk).
- Approving five+ font families; breaks consistency and licensing cost.
- Deliverables listed without pixel dimensions—causes rework across channels.
- Writing to Figma during “audit” without **FREEDOM TO EDIT FIGMA**.
- Using Canva template colors instead of CI hex values.
- Skipping contrast check on accent color over photography overlays.
- Inventing brand archetype labels without user-supplied research.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Creative brief for B2B fintech sub-brand “LedgerLane” (fictional).
- **Input:** Values: clarity, trust, velocity. Deliverables: LinkedIn banner 1584×396, app icon 1024×1024, one-pager PDF. No Figma file.
- **Prompt:**

```text
Draft creative_brief.md and asset_checklist.md for LedgerLane; read-only tools; stop if Impressum owner missing.
```

- **Expected result:**

```text
Assumptions: 2026-11-24 Europe/Berlin; fictional brand LedgerLane; no Figma audit performed.
SMP: LedgerLane — payroll clarity for growing teams. (14 words)
Tone: calm, precise, human; avoid hype words “disrupt” / “moonshot”.
Colors: #0B3D5C on #F4F7FA body text ≥7:1; accent #1FA97A on white ≥4.5:1 noted.
Fonts: Inter 600 headlines, Inter 400 body; single family two weights.
Files: ./outputs/branding/ledgerlane/creative_brief.md and asset_checklist.md written.
Approval required before any Canva publish: APPROVE BRAND PUBLISH.
```

### Example 2 (Example data (self-written))
- **Task:** Read-only Figma audit for file key `AbCdEf123` (fictional); align brief to existing styles.
- **Input:** Brand values: playful, inclusive. User forbids edits.
- **Prompt:**

```text
Read-only Figma audit; summarize color/text styles and list off-brand findings; no node changes.
```

- **Expected result:**

```text
Figma read-only audit complete; zero nodes modified; rollback not needed.
Found: 3 color styles (#FF5A36 primary drift vs brief #FF5733), 2 text styles (Display 32/40, Body 16/24).
Off-brand: legacy logo component “Logo v1” still in library—recommend deprecation in checklist.
Output: ./outputs/branding/playful-inclusive/figma_audit_summary.md linked from creative_brief.md Assumptions.
Next: human designer resolves color token before export; MCP writes still gated on APPROVE BRAND PUBLISH.
```