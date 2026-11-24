---
id: meeting-transcription-mcp-focus
title: "Meetings and transcription: MCP/skill focus"
domain: communication
category: meeting-transcription
tags:
  - meetings
  - communication
  - skill
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: ClawHub / OpenClaw Skill Openai Whisper (steipete)
    install: "https://clawhubtrends.com/leaderboard.html"
    version_notes: "303 GitHub Stars"
  - name: Hermes-Skills meeting-action-items, teams-meeting-pipeline
    install: "https://hermes-agent.nousresearch.com/docs/reference/skills-catalog"
    version_notes: "Bundled."
inputs:
  - "Transcript source (local vs. Fireflies)"
  - "Permitted data outflows"
outputs:
  - "Tool-Entscheidungsbaum"
  - "Minimales MCP/Skill-Set"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

**Set transcription stack**: local Whisper vs. Fireflies MCP vs. Team Pipeline—Keep data residence, skills, and MCP minimal.

## When to use

Compliance asks for cloud vs. on-device ASR.
Agent should only read Fireflies, not re-upload.
- Install and verify OpenClaw Whisper.

**When not to use**

- Fertiges Audio bereits transcribed → direkt Action-Item-Extraktion.
- No Fireflies account and no GPU/CPU time for Whisper.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| OpenClaw Whisper | Lokal ASR | Kein Audio-Upload |
| fireflies MCP | Vorhandene Transkripte | SaaS bereits im Einsatz |
| meeting-action-items | Post-Processing | Struktur, no ASR |

## System prompt

```text
You design meeting transcription tooling for communication/meeting-transcription.

Inputs: data_residency (local_only | saas_ok), has_fireflies (bool), openclaw_available (bool), gpu (bool).

Decision tree:
- local_only → openclaw whisper + ffmpeg; disable fireflies mcp
- has_fireflies + saas_ok → fireflies MCP read only; whisper optional for gaps
- teams_meeting_pipeline skill if recordings live in M365 and skill configured

Document in meeting-tooling.md:
install commands, verify steps (openclaw skills verify whisper), model size recommendation from gpu flag.
Set never upload_without_approval default true.

List disabled tools explicitly.
```

## Workflow

1. Data residency policy of the user (`local only` / `saas ok`).
2. Check availability: OpenClaw, Fireflies Token, Hermes Skills.
3. Entscheidungsbaum in `meeting-tooling.md` schreiben.
individuals Openclaw skills verify for whisper skills.pen.
- ins and overs are Security,ing overs and over interfere.
6. Test: short 30s sample clip local OR Fireflies get last transcript metadata.
7. User sign-off on Tooling-Doc.

## Definition of done

- [ ] Datenabfluss dokumentiert (lokal vs. SaaS)
- [ ] Unbenutzte Upload-Tools deaktiviert
- [ ] Verify step for ClawHub skill
- [ ] Model choice justified (CPU vs. GPU)

## Security

- Recording rights concerned and concerned'' country consent outside of tooling, but linked in doc.
- Fireflies exports are not in public tickets.
In the  heat treats of the bro- got the next month, ---, the show.

## Pitfalls

The end of the entity in front a cross- poster, a crossnap of a cross-aper a cross-aper a cross-aper a cross-aper a cross-aper a cross-aper a cross-aper a cross-ap-o cross over the in a cross-aper cross-aper a cross-aper a cross-aper a cross-aper a cross-apr cross-aper a cross-aper a cross-aper a cross-aper a cross-aper a cross-aper a cross-aper cross-ap a those cross- a cross-aper a cross-aper a cross-aper a cross-aper a cross-aper a cross-aper a cross-aper a cross-aper a cross-aper a cross-aper a cross-aper a cross-aper cross-aper a cross-aper a cross-aper a cross-aper a cross-aper a cross-aper a cross-aper a cross-aper a cross-aper a cross cross-aper a cross-aper a cross-aper a cross-
- Whisper large auf CPU → Stunden Laufzeit without Warnung.
- Teams-Pipeline without OAuth → leere Runs.
- MCP upload tool forget to disable at local only.
- Veraltetes Whisper-Skill without VAD → schlechte Segmente.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** local_only Setup.
- **Input:** `data_residency=local_only`, GPU nein.
- **Prompt:**

```text
Choose tools for on-device transcription only, recommend whisper model for CPU.
```

- **Expected result:**

```text
ASR: openclaw whisper base or small
Disabled: fireflies mcp, any upload MCP
Model note: small for CPU, expect ~2x realtime
File: meeting-tooling.md
```

### Example 2 (Example data (self-written))
- **Task:** Fireflies-only read.
- **Input:** `has_fireflies=true`, `saas_ok=true`.
- **Prompt:**

```text
Enable only fireflies MCP read; meeting-action-items for parsing.
```

- **Expected result:**

```text
Read: fireflies MCP get_transcript
Post: hermes meeting-action-items
Disabled: whisper install required false
upload_without_approval: false (enforced)
```