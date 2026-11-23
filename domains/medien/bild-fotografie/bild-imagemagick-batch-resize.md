---
id: bild-imagemagick-batch-resize
domain: medien
title: "Bilder stapelweise skalieren und optimieren"
category: bild-fotografie
tags:
  - imagemagick
  - webp
  - batch
target_agents:
  - hermes
  - generic
required_tools:
  - name: imagemagick
    install: "apt/brew: imagemagick"
    version_notes: "v7 mit magick CLI"
  - name: oxipng
    install: "cargo/apt: oxipng"
    version_notes: "Lossless PNG shrink"
inputs:
  - "Ordner mit Quellbildern"
  - "Zielbreite/Höhe"
  - "Format WebP/JPEG"
outputs:
  - "Optimierter Zielordner"
  - "Manifest CSV"
risk_level: low
version: "1.0.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

Produktfotos oder Screenshots einheitlich skalieren, komprimieren und für Web/CDN vorbereiten.

## Wann nutzen

- Shop-Relaunch, Docs-Screenshots, Thumbnail-Pipelines.
- Nicht für kreative Retusche (dafür GIMP/Krita).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| ImageMagick | resize, strip EXIF | Skriptierbar |
| oxipng | PNG lossless | Kleinere Assets |
| cwebp | WebP | Bessere Kompression |

## System-Prompt / Instruktionen

```text
Batch resize images with ImageMagick magick mogrify or convert.
Preserve aspect ratio; never upscale beyond source.
Strip metadata unless copyright EXIF requested.
Emit CSV manifest: source, output, bytes before/after.
```

## Arbeitsablauf

1. Inventar Quellordner; EXIF prüfen (GPS entfernen).
2. Resize-Pipeline mit einheitlichem Profil.
3. Formatwahl WebP q=82 oder JPEG q=85.
4. oxipng für verbleibende PNGs.
5. Manifest und Stichprobe visuell prüfen.

## Qualitätskriterien / Definition of Done

- [ ] Keine upscaled Artefakte
- [ ] Dateigröße Reduktion dokumentiert
- [ ] Farbprofil sRGB konsistent

## Sicherheit & Freigaben

- GPS/PII aus EXIF strippen standardmäßig.
- Markenlogos nur mit Rechteklärung.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

_Siehe vorheriger Abschnitt; bei Migration ergänzt._

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Validierung
- **Input:** n/a
- **Prompt:** `validate output`
- **Erwartetes Ergebnis:** OK

## Beispiele (Legacy)

**Eingabe:** `products/*.jpg`, max 1200px breit, WebP
**Erwartetes Ergebnis:** `out/webp/`, `manifest.csv`
