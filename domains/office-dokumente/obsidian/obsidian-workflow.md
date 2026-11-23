---
id: obsidian-workflow
domain: office-dokumente
title: "Obsidian-Vault Wissen pflegen"
category: obsidian
tags:
  - obsidian
  - markdown
  - wiki
target_agents:
  - cursor
  - claude-code
  - generic
required_tools:
  - name: git
    install: "system"
    version_notes: "Vault versioniert"
  - name: ripgrep
    install: "rg"
    version_notes: "Vault-Suche"
inputs:
  - "Vault-Pfad"
  - "Note-Thema oder Link-Graph"
outputs:
  - "Neue/aktualisierte .md"
  - "Backlinks-Übersicht"
risk_level: low
version: "1.1.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

**Obsidian-Vaults** als lokale Markdown-Wikis pflegen—Notes, Wikilinks, Frontmatter—git-versioniert, ohne Cloud-Zwang.

## Wann nutzen

- PKM/Team-Wiki liegt als Ordner im Repo.
- Agent arbeitet im IDE mit direktem Dateizugriff.
- Offline-first, Sync separat (Syncthing/Git).

**Wann nicht**

- Zentrale Notion-DB mit Properties (→ notion-workflow).
- Binary-only Attachments ohne LFS-Policy.
- Automatisches Löschen ohne Git-History-Bewusstsein.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| ripgrep | Suche | Schnell im Vault |
| git | Versionierung | Rollback |
| obsidian linter | Optional | MD-Style |
| pandoc | Export | Optional PDF |

## System-Prompt / Instruktionen

```text
You maintain an Obsidian vault as plain markdown files with [[wikilinks]] and YAML frontmatter.

Inputs: vault root path, note title, content outline, tags list, link targets existing notes, template daily|meeting|concept.

Conventions:
- One note per concept; filename Title Case or kebab per user vault rules.
- Frontmatter: title, tags, date, aliases optional.
- Link only to existing notes or create stub with user approval for stubs.
- Embeds ![[image.png]] only if files exist in attachments/.

Before create: rg search title and aliases to avoid duplicates.

Updates: surgical edit; preserve manual sections between HTML comments if user uses them.

Git: stage only vault paths; commit message conventional; never force push.

Approvals: delete note, rename breaking links, or publish vault subtree requires user yes.

Output: file paths, new backlinks list (rg for [[note]]), suggested MOC updates.

Do not run arbitrary community plugins unless user names them.

Respect .obsidian config—do not commit secrets from plugins.

For daily notes use YYYY-MM-DD.md when user pattern says so.

Keep code blocks with language tags.
Add see-also section with 2-3 wikilinks when helpful.
```

## Arbeitsablauf

1. Vault-Struktur und Naming-Regel lesen.
2. `rg` Duplikat-Suche.
3. Note aus Template erzeugen.
4. Wikilinks setzen; stubs melden.
5. Optional MOC-Index aktualisieren.
6. `git diff` zeigen.
7. Commit nur nach Nutzer-Freigabe.

## Qualitätskriterien / Definition of Done

- [ ] Kein ungewolltes Duplikat
- [ ] Frontmatter valide YAML
- [ ] Links zu existierenden Notes oder stub list
- [ ] Kein force push
- [ ] Pfadliste im Output

## Sicherheit & Freigaben

- Vault kann Secrets enthalten—nicht committen.
- `.obsidian/plugins` API keys prüfen.
- Löschen nur mit Freigabe.

## Fallstricke

- Case-sensitive Links auf Linux.
- Rename ohne Backlink-Update.
- Große Binaries in Git.
- Templater-Syntax ohne Plugin.
- Merge-Konflikte bei Sync.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Concept Note mit Backlinks.
- **Input:** Vault `/wiki`, Thema „CAMT Import“.
- **Prompt:**

```text
Create note CAMT Import; link to [[Buchhaltung]] and [[SEPA]]; rg dupes first.
```

- **Erwartetes Ergebnis:**

```text
wiki/CAMT Import.md; links to existing notes; changelog paths.
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Daily Note.
- **Input:** Date 2026-11-23, 3 bullets standup.
- **Prompt:**

```text
2026-11-23.md daily template; no duplicate if exists—append instead.
```

- **Erwartetes Ergebnis:**

```text
daily/2026-11-23.md created or appended; git diff shown.
```