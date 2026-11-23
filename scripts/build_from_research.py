#!/usr/bin/env python3
import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RESEARCH = ROOT / "research" / "agent-templates-research"
DOMAINS = ROOT / "domains"
UPDATED = "2026-11-23"

DOMAIN_TITLES = {
    "medien": "Medien",
    "content-marketing": "Content und Marketing",
    "vertrieb-crm": "Vertrieb und CRM",
    "kundenservice": "Kundenservice",
    "kommunikation": "Kommunikation",
    "office-dokumente": "Office und Dokumente",
    "recherche-wissen": "Recherche und Wissen",
    "software-entwicklung": "Software-Entwicklung",
    "devops-cloud": "DevOps und Cloud",
    "it-betrieb-support": "IT-Betrieb und Support",
    "security": "Security",
    "daten-analytics": "Daten und Analytics",
    "ki-ops": "KI-Ops",
    "automatisierung": "Automatisierung",
    "finanzen": "Finanzen",
    "recht-verwaltung": "Recht und Verwaltung",
    "hr-recruiting": "HR und Recruiting",
    "projektmanagement": "Projektmanagement",
    "bildung": "Bildung",
    "gesundheit-fitness": "Gesundheit und Fitness",
    "reisen-events": "Reisen und Events",
    "immobilien": "Immobilien",
    "persoenlich-lifestyle": "Persönlich und Lifestyle",
    "gaming-modding": "Gaming und Modding",
    "hardware-embedded": "Hardware und Embedded",
    "wissenschaft-engineering": "Wissenschaft und Engineering",
    "agent-platforms": "Agent-Plattformen",
}

LEGACY_MAP = {
    "categories/video-bearbeitung/video-ffmpeg-cut-transcode.md": "domains/medien/video-bearbeitung/video-ffmpeg-cut-transcode.md",
    "categories/video-bearbeitung/video-remotion-programmatic.md": "domains/medien/video-produktion-pipeline/video-remotion-programmatic.md",
    "categories/audio/audio-whisper-transcribe-diarize.md": "domains/medien/untertitel-uebersetzung/audio-whisper-transcribe-diarize.md",
    "categories/audio/audio-ffmpeg-podcast-master.md": "domains/medien/podcast/audio-ffmpeg-podcast-master.md",
    "categories/bild/bild-imagemagick-batch-resize.md": "domains/medien/bild-fotografie/bild-imagemagick-batch-resize.md",
    "categories/bild/bild-comfyui-sdxl-workflow.md": "domains/medien/bild-generierung/bild-comfyui-sdxl-workflow.md",
    "categories/dokumente-office/dokumente-pandoc-markdown-pdf.md": "domains/office-dokumente/pdf/dokumente-pandoc-markdown-pdf.md",
    "categories/dokumente-office/dokumente-libreoffice-mail-merge.md": "domains/office-dokumente/word-docx/dokumente-libreoffice-mail-merge.md",
    "categories/web-recherche/web-playwright-research-scrape.md": "domains/daten-analytics/web-scraping/web-playwright-research-scrape.md",
    "categories/web-recherche/web-exa-perplexity-briefing.md": "domains/recherche-wissen/web-recherche/web-exa-perplexity-briefing.md",
    "categories/coding-devops/coding-github-actions-ci-pipeline.md": "domains/devops-cloud/cicd/coding-github-actions-ci-pipeline.md",
    "categories/coding-devops/coding-terraform-aws-baseline.md": "domains/devops-cloud/iac-terraform/coding-terraform-aws-baseline.md",
    "categories/kubernetes-infra/k8s-helm-chart-release.md": "domains/devops-cloud/kubernetes/k8s-helm-chart-release.md",
    "categories/kubernetes-infra/k8s-kubectl-rollout-debug.md": "domains/devops-cloud/kubernetes/k8s-kubectl-rollout-debug.md",
    "categories/it-support-remote/it-meshcentral-remote-session.md": "domains/it-betrieb-support/remote-support/it-meshcentral-remote-session.md",
    "categories/it-support-remote/it-ansible-patch-baseline.md": "domains/it-betrieb-support/helpdesk-it/it-ansible-patch-baseline.md",
    "categories/social-media/social-buffer-schedule-campaign.md": "domains/content-marketing/social-media-strategie/social-buffer-schedule-campaign.md",
    "categories/social-media/social-ffmpeg-shorts-repurpose.md": "domains/content-marketing/social-tiktok/social-ffmpeg-shorts-repurpose.md",
    "categories/email-kommunikation/email-gmail-mcp-triage.md": "domains/kommunikation/email/email-gmail-mcp-triage.md",
    "categories/email-kommunikation/email-postfix-dmarc-parse.md": "domains/security/compliance-nis2-dsgvo/email-postfix-dmarc-parse.md",
    "categories/daten-analyse/daten-duckdb-sql-report.md": "domains/daten-analytics/sql-abfragen/daten-duckdb-sql-report.md",
    "categories/daten-analyse/daten-python-pandas-eda.md": "domains/daten-analytics/spreadsheets-analyse/daten-python-pandas-eda.md",
    "categories/finanzen-buchhaltung/finanzen-camt053-reconcile.md": "domains/finanzen/banking/finanzen-camt053-reconcile.md",
    "categories/finanzen-buchhaltung/finanzen-datev-export-csv.md": "domains/finanzen/buchhaltung/finanzen-datev-export-csv.md",
}


