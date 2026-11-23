from phase3_builder import render_body

SAFETY_HEALTH = [
    "Keine medizinische Diagnose, Therapie oder Notfallsteuerung — bei akuten Symptomen 112/Notdienst.",
    "Gesundheitsdaten minimieren und nicht an Dritte senden.",
    "Strava oder andere APIs nur mit Nutzer-OAuth.",
]

STRAVA = [
    (
        "strava MCP (Hermes-Katalog)",
        "Aktivitätsdaten",
        "Nur mit installiertem und autorisiertem Strava MCP.",
    ),
]

PAYLOAD = {
    "domains/gesundheit-fitness/ernaehrung/ernaehrung-workflow.md": render_body(
        zweck="Mahlzeitenplanung, Nährwert-Schätzungen und Einkaufslisten — Lifestyle, keine klinische Ernährungstherapie.",
        wann=[
            "Wochenplan unter Kalorien-/Makroziel mit Vorlieben und Ausschlüssen.",
            "Einkaufsliste aus Rezeptliste generieren.",
            "Nicht bei Essstörungen, Schwangerschaftsdiät oder insulinpflichtigem Diabetes ohne Fachkraft.",
        ],
        tools=STRAVA,
        system_prompt="""Role: Meal planning assistant (gesundheit-fitness/ernaehrung).
Mission: Build meal plans, grocery lists, and rough macro estimates—no medical nutrition therapy.
Tools: strava MCP only if user wants calorie burn cross-check with activity data and OAuth is active.
Collect allergies, cultural/ethical diet, budget, cooking time, equipment—not diagnoses.
Macro targets user-supplied goals; label estimates APPROXIMATE using standard tables.
No weight-loss guarantees; no eating disorder enabling (extreme restriction refused gently).
Recipes: cite sources or generic staples; portion sizes explicit.
Grocery list grouped by store aisle; metric units default DE.
Substitutions for allergens flagged inline.
Meal prep batching suggestions with fridge life notes—not food safety certification.
Strava: compare weekly burn vs intake only if user links data; do not infer medical calories needs.
Supplements: informational caution—refer to physician.
Hydration reminders optional—not clinical fluid prescription.
Children menus: general family-friendly ideas; pediatric rules out of scope.
Language German for recipes unless user prefers EN.
Log disclaimers on every export file header.""",
        steps=[
            "Ziele, Ausschlüsse und Kochzeit budgetieren.",
            "7-Tage Raster mit Frühstück/Mittag/Abend vorschlagen.",
            "Makro-Schätzung pro Tag (optional).",
            "Einkaufsliste aggregieren.",
            "Strava-Abgleich nur wenn autorisiert.",
            "Nutzer passt Portionen an.",
            "Export Markdown oder xlsx nach Freigabe.",
        ],
        dod=[
            "Allergie-Hinweise pro Rezept",
            "Keine Diagnose oder Therapie",
            "Makros als Schätzung markiert",
            "Notfall-Hinweis bei klinischen Themen",
        ],
        safety=SAFETY_HEALTH,
        pitfalls=[
            "Nüsse bei unbekannter Allergie nicht defaulten.",
            "Extreme Kaloriendefizite nicht planen.",
            "Roh-Fleisch Kreuzkontamination nicht ignorieren — Kochtemperatur-Hinweis.",
            "Strava ohne OAuth aktivieren.",
        ],
        examples=[
            {
                "aufgabe": "Vegetarischer Wochenplan Büro",
                "input": "2000 kcal Ziel, keine Erdnüsse, 30 Min Kochzeit/Abend",
                "prompt": "5 Abendessen mit Prep, Einkaufsliste DE Supermarkt Gänge.",
                "ergebnis": "Markdown Plan + Liste 28 Zutaten; kcal als Schätzung markiert.",
            },
            {
                "aufgabe": "Makro-Abgleich mit Strava",
                "input": "OAuth aktiv, letzte Woche 2200 kcal Ø Verbrauch laut User",
                "prompt": "Plane leichte Defizit 300 kcal nur wenn User explizit abnimmt.",
                "ergebnis": "Tagesplan angepasst; Disclaimer kein medizinischer Rat.",
            },
        ],
    ),
    "domains/gesundheit-fitness/fitness-training/fitness-training-workflow.md": render_body(
        zweck="Trainingspläne, Periodisierung und Tracking-Auswertung — keine sportmedizinische Freigabe.",
        wann=[
            "Kraft- oder Ausdauerplan für gesunden aktiven Erwachsenen mit Nutzerangaben.",
            "Strava-Aktivitäten für Wochenreview auswerten.",
            "Nicht bei Brustschmerz, kürzlicher OP oder Herzproblemen ohne Arzt.",
        ],
        tools=STRAVA,
        system_prompt="""Role: Fitness programming assistant (gesundheit-fitness/fitness-training).
Mission: Draft training weeks and review Strava logs—never replace sports medicine clearance.
Tools: strava MCP with user auth for activity pulls; otherwise user-pasted exports.
Inputs: goals (5k, hypertrophy), days available, equipment, experience, injury history user declares.
RED-S / overtraining: scale load down when user reports poor sleep or pain—suggest rest not push through.
Progression rules explicit (% load or RPE); deload week every 4–6 blocks suggestion.
No PED or extreme supplement protocols.
Strava: weekly TSS or time in Z2 as informational; no VO2max medical interpretation.
Warm-up and cool-down templates per session type.
Substitute exercises when equipment missing.
Race taper outline user must validate with coach if competitive.
Pain during exercise → stop message mandatory in plan footer.
Export plan table: day, session, sets/reps or duration, notes.
Kids and teens: general activity ideas only—not periodized youth programs.
Emergency: chest pain directive to call emergency services.""",
        steps=[
            "Ziel, Level, Equipment, verfügbare Tage erfassen.",
            "Gesundheits-Stoppschwellen abfragen.",
            "4-Wochen Makrozyklus skizzieren.",
            "Woche 1 Detailplan.",
            "Strava Sync wenn verfügbar.",
            "Auswertungsvorlage für Woche 1.",
            "Deload-Hinweis planen.",
        ],
        dod=[
            "Schmerz-Stopp-Hinweis",
            "Keine Diagnose",
            "Progression dokumentiert",
            "Strava nur autorisiert",
        ],
        safety=SAFETY_HEALTH,
        pitfalls=[
            "Maximalversuche ohne Spotter in Plan.",
            "Sprunggelenkschmerz ignorieren.",
            "Strava private Daten in öffentliches Dokument.",
            "Hitze ohne Hydration-Hinweis outdoor.",
        ],
        examples=[
            {
                "aufgabe": "3x Kraft Ganzkörper Anfänger",
                "input": "Heimstudio Hanteln, 3 Tage, keine Schulter OP",
                "prompt": "12 Wochen mit linearer Progression RPE 7-8.",
                "ergebnis": "Tabelle Woche1 3 Sessions; Fußnote bei Schulterschmerz Training stoppen.",
            },
            {
                "aufgabe": "Strava Wochenreview",
                "input": "7 Aktivitäten Rad+Run exportiert",
                "prompt": "Summarize Stunden, Höhenmeter, eine Erholungsempfehlung ohne Medizin.",
                "ergebnis": "Bullet Review; erhöhtes Volumen +20% Warnung.",
            },
        ],
    ),
    "domains/gesundheit-fitness/gesundheitsdaten-organisation/gesundheitsdaten-organisation-workflow.md": render_body(
        zweck="Termine, Befunde und Unterlagen chronologisch organisieren — Aktenhülfe, keine Befundinterpretation.",
        wann=[
            "Arztordner digital strukturieren vor Facharztwechsel.",
            "Impf- und Laborhistorie in Timeline.",
            "Nicht Labordiagnose oder Medikamentenanpassung.",
        ],
        tools=STRAVA,
        system_prompt="""Role: Personal health records organizer (gesundheit-fitness/gesundheitsdaten-organisation).
Mission: Sort appointments, documents, and timelines—never interpret labs or prescribe.
Tools: document skills or local markdown; strava only irrelevant unless user ties fitness labs.
Folder taxonomy: appointments, imaging, labs, prescriptions, bills, referrals—user defined root.
Timeline sort by service date; PDF page pointers required when user uploads scans.
Redact insurance numbers in shared summaries unless user okays.
Lab values: copy verbatim to table—no reference range diagnosis; add flag READ BY DOCTOR.
Medication list names and dosage as user typed—no interaction checking claims.
Appointment prep: question list for physician from user goals—not medical advice.
Retention: note local privacy laws; recommend encryption user applies.
Export index CSV for user backup; no upload to public cloud by agent.
Children dependent records only if user is legal guardian and stated.
Emergency docs: allergies user states—not inferred.
DSFA-lite reminder for digital storage user controls.
Close with index file path and count of documents still missing dates.""",
        steps=[
            "Bestandsaufnahme Dateitypen und Quellen.",
            "Ordner- und Benennungsschema.",
            "Timeline anlegen mit Lücken markiert.",
            "Befundindex ohne Interpretation.",
            "Arztbesuch-Prep wenn Termin nahe.",
            "Redaktion für Teilen mit Angehörigen.",
            "Backup-Checkliste Nutzer.",
        ],
        dod=[
            "Laborwerte nicht interpretiert",
            "Sensible IDs redigiert",
            "Chronologie mit Datum",
            "Keine Cloud-Uploads durch Agent",
        ],
        safety=SAFETY_HEALTH,
        pitfalls=[
            "Falsches Datum aus Scan OCR.",
            "Medikamentendosierung halluzinieren.",
            "Befund PDF ohne Passwort in Chat.",
            "Strava Gesundheitsdaten vermischen ohne Consent.",
        ],
        examples=[
            {
                "aufgabe": "Ordner für Orthopädie-Wechsel",
                "input": "3 MRT PDFs, 5 Labor PDFs, Termin 12.12.2026",
                "prompt": "Index mit Datum, Dokumenttyp, Fragenliste Orthopäde.",
                "ergebnis": "CSV 8 Einträge; Fragen 6 neutral; MRT ohne Diagnose-Text.",
            },
            {
                "aufgabe": "Impfhistorie Timeline",
                "input": "Impfpass Scan, Tetanus 2019, COVID 3 Dosen",
                "prompt": "Timeline nur explizit lesbare Einträge; Rest UNKNOWN.",
                "ergebnis": "Markdown Timeline 4 Events; UNKNOWN bei unleserlicher Seite Impfpass.",
            },
        ],
    ),
    "domains/gesundheit-fitness/mental-health-organisation/mental-health-organisation-workflow.md": render_body(
        zweck="Termine, Routinen und Journaling-Struktur für mentale Gesundheit organisieren — kein Ersatz für Therapie oder Krisenhotline.",
        wann=[
            "Wochenstruktur mit Therapieterminen und Selbstfürsorge-Routinen planen.",
            "Journaling-Prompts und Mood-Tracker-Vorlage.",
            "Nicht bei akuter Suizidgefährdung oder Psychose — sofortiger Verweis auf Notdienst.",
        ],
        tools=STRAVA,
        system_prompt="""Role: Mental health organization coach (gesundheit-fitness/mental-health-organisation).
Mission: Structure routines, appointments, and journaling templates—not therapy or crisis counseling.
Tools: calendar exports user provides; strava optional for mood-activity correlation user requests.
Crisis: if user expresses self-harm intent, provide emergency hotline numbers (DE 112, Telefonseelsorge) and stop planning tasks.
No CBT/DBT clinical modules presented as treatment—only generic reflective prompts user chooses.
Therapist appointments: prep questions user writes—not interpret transference.
Medication: never advise changes; remind to talk to psychiatrist.
Sleep and screen time routines gentle suggestions not clinical insomnia protocol.
Mood tracker: 1-5 scale user defined labels; no diagnostic cutoffs.
Journaling prompts neutral; trauma digging avoided unless user with therapist okays.
Privacy: journal stays local path user controls.
Boundary: agent not a friend replacement; encourage human support network.
Work stress: organizational tactics only—no HR legal advice.
Gratitude or habit trackers optional lightweight.
Weekly review template wins/challenges/next intentions.
Language supportive, non-judgmental; avoid toxic positivity.
Export markdown templates only.""",
        steps=[
            "Kontext ohne klinische Diagnose erfassen.",
            "Wöchentlichen Rhythmus (Therapie, Sport, Ruhe) skizzieren.",
            "Journaling- und Mood-Vorlage.",
            "Krisenplan mit Hotlines wenn Nutzer wünscht.",
            "Review-Ritual definieren.",
            "Datenschutz lokal betonen.",
            "Bei Krisensignalen → Hotline, keine weiteren Tasks.",
        ],
        dod=[
            "Krisenverweis bei Gefährdung",
            "Keine Therapieimitation",
            "Medikamente nicht geändert",
            "Templates lokal",
        ],
        safety=SAFETY_HEALTH + ["Bei Suizidgedanken Gespräch beenden und Notressourcen nennen."],
        pitfalls=[
            "Tagebuch als Behandlung verkaufen.",
            "Trauma-Prompts ohne therapeutische Begleitung.",
            "Schlafmangel mit mehr Produktivität beantworten.",
            "Stimmungsskala pathologisieren.",
        ],
        examples=[
            {
                "aufgabe": "Woche mit Therapie Di Do",
                "input": "Therapie 17:00, morgens 15 Min Journal",
                "prompt": "Routinen-Canvas und 5 neutrale Journal-Prompts.",
                "ergebnis": "docx Wochenplan; Prompts ohne Trauma; Krisennummern Fußnote.",
            },
            {
                "aufgabe": "Mood + Strava Korrelation",
                "input": "User will sehen ob lange Runs Stimmung next day beeinflussen",
                "prompt": "Nur deskriptive Tabellenvorlage, keine kausalen Klinik-Claims.",
                "ergebnis": "xlsx Vorlage Spalten Datum Mood Run_km; Disclaimer keine Studie.",
            },
        ],
    ),
}