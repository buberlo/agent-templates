# Generischer System-Prompt-Export

1. Datei `categories/<category>/<template>.md` öffnen.
2. Frontmatter als strukturierte Metadaten (JSON/YAML) für ein beliebiges Agent-Framework exportieren:
   - Felder: `id`, `title`, `category`, `tags`, `required_tools`, `risk_level`, `version`.
3. **System-Prompt zusammenstellen** (empfohlenes Layout):

```text
[ROLE]
<title> — <Zweck in einem Satz>

[TOOLS]
<Liste aus required_tools: name + wann nutzen>

[WORKFLOW]
<Arbeitsablauf nummeriert>

[QUALITY]
<Qualitätskriterien / DoD>

[SAFETY]
<Sicherheit & Freigaben>
```

4. Abschnitt **System-Prompt / Instruktionen** bleibt die kanonische Kurzfassung für Copy-Paste.
5. Vor Produktion: `python3 scripts/validate_and_index.py` und `catalog.json` als Maschinenlesbare Übersicht nutzen.