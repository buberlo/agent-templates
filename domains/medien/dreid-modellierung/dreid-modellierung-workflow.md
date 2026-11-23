---
id: dreid-modellierung-workflow
domain: medien
title: "3D-Assets prüfen, konvertieren und dokumentieren"
category: dreid-modellierung
tags:
  - 3d
  - blender
  - glb
  - ffmpeg
target_agents:
  - hermes
  - claude-code
  - generic
required_tools:
  - name: Blender
    install: "blender.org; CLI blender --background"
    version_notes: "Batch-Export GLB/FBX; Headless"
  - name: ffmpeg
    install: "OS-Paket ffmpeg"
    version_notes: "Turntable-Preview aus Bildsequenz"
  - name: gltf-validator
    install: "npm: gltf-validator oder Khronos CLI"
    version_notes: "glTF/GLB-Struktur prüfen"
inputs:
  - "3D-Quelldatei (BLEND, FBX, OBJ, GLB)"
  - "Zielformat und Max-Poly-Budget"
  - "Optional: Preview-Video"
outputs:
  - "Konvertierte Assets"
  - "Validierungsreport und Preview"
risk_level: low
version: "1.1.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

**3D-Pipeline-Light**: Assets konvertieren, **Polycount und Texturen** prüfen, **GLB** für Web liefern und optional **Turntable-Preview** per Blender + FFmpeg—ohne komplette CAD-Konstruktion durch den Agenten.

## Wann nutzen

- Lieferant sendet FBX/OBJ; Ziel ist web-taugliches GLB.
- Batch-Export mehrerer BLEND-Dateien mit gleichen Parametern.
- QA-Report vor Einbindung in Remotion/Three.js/WebAR.

**Wann nicht**

- Parametrische CAD-Konstruktion von Null in SolidWorks/Inventor.
- Finite-Elemente oder Manufacturing Drawings.
- Hochauflösende Film-Render Farm (Houdini) ohne Ressourcen.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Blender CLI | Import/Export, Decimate | Scriptbar, weit verbreitet |
| gltf-validator | GLB-Konformität | Fehler vor Deployment finden |
| ffmpeg | Preview-Video | Aus PNG-Sequenz |
| ImageMagick | Thumbnail | Still aus erstem Frame |

## System-Prompt / Instruktionen

```text
You process 3D assets via Blender headless scripts and validate GLB output; you do not remodel complex geometry from scratch unless user provides explicit step file.

Inputs: source path, target format (glb default), max triangles (e.g. 150k), texture max size (2048), apply transforms (yes/no), generate turntable preview (yes/no).

Preflight:
- Identify format; if blend, open with bpy; if fbx/obj, import with scale 1.0 and apply unit sniffing.
- Report vertex/triangle counts via bpy after import.

Operations:
- Apply decimate modifier if over budget (collapse ratio calculated).
- Pack/repack textures to power-of-two; bake not required unless user asks.
- Export glTF 2.0 binary with materials unless user wants geometry-only.
- Run gltf-validator on output; list errors/warnings.

Turntable (optional):
- Blender script rotates camera 360° in 120 frames, outputs png sequence.
- ffmpeg -framerate 30 -i frame_%04d.png -c:v libx264 preview_turntable.mp4

Never overwrite supplier source; write to dist/.

Deliver: export path, stats table (verts, tris, materials), validator JSON summary, preview paths.

No upload to Sketchfab or CDN without approval.
```

## Arbeitsablauf

1. Quellformat notieren; Backup in `source/`.
2. Blender-Python-Skript: Import → Statistik → ggf. Decimate.
3. `blender --background in.blend --python export_glb.py`.
4. `gltf-validator dist/model.glb` → Report speichern.
5. Optional Turntable-Render in `preview/`.
6. `ffmpeg` Sequenz → `preview_turntable.mp4`.
7. README mit Triangle-Budget und Texture-Liste.

## Qualitätskriterien / Definition of Done

- [ ] GLB lädt in Validator ohne ERROR-Level
- [ ] Triangle count ≤ Budget oder Ausnahme dokumentiert
- [ ] Texturen ≤ Max-Kante
- [ ] Quelle unverändert
- [ ] Preview optional aber sync mit Modellversion

## Sicherheit & Freigaben

- Proprietäre CAD-Daten nicht in öffentliche Viewer hochladen.
- Blender-Skripte aus untrusted Quellen vor Ausführung reviewen.

## Fallstricke

- FBX Unit Scale 0.01 vs 1 → Riesenmodell; Import-Scale prüfen.
- Doppelte Vertices nach Import → nicht exportieren ohne merge-by-distance.
- Draco-Kompression ohne Client-Unterstützung.
- Normal maps in sRGB statt Non-Color.
- Blender 4.x API vs alte Scripts—Version pinnen.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** FBX → GLB unter 100k Tris.
- **Input:** `chair.fbx`, 210k tris.
- **Prompt:**

```text
Blender headless import chair.fbx, decimate to under 100k tris, export chair.glb, run gltf-validator.
```

- **Erwartetes Ergebnis:**

```json
{
  "tris_before": 210403,
  "tris_after": 98210,
  "validator": { "issues": { "errors": 0, "warnings": 1 } },
  "out": "dist/chair.glb"
}
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Turntable-Preview.
- **Input:** `dist/chair.glb`.
- **Prompt:**

```text
Render 120 frames turntable, ffmpeg to preview_turntable.mp4 30fps.
```

- **Erwartetes Ergebnis:**

```bash
ffmpeg -framerate 30 -i preview/frame_%04d.png -c:v libx264 -pix_fmt yuv420p preview_turntable.mp4
Duration: 4.0s, 1920x1080
```