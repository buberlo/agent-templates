---
id: bild-imagemagick-batch-resize
domain: medien
title: "Fotos batchweise skalieren und exportieren"
category: bild-fotografie
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
    install: "apt/brew: imagemagick; CLI: magick oder convert"
    version_notes: "IM7 bevorzugt; sRGB-Profil bewusst setzen"
  - name: exiftool
    install: "apt/brew: exiftool"
    version_notes: "Optional: Metadaten und Orientation"
inputs:
  - "Ordner mit Quellbildern (JPEG/PNG/TIFF)"
  - "Zielbreite/Höhe oder lange Kante"
  - "Exportprofil (JPEG-Qualität, WebP, Strip-EXIF ja/nein)"
outputs:
  - "Ausgabeordner mit einheitlichen Abmessungen"
  - "Manifest (Dateiname → Maße)"
risk_level: low
version: "1.1.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

**Homogene Web- oder Katalog-Exporte** aus Foto-Ordnern: skalieren, schärfen (dezent), Farbprofil und Metadaten kontrolliert—reproduzierbar mit ImageMagick, ohne GUI-Batch.

## Wann nutzen

- Hunderte Produktfotos oder Event-Shots sollen dieselbe Kantenlänge haben.
- Agent soll EXIF-Orientation automatisch berücksichtigen und ein CSV/Manifest liefern.
- Keine retusche auf Pixelebene nötig.

**Wann nicht**

- RAW-Entwicklung (Lightroom/Capture One) mit individueller Belichtung.
- Gesichtserkennung und smartes Cropping auf Motivmittelpunkt.
- DRM-geschützte Bildarchive oder Stock-Lizenzen ohne Freigabe zum Strip.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| ImageMagick `magick mogrify` | Batch-Resize | Ein Befehl über viele Dateien |
| ImageMagick `magick identify` | Maße, Format | Manifest und QA |
| exiftool | Orientation, Copyright | Vor Strip dokumentieren |

## System-Prompt / Instruktionen

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

## Arbeitsablauf

1. `find in/ -type f \( -iname '*.jpg' -o -iname '*.png' \) | wc -l` zählen.
2. Stichprobe: `magick identify -verbose in/sample.jpg | grep -i orientation`.
3. `mkdir -p out && magick mogrify -path out/ -auto-orient -resize 1600x1600\> -strip -quality 85 in/*.jpg`.
4. `magick identify -format '%f %w %h %b\n' out/* > manifest.csv`.
5. Ausreißer: `awk '$2 > 1600 || $3 > 1600' manifest.csv` (sollte leer sein).
6. Optional WebP: `magick mogrify -path out/webp/ -format webp -quality 82 out/*.jpg`.
7. Ergebnis und Manifest an Nutzer; Quellordner unberührt.

## Qualitätskriterien / Definition of Done

- [ ] Keine Quelldatei überschrieben
- [ ] Alle Ausgaben ≤ vereinbarte Kantenlänge (ohne Upscaling)
- [ ] Orientation korrekt (Stichprobe visuell oder EXIF)
- [ ] manifest.csv vollständig
- [ ] Strip-EXIF nur wenn freigegeben

## Sicherheit & Freigaben

- Personenfotos: EXIF-GPS und Gerätenamen vor Publikation entfernen—Nutzer bestätigen.
- Urheberrechtlich geschütztes Bildmaterial nicht ohne Lizenznachweis verarbeiten.

## Fallstricke

- `mogrify` ohne `-path` überschreibt Quellen—immer separaten Zielordner.
- JPEG-Qualität 100: große Dateien ohne sichtlichen Gewinn.
- CMYK-TIFF ohne Profilkonvertierung wirkt auf Web neon—vorher `-colorspace sRGB`.
- Leere oder korrupte Dateien erzeugen 0-Byte-Outputs—`identify` Exit-Code prüfen.
- Thumbnails mit `>` vergessen → Upscaling und Weichzeichnung.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Shop-Katalog auf 1200 px lange Kante.
- **Input:** `catalog/in/` mit 240 JPGs.
- **Prompt:**

```text
Batch resize catalog/in to catalog/out, long edge 1200, JPEG q85, strip GPS only, manifest.csv.
```

- **Erwartetes Ergebnis:**

```csv
sku_001.jpg 1200 900 241033
sku_002.jpg 800 1200 198022
...
240 rows, no width/height > 1200
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Ein Bild mit falscher EXIF-Orientation korrigieren.
- **Input:** `tilted.jpg` Orientation 6.
- **Prompt:**

```text
Auto-orient single file to out/tilted_fixed.jpg and report dimensions before/after.
```

- **Erwartetes Ergebnis:**

```text
Before: 4032x3024 (orientation 6)
After:  3024x4032
Command: magick in/tilted.jpg -auto-orient out/tilted_fixed.jpg
```