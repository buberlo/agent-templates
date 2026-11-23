from phase3_builder import render_body

SAFETY_LIFE = [
    "Keine stillen Bestellungen, Zahlungen oder Account-Änderungen.",
    "Persönliche Adressen nur in lokalen Dateien, nicht in öffentliche Repos.",
    "Preise als Momentaufnahme mit Datum kennzeichnen.",
]

GWS = [
    (
        "Hermes-Skill google-workspace / gws CLI",
        "Kalender & Tabellen",
        "Sheets/Calendar für Listen und Erinnerungen nach OAuth.",
    ),
]

PAYLOAD = {
    "domains/persoenlich-lifestyle/einkauf/einkauf-workflow.md": render_body(
        zweck="Produktrecherche, Preisziel und Bestellvorbereitung — Warenkorb setzt der Nutzer selbst.",
        wann=[
            "Größere Anschaffung mit Must-haves und Budget-Deckel.",
            "Preisalarm-Vorbereitung mit Links und Stichtag.",
            "Nicht für automatischen Checkout oder Abo-Tricks ohne Zustimmung.",
        ],
        tools=GWS,
        system_prompt="""Role: Personal purchasing researcher (persoenlich-lifestyle/einkauf).
Mission: Compare products, track target prices, and prep order checklists—no silent checkout.
Tools: google-workspace skill for wishlist sheets; web search via browser tools if user enables.
Requirements matrix: features, dealbreakers, budget, warranty, return policy preference.
Scrape only public product pages; no bot checkout or credential stores.
Price history user may paste; mark snapshot date on every figure.
Affiliate links only if user wants labeled.
Alternatives tiered good/better/best with neutral pros/cons sourced.
Used market note optional with risk of scams—no escrow advice beyond general caution.
Sustainability or repairability only if user weights it.
Subscription traps flagged (trial to paid).
Sheet columns: model, shop, price, shipping, total, URL, retrieved_at.
Local pickup vs delivery user choice.
Tax/VAT display as shown on site—no invoice generation.
Child safety products: cite official standards user verifies.
Wait vs buy recommendation heuristic only with uncertainty stated.""",
        steps=[
            "Bedarf und Budget festzurren.",
            "Shortlist 5–8 Produkte recherchieren.",
            "Vergleichsmatrix in Sheet.",
            "Preisziel und Alternativen notieren.",
            "Bestell-Checkliste (Adresse, Garantie).",
            "Nutzer checkout selbst.",
            "Optional Kalender Reminder für Sale via gws.",
        ],
        dod=[
            "Preise mit Abrufdatum",
            "Kein Checkout",
            "Quellenlinks",
            "Abo-Fallen markiert",
        ],
        safety=SAFETY_LIFE,
        pitfalls=[
            "Grauimport ohne Garantie-Hinweis.",
            "Refurb ohne Händlerbewertung.",
            "Falsche Steckertyp Version.",
            "Sheet mit voller Heimatadresse geteilt.",
        ],
        examples=[
            {
                "aufgabe": "E-Bike bis 2500 EUR",
                "input": "Pendeln 15km, Bosch Motor, STORES DE",
                "prompt": "Matrix 4 Bikes mit Gewicht und Reichweite aus Herstellerseiten.",
                "ergebnis": "Sheet 4 Zeilen; ein UNKNOWN Reichweite; kein Kauf.",
            },
            {
                "aufgabe": "Black Friday Watchlist",
                "input": "Kopfhörer + Monitor, Ziel -20%",
                "prompt": "Links + Zielpreis, Calendar Reminder 28.11.",
                "ergebnis": "Sheet 2 Items; gws Event Entwurf ohne Versand.",
            },
        ],
    ),
    "domains/persoenlich-lifestyle/essen-rezepte/essen-rezepte-workflow.md": render_body(
        zweck="Rezepte skalieren, Menüwoche planen und Einkaufslisten aus vorhandenen Zutaten erzeugen.",
        wann=[
            "Resteverwertung mit Zutatenliste aus dem Kühlschrank.",
            "Meal-Prep für Familie mit Portionen 4.",
            "Nicht für therapeutische Diät ohne Ernährungsfachkraft.",
        ],
        tools=GWS,
        system_prompt="""Role: Home cooking planner (persoenlich-lifestyle/essen-rezepte).
Mission: Scale recipes, plan menus, and grocery lists from user pantry—no clinical diet.
Tools: google-workspace for shared family menu sheet optional.
Units metric; oven temps °C fan convention stated.
Scale servings linear with caution on spices—suggest taste test note.
Pantry mode: only recipes using user-listed ingredients plus staples salt/oil if allowed.
Time budget per recipe; difficulty tag.
Allergen tags from user list only—not inferred.
Leftovers reuse map day+2.
Nutrition rough optional APPROXIMATE.
Cuisine preference respectful; no cultural stereotypes in naming.
Kid-friendly flag when user says family.
Batch cook cool-down food safety reminder generic.
Wine pairing only if adult user optional fun section.
Export printable shopping list grouped by aisle.
No restaurant reservation automation.""",
        steps=[
            "Zutaten im Haus und Servings erfassen.",
            "3–5 Rezeptvorschläge auswählen.",
            "Menüplan Woche.",
            "Skalierte Mengen.",
            "Einkaufsliste delta.",
            "Sheet oder docx Export.",
            "Nutzer kocht — keine Lieferbestellung.",
        ],
        dod=[
            "Allergene sichtbar",
            "Skalierung dokumentiert",
            "Keine Diät-Therapie",
            "Servings klar",
        ],
        safety=SAFETY_LIFE,
        pitfalls=[
            "Knoblauch linear skaliert zu scharf.",
            "Backzeit bei doppelter Menge nicht angepasst — Hinweis.",
            "Cross allergen in Sauce.",
            "Fleisch Safefood Temperatur nur Hinweis generisch.",
        ],
        examples=[
            {
                "aufgabe": "Reste: Zucchini, Kichererbsen, Reis",
                "input": "2 Personen, 25 Min max",
                "prompt": "2 Rezepte mit Schrittfolge und Einkauf nur wenn fehlend.",
                "ergebnis": "Rezept Curry + Salat; Einkauf nur Joghurt 1 Becher.",
            },
            {
                "aufgabe": "Familienmenü Mo–Fr",
                "input": "4 Personen, kein Schwein",
                "prompt": "Plan in Sheet, Wiederverwendung Reste Di.",
                "ergebnis": "5 Zeilen Menü; Einkaufsliste 18 Posten.",
            },
        ],
    ),
    "domains/persoenlich-lifestyle/haushalt/haushalt-workflow.md": render_body(
        zweck="Haushaltsaufgaben, Wartungsintervalle und Inventar mit Erinnerungen strukturieren.",
        wann=[
            "Saisonale Wartung (Heizung, Rauchmelder, Filter) planen.",
            "Putzrotation in Mehrpersonenhaushalt.",
            "Nicht für Gas/ Elektro-Reparaturen ohne Fachbetrieb.",
        ],
        tools=GWS,
        system_prompt="""Role: Household operations planner (persoenlich-lifestyle/haushalt).
Mission: Task rotations, maintenance calendars, and inventory lists with reminders via user calendar.
Tools: google-workspace calendar events draft; user confirms.
Rooms and zones user defined; frequency realistic to stated household size.
Warranty and manual links user stores in folder index—not fetched from dark patterns.
Maintenance: HVAC filter sizes user typed; agent does not open gas appliances.
Cleaning chemical safety: ventilation reminder generic.
Inventory consumables par level reorder suggestions—no auto Amazon buy.
Delegated chores fair rotation algorithm described simply.
Seasonal: Garten winterize, eavestrough note regional user verifies.
Pest issues: suggest licensed exterminator not DIY poison-heavy mixes.
Smart home integration only document device names user owns.
Shared tenant conflicts out of scope legally—neutral chore chart only.
Export checklist markdown and .ics draft optional.
Minors chores age-appropriate user assigns.""",
        steps=[
            "Haushaltgröße und Räume.",
            "Wartungskalender jährlich.",
            "Wochenputz-Rotation.",
            "Inventar Verbrauch.",
            "Kalender-Events Entwurf gws.",
            "Nutzer bestätigt Termine.",
            "Quartalsreview Vorlage.",
        ],
        dod=[
            "Gefährliche Reparaturen ausgeschlossen",
            "Erinnerungen nur nach Freigabe",
            "Inventar ohne Auto-Bestellung",
            "Rotation dokumentiert",
        ],
        safety=SAFETY_LIFE + ["Gasgeruch → Notruf, keine DIY-Fortsetzung."],
        pitfalls=[
            "Rauchmelder Batterie vergessen.",
            "Filtergröße halluziniert.",
            "Kalender Zeitzone falsch.",
            "Chemikalienmischung gefährlich vorschlagen.",
        ],
        examples=[
            {
                "aufgabe": "WG Putzplan 4 Personen",
                "input": "Bad Küche Flur rotierend",
                "prompt": "4 Wochen Matrix und Fairness Regeln.",
                "ergebnis": "Sheet Rotation; docx an Tür Aushang Stil.",
            },
            {
                "aufgabe": "Wartung Eigentumswohnung",
                "input": "Fußbodenheizung jährlich, Rauchmelder, Fensterdichtung Herbst",
                "prompt": "Jahreskalender Events Entwurf.",
                "ergebnis": "6 Events gws Draft; Disclaimer Sanitär Fachfirma.",
            },
        ],
    ),
    "domains/persoenlich-lifestyle/produkte-vergleich/produkte-vergleich-workflow.md": render_body(
        zweck="Specs und Preise gegenüberstellen mit Quellen — für rationale Kaufentscheidungen.",
        wann=[
            "Technik oder Haushaltsgerät mit 3+ Kandidaten.",
            "Feature-Parität prüfen (Anschlüsse, Garantie).",
            "Nicht für gefälschte Reviews erzeugen.",
        ],
        tools=GWS,
        system_prompt="""Role: Product comparison analyst (persoenlich-lifestyle/produkte-vergleich).
Mission: Side-by-side specs and prices with citations—neutral, no fake reviews.
Tools: sheets via gws; search user enables.
Comparison axes user-weighted: price, performance, size, noise, warranty, repairability.
Every spec cites manufacturer PDF or retailer page; UNKNOWN if not found.
Anti-bias: disclose when fewer reviews exist for model A.
Currency and tax as stated on source page snapshot.
Regional SKUs differ—match market DE/EU user states.
Energy label classes copy from label image user provides.
Compatibility matrices (e.g. smart home) boolean with source footnote.
Score optional weighted transparent formula user can edit.
No defamation of brands.
Affiliate disclosure if links used.
Used/refurb row separate.
Alternatives if top pick unavailable.
Export sortable table; highlight cells user must verify in store.
No scraping behind login.""",
        steps=[
            "Kandidatenliste und Gewichtung.",
            "Specs recherchieren pro Modell.",
            "Tabelle mit Quellen-Spalte.",
            "Preis-Snapshot Datum.",
            "Gewichtetes Ranking optional.",
            "Kaufentscheid-Hinweise offen.",
            "Sheet Export.",
        ],
        dod=[
            "UNKNOWN statt raten",
            "Quelle pro Spec",
            "Neutrale Sprache",
            "Keine Fake-Reviews",
        ],
        safety=SAFETY_LIFE,
        pitfalls=[
            "US-Modell ohne EU-Spannung.",
            "Spec von Vorgängermodell übernommen.",
            "Einzelnes Affiliate-Review als Fakt.",
            "Garantiedauer Markt verwechselt.",
        ],
        examples=[
            {
                "aufgabe": "Staubsauger Vergleich",
                "input": "Dreame V12, Dyson V15, Bosch Unlimited",
                "prompt": "Akku Laufzeit, Gewicht, Hepa, Preis DE Stand heute.",
                "ergebnis": "Sheet 3 Spalten; Laufzeit eine UNKNOWN; Fußnote Messmethode Hersteller.",
            },
            {
                "aufgabe": "Smartphone Kamera",
                "input": "Pixel 9, iPhone 16, Galaxy S24",
                "prompt": "Sensor specs nur von Hersteller; kein DXO erfundene Werte.",
                "ergebnis": "Tabelle; Kamera UNKNOWN wo nicht veröffentlicht.",
            },
        ],
    ),
    "domains/persoenlich-lifestyle/termine-persoenlich/termine-persoenlich-workflow.md": render_body(
        zweck="Private und behördliche Termine bündeln, Unterlagen-Packlisten und Erinnerungen vorbereiten.",
        wann=[
            "Arzt + Behörde + Familie in einem Monatskalender harmonisieren.",
            "Termin mit Dokumenten-Checkliste (Ausweis, Bescheide).",
            "Nicht Termine beim Arzt ohne Nutzer buchen.",
        ],
        tools=GWS,
        system_prompt="""Role: Personal scheduling coordinator (persoenlich-lifestyle/termine-persoenlich).
Mission: Align appointments, document checklists, and draft calendar holds—user confirms bookings.
Tools: google-workspace calendar create drafts via gws; no unsolicited invites to third parties.
Timezone explicit Europe/Berlin default confirm.
Buffer travel between locations user estimates—agent suggests 15min default configurable.
Appointment types: medical, government, school, personal; prep list per type template.
Documents: ID, insurance card, referral, forms—checkbox per event.
No medical results interpretation.
Behörde: arrival early margin; ticket system note if user provides.
Privacy: event titles generic in shared calendars if user requests (e.g. Arzttermin vs specialty).
Conflicts detection when user exports existing ics.
Reminders T-1d and T-2h pattern optional.
Reschedule playbook if user misses slot.
No cold calls to offices on user behalf.
Import only user-supplied data; no mailbox scrape without permission.""",
        steps=[
            "Terminliste und bestehenden Kalender importieren.",
            "Konflikte markieren.",
            "Prep-Checklisten pro Termin.",
            "Reisezeit-Puffer.",
            "gws Event-Entwürfe.",
            "Nutzer akzeptiert Einträge.",
            "Wochenübersicht ausgeben.",
        ],
        dod=[
            "Zeitzone konsistent",
            "Keine Buchung ohne OK",
            "Dokumentenliste je Termin",
            "Geteilte Kalender privacy",
        ],
        safety=SAFETY_LIFE,
        pitfalls=[
            "DST Umstellung vergessen.",
            "Doppelbuchung zwei Ärzte.",
            "Falsche Behördenadresse.",
            "Öffentlicher Kalender sensible Titel.",
        ],
        examples=[
            {
                "aufgabe": "November Arzt + Bürgeramt",
                "input": "Hautarzt 14.11 10:30, Bürgeramt 19.11 8:00, 45 Min Fahrt",
                "prompt": "Kalender Drafts + Checkliste Ausweis Meldebescheinigung.",
                "ergebnis": "2 Events Draft; Checklisten 5 Items; Konflikt keiner.",
            },
            {
                "aufgabe": "Familien-Sporttraining Kinder",
                "input": "Training Di+Do 17:00, Eltern Abholung 18:15",
                "prompt": "Recurring Events Entwurf und Erinnerung T-30m.",
                "ergebnis": "RRULE Vorschlag; neutrale Titel Sport.",
            },
        ],
    ),
}