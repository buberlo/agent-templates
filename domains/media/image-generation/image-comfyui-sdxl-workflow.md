---
id: image-comfyui-sdxl-workflow
title: "SDXL-Bilder over ComfyUI-Workflow"
domain: media
category: image-generation
tags:
  - comfyui
  - sdxl
  - generative
target_agents:
  - hermes
  - generic-mcp-agents
  - openclaw
required_tools:
  - name: ComfyUI
    install: "github.com/comfyanonymous/ComfyUI; lokaler Server or comfy-cloud MCP"
    version_notes: "SDXL-Checkpoint; Workflow as API-JSON"
  - name: comfy-cloud MCP
    install: "hermes mcp install comfy-cloud (optional)"
    version_notes: "only with an approved cloud account"
inputs:
  - "Prompt (Motiv, Stil, Negativliste)"
  - "Aspect ratio and resolution (SDXL-safe)"
  - "Checkpoint/LoRA-Namen (lokal vorhanden)"
outputs:
  - "PNG(s) with Seed and Workflow-Snapshot"
  - "Parameter JSON for reproduction"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

**Reproducible SDXL generation** via ComfyUI: workflow as JSON, fixed seeds, documented checkpoints—locally or via approved comfy-cloud MCP, with visual approval before brand use.

## When to use

- Brands need a recurring layout (product mockup, social format) with lightly varying prompts.
- Team betreibt ComfyUI lokal or Hermes comfy-cloud with Vertrag.
- Output should be archived reproducibly (seed, nodes).

**When not to use**

- Echtzeit-Inpainting in Kundenfotos without Retusche-approval and Urheberklaerung.
- Sensitive prompts with prohibited content or identifiable individuals without permission.
- Allein API-basierte DALL·E/Midjourney-Flows without Comfy-Infrastruktur.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| ComfyUI API | `/prompt` POST, History | Nodegraph serverseitig |
| SDXL Base + Refiner | Qualitaet 1024² | Standard-Pipeline |
| comfy-cloud MCP | Remote-GPU | Optional, Kostenkontrolle |
| ffmpeg or imagemagick | Thumbnail/Resize | Post-Export for Web |

## System prompt

```text
You generate images via ComfyUI using an explicit workflow JSON (API format), not ad-hoc UIs.

Inputs: positive and negative prompts, width/height (multiples of 8, typical 1024x1024 or 1344x768), checkpoint name on server, seed (fixed or -1 random), batch size (default 1), optional LoRA strength.

Pre-flight:
- Confirm ComfyUI is reachable (GET /system_stats or queue empty).
- List available checkpoints if user did not specify; never download new weights without approval.

Workflow assembly:
- Use standard SDXL txt2img or refiner chain from saved workflow file; inject prompts into CLIPTextEncode nodes by node id.
- Save the exact workflow JSON sent to /prompt as workflow_snapshot.json alongside outputs.

Execute:
- POST /prompt {"prompt": workflow} → prompt_id
- Poll /history/{prompt_id} until outputs appear; download images from /view?filename=...

Log: seed, steps, cfg, sampler, checkpoint, prompt_id, output filenames.

QA: check for anatomical artifacts before brand use; offer 1 variation with new seed only if requested.

Cloud MCP: if using comfy-cloud, respect rate limits; no NSFW or trademarked characters unless user confirms rights.

Never publish images to stock or social without user approval.
```

## Workflow

1. ComfyUI-Status verify: `curl -s http://127.0.0.1:8188/system_stats`.
2. Cross-check the checkpoint list from `models/checkpoints/` against the briefing.
3. Workflow-Template `sdxl_txt2img_api.json` laden; Prompt-Nodes ersetzen.
4. `curl -X POST http://127.0.0.1:8188/prompt -d @job.json` → `prompt_id`.
5. `curl http://127.0.0.1:8188/history/<prompt_id>` bis `outputs` gefuellt.
6. Copy images to `out/`; archive `workflow_snapshot.json` and `params.json`.
7. Optional Web-Vorschau: `magick out/ComfyUI_*.png -resize 512x512 preview.jpg`.

## Definition of done

- [ ] Seed and Workflow-JSON archiviert—Re-Run possible
- [ ] Resolution and aspect ratio as briefed
- [ ] no unautorisierten Checkpoints/LoRAs geladen
- [ ] Spot check for artifacts; user for brand approval
- [ ] Cloud costs/calls documented (if MCP)

## Security

- Generierte Personen not as echte Individuen ausgeben; Markenassets only with Rechteliste.
- Do not put comfy-cloud API keys in chat or repo commits; use environment variables.
- NSFW-Filter and Firmenpolicy before Batch-Generierung clarify.

## Pitfalls

- Falsche Node-IDs when API-Workflow → stille Fehler; against gespeichertes Template diffen.
- SDXL with to hoher CFG → waxy skin; typisch 5–7 testen.
- Random Seed without Log macht approval impossible—immer notieren.
- MCP timeout on long samplers—limit `steps` and queue size.
- Refiner without base output node wiring produces black images.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Hero-Bild 1344×768 for Blog.
- **Input:** Prompt „minimalist office desk, morning light“, SDXL base, seed 4242.
- **Prompt:**

```text
Run SDXL ComfyUI workflow 1344x768, seed 4242, save snapshot and PNG. cfg 6, steps 28.
```

- **Expected result:**

```json
{
  "prompt_id": "a1b2c3d4",
  "seed": 4242,
  "files": ["ComfyUI_00001_.png"],
  "dimensions": { "w": 1344, "h": 768 }
}
```

### Example 2 (Example data (self-written))
- **Task:** Hermes optional-mcps comfy-cloud for GPU-free agents.
- **Input:** Approved comfy-cloud MCP, same prompt as above.
- **Prompt:**

```text
Use comfy-cloud MCP to enqueue SDXL job; archive returned image URL locally; cite Hermes MCP catalog install path.
```

- **Expected result:**

  Local copy `out/hero.png`, log entry with https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/comfy-cloud ; no public upload.