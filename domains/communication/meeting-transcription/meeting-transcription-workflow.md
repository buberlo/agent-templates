---
id: meeting-transcription-workflow
title: "Meetings and transcription"
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
  - name: ClawHub / OpenClaw skill OpenAI Whisper (steipete)
    install: "https://clawhubtrends.com/leaderboard.html"
    version_notes: "303 GitHub stars"
  - name: Hermes skills meeting-action-items, teams-meeting-pipeline
    install: "https://hermes-agent.nousresearch.com/docs/reference/skills-catalog"
    version_notes: "Bundled."
  - name: fireflies MCP (Hermes catalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/fireflies"
    version_notes: "Nous-approved optional-mcps catalog entry (listing 2026-11-23)."
inputs:
  - "Audio/video or meeting URL/Fireflies ID"
  - "Language and recording consent"
outputs:
  - "Transcript"
  - "Action items with quotes"
  - "Email follow-up draft"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

**Transcribe** meetings, extract **decisions and action items** with quotes, and prepare **follow-up emails as drafts only**.

## When to use

- Existing recording (MP4/WAV) or Fireflies/Teams pipeline.
- Participants consented to recording.
- Whisper skill or Fireflies MCP available.

**When not to use**

- Secret or attorney-privileged conversations without ML approval.
- Live captions without later QA.
- Calendar note only, no audio source.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| Whisper (OpenClaw) | Local ASR | Offline, timestamped |
| meeting-action-items | Structuring | Hermes bundled |
| fireflies MCP | Cloud transcript | When already in Fireflies |

## System prompt

```text
You process meetings for communication/meeting-transcription.

Inputs: source (file path | fireflies_id | teams_recording_url), language, attendees list, consent_confirmed (must be true), output lang DE.

Pipeline:
1) If file: ffmpeg to 16kHz mono wav, whisper with timestamps.
2) If fireflies_id: fetch transcript via MCP; do not re-upload audio elsewhere without approval.
3) Extract: decisions[], action_items[]{owner, task, due, quote, t_start}, open_questions[].
4) Every decision must cite transcript quote <= 25 words or mark [uncited—review].
5) Draft follow-up email in user tone; never send.

Hallucination guard: if owner not in transcript, owner=UNASSIGNED.
Deliver: transcript.md, actions.md, email-draft.txt, low_confidence_segments if ASR.
```

## Workflow

1. Collect `consent_confirmed` from user; otherwise abort.
2. Choose source: file → `ffmpeg -i meet.mp4 -vn -ac 1 -ar 16000 audio.wav`.
3. `whisper audio.wav --model large-v3-turbo --language de --output_dir work/`.
4. Apply skill **meeting-action-items** to `work/*.txt`.
5. Spot-check three quotes against transcript for action items.
6. Write follow-up draft `email-draft.txt`.
7. Store package in `output/meeting-YYYY-MM-DD/`.

## Definition of done

- [ ] Transcript with timestamps
- [ ] Each action has quote or UNASSIGNED
- [ ] No email sent
- [ ] Recording consent documented

## Security

- Do not upload audio to unapproved clouds.
- Redact names in external summaries when policy requires.
- Fireflies token only in secret store.

## Pitfalls

- Hallucinated decisions without quotes.
- Wrong owner on similar voices.
- Poor ASR on multi-speaker without diarization.
- Expired Teams link → empty transcript.
- Wrong follow-up date from time zone mix-up.

## Basic examples

### Example 1 (Example data)

- **Task:** Weekly sync MP4.
- **Input:** `sync-2026-11-20.mp4`, DE, consent yes.
- **Prompt:**

```text
Transcribe, extract actions with quotes, draft follow-up email, do not send.
```

- **Expected result:**

```text
actions.md:
- @maria — API spec by Wed — "Maria, can you own the API spec by Wednesday?"
- @tom — QA checklist — UNASSIGNED [uncited—review]

email-draft.txt: Subject "Follow-up Sync 20.11." ...
```

### Example 2 (Example data)

- **Task:** No consent.
- **Input:** `consent_confirmed=false`.
- **Prompt:**

```text
Transcribe board call recording.
```

- **Expected result:**

```text
Abort: recording_consent_required.
No ffmpeg/whisper started.
```