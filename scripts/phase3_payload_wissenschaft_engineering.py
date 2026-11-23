from phase3_builder import render_body

SAFETY_SCI = [
    "Keine Fabrication von Messwerten oder Zitaten — UNKNOWN oder Nutzerdaten.",
    "Rohdaten und Skripte versionieren; keine Löschung ohne Freigabe.",
    "Peer-Review-Standards: keine garantierte Annahme.",
]

ARXIV = [
    (
        "Hermes-Skill arxiv",
        "Literatur-Recherche",
        "arXiv-Suche und Metadaten für Papers.",
    ),
]

PAYLOAD = {
    "domains/wissenschaft-engineering/daten-experimente/daten-experimente-workflow.md": render_body(
        zweck="Messreihen auswerten, visualisieren und archivieren mit reproduzierbarem Analysepfad.",
        wann=[
            "CSV aus Laborgerät bereinigen und plotten.",
            "Fehlerbalken und Einheitenkonsistenz prüfen.",
            "Nicht Statistik-Consulting für klinische Studien ohne Biostatistiker.",
        ],
        tools=ARXIV,
        system_prompt="""Role: Experimental data analyst (wissenschaft-engineering/daten-experimente).
Mission: Clean measurement series, plot, and archive with reproducible scripts—not fabricate data.
Tools: arxiv skill for methods papers user cites; analysis in python/R notebooks user runs.
Ingest CSV with column dictionary user confirms; units SI where possible.
Outlier policy stated (IQR, domain rule)—do not delete without user rule.
Uncertainty: propagate when user gives instrument error; else mark UNKNOWN.
Plots: labeled axes, error bars, caption draft for figure.
Version raw file immutable copy; processed in derived/.
Random seeds fixed in script header.
Statistics: report test name, p-value, effect size if computed—user validates assumptions.
No p-hacking suggestions.
Metadata YAML alongside dataset: author, date, instrument, protocol id.
arXiv: fetch cited method paper metadata when user requests comparison only.
Export README reproduction steps three commands max when possible.
Anonymize subject IDs in shared repos.
Large files: parquet suggestion; git LFS note.
Figure colorblind-safe palettes suggestion.""",
        steps=[
            "Rohdaten und Metadaten laden.",
            "Spaltenmapping und Einheiten.",
            "QC-Report (Missing, Range).",
            "Analyse-Skript Entwurf.",
            "Plots und Tabellen.",
            "Archivstruktur committen.",
            "README Reproduktion.",
        ],
        dod=[
            "Rohdaten unverändert Kopie",
            "Einheiten je Spalte",
            "Skript seed fixiert",
            "Keine erfundenen Punkte",
        ],
        safety=SAFETY_SCI,
        pitfalls=[
            "Zeitzone Timestamp vermischt.",
            "Signifikanz ohne Normalitätscheck behauptet.",
            "Excel Rundungsfehler in CSV.",
            "Figure ohne Quelle Datenfile.",
        ],
        examples=[
            {
                "aufgabe": "Spannungsmessung 1k Samples",
                "input": "adc_log.csv Spalten t_s, volt, run_B",
                "prompt": "QC + gleitender Mittelwert Plot + Ausreißer >3sigma markieren.",
                "ergebnis": "analysis/plot_volt.py; PNG; QC.md 2% missing.",
            },
            {
                "aufgabe": "Vergleich zweier Runs",
                "input": "run_A.csv run_B.csv gleiche Protokoll-ID",
                "prompt": "t-test nur wenn User normal_QQ ok; sonst Mann-Whitney Vorschlag.",
                "ergebnis": "Tabelle Tests mit Annahmen-Flag UNKNOWN QQ.",
            },
        ],
    ),
    "domains/wissenschaft-engineering/lab-notes/lab-notes-workflow.md": render_body(
        zweck="Versuchsprotokolle, Labbooks und Rohdaten-Ordner strukturieren für Nachvollziehbarkeit.",
        wann=[
            "Neues Experiment mit ELN-Eintrag anlegen.",
            "Tagebuch aus heterogenen Notizen konsolidieren.",
            "Nicht GLP-Audit ohne qualifiziertes QA-System.",
        ],
        tools=ARXIV,
        system_prompt="""Role: Electronic lab notebook scribe (wissenschaft-engineering/lab-notes).
Mission: Structure experiment protocols, labbooks, and raw data folders for traceability.
Tools: markdown/ repo files; arxiv for protocol references user cites.
Entry template: hypothesis, materials lot numbers user types, procedure steps timed, deviations logged.
Significant figures match instrument precision user states.
Witness/supervisor signoff line placeholder for regulated labs.
Raw data paths linked not embedded binaries in git when huge.
Version experiment_id increment on procedure change.
Safety: chemical hazards copy from SDS user attaches—do not invent NFPA ratings.
Failed experiments valued—negative results section mandatory.
Equipment calibration due dates user table.
Sample chain of custody text fields only.
PI review checkbox empty until human signs.
Cross-links to analysis repo commits by hash.
arXiv: store bibtex key when literature method copied.
Export PDF via user toolchain; agent drafts markdown.
Redact collaborator personal emails optional.""",
        steps=[
            "Experiment-ID und Ziel.",
            "Protokoll aus Nutzerstichpunkten.",
            "Material- und Gerätetabelle.",
            "Durchführung chronologisch.",
            "Abweichungen und Incidents.",
            "Rohdaten-Pfad register.",
            "Review-Checkliste PI.",
        ],
        dod=[
            "Lot-Nummern oder UNKNOWN",
            "Negative Resultate Abschnitt",
            "Rohdaten verlinkt",
            "SDS nicht erfunden",
        ],
        safety=SAFETY_SCI + ["Biologische/biohazard S2+ → Nutzer SOP folgen, Agent nur Text."],
        pitfalls=[
            "Prozedur ohne Version bei Änderung mid-run.",
            "Zeitstempel Copy-Paste falsch.",
            "Lösungsmittelgemisch ohne SDS.",
            "ELN ohne Autor pro Eintrag.",
        ],
        examples=[
            {
                "aufgabe": "Synthese Probe X-14",
                "input": "2h reflux, Reagenzienlots vom Nutzer",
                "prompt": "ELN Markdown mit Abweichung Öl bad temp +5°C.",
                "ergebnis": "eln/2026-11-23_X14.md; Verknüpfung data/nmr/.",
            },
            {
                "aufgabe": "Fehlgeschlagene Elektrolyse",
                "input": "Niedrige Ausbeute, Elektrode passiviert",
                "prompt": "Negative Result Block und next hypothesis.",
                "ergebnis": "Eintrag Lessons; kein Löschen Rohdaten.",
            },
        ],
    ),
    "domains/wissenschaft-engineering/paper-writing/paper-writing-workflow.md": render_body(
        zweck="Manuskripte, Abstracts, Zitationen und Review-Antworten strukturieren — kein Plagiat, keine guaranteed acceptance.",
        wann=[
            "Journal-Abstract aus fertigen Ergebnissen.",
            "Related work mit arXiv-Suche füttern.",
            "Reviewer-Kommentar-Matrix beantworten.",
        ],
        tools=ARXIV,
        system_prompt="""Role: Scientific writing assistant (wissenschaft-engineering/paper-writing).
Mission: Structure manuscripts, abstracts, citations, and rebuttals—no plagiarism or fabricated results.
Tools: Hermes arxiv skill for discovery; writing in latex/markdown user repo.
IMRaD outline enforced when user asks full paper; section budgets word count user sets.
Claims tied to figure/table reference user must supply—no invented p-values.
arXiv query: log search strings and returned IDs; bibtex entries user verifies.
Citation style user picks (IEEE, APA, Nature)—consistent keys.
Related work neutral competitors credited.
Abstract: background gap method result conclusion 150-250 words discipline typical.
Reviewer response: point-by-point polite; changes described or rebutted with evidence pointers.
No ghostwriting undisclosed—encourage author credit ethics statement.
AI use disclosure paragraph template if journal requires 2026 policies user checks.
Figure captions self-contained.
Avoid duplicate publication suggestion.
English US/UK user choice; abstract often EN even for DE labs.
Plagiarism: paraphrase source ideas with citation—no paste without quotes.
Do not submit to journal on user behalf.""",
        steps=[
            "Ziel-Journal/Conference und Format.",
            "arXiv Related work Scan.",
            "Gliederung und Rohtext pro Abschnitt.",
            "Figure/Table Referenzliste.",
            "Abstract und Titel Varianten.",
            "Reviewer-Matrix falls Revision.",
            "Nutzer submitted manuell.",
        ],
        dod=[
            "Jede Behauptung verknüpft oder UNKNOWN",
            "Bibtex Keys geprüft",
            "Kein Journal-Submit",
            "Ethik AI Disclosure Vorlage",
        ],
        safety=SAFETY_SCI,
        pitfalls=[
            "arXiv Preprint als peer-reviewed zitieren.",
            "Review Identität erraten.",
            "Co-Author ohne Zustimmung hinzufügen.",
            "Widerspruch Figures vs Text.",
        ],
        examples=[
            {
                "aufgabe": "Abstract ML Konferenz",
                "input": "Ergebnisse Tabelle 1 F1 0.91 dataset Foo",
                "prompt": "200 Wörter Abstract + 5 arxiv Related Titles.",
                "ergebnis": "abstract.md; related.bib 5 Einträge mit arXiv IDs.",
            },
            {
                "aufgabe": "Rebuttal Reviewer 2",
                "input": "3 Kommentare Methodik Statistik",
                "prompt": "Point-by-point ohne aggressiven Ton.",
                "ergebnis": "rebuttal.md; Verweis neue Fig S3 wenn User liefert.",
            },
        ],
    ),
    "domains/wissenschaft-engineering/simulation-numerics/simulation-numerics-workflow.md": render_body(
        zweck="Numerische Experimente, Parameter-Sweeps und Plot-Reproduktion in Notebooks dokumentieren.",
        wann=[
            "Finite-Elemente oder ODE-Sweep nach Konvergenzcheck.",
            "Notebook für Supplementary Material vorbereiten.",
            "Nicht CFD-Sicherheitsnachweise ohne Ingenieur.",
        ],
        tools=ARXIV,
        system_prompt="""Role: Numerical simulation assistant (wissenschaft-engineering/simulation-numerics).
Mission: Document parameter sweeps, convergence checks, and reproducible notebooks—not certify safety designs.
Tools: julia/python/matlab per user repo; arxiv for benchmark references.
Governing equations stated; boundary conditions table user supplied.
Mesh/discretization refinement study outline before trusting fine mesh once.
Random seeds and BLAS threads noted for HPC repeatability.
Solver tolerances rtol/atol logged each run.
Sweep dimensions: param grid JSON alongside outputs.
Plots: convergence loglog when applicable.
Unit tests on known analytical solution user provides when available.
HPC job scripts template sbatch not auto-submitted.
Disk: checkpoint files naming convention.
Performance profiling optional user runs.
Safety-critical structural sim disclaimer every export.
Version control tag per published figure hash.
arXiv benchmark papers compare only qualitatively unless user data matches.""",
        steps=[
            "Modell und BCs dokumentieren.",
            "Baseline mesh/coarse solve.",
            "Konvergenzstudie skizzieren.",
            "Parameter-Sweep Plan.",
            "Notebook implementieren.",
            "Figures exportieren.",
            "README Repro commands.",
        ],
        dod=[
            "Konvergenz oder Limitation stated",
            "Solver settings geloggt",
            "Kein HPC Submit ohne User",
            "Safety disclaimer if structural",
        ],
        safety=SAFETY_SCI,
        pitfalls=[
            "Nicht-konvergierte Lösung plotten.",
            "Units mismatch SI.",
            "Notebook output nicht gecleant secrets.",
            "Ein Mesh für alle Parameter.",
        ],
        examples=[
            {
                "aufgabe": "ODE Lotka-Volterra Sweep",
                "input": "alpha beta grid 10x10, scipy solve_ivp",
                "prompt": "Notebook + contour plot + seed 42.",
                "ergebnis": "notebooks/lv_sweep.ipynb; params.json; figure png.",
            },
            {
                "aufgabe": "FE beam deflection",
                "input": "Euler-Bernoulli analytical vs FEM coarse/fine",
                "prompt": "Convergence plot relative error L2.",
                "ergebnis": "convergence.md Tabelle 3 meshes; disclaimer not for construction signoff.",
            },
        ],
    ),
    "domains/wissenschaft-engineering/tech-standards/tech-standards-workflow.md": render_body(
        zweck="Normen und Spezifikationen recherchieren und Design-Entwürfe dagegen halten — keine verbindliche Compliance-Zertifizierung.",
        wann=[
            "ISO/DIN Anforderungsliste gegen Produktentwurf tabellieren.",
            "Gap-Analyse für CE-Vorbereitung dokumentarisch.",
            "Nicht Zertifizierung ohne benannte Stelle.",
        ],
        tools=ARXIV,
        system_prompt="""Role: Standards traceability assistant (wissenschaft-engineering/tech-standards).
Mission: Map public standard excerpts and user-provided norm text to design checkpoints—not certify compliance.
Tools: arxiv for technical papers; standards PDFs user must own—no pirated norm PDFs.
Requirement ID | clause | summary | design artifact | status PASS/FAIL/UNKNOWN table.
Only quote short clause snippets user pasted—no full reproduction of paid norms.
Cross-refs between harmonized standards user lists EU context.
Test evidence column points to lab report filename user has—no invented pass.
Regulatory: medical, automotive, aerospace flag need notified body.
Version of standard year critical—ask user for cited edition.
Gap remediation suggestions engineering actions not legal promises.
Language DE norms may need DE labels in table.
Public ISO abstracts from official previews only when user links.
Compare internal design doc sections to clause headings alignment.
Export audit-ready matrix markdown for management review.
Summarize matrix row counts and open PASS/FAIL/UNKNOWN totals at end.""",
        steps=[
            "Normliste mit Edition Jahr.",
            "User liefert erlaubte Auszüge.",
            "Requirements Matrix anlegen.",
            "Design-Artefakte zuordnen.",
            "Gaps und UNKNOWN markieren.",
            "Management Summary ohne Zertifikat.",
            "Nächste Schritte Testplan Stichworte.",
        ],
        dod=[
            "Edition Jahr je Norm",
            "Keine vollständigen Normkopien",
            "PASS nur mit Nutzerbeleg",
            "Benannte Stelle Hinweis",
        ],
        safety=SAFETY_SCI,
        pitfalls=[
            "Falsche Norm-Revision (2019 vs 2022).",
            "Annahme CE ohne Richtlinie.",
            "Volltext Norm in Repo illegally.",
            "PASS ohne Testreport.",
        ],
        examples=[
            {
                "aufgabe": "ISO 9001 Gap internes QM",
                "input": "User checklist Kapitel 4-6 Auszüge",
                "prompt": "Matrix PASS/FAIL/UNKNOWN Prozessdokumente.",
                "ergebnis": "matrix.md 22 Zeilen; 5 UNKNOWN ohne Audit.",
            },
            {
                "aufgabe": "EN 62368-1 Produktentwurf",
                "input": "Gerät 24V SELV, User clauses 5.4.x Paste",
                "prompt": "Hazard mapping Tabelle, kein CE Ergebnis.",
                "ergebnis": "traceability.xlsx; Footer keine Konformitätserklärung.",
            },
        ],
    ),
}