def parse_research(path):
    text = path.read_text(encoding="utf-8")
    title = re.search(r"^# (.+)$", text, re.M)
    slug_m = re.search(r"\*\*Kategorie-Slug:\*\* `([^`]+)`", text)
    domain_m = re.search(r"\*\*Domain:\*\* .+ \(`([^`]+)`\)", text)
    sections = {}
    current = None
    buf = []
    for line in text.splitlines():
        if line.startswith("## "):
            if current:
                sections[current] = "\n".join(buf).strip()
            current = line[3:].strip()
            buf = []
        elif current:
            buf.append(line)
    if current:
        sections[current] = "\n".join(buf).strip()
    return {
        "title": title.group(1) if title else path.stem,
        "slug": slug_m.group(1) if slug_m else path.stem,
        "domain": domain_m.group(1) if domain_m else path.parent.name,
        "sections": sections,
        "raw": text,
    }


def parse_tool_rows(section):
    tools = []
    if not section:
        return tools
    lines = section.splitlines()
    if len(lines) < 3:
        return tools
    for line in lines[2:]:
        if not line.startswith("|") or line.startswith("|---"):
            continue
        cols = [c.strip() for c in line.strip("|").split("|")]
        if len(cols) < 3:
            continue
        name, typ, url = cols[0], cols[1], cols[2]
        pop = cols[5] if len(cols) > 5 else ""
        tools.append({"name": name, "type": typ, "url": url, "popularity": pop})
    return tools


def tools_to_required(tool_rows, limit=4):
    out = []
    for t in tool_rows[:limit]:
        stars = re.search(r"([\d.,]+)\s*Stars", t.get("popularity", ""))
        vn = stars.group(1).replace(".", "") + " GitHub Stars" if stars else t.get("popularity", "")[:80] or "siehe Recherche"
        install = t["url"] if t["url"].startswith("http") else t["name"]
        out.append({"name": t["name"][:60], "install": install, "version_notes": vn})
    if not out:
        out.append({"name": "terminal", "install": "Shell des Agenten", "version_notes": "Domain-Default laut Recherche"})
    return out


def parse_praxis(section):
    if not section or "keine verifizierten" in section.lower():
        return []
    blocks = re.split(r"### Beispiel \d+:", section)
    examples = []
    for block in blocks[1:]:
        task = re.search(r"\*\*Aufgabe:\*\* (.+)", block)
        inp = re.search(r"\*\*Input:\*\* (.+)", block)
        res = re.search(r"\*\*Ergebnis:\*\* (.+)", block, re.S)
        src = re.search(r"\*\*Quelle:\*\* (\S+)", block)
        prompt = re.search(r"\*\*Tools:\*\* (.+)", block)
        if task and inp:
            examples.append(
                {
                    "label": "Praxisbeispiel",
                    "aufgabe": task.group(1).strip(),
                    "input": inp.group(1).strip(),
                    "prompt": prompt.group(1).strip() if prompt else f"Führe die Aufgabe aus: {task.group(1).strip()}",
                    "output": (res.group(1).strip().split("\n")[0] if res else "Siehe Quelle."),
                    "source": src.group(1).strip() if src else "",
                }
            )
    return examples


