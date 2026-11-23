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
    version_notes: "only at freigegebenem Cloud-Account"
inputs:
  - "Prompt (Motiv, Stil, Negativliste)"
  - "pagesverhaeltnis and Aufloesung (SDXL-safe)"
  - "Checkpoint/LoRA-Namen (lokal vorhanden)"
outputs:
  - "PNG(s) with Seed and Workflow-Snapshot"
  - "Parameter-JSON for Reproduktion"
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
- Ausgabe should nachvollziehbar (Seed, Nodes) archiviert will.

**When not to use**

- Echtzeit-Inpainting in Kundenfotos without Retusche-approval and Urheberklaerung.
- Sensible Prompts with verbotenen Inhalten or identifizierbaren Personen without Recht.
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
2. Checkpoint-list from `models/checkpoints/` against Briefing abgleichen.
3. Workflow-Template `sdxl_txt2img_api.json` laden; Prompt-Nodes ersetzen.
4. `curl -X POST http://127.0.0.1:8188/prompt -d @job.json` → `prompt_id`.
5. `curl http://127.0.0.1:8188/history/<prompt_id>` bis `outputs` gefuellt.
6. Bilder after `out/` kopieren; `workflow_snapshot.json` and `params.json` archivieren.
7. Optional Web-Vorschau: `magick out/ComfyUI_*.png -resize 512x512 preview.jpg`.

## Definition of done

- [ ] Seed and Workflow-JSON archiviert—Re-Run possible
- [ ] Aufloesung and pagesverhaeltnis wie briefed
- [ ] no unautorisierten Checkpoints/LoRAs geladen
- [ ] Stichprobe on Artefakte; User for Markenfreigabe
- [ ] Cloud-Kosten/Calls dokumentiert (falls MCP)

## Security

- Generierte Personen not as echte Individuen ausgeben; Markenassets only with Rechteliste.
- comfy-cloud API-Keys not in Chat or Repo-Commits; Umgebungsvariablen.
- NSFW-Filter and Firmenpolicy before Batch-Generierung clarify.

## Pitfalls

- Falsche Node-IDs when API-Workflow → stille Fehler; against gespeichertes Template diffen.
- SDXL with to hoher CFG → waxy skin; typisch 5–7 testen.
- Random Seed without Log macht approval impossible—immer notieren.
- MCP-Timeout at langen Samplern—`steps` and Queue-Groesse begrenzen.
- Refiner without Base-Output-Node-Verkabelung liefert schwarze Bilder.

## Basic examples

### Example 1 (Example data)

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

### Example 2 (Real-world example)

- **Task:** Hermes optional-mcps comfy-cloud for GPU-freie Agenten.
- **Input:** Freigegebener comfy-cloud MCP, gleicher Prompt wie oben.
- **Prompt:**

```text
Use comfy-cloud MCP to enqueue SDXL job; archive returned image URL locally; cite Hermes MCP catalog install path.
```

- **Expected result:**

  Lokale Kopie `out/hero.png`, Protokolleintrag with https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/comfy-cloud ; no oeffentlicher Upload.