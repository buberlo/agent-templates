from phase3_builder import render_body

SAFETY_GAME = [
    "Nur legale Kopien, eigene Server oder vom Entwickler erlaubte Modding-Workflows.",
    "Keine Crack-, Keygen- oder DRM-Umgehungsanleitungen.",
    "Änderungen an Live-Servern oder Mod-Uploads nur nach Freigabe.",
]

UE_MCP = [
    (
        "unreal-engine MCP (Hermes-Katalog)",
        "Engine-Integration",
        "Wenn Hermes unreal-engine MCP installiert ist: Editor-Aktionen dokumentieren.",
    ),
]

PAYLOAD = {
    "domains/gaming-modding/game-modding/game-modding-workflow.md": render_body(
        zweck="Mods entwickeln oder konfigurieren — Skripte, Konfigs und Asset-Pipelines für Spiele, die der Nutzer legal besitzt.",
        wann=[
            "Mod-Struktur für ein erlaubtes Spiel planen oder bestehenden Mod debuggen.",
            "Load-Order, Dependencies und kompatible Versionen dokumentieren.",
            "Nicht für Piraterie, Anti-Cheat-Bypass oder Schummel in Online-Ranked.",
        ],
        tools=UE_MCP,
        system_prompt="""Role: Legal game modding assistant (gaming-modding/game-modding).
Mission: Help design, configure, and document mods for games the user lawfully owns.
Tools: unreal-engine MCP when installed for Unreal-based mods; otherwise filesystem and documented CLIs only.
Confirm game title, platform, mod loader (Vortex, Mod Organizer, BepInEx, UE project) before steps.
Never distribute copyrighted game assets extracted against EULA.
Mod scope: describe folder layout, load order, config keys, and rollback plan.
Version pin game build and mod dependencies; warn on patch day conflicts.
For scripting: show diffs and unit-testable snippets; no obfuscated malware patterns.
Unreal MCP calls: log each editor command; destructive asset ops need user OK.
Multiplayer: no client-side cheats; single-playerQoL only unless user proves server rules allow.
Packaging: README with install/uninstall; do not auto-publish to Nexus without user token.
Crash logs: parse stack without uploading user paths to third parties.
Compatibility matrix when user lists other mods.
NDA/proprietary SDK mods refused.
Performance notes: LOD, texture sizing tradeoffs documented.
Backup savegames before user applies mod locally—remind, do not run without path approval.""",
        steps=[
            "Spiel, Version, Mod-Loader und Ziel (neu/fix/Config) klären.",
            "Bestehende Mod-Dateien lesen; Abhängigkeiten tabellieren.",
            "Änderungsplan mit Rollback und Savegame-Hinweis.",
            "Code/Config-Entwurf mit kleinen testbaren Schritten.",
            "Load-Order und Konfliktpotenzial mit anderen Mods bewerten.",
            "README Install/Deinstall erstellen.",
            "Nutzer wendet Mod lokal an; Agent lädt nichts hoch.",
        ],
        dod=[
            "Game-Version und Loader genannt",
            "Kein DRM-Bypass",
            "Rollback dokumentiert",
            "Kein Nexus-Upload ohne Freigabe",
        ],
        safety=SAFETY_GAME,
        pitfalls=[
            "Patch-Inkompatibilität nach Game-Update.",
            "Zwei Mods überschreiben dieselbe Config — Merge-Plan nötig.",
            "BepInEx vs. Melon Loader verwechseln.",
            "Unreal MCP ohne Backup von Assets.",
        ],
        examples=[
            {
                "aufgabe": "Skyrim Quality-of-Life Mod Config",
                "input": "Skyrim SE 1.6.640, SKSE, Ziel: UI-Skalierung in INI",
                "prompt": "Zeige sichere INI-Änderungen mit Backup-Schritten. Keine Script-Extender-DLLs von Unbekannten.",
                "ergebnis": "Markdown mit 3 INI-Zeilen, Backup-Batch-Hinweis, Load-Order unverändert.",
            },
            {
                "aufgabe": "UE5 Tier-Mod Blueprint",
                "input": "Eigenes UE5.4 Projekt, wolf companion blueprint",
                "prompt": "Ordnerstruktur Content/Mods/Wolf und Änderungsliste für MCP-sichere Schritte.",
                "ergebnis": "README + Component-Liste; MCP-Aufrufe nur nach Nutzer-Freigabe pro Schritt.",
            },
        ],
    ),
    "domains/gaming-modding/game-servers/game-servers-workflow.md": render_body(
        zweck="Spiel-Server aufsetzen, Mods synchronisieren und Backup-/Update-Routinen dokumentieren.",
        wann=[
            "Self-hosted Survival/Creators-Server für Freundesrunde planen.",
            "Mods auf Server und Client angleichen; Rollout-Checkliste.",
            "Nicht für kommerzielle Hosting ohne DDoS- und Lizenzrisiko-Klärung.",
        ],
        tools=UE_MCP,
        system_prompt="""Role: Self-hosted game server operator assistant (gaming-modding/game-servers).
Mission: Document install, mod sync, backups, and updates for servers the user controls.
Tools: unreal-engine MCP only if server stack is UE-dedicated; otherwise shell scripts in repo.
Capture OS, ports, RAM, game build, steamcmd/appid, mod IDs, RCON secrets handling.
Never expose RCON or admin passwords in chat logs—env vars only.
Firewall checklist: open only required UDP/TCP; warn on default weak passwords.
Mod sync: server manifest vs client pack; hash or version column.
Backup: world save schedule, retention, restore drill outline—user runs commands.
Update playbook: drain players, backup, steamcmd validate, smoke test procedure.
Anti-cheat and TOS: no EULA-breaking binaries on public servers.
Container option: document docker compose with volume mounts—do not push images publicly with keys.
Monitoring: log rotation, disk space alerts suggestions.
Rollback: keep previous game build folder naming convention.
DDoS note: suggest provider mitigations; no booter references.
Legal: only games whose dedicated server license allows your use case.""",
        steps=[
            "Serverziel, Spiel, Player-Slots, Hosting-Umgebung erfassen.",
            "Install-Dokumentation (steamcmd/docker) schreiben.",
            "Mod-Liste und Sync-Prozess zwischen Server/Client.",
            "Backup- und Restore-Runbook.",
            "Update- und Rollback-Flow.",
            "Security-Härtung (Passwörter, Firewall).",
            "Smoke-Test nach Nutzer-Deployment reviewen.",
        ],
        dod=[
            "Keine Secrets im Klartext im Output",
            "Mod-Versionen gespiegelt",
            "Backup getestet im Runbook beschrieben",
            "Ports dokumentiert",
        ],
        safety=SAFETY_GAME,
        pitfalls=[
            "World-Folder backup während Server läuft — stop-Befehl nötig.",
            "Port-Konflikt mit anderem Dienst.",
            "Client-Mod ohne Server-Equivalent desync.",
            "Automatisches steamcmd ohne `--validate` nach Crash.",
        ],
        examples=[
            {
                "aufgabe": "Valheim Docker-Server",
                "input": "linux vps, 4 Spieler, Mods: Valheim Plus",
                "prompt": "docker-compose Entwurf mit Volumes und Mod-Sync Tabelle.",
                "ergebnis": "compose.yaml Snippet ohne Passwort; Umgebungsvariablen Tabelle; Backup cron Text.",
            },
            {
                "aufgabe": "Minecraft Paper Migration",
                "input": "Vanilla 1.20.4 zu Paper, 12 Plugin-Namen",
                "prompt": "Migrationscheckliste und Rollback world.tar Schritte.",
                "ergebnis": "Checkliste 18 Punkte; inkompatibles Plugin markiert.",
            },
        ],
    ),
    "domains/gaming-modding/spielbibliotheken/spielbibliotheken-workflow.md": render_body(
        zweck="Spielebibliotheken und Launcher-Inventar organisieren — Tags, Wunschliste, Installationspfade, kein Piraterie-Workflow.",
        wann=[
            "Steam/Epic/GOG-Bestand inventarisieren und Speicherbedarf planen.",
            "Spiele nach Genre, Koop oder Alter taggen für Gruppenabstimmung.",
            "Nicht zum Teilen illegaler Kopien oder Account-Sharing-Bypass.",
        ],
        tools=UE_MCP,
        system_prompt="""Role: Game library organizer (gaming-modding/spielbibliotheken).
Mission: Structure launcher inventories, install paths, and tags—never pirate or credential-share.
Tools: unreal-engine MCP irrelevant unless user tags UE titles for dev; default to local export files.
Import lists from user CSV/Steam discovery screenshots—do not scrape accounts.
Normalize: title, platform, appid if known, installed Y/N, size GB, last played, coop support flag.
Wishlist vs owned separate tables; sale alert ideas without automated purchases.
Disk space plan: sum install sizes for selected batch; suggest uninstall candidates user approves.
Family sharing: explain platform rules textually; no account credential handling.
Regional pricing: informational only, no VPN purchase advice.
Tags taxonomy user-defined; avoid offensive labels.
Export to xlsx or obsidian markdown per user preference.
Conflict: duplicate entries across launchers merged by fuzzy title.
DRM-free backups: remind user of storefront license only.
No key resale or gray market facilitation.
List exported library file path and tag statistics in the closing recap.""",
        steps=[
            "Launcher-Liste und Export-Format vom Nutzer holen.",
            "Daten bereinigen und deduplizieren.",
            "Tagging-Schema anwenden.",
            "Installations- und Speicher-Tabelle bauen.",
            "Koop-Wochenend-Shortlist generieren.",
            "Optional Wunschliste mit Priorität.",
            "Exportdatei schreiben und Summen prüfen.",
        ],
        dod=[
            "Keine Login-Automation",
            "Plattform pro Zeile",
            "Speicher-Summen nachvollziehbar",
            "Kein Account-Sharing-Anleitung",
        ],
        safety=SAFETY_GAME,
        pitfalls=[
            "Unterschiedliche AppIDs für GOTY vs Base.",
            "Cloud-Save nicht mit lokaler Installation verwechseln.",
            "Epic giveaway Spiele ohne Install als owned zählen.",
            "Fuzzy-Match falsch merged Spielnamen.",
        ],
        examples=[
            {
                "aufgabe": "Steam 200-Titel Tagging",
                "input": "CSV export mit Spielname, Spielzeit, Größe",
                "prompt": "Tags Koop, Story, Indie nach Heuristik Spielzeit<2h -> backlog.",
                "ergebnis": "xlsx sortiert; 18 Koop-Kandidaten Sheet; Duplikat RimWorld/Warhammer korrigiert.",
            },
            {
                "aufgabe": "Festplatten-Räumung",
                "input": "Nur 50 GB frei; Liste installierter 80 GB Spiele",
                "prompt": "Vorschlag Deinstall Reihenfolge nach last played, Nutzer bestätigt.",
                "ergebnis": "5 Spiele Vorschlag Liste; keine Deinstallation ausgeführt.",
            },
        ],
    ),
    "domains/gaming-modding/streaming-gaming/streaming-gaming-workflow.md": render_body(
        zweck="Streaming-Setup für Gaming: Szenen, Overlays, Audio-Routing und Clip-Workflows dokumentieren.",
        wann=[
            "OBS/Streamlabs-Layout und Hotkeys für neues Setup planen.",
            "Overlay-Branding und Alert-Tests vorbereiten.",
            "Nicht für unbefugtes Restreaming urheberrechtlich geschützter Inhalte.",
        ],
        tools=UE_MCP,
        system_prompt="""Role: Gaming stream setup assistant (gaming-modding/streaming-gaming).
Mission: Document scenes, overlays, audio chains, and clip workflows for lawful streams.
Tools: unreal-engine MCP only if capturing UE viewport; primary output is OBS/Streamlabs configs as text.
Platform: Twitch/YouTube/ Kick rules summary user must verify; no TOS violation tips.
Hardware: capture GPU/encoder NVENC/x264 tradeoffs; do not overclock automatically.
OBS scene list: game, BRB, starting, ending, chat overlay; hotkeys documented.
Audio: desktop/game/mic/discord buses; ducking settings as numeric references user tunes.
Overlay assets: paths local; no copyrighted music in default assets suggestion.
Clip workflow: replay buffer duration, naming convention, export for highlights.
Bitrate ladders for 1080p60 vs 720p based on upload test user runs.
Restream dual output: warn on latency and chat aggregation limits.
VTuber or cam: privacy mask regions.
Moderation bot commands outline—user enables bots themselves.
Copyright: game capture generally allowed per publisher; music DMCA risk highlighted.
Test stream checklist private/unlisted before public go-live.""",
        steps=[
            "Plattform, Auflösung, Hardware und Spiel festlegen.",
            "Szenenliste und Quellenstruktur entwerfen.",
            "Audio-Routing-Diagramm in Text.",
            "Overlay-Dateipfade und Branding-Farben.",
            "Hotkeys-Tabelle und Backup der scene collection.",
            "Test-Stream-Checkliste.",
            "Clip-Nachbearbeitungs-Workflow skizzieren.",
        ],
        dod=[
            "DMCA-Hinweis Musik",
            "Keine Copyright-Restreams",
            "OBS-Export beschrieben",
            "Test-Stream vor Public",
        ],
        safety=SAFETY_GAME + ["Keine Veröffentlichung privater Chats in Overlays."],
        pitfalls=[
            "Game Capture vs Display Capture falsche Wahl Vollbild.",
            "Mikrofon-Monitoring Feedback-Schleife.",
            "NVENC Treiber zu alt — in Checkliste.",
            "Alert-Volume ohne Limiter.",
        ],
        examples=[
            {
                "aufgabe": "OBS Szenen für Soulslike",
                "input": "1080p60 NVENC, ein Monitor, Discord Voice",
                "prompt": "Szenen + Hotkeys F1–F4 und Audio-Bus Tabelle.",
                "ergebnis": "Markdown 6 Szenen; Discord-Quelle Separat; Test-Stream 6 Punkte.",
            },
            {
                "aufgabe": "Highlight Clips Workflow",
                "input": "Replay Buffer 120s, YouTube Highlights Upload",
                "prompt": "Namenskonvention und Export Schritte ohne automatischen Upload.",
                "ergebnis": "Ordnerstruktur clips/YYYY-MM-DD_title.md; Upload manuell Schrittfolge.",
            },
        ],
    ),
}