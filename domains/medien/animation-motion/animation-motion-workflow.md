---
id: animation-motion-workflow
domain: medien
title: "Motion Graphics mit Remotion und Hermes-Creative"
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
    version_notes: "Interaktive Sketches als Video"
inputs:
  - "Storyboard oder Skript"
  - "Technikwahl (Remotion vs. Manim vs. p5)"
  - "Dauer und Auflösung"
outputs:
  - "Gerendertes MP4 oder GIF"
  - "Quellcode im Repo"
risk_level: medium
version: "1.1.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

**Programmatische Motion** von der Idee zum Render: Remotion für UI-/Daten-Motion, **Manim** für Erklär-Mathe, **p5.js** für generative Kurzloops—Skills nutzen, Output immer ansehen.

## Wann nutzen

- Animation soll versioniert (Git) und parametrisierbar sein.
- Wiederkehrende Erklärvideos oder Social-Motion aus Templates.
- Hermes bundled creative-Skills verfügbar.

**Wann nicht**

- Handgezeichnete Character-Animation Frame-für-Frame.
- After-Effects-Projekt mit bestehenden AEP-Assets ohne Portierung.
- Echtzeit-Interactive ohne Render-Schritt.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Remotion | React-Composition | Produktion, Skills-Ökosystem |
| Manim CE | Vektor-Erklärung | Formeln, Graphen |
| p5.js | Generativ | Kurze Loops, noise fields |
| ffmpeg | Nachbearbeitung | GIF, Kompression |

## System-Prompt / Instruktionen

```text
You create programmatic motion videos by picking the right engine before coding.

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
If text animates, verify contrast ratio against background for accessibility.
```

## Arbeitsablauf

1. Storyboard in 3–7 Shots; Dauer pro Shot festlegen.
2. Engine wählen und Skill-README öffnen.
3. Scaffold (Remotion project / manim Scene / p5 sketch).
4. Low-res Preview (480p oder -ql).
5. Final render volle Auflösung.
6. `ffprobe` und Stichprobe im Player.
7. Commit mit README: Render-Befehl.

## Qualitätskriterien / Definition of Done

- [ ] Render ohne Fehler; Dauer ±1 Frame
- [ ] Text lesbar auf Zielgerät (min font size checked)
- [ ] Quellcode und Befehl dokumentiert
- [ ] Random Seeds fixiert wo nötig
- [ ] Keine unlizenzierte Musik

## Sicherheit & Freigaben

- Manim/p5 in Sandbox bei untrusted Dependencies.
- Publish auf Social nur nach Freigabe.

## Fallstricke

- Manim-LaTeX fehlt auf Server → Build fail; Dependencies vorab.
- p5 ohne `randomSeed` → nicht reproduzierbar.
- Remotion `durationInFrames` zu kurz.
- GIF aus voller HD ohne Palette → 50 MB Monster.
- Skills veraltet vs. Remotion Major Version—Version pinnen.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** 10 s KPI-Counter in Remotion.
- **Input:** Start 0, End 1200000 EUR, 1080p30.
- **Prompt:**

```text
Remotion composition KpiCount 300 frames, animate number with easing, render out/kpi.mp4.
```

- **Erwartetes Ergebnis:**

```bash
npx remotion render KpiCount out/kpi.mp4
Duration: 10.00s, 1920x1080
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Sinuskurve erklären mit Manim.
- **Input:** 45 s, 1080p.
- **Prompt:**

```text
Single Manim scene PlotSine, voiceover placeholder text on screen only, render -pqh.
```

- **Erwartetes Ergebnis:**

```text
manim -pqh plot_sine.py PlotSine → media/videos/plot_sine/1080p60/PlotSine.mp4
```