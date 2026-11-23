---
id: meetings-transkription-workflow
title: "Meetings und Transkription"
domain: kommunikation
category: meetings-transkription
tags:
  - meetings
  - kommunikation
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
  - name: fireflies MCP (Hermes-Katalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/fireflies"
    version_notes: "Nous-approved optional-mcps-Katalogeintrag (Listing 23.11.2026)."
inputs:
  - "Audio/Video oder Meeting-URL/Fireflies-ID"
  - "Sprache und Aufzeichnungsfreigabe"
outputs:
  - "Transkript"
  - "Action-Items mit Zitaten"
  - "E-Mail-Follow-up-Entwurf"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

Meeting **transkribieren**, **Entscheidungen und Action Items** mit Zitaten extrahieren und **Follow-up-Mails nur als Entwurf** vorbereiten.

## Wann nutzen

- Vorhandene Aufnahme (MP4/WAV) oder Fireflies/Teams-Pipeline.
- Teilnehmer haben Aufzeichnung zugestimmt.
- Whisper-Skill oder Fireflies MCP verfügbar.

**Wann nicht**

- Geheime / anwaltlich geschützte Gespräche ohne ML-Freigabe.
- Live-Untertitel ohne spätere QA.
- Nur Kalender-Notiz ohne Audioquelle.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Whisper (OpenClaw) | Lokale ASR | Offline, timestampt |
| meeting-action-items | Strukturierung | Hermes bundled |
| fireflies MCP | Cloud-Transkript | Wenn schon in Fireflies |

## System-Prompt / Instruktionen

```text
You process meetings for kommunikation/meetings-transkription.

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

## Arbeitsablauf

1. `consent_confirmed` vom Nutzer einholen; sonst abbrechen.
2. Quelle wählen: Datei → `ffmpeg -i meet.mp4 -vn -ac 1 -ar 16000 audio.wav`.
3. `whisper audio.wav --model large-v3-turbo --language de --output_dir work/`.
4. Skill **meeting-action-items** auf `work/*.txt` anwenden.
5. Action-Items gegen Transkript stichproben (3 Zitate).
6. Follow-up-Entwurf `email-draft.txt` schreiben.
7. Paket in `output/meeting-YYYY-MM-DD/` ablegen.

## Qualitätskriterien / Definition of Done

- [ ] Transkript mit Zeitstempeln
- [ ] Jede Action mit Zitat oder UNASSIGNED
- [ ] Keine gesendete E-Mail
- [ ] Aufzeichnungsfreigabe dokumentiert

## Sicherheit & Freigaben

- Audio nicht in nicht freigegebene Clouds hochladen.
- Namen in externen Summaries reduzieren wenn policy verlangt.
- Fireflies-Token nur im Secret Store.

## Fallstricke

- Halluzinierte Beschlüsse ohne Zitat.
- Falsche Owner-Zuweisung bei ähnlichen Stimmen.
- Schlechte ASR bei Mehrsprecher ohne Diarisierung.
- Teams-Link abgelaufen → leeres Transkript.
- Follow-up mit falschem Datum aus Zeitzonenmischung.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Wöchentliches Sync-MP4.
- **Input:** `sync-2026-11-20.mp4`, DE, consent yes.
- **Prompt:**

```text
Transcribe, extract actions with quotes, draft follow-up email, do not send.
```

- **Erwartetes Ergebnis:**

```text
actions.md:
- @maria — API spec by Wed — "Maria, can you own the API spec by Wednesday?"
- @tom — QA checklist — UNASSIGNED [uncited—review]

email-draft.txt: Subject "Follow-up Sync 20.11." ...
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Ohne Einwilligung.
- **Input:** `consent_confirmed=false`.
- **Prompt:**

```text
Transcribe board call recording.
```

- **Erwartetes Ergebnis:**

```text
Abbruch: recording_consent_required.
Kein ffmpeg/whisper gestartet.
```