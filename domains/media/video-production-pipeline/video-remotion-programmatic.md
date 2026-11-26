---
id: video-remotion-programmatic
title: "Datengetriebenes Video with Remotion"
domain: media
category: video-production-pipeline
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
    version_notes: "Remotion 4.x; Remotion Agent Skills from remotion-dev/skills"
  - name: Node.js
    install: "nodejs.org LTS or nvm"
    version_notes: ">= 18; Chromium-Bundle via Remotion"
  - name: ffmpeg
    install: "OS-Paket ffmpeg"
    version_notes: "Post-render checks and light post-editing"
inputs:
  - "Briefing (Targetgruppe, Laenge, Branding)"
  - "Datenquelle (JSON/CSV/API-Stub)"
  - "Composition spec (scenes, timing, resolution)"
outputs:
  - "Gerendertes MP4 (and optional GIF/Still)"
  - "Reproducibles Remotion-Projekt or PR-Diff"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

Agents execute **Briefing → React Composition → Render → QA** for repeatable, data-driven videos (KPI cards, changelogs, social clips) with **Remotion** instead of manual timeline work.

## When to use

- Content varies per run (numbers, names, tables), layout stays the same.
- CI/CD or Cron should monatliche Report-Videos create.
- Team beherrscht TypeScript/React or akzeptiert generierten Scaffold.

**When not to use**

- One-off cinematic montage cut with lots of B-roll and an intuitive timeline (NLE).
- Legally sensitive data must not leave the render worker or enter the cloud without a clear hosting boundary.
- Echtzeit-Livestream-Grafiken (OBS/NDI) without Remotion-Pipeline.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| Remotion + @remotion/cli | Composition, Preview, Render | Official Render-path, Headless Chromium |
| Remotion Agent Skills | Prompt-Patterns, Best Practices | Empfohlen statt veralteter MCP-pathe (Recherche 2026) |
| ffmpeg / ffprobe | Bitrate, Dauer, Thumbnail | Schnelle approval without Studio |
| git | Versionierung the Composition | Reproduzierbarkeit |

## System prompt

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

## Workflow

1. Record the briefing and JSON schema of the data rows; derive duration from `fps × frames`.
2. `npx create-video@latest` or bestehendes Repo; `npm install` and Remotion-Skills-README konsultieren.
3. Create composition `ReportVideo`; define props type in `src/types.ts`.
4. `npm run start` — Preview with Example-`inputProps` im Remotion Studio.
5. `npx remotion render ReportVideo deliver/report_2026-11.mp4 --props=@data/payload.json`.
6. `ffprobe deliver/report_2026-11.mp4`; Poster `npx remotion still ReportVideo poster.png --frame=30`.
7. Approval checklist with stakeholder; optional commit and tag.

## Definition of done

- [ ] Render without errors; resolution and fps match briefing
- [ ] all Datenzeilen from Props sichtbar and lesbar (no Overflow without approval)
- [ ] Render command and props file documented—reproduction without agent possible
- [ ] no unlizenzierten Fonts/Bilder im Bundle
- [ ] ffprobe-Dauer ±1 Frame against `durationInFrames`

## Security

- Do not write customer data in props to public issue trackers or cloud render logs.
- FFmpeg post-editing with watermark or upload only after approval.
- Dependencies: mention `npm audit` for new packages; no arbitrary postinstall scripts.

## Pitfalls

- `durationInFrames` to knapp—letzte Animation will abgeschnitten; immer `+fps` Puffer.
- Grosse Bilder without `width`/`height` in `<Img>` verursachen Layout-Shifts im Render.
- `--props` as a shell string breaks on quotation marks—prefer file `@payload.json`.
- Headless Chromium on servers without fonts—embed brand fonts in `public/`.
- Skills vs. MCP: Remotion-Skills nutzen; veraltete MCP-Doku kann falsche Tool-Namen liefern.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Monatliches Sales-Dashboard-Video from CSV.
- **Input:** `sales_nov.json` with `{ "month", "revenue_eur", "deals" }`, 1080×1920, 15 s.
- **Prompt:**

```text
Add Remotion composition SalesStory (1080x1920, 30fps, 450 frames). Animate revenue and deal count from sales_nov.json. Render to out/sales_nov.mp4.
```

- **Expected result:**

```json
{
  "render": "npx remotion render SalesStory out/sales_nov.mp4 --props=./sales_nov.json",
  "ffprobe": { "width": 1080, "height": 1920, "duration_sec": 15.0 }
}
```

### Example 2 (Example data (self-written))
- **Task:** Remotion-Skills as Referenz for Agent-Prompting statt Legacy-MCP.
- **Input:** Neues Repo, Skill-README of remotion-dev/skills.
- **Prompt:**

```text
Follow remotion-dev/skills for composition structure and render CLI. Document why skills are preferred over deprecated MCP paths in 2026.
```

- **Expected result:**

  The project lists at least one composition with `npx remotion compositions`; README link https://github.com/remotion-dev/skills in the agent log; render artifact locally under `out/`.