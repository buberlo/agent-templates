---
id: animation-motion-workflow
title: "Motion Graphics with Remotion and Hermes-Creative"
domain: media
category: animation-motion
tags:
  - remotion
  - manim
  - motion
target_agents:
  - hermes
  - claude-code
  - cursor
required_tools:
  - name: Remotion Agent Skills
    install: "https://github.com/remotion-dev/skills"
    version_notes: "React-basierte Videos"
  - name: Hermes-Skills manim-video
    install: "Bundled creative/manim"
    version_notes: "Mathe/Explain-Animationen"
  - name: Hermes-Skills p5js
    install: "Bundled creative/p5js"
    version_notes: "Interaktive Sketches as Video"
inputs:
  - "Storyboard or Skript"
  - "Technikwahl (Remotion vs. Manim vs. p5)"
  - "Dauer and Aufloesung"
outputs:
  - "Gerendertes MP4 or GIF"
  - "Quellcode im Repo"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

**Programmatische Motion** of the Idee zum Render: Remotion for UI-/Daten-Motion, **Manim** for Erklaer-Mathe, **p5.js** for generative Kurzloops—Skills nutzen, Output immer ansehen.

## When to use

- Animation should versioniert (Git) and parametrisierbar sein.
- Recurring explainer videos or social motion from templates.
- Hermes bundled creative-Skills verfuegbar.

**When not to use**

- Handgezeichnete Character-Animation Frame-for-Frame.
- After-Effects-Projekt with bestehenden AEP-Assets without Portierung.
- Echtzeit-Interactive without Render-step.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| Remotion | React-Composition | Produktion, Skills-Oekosystem |
| Manim CE | Vektor-Erklaerung | Formeln, Graphen |
| p5.js | Generativ | Kurze Loops, noise fields |
| ffmpeg | Nachediting | GIF, Kompression |

## System prompt

```text
You create programmatic motion videos by picking the right engine before coding.

You are a careful assistant for this workflow. You work read-first by default and you must not run destructive or production changes until the user confirms the approval gate named in their request.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.


Inputs: script/storyboard, resolution, fps, duration, brand colors/fonts, engine hint (remotion|manim|p5|auto).
Auto choice:
- UI mockups, KPI counters, text-heavy corporate → Remotion.
- Equations, graphs, geometric proofs → Manim (Community Edition).
- Abstract generative loops, particle fields → p5.js record via ccapture or frame export.
Remotion: follow remotion-dev/skills; compose with Series/Sequence; render via npx remotion render.
Manim: scene per file; manim -pqh scene.py SceneName; respect safe margins for text.
p5: fixed randomSeed for reproducibility; export frames then ffmpeg -framerate 30 -i frame_%04d.png out.mp4.
Always preview low resolution before final render to save time.
Store source in repo; attach render command and dependency versions.
ffmpeg post: only if user needs gif (-vf fps=15,palettegen) or lighter mp4.
No stock audio without license. Get approval before publishing.
Match frame rate to delivery platform (30 vs 60) before final render.
Export a contact sheet still every 5s for stakeholder async review.
Pin dependency versions in README after first successful render.
If text animates, verify contrast ratio against background for accessibility.```

## Workflow

1. Storyboard in 3–7 Shots; Dauer pro Shot festlegen.
2. Engine waehlen and Skill-README oeffnen.
3. Scaffold (Remotion project / manim Scene / p5 sketch).
4. Low-res Preview (480p or -ql).
5. Final render volle Aufloesung.
6. `ffprobe` and Stichprobe im Player.
7. Commit with README: Render-Befehl.

## Definition of done

- [ ] Render without Fehler; Dauer ±1 Frame
- [ ] Text lesbar on Targetgeraet (min font size checked)
- [ ] Quellcode and Befehl dokumentiert
- [ ] Random seeds fixiert wo required
- [ ] no unlizenzierte Musik

## Security

- Manim/p5 in Sandbox at untrusted Dependencies.
- Publish on Social only after approval.

## Pitfalls

- Manim-LaTeX fehlt on Server → Build fail; Dependencies vorab.
- p5 without `randomSeed` → not reproduzierbar.
- Remotion `durationInFrames` to kurz.
- GIF from voller HD without Palette → 50 MB Monster.
- Skills veraltet vs. Remotion Major Version—Version pinnen.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** 10 s KPI-Counter in Remotion.
- **Input:** Start 0, End 1200000 EUR, 1080p30.
- **Prompt:**

```text
Remotion composition KpiCount 300 frames, animate number with easing, render out/kpi.mp4.
```

- **Expected result:**

```bash
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.npx remotion render KpiCount out/kpi.mp4
Duration: 10.00s, 1920x1080
```

### Example 2 (Example data (self-written))
- **Task:** Sinuskurve erclarify with Manim.
- **Input:** 45 s, 1080p.
- **Prompt:**

```text
Single Manim scene PlotSine, voiceover placeholder text on screen only, render -pqh.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.manim -pqh plot_sine.py PlotSine → media/videos/plot_sine/1080p60/PlotSine.mp4
```