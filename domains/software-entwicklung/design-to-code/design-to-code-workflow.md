---
id: design-to-code-workflow
title: "Design to Code"
domain: software-entwicklung
category: design-to-code
tags:
  - design
  - frontend
  - playwright
target_agents:
  - hermes
  - claude-code
  - cursor
  - generic-mcp-agents
required_tools:
  - name: playwright
    install: "visual compare optional"
    version_notes: "npx playwright test"
  - name: figma-export
    install: "tokens/screenshots user provides"
    version_notes: "no token in repo"
inputs:
  - "Figma frame export or spec"
  - "Component library (shadcn/MUI)"
outputs:
  - "React/Vue components"
  - "Visual regression test optional"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Designs in **zugängliche, responsive UI-Komponenten** übersetzen und mit Playwright-Screenshot-Tests gegen Staging abgleichen.

## Wann nutzen

- Neue Landing-Section, Dashboard-Widget.
- Design-Tokens sync.

**Wann nicht:** Vollständiges Brand-Redesign ohne Design-Review.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| React/Vue | UI | project stack |
| Tailwind/tokens | Styling | consistency |
| playwright | Visual | toHaveScreenshot |

## System-Prompt / Instruktionen

```text
Design to code workflow (software-entwicklung/design-to-code).

Match spacing, typography, color tokens from design spec; use rem not magic px except borders.
Semantic HTML and aria labels for interactive controls.
Responsive breakpoints: mobile-first; test at 375 and 1280 widths in playwright.
No absolute positioning unless design requires; prefer flex/grid.
Extract reusable components; avoid copy-paste sections.
Assets: optimized images; provide width/height to avoid CLS.
Compare: npx playwright test --grep visual when snapshots approved.
Do not embed Figma API tokens in code.
Dark mode if spec includes: use CSS variables.
Keyboard focus visible styles required.
Document deviations from design with reason (a11y, performance).
```

## Arbeitsablauf

1. Spec/PNG/Tokens einlesen.
2. Komponent-Hierarchie skizzieren.
3. Implementieren im Designsystem.
4. Story/page route lokal.
5. `npm run dev` smoke.
6. `npx playwright test tests/visual/hero.spec.ts`.
7. PR mit Screenshots vor/nach.

## Qualitätskriterien / Definition of Done

- [ ] a11y: landmarks, labels
- [ ] Responsive breakpoints getestet
- [ ] Keine Design-Token-Secrets im Repo

## Sicherheit & Freigaben

- Keine personenbezogenen Bilder in Fixtures ohne Rechte.

## Fallstricke

- Pixel-perfect auf allen Browsern unmöglich — Toleranz.
- shadcn Override-Kaskade.
- Fonts FOIT.
- playwright snapshot auf animierten Elementen — flaky.
- Fehlende focus styles.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Hero section aus PNG.
- **Input:** 1280w mockup.
- **Prompt:**

```text
Build Hero.tsx; playwright screenshot test desktop+mobile.
```

- **Erwartetes Ergebnis:**

```bash
npx playwright test tests/visual/hero.spec.ts --project=chromium
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Token sync.
- **Input:** colors.json from design.
- **Prompt:**

```text
Map tokens to tailwind theme extend; document diff from Figma hex.
```

- **Erwartetes Ergebnis:**

```text
tailwind.config.ts updated; primary=#1B4DFF per tokens.json
```