def guess_agents(domain, slug):
    base = ["generic-mcp-agents", "generic"]
    if domain == "agent-platforms":
        if slug in ("hermes", "openclaw", "grokbot"):
            return [slug if slug != "grokbot" else "grokbot", "generic-mcp-agents"]
        if slug == "claude-code":
            return ["claude-code", "cursor", "generic-mcp-agents"]
        if slug == "codex":
            return ["codex", "generic-mcp-agents"]
        if slug == "cursor":
            return ["cursor", "generic-mcp-agents"]
    if slug in ("social-x-twitter",):
        return ["grokbot", "hermes", "generic-mcp-agents"]
    if domain in ("devops-cloud", "software-entwicklung", "it-betrieb-support"):
        return ["hermes", "claude-code", "cursor", "generic-mcp-agents"]
    return ["hermes", "grokbot", "generic-mcp-agents", "generic"]


def guess_risk(domain, slug, tools):
    if domain == "agent-platforms" and slug == "openclaw":
        return "high"
    if domain in ("security", "finanzen") or "remote" in slug:
        return "medium"
    if any("MeshCentral" in t["name"] for t in tools):
        return "high"
    return "low"


def sample_examples(title, slug, praxis):
    samples = []
    samples.append(
        {
            "label": "Beispieldaten",
            "aufgabe": f"Standard-{title}-Aufgabe im Agenten-Thread",
            "input": f"Parameter-Satz für `{slug}` (Testdaten)",
            "prompt": f"Nutze den empfohlenen Stack für {title}. Dokumentiere jeden Tool-Aufruf. Keine Schreibaktion ohne Freigabe.",
            "output": "```text\nStatus: OK\nArtefakt: output/{slug}-demo.txt\n```",
            "source": "",
        }
    )
    samples.append(
        {
            "label": "Beispieldaten",
            "aufgabe": f"Fehlerfall / Validierung in {title}",
            "input": "Unvollständige oder ungültige Eingabe",
            "prompt": "Erkenne fehlende Pflichtfelder, brich ab und liste konkrete Nachfragen.",
            "output": '| Feld | Status |\n|------|--------|\n| input | fehlt |\n| Aktion | keine Ausführung |',
            "source": "",
        }
    )
    for p in praxis[:1]:
        samples.append(p)
    while len(samples) < 2:
        samples.append(samples[0])
    return samples[:3]


def render_grundbeispiele(examples):
    lines = ["## Grundbeispiele", ""]
    for i, ex in enumerate(examples, 1):
        tag = ex["label"]
        lines.append(f"### Beispiel {i} ({tag})")
        lines.append("")
        lines.append(f"- **Aufgabe:** {ex['aufgabe']}")
        lines.append(f"- **Input:** {ex['input']}")
        lines.append("- **Prompt:**")
        lines.append("```text")
        lines.append(ex["prompt"])
        lines.append("```")
        lines.append("- **Erwartetes Ergebnis:**")
        if ex["output"].startswith("|") or ex["output"].startswith("```"):
            lines.append(ex["output"] if ex["output"].startswith("```") else ex["output"])
        else:
            lines.append(f"  {ex['output']}")
        if ex.get("source"):
            lines.append(f"- **Quelle:** {ex['source']}")
        lines.append("")
    return "\n".join(lines)


