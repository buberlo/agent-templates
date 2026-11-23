---
id: video-remotion-programmatic
domain: medien
title: "Datengetriebenes Video mit Remotion"
category: video-produktion-pipeline
tags:
  - remotion
  - react
  - programmatic-video
target_agents:
  - hermes
  - claude-code
  - cursor
  - generic-mcp-agents
required_tools:
  - name: Remotion
    install: "npm: create-video / remotion in bestehendem Node-Projekt"
    version_notes: "Remotion 4.x; Remotion Agent Skills aus remotion-dev/skills"
  - name: Node.js
    install: "nodejs.org LTS oder nvm"
    version_notes: ">= 18; Chromium-Bundle via Remotion"
  - name: ffmpeg
    install: "OS-Paket ffmpeg"
    version_notes: "Post-Render-Checks und leichte Nachbearbeitung"
inputs:
  - "Briefing (Zielgruppe, Länge, Branding)"
  - "Datenquelle (JSON/CSV/API-Stub)"
  - "Komposition-Spec (Szenen, Timing, Auflösung)"
outputs:
  - "Gerendertes MP4 (und optional GIF/Still)"
  - "Reproduzierbares Remotion-Projekt oder PR-Diff"
risk_level: medium
version: "1.1.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

Agenten führen **Briefing → React-Komposition → Render → QA** für wiederholbare, datengetriebene Videos (KPI-Karten, Changelogs, Social-Clips) mit **Remotion** statt manueller Timeline-Arbeit.

## Wann nutzen

- Inhalt variiert pro Lauf (Zahlen, Namen, Tabellen), Layout bleibt gleich.
- CI/CD oder Cron soll monatliche Report-Videos erzeugen.
- Team beherrscht TypeScript/React oder akzeptiert generierten Scaffold.

**Wann nicht**

- Einmaliger Kinomontage-Schnitt mit viel B-Roll und intuitiver Timeline (NLE).
- Rechtlich sensible Daten dürfen den Render-Worker oder Cloud nicht verlassen—ohne klare Hosting-Grenze.
- Echtzeit-Livestream-Grafiken (OBS/NDI) ohne Remotion-Pipeline.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Remotion + @remotion/cli | Komposition, Preview, Render | Offizieller Render-Pfad, Headless Chromium |
| Remotion Agent Skills | Prompt-Patterns, Best Practices | Empfohlen statt veralteter MCP-Pfade (Recherche 2026) |
| ffmpeg / ffprobe | Bitrate, Dauer, Thumbnail | Schnelle Abnahme ohne Studio |
| git | Versionierung der Composition | Reproduzierbarkeit |

## System-Prompt / Instruktionen

```text
You build and render Remotion videos in an existing or new Remotion project (TypeScript/React).

Inputs: creative brief, target resolution/fps/duration, data payload (JSON/CSV), brand tokens (fonts, colors—paths or CSS variables), output filename.

Setup:
- If no project: npx create-video@latest with appropriate template; pin remotion version in package.json.
- Define Composition in Root.tsx with explicit width, height, fps, durationInFrames.

Implementation rules:
- All timing via useCurrentFrame() and interpolate(); avoid setState for animation.
- Load data via getInputProps() or staticFile() for assets; never hardcode secrets in props.
- Use <Series>, <Sequence>, and premount patterns for scene changes per Remotion skills.

Preview before render: npm run start OR npx remotion preview; confirm one representative data row.

Render: npx remotion render <CompositionId> out.mp4 --props='{"rows":[...]}' (escape JSON safely).
Log stdout; on failure capture stack trace and last frame.

Post-render: ffprobe duration and resolution; extract poster frame at 1s.

Deliver: path to mp4, git diff summary, render command, and props schema for the next run.

Do not deploy to cloud render farms or upload outputs without user approval.
Stock assets and fonts: only use files the user provided or licenses they confirmed.
```

## Arbeitsablauf

1. Briefing und JSON-Schema der Datenzeilen festhalten; Dauer aus `fps × frames` ableiten.
2. `npx create-video@latest` oder bestehendes Repo; `npm install` und Remotion-Skills-README konsultieren.
3. Komposition `ReportVideo` anlegen; Props-Typ in `src/types.ts` definieren.
4. `npm run start` — Preview mit Beispiel-`inputProps` im Remotion Studio.
5. `npx remotion render ReportVideo deliver/report_2026-11.mp4 --props=@data/payload.json`.
6. `ffprobe deliver/report_2026-11.mp4`; Poster `npx remotion still ReportVideo poster.png --frame=30`.
7. Abnahme-Checkliste mit Stakeholder; optional Commit und Tag.

## Qualitätskriterien / Definition of Done

- [ ] Render ohne Fehler; Auflösung und fps entsprechen Briefing
- [ ] Alle Datenzeilen aus Props sichtbar und lesbar (kein Overflow ohne Freigabe)
- [ ] Render-Befehl und Props-Datei dokumentiert—Wiederholung ohne Agent möglich
- [ ] Keine unlizenzierten Fonts/Bilder im Bundle
- [ ] ffprobe-Dauer ±1 Frame gegen `durationInFrames`

## Sicherheit & Freigaben

- Kundendaten in Props nicht in öffentliche Issue-Tracker oder Cloud-Render-Logs schreiben.
- FFmpeg-Nachbearbeitung mit Wasserzeichen oder Upload nur nach Freigabe.
- Dependencies: `npm audit` bei neuen Paketen erwähnen; keine willkürlichen Postinstall-Skripte.

## Fallstricke

- `durationInFrames` zu knapp—letzte Animation wird abgeschnitten; immer `+fps` Puffer.
- Große Bilder ohne `width`/`height` in `<Img>` verursachen Layout-Shifts im Render.
- `--props` als Shell-String bricht bei Anführungszeichen—Datei `@payload.json` bevorzugen.
- Chromium-Headless auf Servern ohne Fonts—Brand-Fonts in `public/` einbinden.
- Skills vs. MCP: Remotion-Skills nutzen; veraltete MCP-Doku kann falsche Tool-Namen liefern.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Monatliches Sales-Dashboard-Video aus CSV.
- **Input:** `sales_nov.json` mit `{ "month", "revenue_eur", "deals" }`, 1080×1920, 15 s.
- **Prompt:**

```text
Add Remotion composition SalesStory (1080x1920, 30fps, 450 frames). Animate revenue and deal count from sales_nov.json. Render to out/sales_nov.mp4.
```

- **Erwartetes Ergebnis:**

```json
{
  "render": "npx remotion render SalesStory out/sales_nov.mp4 --props=./sales_nov.json",
  "ffprobe": { "width": 1080, "height": 1920, "duration_sec": 15.0 }
}
```

### Beispiel 2 (Praxisbeispiel)

- **Aufgabe:** Remotion-Skills als Referenz für Agent-Prompting statt Legacy-MCP.
- **Input:** Neues Repo, Skill-README von remotion-dev/skills.
- **Prompt:**

```text
Follow remotion-dev/skills for composition structure and render CLI. Document why skills are preferred over deprecated MCP paths in 2026.
```

- **Erwartetes Ergebnis:**

  Projekt mit `npx remotion compositions` listet mindestens eine Composition; README-Link https://github.com/remotion-dev/skills im Agent-Protokoll; Render-Artefakt lokal unter `out/`.