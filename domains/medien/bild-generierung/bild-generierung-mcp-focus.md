---
id: bild-generierung-mcp-focus
domain: medien
title: "Bildgenerierung: ComfyUI, Cloudinary und Skills"
category: bild-generierung
tags:
  - image-gen
  - comfy
  - mcp
  - cloudinary
target_agents:
  - hermes
  - generic-mcp-agents
  - openclaw
required_tools:
  - name: comfy-cloud MCP
    install: "hermes mcp install comfy-cloud"
    version_notes: "Optional; API-Key nötig"
  - name: cloudinary MCP
    install: "hermes mcp install cloudinary"
    version_notes: "Asset-CDN nach Freigabe"
  - name: ClawHub Nano Banana Pro
    install: "openclaw skills install (steipete)"
    version_notes: "Generatives Skill; Policy prüfen"
inputs:
  - "Creative Brief (Motiv, Format, Marke)"
  - "Budget/Freigabe für Cloud-Generierung"
outputs:
  - "Generierte Assets mit Metadaten"
  - "Entscheidungslog MCP vs. lokal"
risk_level: medium
version: "1.1.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

Agenten orchestrieren **generative Bildproduktion** mit klarem Split: **lokale ComfyUI-Workflows** vs. **Hermes MCPs** (comfy-cloud, cloudinary) vs. **ClawHub-Skills**—inklusive Kosten-, Rechte- und QA-Gates.

## Wann nutzen

- Marke braucht Varianten (Banner, Social) aus wiederholbarem Prompt-Set.
- Hermes/OpenClaw-Umgebung hat freigeschaltete MCPs oder Skills.
- CDN-Upload nur nach expliziter Freigabe (cloudinary).

**Wann nicht**

- Ein einziges Stock-Foto suchen (Recherche-Template).
- Fotorealistische Darstellung identifizierbarer Personen ohne Einwilligung.
- GPU-freie Umgebung ohne Cloud-Budget.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| ComfyUI lokal / comfy-cloud MCP | Bild erzeugen | Volle Kontrolle über Workflow-JSON |
| cloudinary MCP | Hosting/Transform | Nach Freigabe; nicht für Secrets |
| Nano Banana Pro Skill | Alternative Gen | ClawHub-Reichweite; Policy lesen |
| ImageMagick | Resize/QA | Schnelle Web-Varianten |

## System-Prompt / Instruktionen

```text
You generate and prepare brand images using only approved tools from required_tools.

Inputs: prompt, negative prompt, aspect ratio, resolution, brand colors hex list, seed strategy (fixed/random), delivery formats (png, webp), upload_to_cdn (default false).

Routing:
1) If user has local ComfyUI and GPU → POST /prompt with archived workflow (see bild-comfyui-sdxl-workflow patterns).
2) If only comfy-cloud MCP → enqueue via MCP, track job id, download result to local out/.
3) If skill Nano Banana Pro is in policy and user asked for quick gen → follow skill steps; still save prompt and seed.
4) cloudinary MCP only after user approves upload; use transformations for web sizes, never store API secret in chat.

Every image: save sidecar JSON {prompt, seed, model, tool_path, timestamp}.

QA checklist before handoff: readability of text in image (if any), logo distortion, extra fingers, offensive content.

Reject requests violating IP, celebrity likeness, or NSFW without policy clearance.

Report cost-impacting cloud calls. Do not auto-post to social.

Prefer fixed seed for brand review cycles; document any intentional seed change.
If local GPU unavailable and cloud rejected, stop instead of switching provider silently.
Watermarking or logo overlay happens only after base image approved.
Archive negative prompts alongside positive prompts in sidecar JSON.
```

## Arbeitsablauf

1. Briefing und Tool-Policy lesen; MCPs nicht „alle aktivieren“.
2. Pfad wählen: lokal Comfy vs. comfy-cloud vs. Skill.
3. Generierung mit festem Seed für V1; Varianten nur auf Anfrage.
4. `magick identify` und visuelle Stichprobe.
5. Web-Varianten lokal erzeugen (`-resize 1200>`).
6. Optional cloudinary upload nach Freigabe mit transform URL dokumentieren.
7. sidecar JSON und Pfade liefern.

## Qualitätskriterien / Definition of Done

- [ ] Prompt/Seed/Modell archiviert
- [ ] Markenfarben und Safe-Area eingehalten (briefing)
- [ ] Kein unautorisierter CDN-Upload
- [ ] MCP-Calls protokolliert
- [ ] QA-Flags an Kreativteam

## Sicherheit & Freigaben

- API-Keys in Umgebungsvariablen; nicht in Repo.
- Generierte Bilder mit Markenzeichen Dritter vermeiden.
- Cloudinary-Upload nur mit Datenschutz-Freigabe.

## Fallstricke

- comfy-cloud Timeout bei hohen Steps—Queue klein halten.
- Skill und MCP parallel → doppelte Kosten.
- cloudinary ohne Optimierung liefert riesige PNGs—Transformation setzen.
- Nano Banana Skill-Namen variieren—`openclaw skills verify`.
- Keine Rechte-Prüfung bei Trainingsstil bekannter Künstler.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** LinkedIn-Banner 1584×396 aus SDXL lokal.
- **Input:** Blau/weiß Brand, seed 99.
- **Prompt:**

```text
Local ComfyUI SDXL 1584x396, seed 99, save workflow JSON; no cloud upload.
```

- **Erwartetes Ergebnis:**

```json
{ "file": "banner_v1.png", "seed": 99, "tool": "comfyui_local", "workflow": "workflow_snapshot.json" }
```

### Beispiel 2 (Praxisbeispiel)

- **Aufgabe:** Nach Freigabe WebP auf Cloudinary.
- **Input:** `banner_v1.png`, cloudinary MCP aktiv.
- **Prompt:**

```text
Upload banner_v1 as brand/linkedin/banner_v1, return https URL with f_auto,q_85; confirm user approval in log.
```

- **Erwartetes Ergebnis:**

```text
secure_url: https://res.cloudinary.com/<cloud>/image/upload/f_auto,q_85/v.../banner_v1.webp
approval: user_confirmed yes
```