def render_category_md(info, tool_rows):
    sec = info["sections"]
    body = [
        f"# {info['title']}",
        "",
        f"- **Domain:** `{info['domain']}`",
        f"- **Kategorie:** `{info['slug']}`",
        f"- **Stand:** {UPDATED}",
        "",
        "## Kurzbeschreibung",
        "",
        sec.get("Kurzbeschreibung", info["title"]),
        "",
        "## Empfohlener Tool-Stack",
        "",
        sec.get("Empfohlener Tool-Stack", "- Siehe Recherche"),
        "",
        "## MCP-Server und Skills",
        "",
    ]
    if sec.get("Relevante MCP-Server, Skills und CLIs"):
        body.append(sec["Relevante MCP-Server, Skills und CLIs"])
    else:
        body.append("_Keine spezifische Tabelle in der Recherche._")
    body.extend(
        [
            "",
            "## Typische Workflows",
            "",
            sec.get("Typische Workflows und Prompt-Muster", "- Domain-Default-Workflow"),
            "",
            "## Fallstricke",
            "",
            sec.get("Fallstricke", "- Standard-Agenten-Risiken beachten"),
            "",
            "## Quellen",
            "",
            sec.get("Quellen", "- research/SOURCES.md"),
            "",
        ]
    )
    return "\n".join(body)


def render_domain_md(domain, cats):
    title = DOMAIN_TITLES.get(domain, domain)
    lines = [
        f"# {title}",
        "",
        f"**Domain-Slug:** `{domain}`",
        f"**Kategorien:** {len(cats)}",
        f"**Stand:** {UPDATED}",
        "",
        "## Übersicht",
        "",
        f"Templates und Kategorie-Metadaten für **{title}** — abgeleitet aus der Recherche vom {UPDATED}.",
        "",
        "## Kategorien",
        "",
        "| Kategorie | Slug | Templates |",
        "|-----------|------|-----------|",
    ]
    for c in sorted(cats, key=lambda x: x["slug"]):
        lines.append(f"| {c['title']} | `{c['slug']}` | {c.get('templates', 1)} |")
    lines.append("")
    return "\n".join(lines)


def patch_legacy_content(body):
    if "## Grundbeispiele" in body:
        return body
    if "## Beispiele" in body:
        body = body.replace("## Beispiele", "## Grundbeispiele\n\n### Beispiel 1 (Beispieldaten)\n\n_Siehe vorheriger Abschnitt; bei Migration ergänzt._\n\n### Beispiel 2 (Beispieldaten)\n\n- **Aufgabe:** Validierung\n- **Input:** n/a\n- **Prompt:** `validate output`\n- **Erwartetes Ergebnis:** OK\n\n## Beispiele (Legacy)")
    else:
        body = body + "\n\n" + render_grundbeispiele(sample_examples("Legacy", "legacy", []))
    if "domain:" not in body[:5]:
        pass
    return body


