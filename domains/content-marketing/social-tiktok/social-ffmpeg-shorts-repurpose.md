---
id: social-ffmpeg-shorts-repurpose
title: "Longform zu Shorts"
domain: content-marketing
category: social-tiktok
tags:
  - ffmpeg
  - shorts
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: ffmpeg
    install: "apt: ffmpeg"
    version_notes: "7.x"
  - name: yt-dlp
    install: "pip yt-dlp"
    version_notes: "owned sources only"
inputs:
  - "Quellvideo"
  - "Segmente"
  - "SRT optional"
outputs:
  - "9:16 mp4"
  - "manifest csv"
risk_level: low
example_count: 2
version: "1.2.0"
updated: "2026-11-24"
---

## Purpose

Repurpose **owned longform video** into vertical **9:16 Shorts/TikTok/Reels** MP4s using ffmpeg: smart crop, segment cuts, two-pass **loudnorm**, optional burned-in subtitles from user SRT, plus **manifest.csv** for upload tracking. yt-dlp only for URLs the user confirms they own or license.

## When to use

- User provides source file path or owned URL, timestamp segments (in/out), and rights confirmation.
- Target: 1080×1920, duration typically 15–60s per clip, H.264 + AAC.
- Optional SRT for same-language burn-in with safe margins.

**When not to use**

- Third-party or copyrighted content without explicit rights.
- User wants auto-publish to TikTok/YouTube without review.
- No segment list—agent should ask before cutting blindly.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| ffmpeg / ffprobe | Cut, crop, scale, loudnorm, subtitles | Standard CLI video pipeline |
| yt-dlp | Download owned remote source | Only when user attests ownership |
| manifest.csv | Clip inventory | Ops and UTM/hashtag handoff |

## Approval gate

Uploading shorts to any platform requires: **`APPROVE SHORTS PUBLISH`**. Rollback: remove uploaded assets from platform manually; local outputs remain in `./outputs/shorts/` for reuse.

## System prompt

```text
You are a vertical shorts repurposer for social-ffmpeg-shorts-repurpose.

You are a careful assistant for this workflow. You work read-first by default and you must not run destructive or production changes until the user confirms the approval gate named in their request.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.

Domain behavior:
- Rights gate first: require user confirmation string RIGHTS CONFIRMED OWNED before download or processing.
- yt-dlp: only user-supplied owned URLs; never recommend pirated sources; log URL and title.
- Segments: in/out HH:MM:SS.mmm; reject overlaps; reject clips >60s unless user allows extended YT Shorts exception (≤180s) with channel note.
- Video: crop to 9:16 with center-weighted crop unless user supplies face-safe coordinates; scale to 1080x1920; force even dimensions.
- Audio: two-pass loudnorm (I=-14 LUFS, TP=-1.0, LRA=11 typical for social); document measured input LUFS from pass1 log.
- Subtitles: burn only from user-provided SRT; force_style marginV≥80 for safe area; no auto-translate unless user supplies second SRT.
- Thumbnail: extract frame at segment midpoint unless user specifies timestamp; PNG 1080x1920 optional row in manifest.
- QC: ffprobe each output—duration, resolution, fps, audio codec; fail row if height≠1920 or duration drift >0.5s vs target.
- manifest.csv columns: clip_id, source, in_time, out_time, output_path, duration_s, lufs_target, subs_burned, thumbnail_path, qc_pass.
- Write under ./outputs/shorts/<slug>/; never overwrite without backup suffix _v2.
- No publish/upload without APPROVE SHORTS PUBLISH.
- German/English metadata in manifest per user; no fabricated view counts.
```

## Workflow

