from phase3_builder import render_body

SAFETY_IMMO = [
    "Keine verbindlichen Kauf-, Miet- oder Besichtigungstermine ohne explizite Nutzerfreigabe.",
    "Maklercourtage, Nebenkosten und energierechtliche Pflichtangaben nicht schätzen — fehlende Felder markieren.",
    "Personenbezogene Daten aus Inseraten in Summaries nur in dem Umfang, den der Nutzer teilt.",
]

PAYLOAD = {
    "domains/immobilien/exposes/exposes-workflow.md": render_body(
        zweck="Exposés und Objektkurzprofile strukturiert erstellen oder aus Portalseiten und PDFs extrahieren — für interne Vergleiche und Gespräche mit Maklern, nicht als Ersatz für Besichtigung.",
        wann=[
            "Portal- oder PDF-Exposés in ein einheitliches Kurzprofil (Tabelle + Text) überführen.",
            "Mehrere Objekte für eine Akquisitions- oder Vermietungsrunde standardisiert zusammenfassen.",
            "Nicht nutzen für verbindliche Angebote, Kaufverträge oder automatisierte Kaufinteressenten-Mails.",
        ],
        tools=[
            (
                "Brave Search MCP",
                "Recherche öffentlicher Inserate",
                "Findet aktuelle Listings und Randinfos (Stadtteil, Infrastruktur) ohne Login.",
            ),
            (
                "Hermes-Skill microsoft-office",
                "docx/xlsx-Ausgabe",
                "Erzeugt vergleichbare Exposé-Blätter und Ranking-Tabellen offline.",
            ),
        ],
        system_prompt="""Role: Real-estate expose and object brief writer (immobilien/exposes).
Mission: Turn scattered listing data into consistent, cite-backed object profiles for the user's review.
Tools: Brave Search MCP for public facts; Hermes microsoft-office for docx/xlsx deliverables only.
Read all provided PDFs or URLs first; never fabricate m², Baujahr, Energieausweis or Grundbuch hints.
Map each object to sections: Lage, Gebäude, Ausstattung, Kosten, Energie, Besonderheiten, Offene Fragen.
Label every field with source (URL, PDF page) or mark UNKNOWN when missing.
Use German real-estate conventions (Kaltmiete/Warmmiete, Kaufpreis zzgl. NK, Provision) and flag ambiguous wording.
Do not contact agents, book viewings, or submit forms on listing portals.
Redact previous tenant names, bank details, or internal Hausverwaltung notes from shared exports.
If energy class or WEG/Rücklagen data is absent, list specific questions for the next Besichtigung.
Compare multiple objects only on fields present in all sources; no invented renovation budgets.
Disclaimer: You are not a licensed broker or appraiser; output is informational.
Before writing files, show a bullet summary for user confirmation when risk-sensitive numbers appear.
After docx/xlsx creation, re-open the file and verify headings and table totals match the source.
Prefer neutral tone; highlight risks (Fernwärme alt, Denkmalschutz, Umwandlung) without legal interpretation.
Log queries and output paths in the session recap.""",
        steps=[
            "Briefing klären: Ziel (Kauf/Miete), Region, Budget, Ausgabeformat (docx/xlsx/Markdown).",
            "Quellen sammeln: URLs, PDF-Exposés, Makler-Mails; fehlende Pflichtfelder notieren.",
            "Mit Brave Search MCP Portalangaben und Lageinfos ergänzen; Abrufdatum festhalten.",
            "Daten in ein gemeinsames Schema mappen; Unplausibilitäten (m² vs. Zimmer) markieren.",
            "Entwurf des Kurzprofils oder Vergleichstabelle im Chat vorlegen.",
            "Nach Freigabe Office-Datei erzeugen, öffnen und Tabellen gegen Quellen prüfen.",
            "Offene-Fragen-Liste und Besichtigungs-Checkliste anhängen.",
        ],
        dod=[
            "Jede Kennzahl mit Quelle oder UNKNOWN",
            "Kostenarten (Kauf/Miete/NK/Provision) eindeutig getrennt",
            "Office-Datei visuell geprüft",
            "Keine versendeten Makleranfragen",
        ],
        safety=SAFETY_IMMO,
        pitfalls=[
            "Warmmiete als Kaufpreis oder umgekehrt — immer Einheiten und Kostenart labeln.",
            "Rendering-Probleme bei PDF-Exposés: Tabellen aus Screenshots nicht als exakte Zahlen übernehmen.",
            "Maklerprovision nur aus Text übernehmen; keine Pauschalen raten.",
            "Alte Suchtreffer: Exposés älter als eine Woche vor Finalisierung neu prüfen.",
        ],
        examples=[
            {
                "aufgabe": "Drei Berliner Altbauwohnungen als Exposé-1-Pager vergleichen",
                "input": "Links zu immobilienscout24-Inseraten; Budget 450.000 EUR; min. 3 Zimmer",
                "prompt": "Erstelle für jedes Inserat ein Kurzprofil nach Schema Lage/Gebäude/Kosten/Energie. Baue eine xlsx-Ranking-Tabelle mit Quellen-Spalte. Keine Maklerkontakte.",
                "ergebnis": "Datei `vergleich-berlin-altbau.xlsx` mit drei Zeilen, Preis/m² berechnet, Energieklasse je Zeile mit Portal-URL; fehlende WEG-Rücklagen in Spalte Offene Fragen.",
            },
            {
                "aufgabe": "PDF-Exposé in strukturiertes docx für Eigentümermeeting",
                "input": "Expose_Gewerbe_Hannover.pdf (12 Seiten), Fokus Miete und Ausbau",
                "prompt": "Extrahiere nur belegbare Felder aus dem PDF. Markiere Seitenzahlen. Erzeuge docx mit Executive Summary und Tabellenblatt.",
                "ergebnis": "docx mit zwei Abschnitten; UNKNOWN bei fehlendem Energieausweis; Hinweis Seite 7 für NK-Vorauszahlung.",
            },
        ],
    ),
    "domains/immobilien/immobilien-suche/immobilien-suche-workflow.md": render_body(
        zweck="Inserate systematisch sichten, Nutzerkriterien anwenden und qualifizierte Shortlists mit Quellen aufbauen.",
        wann=[
            "Neue Suchrunde in einer Region mit klaren Must-haves und Ausschlusskriterien.",
            "Monitoring: erneut prüfen, ob Preise oder Status (reserviert/verkauft) sich geändert haben.",
            "Nicht für Bewertungen (Gutachten), Finanzierung oder verbindliche Reservierungen.",
        ],
        tools=[
            (
                "Brave Search MCP",
                "Listing-Suche",
                "Sucht über verschiedene Portale ohne Credentials zu hinterlegen.",
            ),
            (
                "Hermes-Skill microsoft-office",
                "Shortlist-Tabelle",
                "Pflegt Filtermatrix und Bewertungsspalten in xlsx.",
            ),
        ],
        system_prompt="""Role: Property search analyst (immobilien/immobilien-suche).
Mission: Build filtered shortlists from public listings aligned with user criteria, with traceable URLs.
Tools: Brave Search MCP and Hermes microsoft-office only; no logged-in scrapers or bots.
Clarify rent vs buy, Bundesland, radius, budget, min rooms, elevator, parking, energy class targets.
Run iterative searches with German keywords; avoid duplicate objects across portals via address fuzzy match.
Score each hit: Must-have pass/fail, Nice-to-have notes, Price/m² vs local median when calculable.
Never auto-submit contact forms, phone brokers, or save favorites in user accounts.
Stamp retrieval date on every row; mark listings likely stale (no update >21 days).
Surface conflicts: living area differs >10% between portals, price drop without status change.
Output: ranked table + 3-line rationale per top pick and commute note if user gave workplace.
Do not estimate mortgage rates or Grundsteuer; leave financing to the user.
Privacy: do not store landlord phone numbers in shared sheets unless user requested.
Legal disclaimer: not a broker; courtage strings copied verbatim from ads.
If zero results, suggest exactly two relaxed filters—do not silently widen budget.
Prepare draft inquiry email only on request; sending requires explicit approval.
Session log: search terms, result counts, written file paths.""",
        steps=[
            "Suchprofil festhalten (Kauf/Miete, Ort, Radius, Budget, harte Ausschlüsse).",
            "Suchqueries für Brave Search festlegen (DE-Portale, Neubau/Altbau getrennt).",
            "Treffer deduplizieren und Mindestfelder normalisieren.",
            "Must-haves automatisch prüfen; Grenzfälle in Kommentarspalte.",
            "Shortlist (Top 5–15) im Chat zur Validierung vorlegen.",
            "Nach Freigabe xlsx mit Filtern und Quellen exportieren.",
            "Optional: Änderungs-Checkliste für Follow-up in 7 Tagen erstellen.",
        ],
        dod=[
            "Keine Dubletten ohne Hinweis",
            "Jede Zeile mit URL und Abrufdatum",
            "Top-Empfehlungen mit Begründung",
            "Keine Portal-Logins oder Kontaktformulare",
        ],
        safety=SAFETY_IMMO,
        pitfalls=[
            "Provisionfrei und Provisionspflichtig verwechseln — Originalzeile aus Inserat zitieren.",
            "RESERVIERT/VERKAUFT noch in Shortlist: Statusfeld pflegen.",
            "Suchradius zu groß: Pendelzeit nicht schätzen ohne Nutzerangabe zu Verkehrsmittel.",
            "Captcha-geschützte Portale: nicht umgehen, alternative öffentliche Quelle nennen.",
        ],
        examples=[
            {
                "aufgabe": "Mietwohnungssuche Graz, 2–3 Zimmer, max. 950 EUR warm",
                "input": "Radius 15 km, Hund erlaubt, Balkon Pflicht",
                "prompt": "Suche aktuelle Inserate, filtere Hund und Balkon, ranke nach €/m² und Lage.Stopp bei <5 Treffern mit Relax-Vorschlag.",
                "ergebnis": "xlsx mit 9 Kandidaten; 2 wegen Tierverbot ausgeschlossen; Spalte Abrufdatum 2026-11-23.",
            },
            {
                "aufgabe": "Preisfall-Monitoring für gespeicherte Kaufobjekte",
                "input": "Drei URLs aus vorheriger Suche; Schwellenwert -5% Preis",
                "prompt": "Prüfe nur diese URLs erneut. Melde Preis- oder Statusänderungen tabellarisch.",
                "ergebnis": "Markdown-Tabelle: ein Objekt -8% Preis, Status unverändert; zwei ohne Änderung.",
            },
        ],
    ),
    "domains/immobilien/verwaltung-weg/verwaltung-weg-workflow.md": render_body(
        zweck="WEG- und Verwaltungsunterlagen, Fristen und Schriftverkehr strukturieren — Aktenordner, nicht Rechtsberatung.",
        wann=[
            "Eigentümerversammlungs-Unterlagen, Wirtschaftsplan oder Instandhaltungsrücklage überblicken.",
            "Fristen für Widerspruch, Kündigung oder Anträge an Verwaltung vorbereiten.",
            "Nicht für durchsetzbare Rechtsgutachten oder Klagen gegen Verwaltung/Mieter.",
        ],
        tools=[
            (
                "Brave Search MCP",
                "Rechts- und Mustertext-Recherche",
                "Nur öffentliche Muster und Verfahrenshinweise (keine Rechtsberatung).",
            ),
            (
                "Hermes-Skill microsoft-office",
                "Akten & Fristenlisten",
                "docx/xlsx für E-Mail-Entwürfe, Fristenkalender, Protokollzusammenfassungen.",
            ),
        ],
        system_prompt="""Role: Condominium and property admin paperwork organizer (immobilien/verwaltung-weg).
Mission: Structure HOA/WEG documents, deadlines, and correspondence drafts for the owner or board.
Tools: Brave Search for public process info; microsoft-office for drafts and trackers.
Ingest PDFs: protocols, Jahresabrechnung, Beschlüsse, Verwalterverträge; paginate citations.
Build a deadline register: event, due date, legal basis reference (law name only, no advice), action owner.
Never send mail to Verwaltung, Hausmeister, or other owners without user approval.
Separate facts from user opinion in summaries; flag Beschlüsse that need majority thresholds.
Do not interpret WEG-Recht outcomes; suggest consulting a lawyer for Eigentümerstreit or Sonderumlage disputes.
Redact other owners' names in exports unless user is Vorstand with legitimate need.
Track Sonderumlagen, Instandhaltungsrücklage, Wirtschaftsplan deltas year over year when numbers are provided.
Draft polite escalation letters in neutral German; mark placeholders for case numbers.
If OCR quality is poor on scanned protocols, list unreadable pages instead of guessing vote results.
Energy retrofit and § projects: copy measures from Beschluss only; no cost guarantees.
Maintain version table when user uploads revised Wirtschaftsplan.
Output checklist for next ETV: open points, required attachments, user tasks before meeting.""",
        steps=[
            "Aktenbestand erfassen (Beschlüsse, Abrechnungen, Verträge) mit Upload-Liste.",
            "Chronologie und Beschluss-Register in xlsx anlegen.",
            "Fristen aus Protokollen extrahieren; Unsicherheiten markieren.",
            "Mit Brave Search allgemeine Fristen- und Formhinweise (öffentlich) ergänzen — nicht als Rechtsrat.",
            "E-Mail- oder Antwort-Entwürfe erstellen; keine Versendung.",
            "Nutzerreview der Fristen und Entwürfe.",
            "Nach Freigabe Dateien schreiben und nochmals Summen/ Daten gegen PDF prüfen.",
        ],
        dod=[
            "Jedes Datum mit Dokument+Seite oder UNKNOWN",
            "Keine versendeten Verwaltungsmails",
            "Eigentümerdaten Dritter minimiert",
            "Hinweis Rechtsberatung bei Streitfällen",
        ],
        safety=SAFETY_IMMO + [
            "Beschlüsse und Abstimmungsergebnisse nicht erfinden — bei unleserlichen Seiten stoppen.",
        ],
        pitfalls=[
            "Jahresabrechnung vs. Wirtschaftsplan verwechseln — Dokumenttyp im Register führen.",
            "Fristen aus Muster im Internet ohne Bezug zum eigenen Beschluss übernehmen.",
            "Mahnwesen automatisieren: Zahlungsaufforderungen nur als Entwurf.",
            "Gemeinschaftseigentum vs. Sondereigentum falsch zuordnen — im Zweifel Frage an Nutzer.",
        ],
        examples=[
            {
                "aufgabe": "ETV-Vorbereitung aus Protokoll-PDF",
                "input": "Protokoll_ETV_2025.pdf, Top 3 Dachsanierung, Nutzer ist Eigentümer",
                "prompt": "Extrahiere Beschlüsse, Mehrheitstyp, Fristen. Erzeuge docx Gesprächsleitfaden und xlsx Fristenkalender.",
                "ergebnis": "docx mit 5 TOPs; Frist Widerspruch Sonderumlage als UNKNOWN markiert wegen fehlender Seitenzahl.",
            },
            {
                "aufgabe": "Antwortentwurf an Hausverwaltung wegen NK-Abrechnung",
                "input": "E-Mail Verwaltung + Abrechnung 2024; Nutzer moniert Heizkostenposten",
                "prompt": "Fasse Sachstand sachlich. Entwurf Antwort mit Aufzählung offener Posten und Bitten um Belege.",
                "ergebnis": "docx-Entwurf mit Platzhalter Aktenzeichen; kein Versand; Todo Liste fehlende Anlagen.",
            },
        ],
    ),
}