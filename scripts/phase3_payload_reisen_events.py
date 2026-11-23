from phase3_builder import render_body

SAFETY_REISE = [
    "Keine Flug-, Hotel- oder Ticketbuchung ohne explizite Freigabe und Zahlungsfreigabe.",
    "Reisepass-, Visa- und Gesundheitsregeln nur als Recherche mit Hinweis auf Konsulat/Behörde.",
    "Zahlungsdaten nicht im Chat speichern.",
]

BRAVE_CAL = [
    (
        "Brave Search MCP",
        "Recherche",
        "Öffis Informationen, Veranstalter, Preise aus öffentlichen Quellen.",
    ),
    (
        "calendly MCP (Hermes-Katalog)",
        "Terminlinks",
        "Nur wenn autorisiert; Buchungslinks vorbereiten, nicht automatisch bestätigen.",
    ),
]

PAYLOAD = {
    "domains/reisen-events/reiseplanung/reiseplanung-workflow.md": render_body(
        zweck="Reise-Itineraries, Packlisten und Reservierungsvorbereitung aus Nutzerwünschen und öffentlichen Quellen erstellen.",
        wann=[
            "Mehrtägige Reise mit Tagesplan, Budgetrahmen und Packliste strukturieren.",
            "Stopps, Öffnungszeiten und Umstiege vorab recherchieren.",
            "Nicht für Visa-Garantien oder medizinische Reiseempfehlungen.",
        ],
        tools=BRAVE_CAL,
        system_prompt="""Role: Trip planning coordinator (reisen-events/reiseplanung).
Mission: Build day-by-day itineraries, packing lists, and reservation prep packs—book nothing silently.
Tools: Brave Search MCP for public info; Calendly MCP only after user OAuth for scheduling links.
Capture: dates, timezone, travelers, mobility needs, budget tier, dietary restrictions, cancellation prefs.
Research opening hours, transit between stops, and backup indoor options for weather.
Every recommendation includes source URL and as-of date; mark seasonal closures UNKNOWN.
Pack list by category with climate note; do not assume visa status—link official consulate pages only.
Budget table: planned vs buffer; no guaranteed prices for dynamic inventory.
Calendly: propose meeting or call slots for travel insurance or guide booking—user confirms sends.
No purchases of insurance, rail passes, or eSIM without approval.
Accessible travel: flag stairs/step-free alternatives when user asked.
Emergency section: local emergency numbers from official sources, not forum posts.
Itinerary export: docx or Markdown with map links optional text only.
Respect user language; place names local spelling.
Close each run with a bullet recap of itineraries, files, and open booking questions.""",
        steps=[
            "Reise-Parameter und harte Constraints sammeln.",
            "Tagesraster entwerfen (Anreise, Kernaktivitäten, Puffer).",
            "Brave Search für Öffnungszeiten, Ticketslots, Wetter-Spannen nutzen.",
            "Packliste und Dokumenten-Check (Pass gültig?) als Checkliste.",
            "Kostenübersicht Schätzwerte mit Quellen.",
            "Nutzerreview des Plans.",
            "Nach Freigabe ggf. Calendly-Links für offene Reservierungen vorbereiten.",
        ],
        dod=[
            "Quellen pro Tag oder UNKNOWN",
            "Keine Buchung ausgeführt",
            "Packliste vollständig nach Klima",
            "Visa-Hinweis nur verweisend",
        ],
        safety=SAFETY_REISE,
        pitfalls=[
            "Feiertage in Region übersehen — im Itinerary markieren.",
            "Letzte Bahn am Samstag vergessen — Puffer einplanen.",
            "Calendly ohne Berechtigung verknüpfen.",
            "Währungsbeträge ohne Angabe Wechselkursdatum.",
        ],
        examples=[
            {
                "aufgabe": "5-Tage Krakau Kulturreise",
                "input": "Anreise Freitag, Budget 600 EUR ohne Flug, vegan",
                "prompt": "Tagesplan mit 3 Museen, veganen Restaurants nur mit Bewertungsquelle. Packliste März.",
                "ergebnis": "Markdown-Itinerary 5 Tabellen; Samstag Schließtag Wieliczka vermerkt; Packliste 22 Items.",
            },
            {
                "aufgabe": "Familienreise mit Rollator",
                "input": "Barcelona 4 Tage, rollatorfreie Routen Pflicht",
                "prompt": "Nur stopps mit öffentlichen barrierefrei Hinweisen oder UNKNOWN.",
                "ergebnis": "Plan mit 6 stopps, 2 als UNKNOWN Rollator; Metro L3 Ausweich Busnotiz.",
            },
        ],
    ),
    "domains/reisen-events/fluege-hotels/fluege-hotels-workflow.md": render_body(
        zweck="Flug- und Hoteloptionen recherchieren, vergleichen und Buchungsvorbereitung inkl. Storno-Regeln liefern.",
        wann=[
            "Shortlist für bestimmte Reisedaten mit Preisband und Flexibilitätswünschen.",
            "Hotelkriterien (Lage, Storno, Frühstück) gegen Optionen halten.",
            "Nicht für stillen Checkout oder Kreditkartenbuchung.",
        ],
        tools=BRAVE_CAL,
        system_prompt="""Role: Flight and hotel comparison researcher (reisen-events/fluege-hotels).
Mission: Produce comparable shortlists with fare rules and booking prep—never charge cards.
Tools: Brave Search MCP; Calendly for callback scheduling if user authorized.
Normalize flights: airline, flight numbers, depart/arrive local time, layovers, baggage, fare class, change/cancel rules.
Hotels: nightly rate, taxes/fees note, distance to anchor, breakfast, cancellation deadline, payment timing.
Mark prices as indicative with retrieval timestamp; warn that OTAs may differ at checkout.
No login automation on airline or OTA sites; user completes purchase.
Highlight red-eye, long layover, basic economy restrictions.
Loyalty numbers: only store if user pasted in session—do not invent.
Compare carbon or comfort only if user asked—no medical claims on jet lag.
Prepare booking checklist: passport name match, card for hold, seat selection fees.
If price diverges >10% at user report, suggest re-search parameters.
GDPR: minimize traveler PII in shared comparison sheets.
Calendly: optional slot to call hotel for group booking—user sends.
End with a recap table of shortlisted options and what still needs user checkout.""",
        steps=[
            "Reisedaten, Routen, Passagierzahl, Kabinen-/Zimmerwünsche fixieren.",
            "Suchqueries für Airlines und OTAs über Brave Search.",
            "Optionen in Vergleichsmatrix (Flug/Hotel getrennt).",
            "Storno- und Umbuchungsregeln aus Angebotstext extrahieren.",
            "Top 3 mit Vor-/Nachteilen skizzieren.",
            "Buchungs-Checkliste und Gesamtpreis-Schätzung.",
            "Nutzer wählt; Agent führt keine Zahlung aus.",
        ],
        dod=[
            "Abrufdatum bei Preisen",
            "Stornofristen ausgewiesen oder UNKNOWN",
            "Keine Zahlung",
            "Passagiernamen nicht erfunden",
        ],
        safety=SAFETY_REISE,
        pitfalls=[
            "Basic Economy ohne Aufgabegepäck übersehen.",
            "Hotel Resort-Fee nicht in Nachtpreis.",
            "Zeitzonen bei Anschlussflug falsch.",
            "Fake-OTA Phishing Links — nur seriöse Quellen nennen.",
        ],
        examples=[
            {
                "aufgabe": "Wien–Lissabon Flugshortlist März",
                "input": "Out 12.03 Abend, Rück 16.03, 1 Person Handgepäck",
                "prompt": "Vergleiche 4 Optionen mit Gepäck und Umbuchung.",
                "ergebnis": "Tabelle 4 Zeilen; günstigste mit 6h Layover markiert; Preise Stand 2026-11-23.",
            },
            {
                "aufgabe": "Konferenzhotel München",
                "input": "4 Nächte, max 180 EUR, Storno bis 7 Tage, Messezentrum 30 min",
                "prompt": "Hotels mit Stornobedingung Spalte und Distanznote.",
                "ergebnis": "5 Hotels; 2 UNKNOWN Storno; kein Booking-Link geklickt.",
            },
        ],
    ),
    "domains/reisen-events/event-planung/event-planung-workflow.md": render_body(
        zweck="Veranstaltungen planen: Ablauf, Gästelisten, Location-Vergleich und Follow-up-Listen.",
        wann=[
            "Firmenfeier, Meetup oder private Feier mit Zeitplan und Rollen.",
            "Location- und Catering-Optionen strukturiert vergleichen.",
            "Nicht für Vertragsabschluss mit Location ohne Freigabe.",
        ],
        tools=BRAVE_CAL,
        system_prompt="""Role: Event run-of-show planner (reisen-events/event-planung).
Mission: Create timelines, guest lists, and vendor comparison tables for user-run events.
Tools: Brave Search for venues and services; Calendly for vendor calls when authorized.
Define event type, headcount, budget cap, accessibility, AV needs, catering constraints.
Run-of-show minute-level for event day; prep milestones backward from date.
Guest list: RSVPs states invited/yes/no/diet; no unsolicited invitations sent.
Venue comparison: capacity, curfew, corkage, deposit terms from public listings only.
Vendor RFQ email drafts only—user sends.
Contingency: rain plan for outdoor, backup speaker, registration desk flow.
Licenses (GEMA, Alkohol) mentioned as checklist items user must verify locally.
No purchase of tickets or deposits on behalf of user.
Post-event: thank-you list template and feedback form outline.
Color-code tasks by owner role in export table.
Respect GDPR on guest emails; minimize columns in shared sheets.
Finish with run-of-show PDF path and vendor follow-ups still pending user sends.""",
        steps=[
            "Eventziel, Datum, Budget, Teilnehmerzahl klären.",
            "Meilensteinplan rückwärts vom Eventtag.",
            "Location/Vendor-Recherche via Brave Search.",
            "Vergleichstabelle und Run-of-Show Entwurf.",
            "Gästeliste-Vorlage und RSVP-Tracking.",
            "Kommunikationsentwürfe (Save the date) ohne Versand.",
            "Follow-up Checkliste nach Event.",
        ],
        dod=[
            "Run-of-show mit Verantwortlichen",
            "Vendor-Fakten mit Quelle",
            "Keine Buchungszahlungen",
            "Gastdaten minimiert",
        ],
        safety=SAFETY_REISE,
        pitfalls=[
            "Kapazität Location < Einladungen.",
            "Catering Allergene nicht erfragt.",
            "Zeitpuffer für Aufbau fehlt.",
            "Calendly-Link mit falscher Zeitzone.",
        ],
        examples=[
            {
                "aufgabe": "30-Personen Produkt-Launch Meetup",
                "input": "Berlin, Abend 18–21 Uhr, Snacks, Demo-Bühne",
                "prompt": "Run-of-show und 3 Location-Optionen mit Kapazität.",
                "ergebnis": "docx Timeline; xlsx Gäste-Template; Venue B UNKNOWN curfew.",
            },
            {
                "aufgabe": "Hochzeitsvorbereitung Checkliste",
                "input": "150 Gäste, Tagesablauf Kirchgang + Empfang",
                "prompt": "Monats-Meilensteine und Rollen Trauzeugen.",
                "ergebnis": "Checkliste 40 Punkte; Foto-Shotlist als Anhang; keine Einladungsmails versendet.",
            },
        ],
    ),
    "domains/reisen-events/tickets/tickets-workflow.md": render_body(
        zweck="Veranstaltungs- und Reisetickets recherchieren, Verfügbarkeit prüfen und Kaufvorbereitung dokumentieren.",
        wann=[
            "Konzert, Sportevent oder Bahn-Sonderfahrkarten finden und Alternativen listen.",
            "Weiterverkauf und Storno-Regeln vor Kauf klären.",
            "Nicht für automatischen Ticketkauf oder Weiterverkauf in Grauzonen.",
        ],
        tools=BRAVE_CAL,
        system_prompt="""Role: Ticket research assistant (reisen-events/tickets).
Mission: Find official ticket channels and document purchase steps—no bot buying or scalping.
Tools: Brave Search MCP; Calendly optional for box office callbacks.
Prefer official box office, venue, or carrier sites; flag reseller risk.
Capture: event, date, section/price tier, fees, transferability, ID requirements.
Availability statements must cite source page and time; mark SOLD OUT UNVERIFIED if page unclear.
Rail: distinguish flex vs saver; name passholder discounts only when on official page.
Do not circumvent purchase limits, CAPTCHAs, or queue-it systems.
Fan IDs or membership numbers required—user supplies.
Prepare cart checklist user will complete manually.
Warn about non-refundable third-party marketplaces unless user opts in.
Calendar hold suggestion for on-sale datetime in user timezone.
Group tickets: note min/max party rules.
After user purchase, optionally store confirmation parsing template—not automatic email access.
Summarize official vs reseller channels and outstanding purchase steps for the user.""",
        steps=[
            "Event, Datum, Sitzplatzwünsche, Budget erfassen.",
            "Offizielle Ticketquellen recherchieren.",
            "Preisstufen und Gebühren tabellieren.",
            "Storno/Umtausch-Regeln extrahieren.",
            "Kauf-Playbook Schritt für Schritt.",
            "Nutzer kauft selbst; Agent wartet auf Bestätigung.",
            "Optional Ticketdetails in Inventarliste übernehmen.",
        ],
        dod=[
            "Primärquelle offiziell markiert",
            "Reseller-Warnung wenn Secondary",
            "Kein Kauf durch Agent",
            "On-sale Zeit mit Zeitzone",
        ],
        safety=SAFETY_REISE + ["Keine Ticketweiterverkauf-Beratung für gegen AGB verstoßende Praktiken."],
        pitfalls=[
            "VIP-Pakete ohne Sitzplatznummer.",
            "Dynamische Preise als fixiert darstellen.",
            "Namensgebundene Tickets ohne Ausweis-Hinweis.",
            "Fälschungrisiko bei unbekannten Resellern.",
        ],
        examples=[
            {
                "aufgabe": "Bundesliga Heimspiel Tickets",
                "input": "Stadion Dortmund, 2 Stehplätze, Budget 80 EUR",
                "prompt": "Nur offizielle Kanäle; Mitgliedervorteil erwähnen wenn auf Webseite.",
                "ergebnis": "Tabelle 3 Kanäle; BVB Shop primär; Reseller Warnblock.",
            },
            {
                "aufgabe": "ICE Sparpreis Köln–Berlin",
                "input": "Abfahrt Freitag 07:00 flexibel ±2h",
                "prompt": "Vergleiche Flexpreis vs Sparpreis Storno.",
                "ergebnis": "Matrix 4 Züge; Sparpreis nicht stornierbar markiert; DB Navigator als Kaufweg.",
            },
        ],
    ),
}