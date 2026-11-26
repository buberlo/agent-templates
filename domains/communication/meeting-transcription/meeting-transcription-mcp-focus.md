---
id: meeting-transcription-mcp-focus
title: "Meeting transcription: MCP and skill stack"
domain: communication
category: meeting-transcription
tags:
  - meetings
  - transcription
  - mcp
target_agents:
  - hermes
  - openclaw
  - cursor
  - generic-mcp-agents
required_tools:
  - name: OpenClaw OpenAI Whisper skill
    install: "https://docs.openclaw.ai/skills/"
    version_notes: "Local ASR after skills verify; see ClawHub listing"
  - name: fireflies MCP (Hermes catalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/fireflies"
    version_notes: "Read existing transcripts; do not re-upload audio without approval"
  - name: Hermes meeting-action-items skill
    install: "https://hermes-agent.nousresearch.com/docs/reference/skills-catalog"
    version_notes: "Post-processing only; no ASR"
inputs:
  - "Data residency policy: local_only or saas_ok"
  - "Whether Fireflies or Teams recordings already exist"
  - "GPU availability for on-device Whisper model sizing"
outputs:
  - "meeting-tooling.md with chosen stack and disabled tools list"
  - "Model size recommendation and verify commands"
  - "Handoff to meeting-transcription-workflow for processing"
risk_level: low
example_count: 2
version: "1.2.0"
updated: "2026-11-26"
---

## Purpose

Select a minimal meeting transcription toolchain before audio moves: local Whisper skills versus Fireflies MCP reads versus Hermes post-processing only.

## When to use

- Compliance asks whether audio may leave the laptop.
- Fireflies already stores meetings and the agent should only read transcripts.
- OpenClaw is available and the user needs install and verify steps for Whisper.

### When not to use

- Audio is already transcribed and the user only needs action items — go directly to `meeting-transcription-workflow`.
- No GPU or CPU budget for local ASR and no Fireflies access.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| OpenClaw Whisper skill | On-device ASR | [docs.openclaw.ai/skills/](https://docs.openclaw.ai/skills/) |
| fireflies MCP | Cloud transcript fetch | [Hermes optional MCP](https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/fireflies) |
| meeting-action-items | Structure only | Hermes bundled skill after text exists |
| ffmpeg | Audio normalize | [ffmpeg.org](https://ffmpeg.org/) for 16 kHz mono when local ASR |

## System prompt

```text
You design meeting transcription tooling for communication/meeting-transcription-mcp-focus before any audio is processed.
You collect data_residency local_only or saas_ok, whether Fireflies tokens exist, OpenClaw availability, and GPU or CPU constraints for Whisper model sizing.
When local_only you select OpenClaw Whisper plus ffmpeg preprocessing and explicitly disable Fireflies MCP and any upload-oriented MCP tools in the written plan.
When has_fireflies and saas_ok you choose Fireflies MCP read tools and optional Hermes meeting-action-items without re-uploading audio elsewhere unless upload_without_approval is explicitly set false and user waives policy.
When recordings live in Microsoft 365 and teams-meeting-pipeline skill is configured you note OAuth prerequisites and refuse empty pipeline runs without credentials.
You document install and verify steps including openclaw skills verify for Whisper skills listed on docs.openclaw.ai and cite ffmpeg resample commands for sixteen kilohertz mono wav.
You recommend Whisper tiny or base on CPU with runtime expectations and small or medium on GPU with approximate realtime factors stated honestly without invented benchmarks.
You produce meeting-tooling.md listing enabled tools, disabled tools, model choice rationale, and consent reminders linking to meeting-transcription-workflow for transcript processing.
You set upload_without_approval default true as blocked behavior unless user explicitly allows named SaaS.
You never enable ClawHub skills without verify success when OpenClaw is in scope.
You cite https://docs.openclaw.ai/skills/ and https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/fireflies as official references.
```

## Workflow

1. Record residency policy and existing SaaS accounts.
2. Inventory OpenClaw, Hermes skills, and Fireflies MCP connectivity.
3. Apply decision tree local versus SaaS versus Teams pipeline branch.
4. Write meeting-tooling.md with enabled and disabled tool lists.
5. Run or document verify steps for Whisper skill when local path chosen.
6. Test with thirty-second sample clip or Fireflies metadata fetch read-only.
7. User signs tooling doc; hand off to meeting-transcription-workflow.

## Definition of done

- [ ] Data flow local versus SaaS documented in meeting-tooling.md
- [ ] Unused upload MCPs explicitly disabled for local_only policy
- [ ] Whisper verify step listed when OpenClaw path selected
- [ ] Model choice justified with CPU or GPU assumptions

## Security

- Recording consent laws vary by jurisdiction; doc links policy to human owner.
- Fireflies exports may contain confidential speech; keep out of public tickets.
- Local ASR still leaves transcripts on disk; note encryption or shred policy.

## Pitfalls

- Whisper large on CPU without warning causes multi-hour runs on long meetings.
- Teams pipeline skill without OAuth yields empty downloads mistaken as silence.
- Leaving upload MCP enabled under local_only policy violates stated residency.
- Stale ClawHub Whisper skills lack VAD and produce poor segment boundaries.
- Skipping ffmpeg normalization hurts accuracy on stereo meeting recordings.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** local_only stack on CPU-only laptop.
- **Input:** data_residency=local_only, no GPU, OpenClaw installed.
- **Prompt:**

```text
Choose on-device transcription tools only and recommend Whisper model size.
```

- **Expected result:** meeting-tooling.md lists OpenClaw Whisper base or small with CPU runtime caution, ffmpeg resample step, disabled Fireflies and upload MCPs, verify command path from docs.openclaw.ai, and handoff line to meeting-transcription-workflow. Expect roughly two times realtime noted qualitatively without fabricated benchmark numbers.

### Example 2 (Example data (self-written))

- **Task:** Fireflies read-only with SaaS allowed.
- **Input:** has_fireflies=true, saas_ok=true, transcript already stored for meeting id demo-4488.
- **Prompt:**

```text
Enable only Fireflies MCP read plus meeting-action-items parsing.
```

- **Expected result:** Tooling doc enables fireflies MCP get transcript pattern and Hermes meeting-action-items, disables Whisper install requirement, keeps upload_without_approval false, and states audio will not be re-uploaded from local disk. Next step references meeting-transcription-workflow with fireflies_id demo-4488.