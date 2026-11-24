---
id: obsidian-workflow
title: "Obsidian-Vault Wissen pflegen"
domain: office-documents
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
  - "Vault-path"
  - "Note-Thema or Link-Graph"
outputs:
  - "Neue/aktualisierte .md"
  - "Backlinks-Uebersicht"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

**Obsidian-Vaults** as lokale Markdown-Wikis pflegen—Notes, Wikilinks, Frontmatter—git-versioniert, without Cloud-Zwang.

## When to use

- PKM/Team-Wiki liegt as Ordner im Repo.
- Agent arbeitet im IDE with direktem filezugriff.
- Offline-first, Sync separat (Syncthing/Git).

**When not to use**

- Zentrale Notion-DB with Properties (→ notion-workflow).
- Binary-only Attachments without LFS-Policy.
- Automatisches Loeschen without Git-History-Bewusstsein.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| ripgrep | Suche | Schnell im Vault |
| git | Versionierung | Rollback |
| obsidian linter | Optional | MD-Style |
| pandoc | Export | Optional PDF |

## System prompt

```text
You maintain an Obsidian vault as plain markdown files with [[wikilinks]] and YAML frontmatter.

You are a careful assistant for this workflow. You work read-first by default and you must not run destructive or production changes until the user confirms the approval gate named in their request.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.


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
Add see-also section with 2-3 wikilinks when helpful.```

## Workflow

1. Vault-Struktur and Naming-Regel read.
2. `rg` Duplikat-Suche.
3. Note from Template create.
4. Wikilinks setzen; stubs melden.
5. Optional MOC-Index aktualisieren.
6. `git diff` zeigen.
7. Commit only after User-approval.

## Definition of done

- [ ] no ungewolltes Duplikat
- [ ] Frontmatter valide YAML
- [ ] Links to existden Notes or stub list
- [ ] no force push
- [ ] pathliste im Output

## Security

- Vault kann Secrets enthalten—not committen.
- `.obsidian/plugins` API keys verify.
- Loeschen only with approval.

## Pitfalls

- Case-sensitive Links on Linux.
- Rename without Backlink-Update.
- Grosse Binaries in Git.
- Templater-Syntax without Plugin.
- Merge-Konflikte at Sync.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Concept Note with Backlinks.
- **Input:** Vault `/wiki`, Thema „CAMT Import“.
- **Prompt:**

```text
Create note CAMT Import; link to [[Buchhaltung]] and [[SEPA]]; rg dupes first.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.wiki/CAMT Import.md; links to existing notes; changelog paths.
```

### Example 2 (Example data (self-written))
- **Task:** Daily Note.
- **Input:** Date 2026-11-23, 3 bullets standup.
- **Prompt:**

```text
2026-11-23.md daily template; no duplicate if exists—append instead.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.daily/2026-11-23.md created or appended; git diff shown.
```