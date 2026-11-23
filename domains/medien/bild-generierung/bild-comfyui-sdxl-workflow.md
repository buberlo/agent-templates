---
id: bild-comfyui-sdxl-workflow
domain: medien
title: "SDXL-Bilder über ComfyUI-Workflow"
category: bild-generierung
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
    install: "github.com/comfyanonymous/ComfyUI; lokaler Server oder comfy-cloud MCP"
    version_notes: "SDXL-Checkpoint; Workflow als API-JSON"
  - name: comfy-cloud MCP
    install: "hermes mcp install comfy-cloud (optional)"
    version_notes: "Nur bei freigegebenem Cloud-Account"
inputs:
  - "Prompt (Motiv, Stil, Negativliste)"
  - "Seitenverhältnis und Auflösung (SDXL-safe)"
  - "Checkpoint/LoRA-Namen (lokal vorhanden)"
outputs:
  - "PNG(s) mit Seed und Workflow-Snapshot"
  - "Parameter-JSON für Reproduktion"
risk_level: medium
version: "1.1.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

**Reproduzierbare SDXL-Generierung** über ComfyUI: Workflow als JSON, feste Seeds, dokumentierte Checkpoints—lokal oder über freigegebenes comfy-cloud MCP, mit visueller Abnahme vor Markenverwendung.

## Wann nutzen

- Marken brauchen wiederkehrendes Layout (Produkt-Mockup, Social-Format) mit leicht variablen Prompts.
- Team betreibt ComfyUI lokal oder Hermes comfy-cloud mit Vertrag.
- Ausgabe soll nachvollziehbar (Seed, Nodes) archiviert werden.

**Wann nicht**

- Echtzeit-Inpainting in Kundenfotos ohne Retusche-Freigabe und Urheberklärung.
- Sensible Prompts mit verbotenen Inhalten oder identifizierbaren Personen ohne Recht.
- Allein API-basierte DALL·E/Midjourney-Flows ohne Comfy-Infrastruktur.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| ComfyUI API | `/prompt` POST, History | Nodegraph serverseitig |
| SDXL Base + Refiner | Qualität 1024² | Standard-Pipeline |
| comfy-cloud MCP | Remote-GPU | Optional, Kostenkontrolle |
| ffmpeg oder imagemagick | Thumbnail/Resize | Post-Export für Web |

## System-Prompt / Instruktionen

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

## Arbeitsablauf

1. ComfyUI-Status prüfen: `curl -s http://127.0.0.1:8188/system_stats`.
2. Checkpoint-Liste aus `models/checkpoints/` gegen Briefing abgleichen.
3. Workflow-Template `sdxl_txt2img_api.json` laden; Prompt-Nodes ersetzen.
4. `curl -X POST http://127.0.0.1:8188/prompt -d @job.json` → `prompt_id`.
5. `curl http://127.0.0.1:8188/history/<prompt_id>` bis `outputs` gefüllt.
6. Bilder nach `out/` kopieren; `workflow_snapshot.json` und `params.json` archivieren.
7. Optional Web-Vorschau: `magick out/ComfyUI_*.png -resize 512x512 preview.jpg`.

## Qualitätskriterien / Definition of Done

- [ ] Seed und Workflow-JSON archiviert—Re-Run möglich
- [ ] Auflösung und Seitenverhältnis wie briefed
- [ ] Keine unautorisierten Checkpoints/LoRAs geladen
- [ ] Stichprobe auf Artefakte; Nutzer für Markenfreigabe
- [ ] Cloud-Kosten/Calls dokumentiert (falls MCP)

## Sicherheit & Freigaben

- Generierte Personen nicht als echte Individuen ausgeben; Markenassets nur mit Rechteliste.
- comfy-cloud API-Keys nicht in Chat oder Repo-Commits; Umgebungsvariablen.
- NSFW-Filter und Firmenpolicy vor Batch-Generierung klären.

## Fallstricke

- Falsche Node-IDs beim API-Workflow → stille Fehler; gegen gespeichertes Template diffen.
- SDXL mit zu hoher CFG → waxy skin; typisch 5–7 testen.
- Random Seed ohne Log macht Abnahme unmöglich—immer notieren.
- MCP-Timeout bei langen Samplern—`steps` und Queue-Größe begrenzen.
- Refiner ohne Base-Output-Node-Verkabelung liefert schwarze Bilder.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Hero-Bild 1344×768 für Blog.
- **Input:** Prompt „minimalist office desk, morning light“, SDXL base, seed 4242.
- **Prompt:**

```text
Run SDXL ComfyUI workflow 1344x768, seed 4242, save snapshot and PNG. cfg 6, steps 28.
```

- **Erwartetes Ergebnis:**

```json
{
  "prompt_id": "a1b2c3d4",
  "seed": 4242,
  "files": ["ComfyUI_00001_.png"],
  "dimensions": { "w": 1344, "h": 768 }
}
```

### Beispiel 2 (Praxisbeispiel)

- **Aufgabe:** Hermes optional-mcps comfy-cloud für GPU-freie Agenten.
- **Input:** Freigegebener comfy-cloud MCP, gleicher Prompt wie oben.
- **Prompt:**

```text
Use comfy-cloud MCP to enqueue SDXL job; archive returned image URL locally; cite Hermes MCP catalog install path.
```

- **Erwartetes Ergebnis:**

  Lokale Kopie `out/hero.png`, Protokolleintrag mit https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/comfy-cloud ; kein öffentlicher Upload.