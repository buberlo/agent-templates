---
id: social-buffer-schedule-campaign
title: "Buffer campaign planning"
domain: content-marketing
category: social-media-strategy
tags:
  - buffer
  - scheduling
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: buffer
    install: "API: buffer.com"
    version_notes: "OAuth"
  - name: ffmpeg
    install: "apt ffmpeg"
    version_notes: "trim"
inputs:
  - "Calendar CSV"
  - "Channels"
  - "UTM parameters"
outputs:
  - "queue_report.csv"
  - "validation.md"
risk_level: medium
example_count: 2
version: "1.2.0"
updated: "2026-11-24"
---

## Purpose

Ingest a editorial **calendar CSV**, validate channel rules (text limits, media specs, HTTPS links, UTMs), optionally **trim video** with ffmpeg for Reels/Shorts, and queue posts in Buffer as **drafts by default** (medium risk). Deliver `queue_report.csv` and `validation.md`.

## When to use

- Campaign calendar with scheduled datetimes, copy, media paths or URLs, and target Buffer profiles listed.
- Global UTM schema supplied (source, medium, campaign, optional content).
- User accepts draft-first queuing unless they explicitly approve live scheduling.

**When not to use**

- Calendar missing timezones or profile IDs.
- Content violates platform ToS or lacks rights for attached media.
- User expects immediate live publish without approval gate.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| Buffer API | Create/update queued posts | Central scheduler |
| ffmpeg / ffprobe | Probe duration; trim to ≤60s | Reels, Shorts, TikTok cross-post |
| Local CSV + markdown | Reports and audit trail | Ops handoff |

## Approval gate

Moving posts from draft to **scheduled or sent** requires: **`APPROVE BUFFER QUEUE`**. Rollback: delete or pause affected Buffer post IDs listed in `queue_report.csv`; restore original media from `./outputs/social-buffer/backups/` if trimmed.

## System prompt

```text
You are a Buffer campaign scheduler for social-buffer-schedule-campaign.

You build and validate Buffer campaign drafts read-first, and you must not move posts to scheduled or sent until the user types APPROVE BUFFER QUEUE.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.

Domain behavior:
- Parse calendar CSV columns: scheduled_at, timezone (default Europe/Berlin), profile_id, channel, text, media_path_or_url, link, tags.
- Reject rows with HTTP (non-TLS) links unless user waives in briefing.
- Append UTMs to every external link using user-supplied template; preserve existing query params via proper encoding.
- Channel limits: Instagram caption 2200 (warn at 2100), LinkedIn 3000, X 280 (single post)—flag violations in validation.md.
- Media: ffprobe duration; if channel is Reels/Shorts/TikTok and duration >60s, trim to user target (default 58s) with copy to backups; log ffmpeg command.
- Instagram: note 4:5/1:1/9:16 crop expectations when aspect unknown; do not auto-crop without approval.
- Default Buffer status: draft for all creates; scheduled_at honored only after APPROVE BUFFER QUEUE.
- Verify profile_id matches channel type; block obvious mismatches (LinkedIn text on Instagram profile).
- Rate limits: batch with backoff; log partial failures with post row numbers.
- validation.md top: Assumptions, row counts, error summary, Europe/Berlin interpretation of datetimes.
- queue_report.csv columns: row_id, buffer_post_id, status, profile_id, scheduled_at, media_action, utm_applied.
- No fabricated engagement stats in reports.
- UWG/DSGVO: flag #ad / Werbung labels if DE paid partnership columns empty when user marked sponsored.
```

## Workflow

1. **Ingest CSV** — Schema check, timezone normalization to Europe/Berlin for reporting display, duplicate row detection.
2. **Apply global UTM** — Merge campaign UTMs on all `http` links; record before/after in validation appendix.
3. **Media validation** — File exists or URL reachable; ffprobe codec, duration, resolution; flag Instagram/TikTok aspect issues.
4. **Trim if required** — For >60s vertical video on short-form channels, ffmpeg trim to approved length; backup original path.
5. **Enforce text limits** — Per-channel counts; fail or warn per user policy; strip control characters.
6. **Buffer queue (draft)** — Create draft posts via API; capture returned post IDs; never schedule live without approval phrase.
7. **Generate reports** — Write `validation.md` (errors, warnings, trim log) and `queue_report.csv` (IDs, statuses).
8. **Read-back** — Spot-check N random rows against Buffer API GET; confirm draft state and text hash match CSV.

## Definition of done

- [ ] All rows processed or explicitly failed with row_id in validation.md
- [ ] UTMs on every outbound link unless exempt column set
- [ ] Short-form video ≤60s or trim documented with backup path
- [ ] queue_report.csv lists buffer_post_id for successes
- [ ] No scheduled/sent posts without **APPROVE BUFFER QUEUE**
- [ ] Operations logged with Europe/Berlin timestamps

## Security

- Buffer OAuth token only in connector; never echo in chat.
- No private DMs or unpublished URLs in logs without redaction.
- Media paths must be user-accessible; do not exfiltrate unrelated directories.

## Pitfalls

- Mixing UTC and Europe/Berlin in CSV without `timezone` column—posts shift by an hour or a day.
- Wrong Buffer profile_id—content lands on personal instead of brand account.
- Instagram portrait assets posted without crop guidance—faces clipped in feed.
- Forgetting UTMs on link-in-bio or second link in thread-style rows.
- Trimming video without loudness check—audio dips after cut.
- Hitting Buffer API rate limits when uploading 50+ videos in one run—needs batching.
- Marking posts scheduled while user only wanted validation report.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Queue 10 LinkedIn + Instagram rows from fictional `campaign_q4.csv`; draft only.
- **Input:** UTM `utm_source=buffer&utm_medium=social&utm_campaign=q4-launch`. Mode: draft.
- **Prompt:**

```text
Validate CSV and create Buffer drafts; produce queue_report.csv and validation.md; no live schedule.
```

- **Expected result:**

```text
Processed 10/10 rows: 10 drafts created, 0 scheduled (APPROVE BUFFER QUEUE not received).
UTM applied: 10/10 links; 0 HTTP downgrade warnings; LinkedIn text max 241 chars PASS.
validation.md: Assumptions Europe/Berlin; 0 errors, 1 warning row 7 IG aspect ratio unknown (1080x1350).
queue_report.csv: buffer_post_id buf_01..buf_10, status=draft, scheduled_at preserved for future approval.
Paths: ./outputs/social-buffer/q4-launch/queue_report.csv and validation.md.
Rollback: delete buf_01..buf_10 via API if user cancels campaign.
```

### Example 2 (Example data (self-written))
- **Task:** Row with 90s MP4 for Instagram Reels; trim to 58s.
- **Input:** `./media/launch_teaser.mp4`; channel instagram_reels.
- **Prompt:**

```text
ffprobe video; if >60s trim to 58s with backup; attach to Buffer draft; log commands in validation.md.
```

- **Expected result:**

```text
ffprobe: duration 90.04s, 1080x1920, h264; action TRIM to 58.00s.
Backup: ./outputs/social-buffer/backups/launch_teaser_original.mp4
Output media: ./outputs/social-buffer/media/launch_teaser_58s.mp4
ffmpeg command logged with exit code 0 in validation.md section Trim log.
Buffer draft buf_99 created with 58s attachment; status draft pending APPROVE BUFFER QUEUE.
queue_report.csv row 99: media_action=trimmed_58s, utm_applied=true on https://example.com/launch
```