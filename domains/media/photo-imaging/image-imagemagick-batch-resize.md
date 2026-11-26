---
id: image-imagemagick-batch-resize
title: "Fotos batchweise scale and exportieren"
domain: media
category: photo-imaging
tags:
  - imagemagick
  - batch
  - resize
  - web
target_agents:
  - cursor
  - claude-code
  - generic
required_tools:
  - name: ImageMagick
    install: "apt/brew: imagemagick; CLI: magick or convert"
    version_notes: "IM7 bevorzugt; sRGB-Profil deliberately setzen"
  - name: exiftool
    install: "apt/brew: exiftool"
    version_notes: "Optional: Metadaten and Orientation"
inputs:
  - "Folder with source images (JPEG/PNG/TIFF)"
  - "Targetbreite/Hoehe or lange Kante"
  - "Exportprofil (JPEG-Qualitaet, WebP, Strip-EXIF ja/nein)"
outputs:
  - "Output folder with uniform dimensions"
  - "Manifest (filename → Masse)"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

**Homogeneous web or catalog exports** from photo folders: scale, sharpen (subtly), and control color profile and metadata—reproducible with ImageMagick, without a GUI batch.

## When to use

- Hunderte Produktfotos or Event-Shots sollen dieselbe Kantenlaenge have.
- Agent should EXIF-Orientation automatisch beruecksichtigen and ein CSV/Manifest liefern.
- no retusche on Pixelebene required.

**When not to use**

- RAW-Entwicklung (Lightroom/Capture One) with individueller Belichtung.
- Gesichtserkennung and smartes Cropping on Motivmittelpunkt.
- DRM-protected image archives or stock licenses without approval for stripping.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| ImageMagick `magick mogrify` | Batch-Resize | Ein Befehl over viele files |
| ImageMagick `magick identify` | Masse, Format | Manifest and QA |
| exiftool | Orientation, Copyright | before Strip document |

## System prompt

```text
You batch-process images with ImageMagick 7 (magick) on Linux/macOS.

Inputs: source directory, max long edge in pixels (e.g. 1600), output directory, format (JPEG q=85, WebP, or PNG), strip EXIF (yes/no), sharpen (0=off, 1=light unsharp).

Safety:
- Never overwrite source; always write to a dedicated output/ tree.
- Before mogrify: duplicate a 3-file sample and get user acknowledgment on visual QA if brand-critical.

Pipeline per file:
- Auto-orient via -auto-orient (or mogrify -auto-orient).
- Resize: magick mogrify -path out/ -resize 1600x1600> -strip -quality 85 -filter Lanczos *.jpg
  The> suffix prevents upscaling.

Verify: magick identify -format '%f %w %h\n' out/* | sort > manifest.txt
Flag any image still wider than max edge or zero-byte.

Color: if washed out on wide-gamut, ask before assigning profiles; default keep embedded sRGB.

Report: command used, file count, failures, and first 5 lines of manifest.

Do not upload batches to stock sites or CDNs without approval.

If PNG with alpha, preserve alpha unless user requests JPEG flatten (white matte default).
Log failed files with identify stderr; do not skip silently.
For CMYK JPEG input, convert to sRGB before resize and note color shift risk.
```

## Workflow

1. `find in/ -type f \( -iname '*.jpg' -o -iname '*.png' \) | wc -l` zaehlen.
2. Spot check: `magick identify -verbose in/sample.jpg | grep -i orientation`.
3. `mkdir -p out && magick mogrify -path out/ -auto-orient -resize 1600x1600\> -strip -quality 85 in/*.jpg`.
4. `magick identify -format '%f %w %h %b\n' out/* > manifest.csv`.
5. Ausreisser: `awk '$2 > 1600 || $3 > 1600' manifest.csv` (sollte leer sein).
6. Optional WebP: `magick mogrify -path out/webp/ -format webp -quality 82 out/*.jpg`.
7. Deliver result and manifest to user; source folder untouched.

## Definition of done

- [ ] no Quelldatei viaschrieben
- [ ] all Ausgaben ≤ vereinbarte Kantenlaenge (without Upscaling)
- [ ] Orientation correct (visual or EXIF spot check)
- [ ] manifest.csv complete
- [ ] Strip-EXIF only when freigegeben

## Security

- Personenfotos: EXIF-GPS and Geraetenamen before Publikation entfernen—User bestaetigen.
- Do not process copyrighted imagery without proof of license.

## Pitfalls

- `mogrify` without `-path` overwrites sources—always use a separate target folder.
- JPEG-Qualitaet 100: grosse files without sichtlichen Gewinn.
- CMYK-TIFF without Profilkonvertierung wirkt on Web neon—before `-colorspace sRGB`.
- Leere or korrupte files create 0-Byte-Outputs—`identify` Exit-Code verify.
- Thumbnails with `>` vergessen → Upscaling and Weichzeichnung.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Shop-catalog on 1200 px lange Kante.
- **Input:** `catalog/in/` with 240 JPGs.
- **Prompt:**

```text
Batch resize catalog/in to catalog/out, long edge 1200, JPEG q85, strip GPS only, manifest.csv.
```

- **Expected result:**

```csv
sku_001.jpg 1200 900 241033
sku_002.jpg 800 1200 198022
...
240 rows, no width/height > 1200
```

### Example 2 (Example data (self-written))
- **Task:** Fix an image with incorrect EXIF orientation.
- **Input:** `tilted.jpg` Orientation 6.
- **Prompt:**

```text
Auto-orient single file to out/tilted_fixed.jpg and report dimensions before/after.
```

- **Expected result:**

```text
Before: 4032x3024 (orientation 6)
After:  3024x4032
Command: magick in/tilted.jpg -auto-orient out/tilted_fixed.jpg
```