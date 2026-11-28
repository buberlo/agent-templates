---
id: weekly-sleep-workout-review-v1
title: "Weekly sleep and workout review from wearable exports"
domain: health-fitness
category: health-data-organization
tags:
  - sleep
  - workouts
  - wearables
  - health-data
  - privacy
target_agents:
  - hermes
  - grokbot
  - openclaw
  - claude-code
  - cursor
required_tools:
  - name: Python xml.etree.ElementTree
    install: "https://docs.python.org/3/library/xml.etree.elementtree.html"
    version_notes: "Stdlib parser; use iterparse for large Apple Health export.xml files."
  - name: Python csv
    install: "https://docs.python.org/3/library/csv.html"
    version_notes: "Stdlib reader for sleep tracker and Strava CSV exports."
  - name: Strava API or strava MCP
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/strava"
    version_notes: "Read scopes activity:read or activity:read_all; endpoint getLoggedInAthleteActivities."
  - name: filesystem MCP
    install: "https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem"
    version_notes: "Local read and write of exports and the weekly report."
inputs:
  - "Apple Health export.xml, sleep tracker CSV, or both for the requested week"
  - "Strava activities export or API access with activity:read scope"
  - "Week start and end dates, time zone, sleep target window"
  - "Two or three habit observations chosen by the user"
outputs:
  - "Weekly sleep table, workout table, and week-over-week delta table"
  - "Habit observations, data coverage notes, and a non-medical disclaimer"
  - "Redacted Markdown report kept on the local machine"
risk_level: medium
example_count: 2
version: "1.0.0"
updated: "2026-11-28"
---

## Purpose

Build a weekly review of sleep and workouts from exported wearable data, covering nightly sleep duration, bedtime consistency, workout count and duration, week-over-week deltas, and two or three habit observations the user selects. The report is informational and is not medical advice or a diagnosis. Health data is sensitive, so processing stays local and only aggregates leave the machine.

## When to use

- A weekly personal review of an Apple Health export.xml or a sleep tracker CSV.
- Checking sleep consistency and training load before adjusting a plan with a coach.
- Comparing a travel week or a high-stress week against a baseline week.
- Turning a Strava activity export into a short, readable weekly summary.

### When not to use

- Diagnosing insomnia, sleep apnea, depression, or any other medical condition.
- Replacing a clinician's review of symptoms, medication effects, or abnormal heart readings.
- Analyzing another person's health data without that person's consent.
- Producing claims about causes of poor sleep or missed training.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| Python xml.etree.ElementTree | Parse Apple Health export | iterparse keeps memory limited for large export.xml files |
| Python csv | Read sleep tracker and Strava exports | Repeatable column mapping with no external service |
| Strava API or strava MCP | Fetch activities | Read-only activity:read scope through getLoggedInAthleteActivities |
| filesystem MCP | Read and write local files | Keeps health exports and the report on the user's machine |

## System prompt

```text
You summarize one calendar week of exported sleep and workout data for health-fitness/health-data-organization without connecting to any live wearable account.
You parse large Apple Health export.xml files with xml.etree.ElementTree.iterparse and extract HKCategoryTypeIdentifierSleepAnalysis records with startDate and endDate before aggregating nightly duration.
You read sleep tracker CSV exports by mapping the user's timestamp, stage, and duration columns and you state any column that is missing.
You pull Strava activities through getLoggedInAthleteActivities using activity:read or activity:read_all and you report the granted scope in the summary header.
You compute sleep duration per night, bedtime consistency as the standard deviation of bedtime in minutes, and flag nights outside the user's stated target window.
You count workouts by type, total duration, and distance, then compare each metric with the prior week and show the delta as both an absolute value and a percent.
You include only the two or three habit observations the user selected, such as caffeine timing or evening screen time, and you mark each as an observation rather than a cause.
You state in the summary header that this is not medical advice and not a diagnosis, and you never infer a condition, disorder, or treatment from the data.
You treat mentions of chest pain, fainting, or severe shortness of breath as a red flag and you tell the user to contact a medical professional promptly.
You process health files locally, keep raw records out of shared documents, and aggregate values to weekly totals before any sharing step.
You redact names, device serial numbers, dates of birth, and location traces before writing the report file.
You present sleep and workout tables with units, week start date, and data coverage notes so the user can spot missing nights or days.
```

## Workflow

1. Confirm the week start and end dates, time zone, sleep target window, and the two or three habit observations with the user.
2. Export Apple Health data from the iPhone Health app via Summary > profile picture > Export All Health Data, or obtain the sleep tracker CSV and the Strava export.
3. Parse export.xml incrementally with iterparse, keep only sleep analysis records inside the date range, and discard unrelated record types early to limit memory.
4. Normalize sleep stages and timestamps into per-night rows with sleep start, wake time, and total asleep minutes.
5. Load Strava activities from the API or export and group them by sport type, count, duration, and distance.
6. Compute weekly totals, nightly averages, bedtime standard deviation, and week-over-week deltas against the prior week.
7. Add the user-selected habit observations as plain observations with the supporting numbers beside them.
8. Write the report with the non-medical disclaimer, red flags section, and data coverage notes, then remove raw personal identifiers.
9. Ask the user to confirm the aggregate numbers before sharing the report with a coach or clinician.

## Definition of done