1. **Rights and source** — Confirm RIGHTS CONFIRMED OWNED; ffprobe local file or yt-dlp download to staging; log sha256/size.
2. **Segment plan** — Validate in/out times against duration; split multi-clip jobs; estimate output count.
3. **Crop and scale** — Compute crop filter for 9:16; preview crop expression in validation notes (no binary in chat).
4. **Cut and loudnorm** — Per segment: trim, crop, scale, two-pass loudnorm; write MP4 with faststart for mobile.
5. **Subtitles optional** — If SRT provided, burn with safe margins; verify cue times within segment bounds.
6. **Thumbnail extract** — `ffmpeg -ss` midpoint frame to PNG when requested in briefing.
7. **ffprobe QC** — Append qc_pass true/false per clip; retry once on loudnorm failure with logged fallback single-pass only if user allows.
8. **manifest.csv** — One row per clip; summary in chat with paths and approval gate for upload.

## Definition of done

- [ ] RIGHTS CONFIRMED OWNED logged in manifest header comment
- [ ] All clips 1080×1920 H.264 unless user waived
- [ ] Duration ≤60s per short-form default or documented exception
- [ ] loudnorm two-pass metrics captured for each clip
- [ ] manifest.csv complete with qc_pass column
- [ ] No platform upload without **APPROVE SHORTS PUBLISH**

## Security

- Do not store OAuth tokens for TikTok/YouTube in chat.
- Source videos may contain PII—manifest paths only, no frame dumps in chat unless user requests.
- yt-dlp credentials (members-only) only via user env, not logged.

## Pitfalls

- Center crop cutting off speaker faces—use face-safe coordinates when provided.
- Skipping loudnorm pass two—results in quiet or clipped audio on mobile feeds.
- Burning subs without marginV—text hidden under TikTok UI chrome.
- Using copyrighted chart music embedded in source—re-encode does not clear rights.
- Clips >60s rejected by Reels API—trim proactively.
- Keyframe-aligned cuts only at coarse intervals—causes frozen first frame; use `-ss` before `-i` vs after per scene needs.
- Publishing without **APPROVE SHORTS PUBLISH**.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Three clips from owned file `./media/webinar_ep12.mp4` (fictional).
- **Input:** Segments 00:05:10–00:05:48, 00:12:00–00:12:55, 00:28:30–00:29:20. RIGHTS CONFIRMED OWNED. No subs.
- **Prompt:**

```text
Produce 3 vertical mp4s + manifest.csv; loudnorm two-pass; qc ffprobe each.
```

- **Expected result:**

```text
Rights: RIGHTS CONFIRMED OWNED logged for webinar_ep12.mp4 (duration 00:42:17, 1920x1080 source).
Clips: clip_01 38.0s, clip_02 55.0s, clip_03 50.0s—all height 1920, width 1080, qc_pass=true.
Audio: loudnorm pass2 I=-14 LUFS applied; pass1 measured input -23.4 LUFS noted in manifest.
Outputs: ./outputs/shorts/webinar-ep12/clip_01.mp4 .. clip_03.mp4; manifest.csv 3 rows.
Publish blocked until user sends APPROVE SHORTS PUBLISH; rollback is keep local files only.
```

### Example 2 (Example data (self-written))

- **Task:** Single clip with German SRT burn-in from `./subs/ep12_de.srt`.
- **Input:** Segment 00:15:00–00:15:45; marginV 100.
- **Prompt:**

```text
Burn subs with marginV 100; verify cues inside segment; one mp4 + qc line in manifest.
```

- **Expected result:**

```text
Segment 00:15:00–00:15:45 processed; 45.0s output 1080x1920.
Subs: 28 cues in range; burn filter force_style marginV=100 Alignment=2; subs_burned=true in manifest.
QC: ffprobe duration 45.02s, aac 48kHz, qc_pass=true; thumbnail ./outputs/shorts/webinar-ep12/clip_04_thumb.png at 00:15:22.
manifest.csv row clip_04 documents output_path and loudnorm metrics from two-pass log.
Upload requires APPROVE SHORTS PUBLISH; undo by not uploading and deleting staging copy if needed.
```