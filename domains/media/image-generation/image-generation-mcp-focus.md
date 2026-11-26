---
id: image-generation-mcp-focus
title: "Bildgenerierung: ComfyUI, Cloudinary and Skills"
domain: media
category: image-generation
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
    version_notes: "Optional; API-Key required"
  - name: cloudinary MCP
    install: "hermes mcp install cloudinary"
    version_notes: "Asset-CDN after approval"
  - name: ClawHub Nano Banana Pro
    install: "openclaw skills install (steipete)"
    version_notes: "Generatives Skill; Policy verify"
inputs:
  - "Creative Brief (Motiv, Format, Marke)"
  - "Budget/approval for Cloud-Generierung"
outputs:
  - "Generierte Assets with Metadaten"
  - "Entscheidungslog MCP vs. lokal"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

Agents orchestrate **generative image production** with a clear split: **local ComfyUI workflows** vs. **Hermes MCPs** (comfy-cloud, cloudinary) vs. **ClawHub skills**—including cost, rights, and QA gates.

## When to use

- Brand needs variants (banner, social) from a repeatable prompt set.
- Hermes/OpenClaw-Umgebung has freigeschaltete MCPs or Skills.
- CDN upload only after explicit approval (cloudinary).

**When not to use**

- Ein einziges Stock-Foto suchen (Recherche-Template).
- Fotorealistische Darstellung identifizierbarer Personen without Einwilligung.
- GPU-freie Umgebung without Cloud-Budget.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| ComfyUI lokal / comfy-cloud MCP | Bild create | Volle Kontrolle over Workflow-JSON |
| cloudinary MCP | Hosting/Transform | after approval; not for Secrets |
| Nano Banana Pro Skill | Alternative Gen | ClawHub-Reichweite; Policy read |
| ImageMagick | Resize/QA | Schnelle Web-Varianten |

## System prompt

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

## Workflow

1. Briefing and Tool-Policy read; MCPs not „all enable“.
2. path waehlen: lokal Comfy vs. comfy-cloud vs. Skill.
3. Generierung with fixedm Seed for V1; Varianten only on Anfrage.
4. `magick identify` and visual spot check.
5. Web-Varianten lokal create (`-resize 1200>`).
6. Optional cloudinary upload after approval with transform URL document.
7. sidecar JSON and pathe liefern.

## Definition of done

- [ ] Prompt/Seed/Modell archiviert
- [ ] Markenfarben and Safe-Area eingehalten (briefing)
- [ ] no unautorisierter CDN-Upload
- [ ] MCP-Calls protokolliert
- [ ] QA-Flags an Kreativteam

## Security

- Store API keys in environment variables; not in the repo.
- Generierte Bilder with Markenzeichen Dritter vermeiden.
- Cloudinary-Upload only with Datenschutz-approval.

## Pitfalls

- comfy-cloud Timeout at hohen Steps—Queue klein halten.
- Skill and MCP parallel → doppelte Kosten.
- cloudinary without optimization returns huge PNGs—set transformation.
- Nano Banana Skill-Namen variieren—`openclaw skills verify`.
- No rights check when using the training style of well-known artists.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** LinkedIn-Banner 1584×396 from SDXL lokal.
- **Input:** Blau/weiss Brand, seed 99.
- **Prompt:**

```text
Local ComfyUI SDXL 1584x396, seed 99, save workflow JSON; no cloud upload.
```

- **Expected result:**

```json
{ "file": "banner_v1.png", "seed": 99, "tool": "comfyui_local", "workflow": "workflow_snapshot.json" }
```

### Example 2 (Example data (self-written))
- **Task:** after approval WebP on Cloudinary.
- **Input:** `banner_v1.png`, cloudinary MCP aktiv.
- **Prompt:**

```text
Upload banner_v1 as brand/linkedin/banner_v1, return https URL with f_auto,q_85; confirm user approval in log.
```

- **Expected result:**

```text
secure_url: https://res.cloudinary.com/<cloud>/image/upload/f_auto,q_85/v.../banner_v1.webp
approval: user_confirmed yes
```