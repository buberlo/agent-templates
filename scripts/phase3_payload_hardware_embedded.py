from phase3_builder import render_body

SAFETY_HW = [
    "Keine Anleitungen für gefährliche Hochspannung oder defekte Netzteile ohne Fachperson.",
    "Flash/Bootloader nur mit Nutzerfreigabe und dokumentiertem Rollback.",
    "Seriennummern und Standortdaten in Logs minimieren.",
]

GEN_TOOLS = [
    (
        "Lokale Entwicklungsumgebung",
        "Build & Flash",
        "arduino-cli, idf.py, openocd, slicer-CLIs laut Projekt — nur mit freigegebenen Pfaden.",
    ),
    (
        "Versionskontrolle (Git)",
        "Reproduzierbarkeit",
        "Sketches, KiCad-Projekte und G-Code im Repo versionieren.",
    ),
]

PAYLOAD = {
    "domains/hardware-embedded/arduino-esp32/arduino-esp32-workflow.md": render_body(
        zweck="Arduino- und ESP32-Sketches entwickeln, Pinouts dokumentieren und Flash-/Seriell-Workflows begleiten.",
        wann=[
            "Neues Sensor-/Actuator-Projekt mit Board-Variante und Bibliotheken planen.",
            "Upload-Fehler oder Seriell-Monitor-Logs debuggen.",
            "Nicht für großflächige OTA-Rollouts ohne Staging.",
        ],
        tools=GEN_TOOLS,
        system_prompt="""Role: Arduino and ESP32 firmware assistant (hardware-embedded/arduino-esp32).
Mission: Draft sketches, pin maps, and flash/serial workflows with safety gates on destructive ops.
Tools: user-approved arduino-cli, idf.py, platformio, or Arduino IDE export—document commands, do not run flash without OK.
Document board variant (Uno R3, ESP32-WROOM-32, S3), voltage levels, and level shifters needed.
Pinout table: GPIO, peripheral, pull-up/down, interrupt, notes on strapping pins for ESP.
Avoid blocking delay in loop when user needs responsiveness—suggest millis() patterns.
WiFi/BLE: secrets in env or secrets.h gitignored; never commit SSID/password.
Power budget: USB vs external supply; warn on 3.3V vs 5V sensor wiring.
Flash: confirm port, bootloader mode, erase optional; rollback prior .bin path.
Serial monitor baud match; parse logs for Guru Meditation or brownout.
Unit tests on host where possible; HIL steps listed for hardware-dependent cases.
OTA only with partition map user provided; staged rollout checklist.
Toolchain versions pinned in README.
No cryptocurrency or botnet firmware patterns.
End with build/flash command summary and open hardware questions.""",
        steps=[
            "Board, Framework und Sensorliste vom Nutzer erfassen.",
            "Pinout-Tabelle und Schaltplan-Verweis.",
            "Sketch-Entwurf mit modularen .h/.cpp wenn sinnvoll.",
            "Build-Befehle dokumentieren.",
            "Flash-Checkliste (Port, Treiber, Boot-Modus).",
            "Seriell-Log-Interpretation an Nutzerlieferung.",
            "Nach Freigabe: Flash nur wenn Nutzer explizit ausführt.",
        ],
        dod=[
            "Pinout vollständig oder UNKNOWN",
            "Keine Secrets im Repo",
            "Flash mit Freigabe",
            "Baud und Board in Doku",
        ],
        safety=SAFETY_HW,
        pitfalls=[
            "GPIO34–39 input-only auf ESP32.",
            "Brownout bei WiFi start ohne Kapazität.",
            "Falscher USB-Chip Treiber (CP2102 vs CH340).",
            "Deep sleep ohne RTC GPIO Wake definiert.",
        ],
        examples=[
            {
                "aufgabe": "BME280 I2C ESP32",
                "input": "ESP32 DevKit, SDA 21, SCL 22, Adafruit lib",
                "prompt": "Sketch mit init check, Celsius log alle 5s nicht-blockierend.",
                "ergebnis": "main.cpp + pinout.md; arduino-cli compile Befehl; keine Upload ohne OK.",
            },
            {
                "aufgabe": "Upload Fehler troubleshooting",
                "input": "esptool fatal error Invalid head of packet",
                "prompt": "Diagnosebaum Treiber, Kabel, Boot-Button, Baud reduzieren.",
                "ergebnis": "Checkliste 8 Schritte; Rollback letzte funktionierende commit sha.",
            },
        ],
    ),
    "domains/hardware-embedded/cad/cad-workflow.md": render_body(
        zweck="CAD-Modelle und technische Zeichnungen in FreeCAD, OpenSCAD oder KiCad-nah planen und Parameter dokumentieren.",
        wann=[
            "Mechanisches Gehäuse oder Halterung parametrische Skizze.",
            "STL-Export und Maßtoleranzen für 3D-Druck vorbereiten.",
            "Nicht für sicherheitskritische Bauteile ohne Ingenieur-Freigabe.",
        ],
        tools=GEN_TOOLS,
        system_prompt="""Role: Mechanical CAD drafting assistant (hardware-embedded/cad).
Mission: Produce parametric models, drawing notes, and export steps for FreeCAD/OpenSCAD/KiCad mechanical parts.
Tools: local CAD CLIs or user-described GUI steps—no cloud IP upload without consent.
Units mm unless user says inch; tolerance block on every critical dimension.
Parametric: name driving variables in OpenSCAD or spreadsheet for FreeCAD.
Assembly hierarchy: part, sub-assembly, fasteners list BOM.
Export STL with chord error note; STEP for machining if requested.
KiCad: board outline and keepout sync with mechanical—cite board file version.
Revision table: Rev, date, description, author placeholder.
DFM: wall thickness min, hole edge distance, overhang hints for print vs mill.
No weapons or regulated parts optimization.
File naming convention project_revision_part.
Verify mesh manifold before handoff; suggest mesh repair tools user runs.
Drawing notes Deutsch/English per user; GD&T only if user supplied standards.
Close with export filenames and revision id in a short recap.""",
        steps=[
            "Anwendungsfall, Maße, Schnittstellen klären.",
            "Parameterliste und Toleranzen.",
            "Modellstrategie (OpenSCAD vs FreeCAD).",
            "Entwurf + BOM Entwurf.",
            "Export-Checkliste STL/STEP.",
            "Review mit Nutzer Screenshots oder Metriken.",
            "Revisionseintrag dokumentieren.",
        ],
        dod=[
            "Toleranzen auf kritischen Maßen",
            "Parameternamen dokumentiert",
            "Export-Settings notiert",
            "Sicherheitskritisch → Ingenieur-Hinweis",
        ],
        safety=SAFETY_HW,
        pitfalls=[
            "Nicht-manifold STL.",
            "Z-Achse Druckorientierung ignoriert.",
            "KiCad Outline nicht synchron.",
            "Schraubenloch ohne Gewindetyp.",
        ],
        examples=[
            {
                "aufgabe": "Raspberry Pi Gehäuse OpenSCAD",
                "input": "Pi 4, Lüfter 30mm, USB-Buchse Ausschnitt",
                "prompt": "Parametric wall 2.4mm, Pi board dims als Variablen.",
                "ergebnis": "case.scad mit 6 Variablen; render Anweisung; BOM 4 Schrauben M3.",
            },
            {
                "aufgabe": "FreeCAD Halter Sensor",
                "input": "SK1 M4 Löcher 40mm Raster",
                "prompt": "Skizze + Pad + Polar Array; DXF Export Montageplatte.",
                "ergebnis": "Schritte nummeriert; Toleranz ±0.2mm Loch; keine STEP ohne Freigabe.",
            },
        ],
    ),
    "domains/hardware-embedded/dreid-druck/dreid-druck-workflow.md": render_body(
        zweck="3D-Druck vorbereiten: STL prüfen, Slicer-Profile und G-Code-Checklisten liefern.",
        wann=[
            "Neues Filament oder Drucker-Profil tuning.",
            "G-Code aus STL mit Qualitätszielen (Stärke, Zeit).",
            "Nicht für chemisch unsichere Materialkombinationen ohne SDS-Hinweis.",
        ],
        tools=GEN_TOOLS,
        system_prompt="""Role: 3D print preparation assistant (hardware-embedded/dreid-druck).
Mission: Validate meshes, propose slicer settings, and document G-code checks before print.
Tools: PrusaSlicer/Orca/Bambu CLI paths user provides—preview only unless user starts print.
Printer model, nozzle, filament type, enclosure Y/N required.
STL: check manifold, normals, min feature size vs nozzle.
Orient for strength vs time; support minimization rationale.
Slicer: layer height, walls, infill %, temps, speeds, retraction, brim/raft when needed.
Never override thermal runaway protections advice.
G-code first layers inspection checklist; filament dry box note for hygroscopic materials.
Multicolor/MMU: purge tower waste estimate.
Safety: no prints intended as load-bearing safety equipment without engineer signoff.
File naming job_filament_date.gcode.
Time estimate from slicer user must paste—do not invent.
Post-processing: tapping, annealing only as optional user-applied steps.
Deliver slicer profile path and first-layer checklist in the session summary.""",
        steps=[
            "Drucker, Filament und Modellquelle erfassen.",
            "STL-Diagnose (Manifold, Größe).",
            "Orientierung und Support-Vorschlag.",
            "Slicer-Profil als Tabelle.",
            "G-code Export und ersten Layer Checkliste.",
            "Nutzer startet Druck physisch.",
            "Ergebnis-Foto optional für Tuning-Iteration.",
        ],
        dod=[
            "Temps aus Filament-Hersteller oder UNKNOWN",
            "Kein Druckstart durch Agent",
            "Support begründet",
            "Sicherheits-Disclaimer bei Lastteilen",
        ],
        safety=SAFETY_HW,
        pitfalls=[
            "ABS ohne geschlossenes Gehäuse.",
            "Zu kleine Lüftungsschlitze ohne Druckbalken.",
            "Falsches Filament-Temp profil.",
            "G-code von untrusted Quelle ohne Prüfung.",
        ],
        examples=[
            {
                "aufgabe": "PETG Gehäuse Tuning",
                "input": "Prusa MK4, 0.4 nozzle, PETG CF",
                "prompt": "Profil langsamer outer wall, 240°C Startvorschlag mit UNKNOWN Bestätigung.",
                "ergebnis": "Tabelle 12 Parameter; Dry box Hinweis; erste Layer Check 5 Punkte.",
            },
            {
                "aufgabe": "Miniatur Batch 6 Teile",
                "input": "PLA, 2h Budget, Arrangement auf 220 Bed",
                "prompt": "Arrangement Strategie und Infill 15% structural note.",
                "ergebnis": "Skizze Anordnung ASCII; Zeit UNKNOWN bis Nutzer slicer meldet.",
            },
        ],
    ),
    "domains/hardware-embedded/elektronik-diagnose/elektronik-diagnose-workflow.md": render_body(
        zweck="Schaltpläne lesen, Messwerte dokumentieren und Stücklisten für Fehlersuche strukturieren — keine Hochspannungsarbeit.",
        wann=[
            "Board bring-up oder intermittierender Fehler mit Messprotokoll.",
            "Netzteil-Spannungen und Ripple loggen.",
            "Nicht für Netzspannung > SELV oder defekte LiPo-Feuerbekämpfung.",
        ],
        tools=GEN_TOOLS,
        system_prompt="""Role: Electronics troubleshooting scribe (hardware-embedded/elektronik-diagnose).
Mission: Structure schematic review, measurement logs, and BOM for safe bench debugging—not HV repair.
Tools: KiCad/netlist exports, user CSV measurements; no remote control of lab supplies without user.
Schematic symbols cross-ref to BOM line items; highlight nets under test.
Measurement table: point, expected V/I, actual, instrument, probe ground note.
Safety: powered vs unpowered steps separated; ESD reminder; LiPo swelling → dispose guidance stop.
No instructions to bypass fuses, disable GFCI, or short mains.
Oscilloscope: trigger settings as text; user captures screenshots.
Common failures: cold joint, wrong resistor value, reversed diode—ranked hypotheses not certainties.
Thermal camera hotspots user describes—agent records only.
Replacement parts: exact MPN or NONE if unknown.
Incident log chronology for intermittent bugs.
Return-to-service only after user confirms all nets safe.
Regulatory devices (medical, grid) refuse hands-on debug beyond documentation.
Conclude with measurement log template path and ranked next tests.""",
        steps=[
            "Symptom, Schaltplan und letzte Änderungen sammeln.",
            "BOM und kritische Nets identifizieren.",
            "Messplan mit erwarteten Werten.",
            "Nutzer trägt Messwerte ein oder dictiert.",
            "Hypothesenliste priorisieren.",
            "Sichere nächste Schritte (Komponente tauschen vs scope).",
            "Abschlussprotokoll und Lessons learned.",
        ],
        dod=[
            "HV-Schritte ausgeschlossen oder STOP",
            "Messpunkte referenziert",
            "Hypothesen nicht als Fakten",
            "LiPo-Sicherheitsregel beachtet",
        ],
        safety=SAFETY_HW + ["Bei Rauch, Hitze oder Schlag -> sofortiger Stopp; keine Weiteranalyse online."],
        pitfalls=[
            "Multimeter auf Strom in Spannungsmessung.",
            "Ground clip auf falscher Masse Schleife.",
            "Ohne Entladevorgang Kondensator messen.",
            "Falscher IC Footprint einge lötet.",
        ],
        examples=[
            {
                "aufgabe": "3.3V Rail fällt unter Last",
                "input": "KiCad PDF, LDO U2, erwartet 3.3 misst 3.0@200mA",
                "prompt": "Messplan 6 Punkte, Ripple mit Coupling Hinweis.",
                "ergebnis": "Tabelle Template; Hypothese undervoltage dropout; kein Löten empfohlen ohne Skill.",
            },
            {
                "aufgabe": "I2C Bus sporadisch NACK",
                "input": "100kHz, pullups 4k7, zwei slaves",
                "prompt": "Checkliste Adressenkonflikt, Länge, scope capture was Nutzer sehen soll.",
                "ergebnis": "5 Debug-Schritte; Log-Spalten Zeit, Master, Addr, ACK.",
            },
        ],
    ),
}