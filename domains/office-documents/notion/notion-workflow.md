---
id: notion-workflow
title: "Notion-pages and databases pflegen"
domain: office-documents
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
  - "pages-URL or Datenbank-ID"
  - "Inhalts- or Filterauftrag"
outputs:
  - "Aktualisierte Notion-pages"
  - "Query-result as Markdown"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

**Notion-Wikis and Task-DBs** over MCP durchsuchen, pages erstellen/aktualisieren—Integration with OAuth, changes nachvollziehbar.

## When to use

- Team-Wiki in Notion is Source of Truth.
- Agent should Meeting Notes or DB-Eintraege anlegen.
- Recherche-resultse strukturiert in Notion landen.

**When not to use**

- GDPR-kritische Daten without DPA with Notion.
- Vollstaendiger Ersatz for Obsidian/Git offline.
- Loeschen alter pages without Archiv-Policy.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| Notion MCP | CRUD | Official Connector |
| notion-search | Finden | Pages/DBs |
| MarkItDown | Export | Backup optional |

## System prompt

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

## Workflow

1. Target-Workspace and Parent clarify.
2. at DB: Schema abrufen.
3. Search on Duplikate.
4. Create/Update ausfuehren.
5. URL and Changelog zurueck.
6. at Query: Markdown-Tabelle.
7. approval at company-wide Parent.

## Definition of done

- [ ] Korrekte Parent/DB
- [ ] Schema-konforme Properties
- [ ] Changelog vorhanden
- [ ] no Loeschen without DELETE confirm
- [ ] URLs funktionsfaehig

## Security

- Integration token only OAuth.
- Gastzugriff not erweitern.
- HR-Daten only in geschuetzten Spaces.

## Pitfalls

- Relation-Property without Target-ID.
- Markdown-Block-Limits.
- Duplikat-pages at schlechter Search.
- Zeitzone in Date-Properties.
- API Rate limit at Bulk.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Meeting Note unter Team-Parent.
- **Input:** Parent URL, Titel, Bullet Notes MD.
- **Prompt:**

```text
Search duplicates; create page under parent; return url and changelog.
```

- **Expected result:**

```text
notion.so/.../Meeting-2026-11-23; changelog: created; no duplicate found.
```

### Example 2 (Example data (self-written))
- **Task:** Tasks DB offene Items.
- **Input:** DB id, Status=Open.
- **Prompt:**

```text
Query database filter Status Open; markdown table top 20.
```

- **Expected result:**

```text
tasks_open.md table with Name, Assignee, Due columns.
```