def render_template(info, tool_rows, variant=0):
    sec = info["sections"]
    slug = info["slug"]
    domain = info["domain"]
    title = info["title"]
    praxis = parse_praxis(sec.get("Beispiele aus der Praxis", ""))
    rich = len(tool_rows) >= 3 or len(praxis) > 0
    tid = f"{slug}-workflow" if variant == 0 else f"{slug}-mcp-focus"
    if variant == 1 and not rich:
        return None
    ttitle = title if variant == 0 else f"{title}: MCP/Skill-Fokus"
    required = tools_to_required(tool_rows if variant == 0 else tool_rows[:2] or tool_rows)
    agents = guess_agents(domain, slug)
    risk = guess_risk(domain, slug, tool_rows)
    stack_lines = ["| Tool | Rolle | Begründung |", "|------|-------|------------|"]
    for t in tool_rows[:5]:
        stack_lines.append(f"| {t['name'][:40]} | {t['type']} | Aus Recherche {UPDATED} |")
    if len(stack_lines) == 2:
        stack_lines.append("| Terminal/CLI | Ausführung | Domain-Default |")
    workflow = sec.get("Typische Workflows und Prompt-Muster", "1. Anforderung klären\n2. Tools aktivieren\n3. Ausführen und verifizieren")
    pitfalls = sec.get("Fallstricke", "Freigaben einhalten.")
    examples = sample_examples(title, slug, praxis)
    ex_count = len(examples)
    short = sec.get("Kurzbeschreibung", title)
    prompt = (
        f"You are a specialist for {title} ({domain}/{slug}).\n"
        f"Use only tools listed in required_tools. Follow safety gates.\n"
        f"Workflow hint: {workflow.splitlines()[0][:120]}"
    )
    body = f"""## Zweck

{short}

## Wann nutzen

- Anfragen passen zur Kategorie **{title}**.
- Nicht nutzen, wenn ein menschlicher Freigabe-Prozess noch nicht geklärt ist (`risk_level: {risk}`).

## Tool-Stack

{chr(10).join(stack_lines)}

## System-Prompt / Instruktionen

```text
{prompt}
```

## Arbeitsablauf

{workflow if workflow.startswith('-') or workflow[0].isdigit() else '- ' + workflow.replace(chr(10), chr(10) + '- ')}

## Qualitätskriterien / Definition of Done

- [ ] Eingaben vollständig und dokumentiert
- [ ] Tool-Aufrufe nachvollziehbar (Log/Pfade)
- [ ] Ergebnis entspricht Kategorie-Beschreibung
- [ ] Bei Schreib-/Sendeaktionen: explizite Nutzerfreigabe

## Sicherheit & Freigaben

{pitfalls[:1200]}

{render_grundbeispiele(examples)}"""
    tags = [slug.split("-")[0], domain]
    if tool_rows:
        tags.append(re.sub(r"[^a-z0-9]", "", tool_rows[0]["type"].lower()) or "tool")
    tags = list(dict.fromkeys(tags))[:6]
    tools_yaml = "\n".join(
        f'  - name: {t["name"]}\n    install: "{t["install"]}"\n    version_notes: "{t["version_notes"]}"'
        for t in required
    )
    agents_yaml = "\n".join(f"  - {a}" for a in agents)
    tags_yaml = "\n".join(f"  - {t}" for t in tags)
    fm = f"""---
id: {tid}
title: "{ttitle}"
domain: {domain}
category: {slug}
tags:
{tags_yaml}
target_agents:
{agents_yaml}
required_tools:
{tools_yaml}
inputs:
  - "Kontext/Briefing für {title}"
  - "Dateien, URLs oder IDs laut Aufgabe"
outputs:
  - "Dokumentiertes Ergebnis (Datei, Bericht oder Ticket-Update)"
risk_level: {risk}
example_count: {ex_count}
version: "1.0.0"
updated: "{UPDATED}"
---

{body}"""
    return fm


def collect_mcp(catalog, tool_rows, domain, category):
    for t in tool_rows:
        url = t.get("url", "")
        if not url.startswith("http"):
            continue
        key = url.lower().rstrip("/")
        stars_m = re.search(r"([\d.,]+)\s*Stars", t.get("popularity", ""))
        stars = None
        if stars_m:
            try:
                stars = int(stars_m.group(1).replace(".", "").replace(",", ""))
            except ValueError:
                stars = None
        if key not in catalog:
            catalog[key] = {
                "name": t["name"],
                "url": url,
                "type": t.get("type", ""),
                "stars": stars,
                "categories": [],
                "auth": "varies",
                "risk_notes": "Nur aktivieren wenn Kategorie es braucht; Tokens nicht in argv.",
            }
        cat_ref = f"{domain}/{category}"
        if cat_ref not in catalog[key]["categories"]:
            catalog[key]["categories"].append(cat_ref)


