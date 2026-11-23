---
id: wikis-dokumentation-workflow
domain: recherche-wissen
title: "Wiki-Dokumentation strukturieren"
category: wikis-dokumentation
tags:
  - wiki
  - docs
  - markdown
target_agents:
  - cursor
  - claude-code
  - generic
required_tools:
  - name: git
    install: "system"
    version_notes: "Docs-as-code"
  - name: markdownlint
    install: "npm: markdownlint-cli"
    version_notes: "Style"
inputs:
  - "Thema und Zielgruppe"
  - "Bestehende Docs"
outputs:
  - "Strukturierter Wiki-Tree"
  - "MOC-Index"
risk_level: low
version: "1.1.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

**Technische Wikis** planen und schreiben—Informationsarchitektur, Markdown, Quellen, git-versioniert.

## Wann nutzen

- Neues Produkt- oder Team-Wiki.
- Altdocs konsolidieren.
- Onboarding-Pfad.

**Wann nicht**

- Notion/Obsidian-spezifisch (eigene Templates).
- API-Referenz nur aus Halluzination.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| git | Versionierung | Diffs |
| markdownlint | Lint | Konsistenz |
| mermaid | Diagramme | Wie diagramme-whiteboard |
| ripgrep | Inventar | Bestand |

## System-Prompt / Instruktionen

```text
You design and write technical wiki documentation in markdown under git.

Inputs: audience (dev|ops|user), scope outline, existing paths to preserve, moc path docs/README.md.

IA rules:
- Max depth 3 in sidebar; index pages at each level.
- One topic per file; crosslinks relative.
- Every how-to ends with verification steps.
- ADRs for decisions in docs/adr/ with date.

Writing:
- Imperative titles: "Configure X", not "Configuration of X".
- Code blocks with language; pin versions in setup guides.
- Link to official docs urls when stating facts; UNVERIFIED if not checked.

Do not delete legacy without deprecation notice file.

Lint: markdownlint on changed files if available.

Approvals: publish to public git repo requires user yes.

Output: file tree, MOC markdown, list of UNVERIFIED claims.

Diagrams: mermaid sources co-located with page.

German or English per user locale consistently per subtree.

Include last-reviewed frontmatter date on runbooks.
Avoid duplicating vendor docs—link out with summary.
```

## Arbeitsablauf

1. rg Inventar bestehender MD.
2. IA-Entwurf MOC.
3. Stubs für fehlende Seiten.
4. Priorität 3 Kernseiten schreiben.
5. mermaid wo nötig.
6. markdownlint.
7. git diff + Nutzer review.

## Qualitätskriterien / Definition of Done

- [ ] MOC verlinkt alle Seiten
- [ ] How-tos haben Verify-Schritt
- [ ] Keine ungeprüften Vendor-Fakten ohne URL
- [ ] Lint clean oder Ausnahmen dokumentiert
- [ ] Public publish freigegeben

## Sicherheit & Freigaben

- Keine Secrets in docs.
- Interne URLs in private repo only.
- DSGVO in user docs.

## Fallstricke

- Wiki-Garten ohne MOC.
- Tiefe Ordnerstrukturen.
- Duplikat-Titel.
- Veraltete Screenshots.
- Broken relative links.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Ops Runbook Root.
- **Input:** 5 Services.
- **Prompt:**

```text
MOC + one runbook template per service stub; markdownlint.
```

- **Erwartetes Ergebnis:**

```text
docs/README.md links 5 runbooks; stubs with verify sections.
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** ADR hinzufügen.
- **Input:** Entscheidung Postgres vs MySQL.
- **Prompt:**

```text
docs/adr/0007-database.md with context decision consequences.
```

- **Erwartetes Ergebnis:**

```text
ADR file dated; status proposed; linked from MOC.
```