- [ ] Report covers each night and each workout in the requested week with data coverage notes
- [ ] Non-medical disclaimer and red-flag guidance appear at the top of the report
- [ ] Raw identifiers removed and only weekly aggregates remain in shared files
- [ ] Week-over-week deltas show absolute and percent values against the prior week
- [ ] Habit observations are limited to the user-selected items and labeled as observations

## Security

- Health exports contain dates, device identifiers, and location traces; keep files on the user's machine and delete temporary copies after the report.
- Share only weekly aggregates with coaches or clinicians; do not send raw export.xml or full CSV rows.
- Encrypt the local report folder when the device is shared and avoid public LLM sessions for raw records.
- Revoke Strava tokens after the review and request the narrowest scope that covers the needed activities.
- Remove names, birth dates, and precise routes from any file that leaves the local folder.

## Pitfalls

- Overlapping sleep records from a watch and a phone double-count asleep minutes unless overlapping intervals are merged first.
- A large export.xml loaded with parse instead of iterparse can exhaust memory and crash the review.
- Time zone changes during travel shift bedtime calculations and create false inconsistency scores.
- With only activity:read, private Strava activities are omitted, so workout totals look lower than they are.
- Bedtime standard deviation misleads when naps or split sleep appear; report naps as separate rows.
- Treating one short night as a condition crosses from review into diagnosis.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Build a weekly sleep and workout review for a fictional user, Maya, for 2026-11-16 to 2026-11-22.
- **Input:** Apple Health export.xml (412 MB) and activities.csv; sleep target 23:00-07:00; habits: evening screen time and caffeine after 14:00.
- **Prompt:**

```text
Parse /data/health/export.xml with iterparse. Summarize sleep per night and workouts from /data/health/activities.csv for 2026-11-16..2026-11-22. Target window 23:00-07:00. Add habit notes for evening screen time and caffeine after 14:00. State that this is not medical advice.
```

- **Expected result:**

```text
Weekly review 2026-11-16 to 2026-11-22 (local time America/Chicago)
This report is not medical advice and not a diagnosis.

| Night | Asleep | Bedtime | Wake | Target |
| Mon 11-16 | 7h 12m | 23:18 | 06:40 | inside |
| Tue 11-17 | 6h 05m | 00:02 | 06:20 | late |
| Wed 11-18 | 7h 48m | 22:54 | 06:55 | inside |
| Thu 11-19 | 7h 02m | 23:11 | 06:30 | inside |
| Fri 11-20 | 6h 41m | 23:47 | 06:35 | late |
| Sat 11-21 | 7h 55m | 23:05 | 07:10 | inside |
| Sun 11-22 | 7h 24m | 22:58 | 06:50 | inside |

Sleep: 7 nights, mean 7h 10m, bedtime SD 34 min, 2 nights outside target.
Workouts: 4 activities, 3h 26m total; run 18.4 km, ride 42.1 km, strength 2 sessions.
Week-over-week: sleep +11 min, workout duration +18 min, run distance -2.1 km.
Habit notes: both late bedtimes (Tue, Fri) followed evenings with screen time past 22:30; caffeine after 14:00 on 2 days (Tue, Fri), and those nights averaged 6h 23m asleep vs 7h 28m on the other 5 nights. These are observations, not causes.
Red flags: none reported; contact a medical professional for chest pain, fainting, or severe shortness of breath.
Coverage: 1 night from phone only, 6 nights merged watch and phone; no duplicate minutes counted.
Files: report.md written to /data/health/reports; raw export kept local and not uploaded.
```

### Example 2 (Example data (self-written))

- **Task:** Compare a travel week with a baseline week for a fictional user, Leo, using a sleep tracker CSV and the Strava API.
- **Input:** sleep.csv with columns date, bedtime, wake, minutes_asleep; Strava scope activity:read; week 2026-11-09 to 2026-11-15; habits: late meals and daily steps.
- **Prompt:**

```text
Use /data/sleep/sleep.csv and Strava getLoggedInAthleteActivities with activity:read for 2026-11-09..2026-11-15. Compare with week 2026-11-02..2026-11-08. Habits: late meals and daily steps. State data gaps and no medical advice.
```

- **Expected result:**

```text
Weekly review 2026-11-09 to 2026-11-15 (local time Europe/Lisbon, travel from America/New_York)
This report is not medical advice and not a diagnosis.

| Metric | This week | Prior week | Delta |
| Nights with data | 5 of 7 | 7 of 7 | -2 |
| Mean asleep | 6h 22m | 7h 18m | -56 min |
| Bedtime SD | 52 min | 21 min | +31 min |
| Workouts | 2 | 5 | -3 |
| Workout duration | 1h 40m | 4h 05m | -2h 25m |

Sleep: 2 missing nights after the overnight flight; bedtime shifted +1h 40m after the time zone change.
Workouts: 1 run 6.2 km, 1 walk 4.8 km; Strava scope activity:read returned 2 public activities and may omit private ones.
Habit notes: late meals on 3 nights, mean asleep 6h 05m on those nights vs 6h 47m on the other 2 nights.
Data gaps: sleep.csv has no rows for 11-10 and 11-11; do not treat missing as zero.
Next step: re-authorize with the activity:read_all scope or add private activities manually before sharing with a coach.
Files: weekly-travel-review.md written; raw CSV kept local.
```

## Sources

- https://support.apple.com/guide/iphone/share-your-health-data-iph5ede58c3d/ios
- https://developers.strava.com/docs/reference/
- https://docs.python.org/3/library/xml.etree.elementtree.html
- https://docs.python.org/3/library/csv.html
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/strava
