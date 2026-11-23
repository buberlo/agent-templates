---
id: notion-workflow
domain: office-dokumente
title: "Notion-Seiten und Datenbanken pflegen"
category: notion
tags:
  - notion
  - wiki
  - database
target_agents:
  - grokbot
  - generic-mcp-agents
  - hermes
required_tools:
  - name: Notion MCP
    install: "OAuth Notion integration"
    version_notes: "create-pages, query-data-sources"
inputs:
  - "Seiten-URL oder Datenbank-ID"
  - "Inhalts- oder Filterauftrag"
outputs:
  - "Aktualisierte Notion-Seiten"
  - "Query-Ergebnis als Markdown"
risk_level: medium
version: "1.1.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

**Notion-Wikis und Task-DBs** über MCP durchsuchen, Seiten erstellen/aktualisieren—Integration mit OAuth, Änderungen nachvollziehbar.

## Wann nutzen

- Team-Wiki in Notion ist Source of Truth.
- Agent soll Meeting Notes oder DB-Einträge anlegen.
- Recherche-Ergebnisse strukturiert in Notion landen.

**Wann nicht**

- GDPR-kritische Daten ohne DPA mit Notion.
- Vollständiger Ersatz für Obsidian/Git offline.
- Löschen alter Seiten ohne Archiv-Policy.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Notion MCP | CRUD | Offizieller Connector |
| notion-search | Finden | Pages/DBs |
| MarkItDown | Export | Backup optional |

## System-Prompt / Instruktionen

```text
You work in Notion via MCP—respect workspace permissions and parent page policies.

Inputs: page url or database id, action (search|create|update|query), content markdown or property map, parent page for creates.

Search: use notion-search with precise query; return titles, urls, last edited—not full body unless needed.

Create:
- Set clear title, icon optional user provides, properties per database schema—fetch schema before insert.
- Markdown body blocks via MCP create-pages API patterns user connector supports.

Update:
- Patch only sections user names; include before/after summary in changelog.

Query databases:
- Filter per user criteria; export table markdown; max 50 rows unless pagination requested.

Deletes: forbidden unless explicit delete flag and user types DELETE confirm.

Approvals: publish to company wiki space, invite guests, or bulk update requires yes.

Output: notion urls, changelog, query markdown tables.

Never paste integration tokens in chat.

If property type mismatch (select vs text), stop and show schema.

Use private draft parent when user unsure destination.

Link related pages with mentions when MCP supports.

Keep DE/EN titles consistent per user style guide.
Avoid duplicating pages—search first.
```

## Arbeitsablauf

1. Ziel-Workspace und Parent klären.
2. Bei DB: Schema abrufen.
3. Search auf Duplikate.
4. Create/Update ausführen.
5. URL und Changelog zurück.
6. Bei Query: Markdown-Tabelle.
7. Freigabe bei company-wide Parent.

## Qualitätskriterien / Definition of Done

- [ ] Korrekte Parent/DB
- [ ] Schema-konforme Properties
- [ ] Changelog vorhanden
- [ ] Kein Löschen ohne DELETE confirm
- [ ] URLs funktionsfähig

## Sicherheit & Freigaben

- Integration token nur OAuth.
- Gastzugriff nicht erweitern.
- HR-Daten nur in geschützten Spaces.

## Fallstricke

- Relation-Property ohne Ziel-ID.
- Markdown-Block-Limits.
- Duplikat-Seiten bei schlechter Search.
- Zeitzone in Date-Properties.
- API Rate limit bei Bulk.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Meeting Note unter Team-Parent.
- **Input:** Parent URL, Titel, Bullet Notes MD.
- **Prompt:**

```text
Search duplicates; create page under parent; return url and changelog.
```

- **Erwartetes Ergebnis:**

```text
notion.so/.../Meeting-2026-11-23; changelog: created; no duplicate found.
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Tasks DB offene Items.
- **Input:** DB id, Status=Open.
- **Prompt:**

```text
Query database filter Status Open; markdown table top 20.
```

- **Erwartetes Ergebnis:**

```text
tasks_open.md table with Name, Assignee, Due columns.
```