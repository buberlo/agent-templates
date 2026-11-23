#!/usr/bin/env python3
"""Replace shared German _category.md boilerplate with English."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOMAINS = ROOT / "domains"

OLD_PITFALLS = """## Pitfalls

- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Keine stillen Zahlungen, Trades oder Ueberweisungen.
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern)."""

NEW_PITFALLS = """## Pitfalls

- Do not put tokens or passwords in chat, skill files, or custom MCP command arguments. Grok Bot wiki: OAuth tokens stay on the connector backend; command servers must not put credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- No silent payments, trades, or transfers.
- Skills are workflows/instructions (progressive disclosure); MCPs are connections and tools. Combine both; do not conflate them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/skills the task needs. Hermes filters via include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Write, send, pay, deploy, or delete only after explicit approval; good document skills require a verify step (re-read the file, render PDF/PNG)."""

REPLACEMENTS = [
    ("| nein (so belegt) |", "| no (as cited) |"),
    ("| ja |", "| yes |"),
    ("| Typ |", "| Type |"),
    ("Quelle:", "Source:"),
    ("Quellen:", "Sources:"),
]


def main() -> None:
    count = 0
    for path in DOMAINS.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        orig = text
        if OLD_PITFALLS in text:
            text = text.replace(OLD_PITFALLS, NEW_PITFALLS)
        for a, b in REPLACEMENTS:
            text = text.replace(a, b)
        if text != orig:
            path.write_text(text, encoding="utf-8")
            count += 1
    print(f"Updated {count} files.")


if __name__ == "__main__":
    main()