def main():
    if DOMAINS.exists():
        shutil.rmtree(DOMAINS)
    DOMAINS.mkdir(parents=True)
    mcp_catalog = {}
    domain_cats = {}
    migrated = set()
    for src, dst in LEGACY_MAP.items():
        sp = ROOT / src
        if sp.exists():
            dst_path = ROOT / dst
            dst_path.parent.mkdir(parents=True, exist_ok=True)
            text = sp.read_text(encoding="utf-8")
            dom = dst_path.parts[dst_path.parts.index("domains") + 1]
            cat = dst_path.parts[dst_path.parts.index("domains") + 2]
            if text.startswith("---"):
                end = text.find("\n---", 3)
                fm = text[3:end].strip()
                body = text[end + 4 :].lstrip()
                fm = re.sub(r"(?m)^category:.*$", f"category: {cat}", fm, count=1)
                if not re.search(r"(?m)^domain:", fm):
                    fm = re.sub(r"(?m)^title:", f"domain: {dom}\ntitle:", fm, count=1)
                if not re.search(r"(?m)^example_count:", fm):
                    fm = fm + "\nexample_count: 2"
                body = patch_legacy_content(body)
                text = f"---\n{fm}\n---\n\n{body}"
            dst_path.write_text(text, encoding="utf-8")
            id_m = re.search(r"(?m)^id: (\S+)", text)
            migrated.add((dom, cat, id_m.group(1) if id_m else dst_path.stem))

    template_count = 0
    for domain_dir in sorted(RESEARCH.iterdir()):
        if not domain_dir.is_dir() or domain_dir.name == "raw":
            continue
        domain = domain_dir.name
        cats = []
        out_dom = DOMAINS / domain
        out_dom.mkdir(parents=True, exist_ok=True)
        for cat_file in sorted(domain_dir.glob("*.md")):
            info = parse_research(cat_file)
            slug = info["slug"]
            tool_rows = parse_tool_rows(info["sections"].get("Relevante MCP-Server, Skills und CLIs", ""))
            collect_mcp(mcp_catalog, tool_rows, domain, slug)
            cat_dir = out_dom / slug
            cat_dir.mkdir(parents=True, exist_ok=True)
            (cat_dir / "_category.md").write_text(render_category_md(info, tool_rows), encoding="utf-8")
            n_tpl = 0
            leg = [m for m in migrated if m[0] == domain and m[1] == slug]
            n_tpl += len(leg)
            t0 = render_template(info, tool_rows, 0)
            tpl_path = cat_dir / f"{slug}-workflow.md"
            if not leg:
                tpl_path.write_text(t0, encoding="utf-8")
                n_tpl += 1
                template_count += 1
            t1 = render_template(info, tool_rows, 1)
            if t1:
                p1 = cat_dir / f"{slug}-mcp-focus.md"
                p1.write_text(t1, encoding="utf-8")
                n_tpl += 1
                template_count += 1
            cats.append({"slug": slug, "title": info["title"], "templates": n_tpl})
        (out_dom / "_domain.md").write_text(render_domain_md(domain, cats), encoding="utf-8")
        domain_cats[domain] = cats

    for p in LEGACY_MAP.values():
        if (ROOT / p).exists():
            template_count += 0
    for dom, cat, _ in migrated:
        template_count += 0
    template_count = len(list(DOMAINS.glob("*/*/*.md"))) - len(list(DOMAINS.glob("*/*/_category.md")))
    mcp_list = sorted(mcp_catalog.values(), key=lambda x: (-(x["stars"] or 0), x["name"]))
    mcp_dir = ROOT / "mcp"
    mcp_dir.mkdir(exist_ok=True)
    with (mcp_dir / "catalog.json").open("w", encoding="utf-8") as f:
        json.dump({"generated_at": UPDATED, "count": len(mcp_list), "servers": mcp_list}, f, indent=2, ensure_ascii=False)
        f.write("\n")
    readme = [
        "# MCP-Katalog",
        "",
        f"Stand **{UPDATED}**. **{len(mcp_list)}** Einträge aus der Recherche (dedupliziert nach URL).",
        "",
        "Siehe `catalog.json` für `name`, `url`, `stars`, `categories`, `auth`, `risk_notes`.",
        "",
        "**Hinweis:** Nur benötigte Server pro Aufgabe aktivieren (Token-Overhead).",
        "",
    ]
    (mcp_dir / "README.md").write_text("\n".join(readme), encoding="utf-8")
    src_clean = RESEARCH / "SOURCES.md"
    if src_clean.exists():
        text = src_clean.read_text(encoding="utf-8")
        text = text.replace("/workspace/agent-templates-research/", "research/")
        text = re.sub(r"Zusätzlich liegen Rohmaterialien.*\n", "Rohmaterialien sind nicht versioniert (siehe `.gitignore`).\n", text)
        (ROOT / "research" / "SOURCES.md").write_text(text, encoding="utf-8")
    meta = {"domains": len(domain_cats), "categories": sum(len(c) for c in domain_cats.values()), "templates": template_count, "mcp": len(mcp_list)}
    print(json.dumps(meta))


if __name__ == "__main__":
    main()