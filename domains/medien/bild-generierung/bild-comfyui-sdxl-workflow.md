---
id: bild-comfyui-sdxl-workflow
domain: medien
title: "Bildgenerierung mit ComfyUI und SDXL"
category: bild-generierung
tags:
  - comfyui
  - sdxl
  - generative
target_agents:
  - grokbot
  - generic
required_tools:
  - name: comfyui
    install: "git: ComfyUI + models"
    version_notes: "SDXL 1.0 base+refiner"
  - name: cuda
    install: "NVIDIA driver + CUDA 12"
    version_notes: "VRAM >= 12 GB empfohlen"
inputs:
  - "Prompt (DE/EN)"
  - "Workflow JSON"
  - "Seed optional"
outputs:
  - "PNG 1024²"
  - "Workflow-Log"
risk_level: medium
version: "1.0.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

Wiederholbare Marketing- und Stock-Bilder aus SDXL-Workflows erzeugen.

## Wann nutzen

- Varianten für A/B-Tests, Social-Assets.
- Nicht für verpflichtende Foto-Realismus ohne Freigabe (Deepfake-Risiko).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| ComfyUI | Node-Graph | Reproduzierbare Pipelines |
| SDXL | Modell | Hohe Qualität 1:1 |
| GFPGAN | optional Face fix | Portraits |

## System-Prompt / Instruktionen

```text
Generate images via ComfyUI API from saved workflow JSON.
Fixed seeds for regression; vary only when user asks.
Block NSFW and real-person likeness without written approval.
Save PNG + embed workflow metadata in sidecar JSON.
```

## Arbeitsablauf

1. Workflow laden; Modelle versionieren.
2. Prompt und negative prompt setzen.
3. Queue API (localhost:8188); Batch N Varianten.
4. Kuratierte Auswahl + Upscale optional.
5. Metadaten und Lizenzhinweis ausliefern.

## Qualitätskriterien / Definition of Done

- [ ] Keine anatomischen Glitches in Finalauswahl
- [ ] Seed/Workflow reproduzierbar
- [ ] Usage-Rechte dokumentiert (generiert)

## Sicherheit & Freigaben

- Keine Prominenten oder Mitarbeiter ohne Freigabe.
- GPU-Hosts nicht öffentlich exponieren.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

_Siehe vorheriger Abschnitt; bei Migration ergänzt._

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Validierung
- **Input:** n/a
- **Prompt:** `validate output`
- **Erwartetes Ergebnis:** OK

## Beispiele (Legacy)

**Eingabe:** Prompt "modernes Büro, Tageslicht", seed 4242
**Erwartetes Ergebnis:** `asset_4242.png`, `workflow.json`
