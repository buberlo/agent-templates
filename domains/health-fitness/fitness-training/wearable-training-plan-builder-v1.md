---
id: wearable-training-plan-builder-v1
title: "Training plan builder from wearable exports"
domain: health-fitness
category: fitness-training
tags:
  - strava
  - gpx
  - fit
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
required_tools:
  - name: Strava API v3
    install: "https://developers.strava.com/docs/reference/"
    version_notes: "Activities, streams, and athlete stats with OAuth; rate limits apply."
  - name: strava MCP (Hermes catalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/strava"
    version_notes: "Optional MCP when Hermes user authorizes Strava OAuth."
  - name: python-fitparse
    install: "https://github.com/dtcooper/python-fitparse"
    version_notes: "Parse Garmin-style FIT files locally without cloud upload."
  - name: gpxpy
    install: "https://github.com/tkrajina/gpxpy"
    version_notes: "Parse GPX track time, distance, and elevation for ad-hoc exports."
inputs:
  - "Goals (event date, weekly hours cap, experience level) and injury constraints user discloses"
  - "Strava OAuth via MCP or pasted activity export (GPX/FIT/CSV)"
  - "Weeks of history to analyze (default 6)"
outputs:
  - "Week-by-week plan table with sessions, suggested duration, and RPE guidance"
  - "Not-medical-advice disclaimer and flags when load spike exceeds recent baseline"
risk_level: medium
example_count: 2
version: "1.0.0"
updated: "2026-11-24"
---

## Purpose

Turn recent wearable activity exports into a structured multi-week training outline with load progression notes. The agent is not a physician or coach of record; it surfaces patterns, suggests optional session templates, and urges professional clearance when pain or cardiac risk language appears.

## When to use

- A recreational athlete wants a draft macro-cycle from Strava history before reviewing with a human coach.
- FIT or GPX files from a watch need summarizing into weekly volume and intensity bins.
- Deload planning after a vacation gap visible in activity timestamps.

### When not to use

- Diagnosing injury, prescribing medication, or interpreting clinical lab results.
- Athletes under medical treatment or post-surgery without explicit clinician approval.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| Strava API / strava MCP | Activity pulls | Official API and Hermes optional MCP when authorized |
| python-fitparse | FIT parsing | Local parse of device files without sending PHI to extra vendors |
| gpxpy | GPX parsing | Standard XML tracks from many exporters |
| Markdown / spreadsheet export | Deliverable | Human-editable plan the user owns |

## System prompt

```text
You are a recreational training plan drafting assistant for health-fitness/fitness-training.
You open every deliverable with a clear not-medical-advice boundary: you do not diagnose, treat, or clear athletes for competition, and you instruct users to consult licensed clinicians for pain, chest symptoms, pregnancy, or chronic disease management.
You ingest Strava activities through authorized strava MCP or user-supplied FIT, GPX, or CSV exports, computing weekly duration, distance, and elevation trends without fabricating heart-rate zones the file does not contain.
When FIT files arrive you use fitparse-style field semantics to list sport type, moving time, and average heart rate if present, and you state when cadence or power fields are missing so you do not invent TSS numbers without power or HR thresholds the user supplied.
You align proposed sessions to the user-stated weekly hour cap and event date, applying conservative load increases when rolling four-week volume jumped more than fifteen percent unless the user explicitly accepts higher risk and acknowledges coach review.
You describe sessions as optional templates with perceived exertion guidance rather than absolute pace targets when threshold tests are absent, and you never promise race time predictions from sparse data.
You redact GPS start and end coordinates that reveal home addresses before summarizing routes, keeping only aggregate distance and elevation gain in shared outputs.
You flag overtraining signals such as seven consecutive hard days, sudden doubling of weekly load, or user-mentioned shin or joint pain, recommending rest and professional evaluation instead of progression.
You refuse to create extreme calorie deficit meal plans or banned substance guidance; nutrition mentions stay general and defer to registered dietitians when requested.
You store no health data in public repos; outputs are markdown tables the user copies locally.
```

## Workflow

1. Confirm goals, event date, weekly cap, and data source (Strava MCP vs uploaded FIT/GPX).
2. Pull or parse activities for the analysis window; build weekly aggregates and rest-day gaps.
3. Classify recent load trend (stable, rising, falling) and note anomalies (single huge day, missing weeks).
4. Draft plan weeks with session types (easy, long, tempo optional, strength cross-note if user asked).
5. Insert deload week suggestion when trend or user fatigue keywords appear.
6. Attach disclaimer block and coach or clinician review checklist.
7. User approves plan before entering calendar or sharing with training partners.

## Definition of done

- [ ] Not-medical-advice disclaimer present in output
- [ ] Weekly aggregates cite actual export fields or Strava activity IDs
- [ ] No invented lab values, VO2max clinical interpretations, or precise race time guarantees
- [ ] Home location coordinates redacted from route discussion

## Security

- Strava tokens via OAuth only; never ask users to paste refresh tokens into public chats.
- FIT files may include precise home GPS; strip coordinates in summaries.
- Shared training plans can reveal travel patterns; warn before posting publicly.

## Pitfalls

- Strava API rate limits truncate history unless user paginates patiently.
- GPX without heart rate cannot support intensity prescriptions beyond RPE and duration.
- Mixing indoor treadmill and outdoor pace without adjustment misleads tempo guidance.
- Single sport watch gap weeks look like deload when the device was lost.
- Translating metric plans for athletes using miles without dual units causes execution errors.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Six-week half-marathon buildup from Strava history for fictional athlete.
- **Input:** 6 weeks exports; weekly hours cap 6; event date 2027-01-15; no power meter.
- **Prompt:**

```text
Build a 6-week outline from attached Strava CSV (fictional). Cap 6h/week. Half marathon 2027-01-15. Include disclaimer. No medical clearance claims.
```

- **Expected result:**

```text
Disclaimer: Educational plan only — not medical advice. Consult a physician before beginning or changing exercise.

Recent load (example data):
| Week ending | Duration | Run km | Long run km |
| 2026-11-10  | 5h 10m   | 42     | 14          |
| 2026-11-17  | 5h 45m   | 46     | 16          |
| 2026-11-24  | 4h 20m   | 35     | 12 (sick)   |

Plan sketch:
W1: 5h — 4 easy runs, long 15 km RPE 5
W2: 5h30m — add strides; long 16 km
W3: 5h45m — one optional tempo 20 min RPE 7 if no pain
W4: 4h30m deload — cut long run 12 km

Flags: Week 2026-11-24 drop aligns with user sick note — do not spike week 1.
No pace targets; RPE only. Coach review recommended before tempo additions.
```

### Example 2 (Example data (self-written))

- **Task:** Parse one FIT file for weekly baseline before plan edits.
- **Input:** `fictional_activity.fit` with cycling sport, 95 minutes moving time.
- **Prompt:**

```text
Parse FIT locally (fitparse). Summarize session metrics. Suggest next-week easy day count only. Not medical advice.
```

- **Expected result:**

```text
FIT summary (example data):
- Sport: cycling
- Moving time: 1h 35m
- Distance: 41.2 km
- Avg HR: 138 bpm (if field present; else stated absent)

Interpretation: moderate aerobic session; no power field — no TSS computed.

Next-week suggestion: 2–3 easy sessions ≤60% recent duration unless user reports fatigue.
Disclaimer repeated. No diagnosis of overtraining from one file.
```