---
id: 3d-modeling-workflow
title: "Validate, convert, and document 3D assets"
domain: media
category: 3d-modeling
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
    version_notes: "Batch export GLB/FBX; headless"
  - name: ffmpeg
    install: "OS package ffmpeg"
    version_notes: "Turntable preview from image sequence"
  - name: gltf-validator
    install: "npm: gltf-validator or Khronos CLI"
    version_notes: "Validate glTF/GLB structure"
inputs:
  - "3D source file (BLEND, FBX, OBJ, GLB)"
  - "Target format and max poly budget"
  - "Optional: preview video"
outputs:
  - "Converted assets"
  - "Validation report and preview"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

**Light 3D pipeline**: convert assets, check **polycount and textures**, deliver **GLB** for the web, and optionally a **turntable preview** via Blender + FFmpeg—without the agent doing full CAD construction from scratch.

## When to use

- Vendor sends FBX/OBJ; target is web-ready GLB.
- Batch export of multiple BLEND files with the same parameters.
- QA report before embedding in Remotion/Three.js/WebAR.

**When not to use**

- Parametric CAD design from scratch in SolidWorks/Inventor.
- Finite-element analysis or manufacturing drawings.
- High-resolution film render farm (Houdini) without resources.

## Tool stack

| Tool | Role | Rationale |
|------|-------|-----------|
| Blender CLI | Import/export, decimate | Scriptable, widely used |
| gltf-validator | GLB conformance | Find errors before deployment |
| ffmpeg | Preview video | From PNG sequence |
| ImageMagick | Thumbnail | Still from first frame |

## System prompt

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

## Workflow

1. Note source format; back up under `source/`.
2. Blender Python script: import → stats → decimate if needed.
3. `blender --background in.blend --python export_glb.py`.
4. `gltf-validator dist/model.glb` → save report.
5. Optional turntable render under `preview/`.
6. `ffmpeg` sequence → `preview_turntable.mp4`.
7. README with triangle budget and texture list.

## Definition of done

- [ ] GLB loads in validator with no ERROR-level issues
- [ ] Triangle count ≤ budget or documented exception
- [ ] Textures ≤ max edge length
- [ ] Source file unchanged
- [ ] Preview optional but matches model version

## Security

- Do not upload proprietary CAD data to public viewers.
- Review Blender scripts from untrusted sources before execution.

## Pitfalls

- FBX unit scale 0.01 vs 1 → huge model; verify import scale.
- Duplicate vertices after import → merge by distance before export.
- Draco compression without client support.
- Normal maps in sRGB instead of Non-Color.
- Blender 4.x API vs old scripts—pin version.

## Basic examples

### Example 1 (Example data)

- **Task:** FBX → GLB under 100k tris.
- **Input:** `chair.fbx`, 210k tris.
- **Prompt:**

```text
Blender headless import chair.fbx, decimate to under 100k tris, export chair.glb, run gltf-validator.
```

- **Expected result:**

```json
{
  "tris_before": 210403,
  "tris_after": 98210,
  "validator": { "issues": { "errors": 0, "warnings": 1 } },
  "out": "dist/chair.glb"
}
```

### Example 2 (Example data)

- **Task:** Turntable preview.
- **Input:** `dist/chair.glb`.
- **Prompt:**

```text
Render 120 frames turntable, ffmpeg to preview_turntable.mp4 30fps.
```

- **Expected result:**

```bash
ffmpeg -framerate 30 -i preview/frame_%04d.png -c:v libx264 -pix_fmt yuv420p preview_turntable.mp4
Duration: 4.0s, 1920x1080
```