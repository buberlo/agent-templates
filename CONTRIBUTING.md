# Beitragen

1. Branch von `main`, Änderungen in `domains/` oder Schema/Script.
2. Pro logischer Änderung ein Template oder ein Schema-Update — keine Misch-PRs mit unrelated Inhalt.
3. Immer `python3 scripts/validate_and_index.py` ausführen und generierte `INDEX.md` / `catalog.json` committen.
4. **Sprache:** Deutsche Fließtexte in README und Template-Beschreibungen; technische IDs und System-Prompts Englisch oder zweisprachig wo sinnvoll.
5. Keine API-Keys, Kundennamen oder echten personenbezogenen Daten in Beispielen.
6. `risk_level` ehrlich setzen; bei `high` klare Human-in-the-loop-Schritte dokumentieren.

Review-Fokus: Tool-Stack plausibel und aktuell, DoD prüfbar, Prompt kopierfertig.