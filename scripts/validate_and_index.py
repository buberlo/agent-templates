#!/usr/bin/env python3
import json
import re
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = ROOT / "template.schema.json"
DOMAINS_DIR = ROOT / "domains"
SKIP_NAMES = {"_category.md", "_domain.md", "TEMPLATE.md"}

GERMAN_UMLAUT = re.compile(r"[äöüÄÖÜß]")
LEGACY_GERMAN_HEADINGS = re.compile(
    r"^##\s+(Zweck|Wann nutzen|Tool-Stack|Arbeitsablauf|Fallstricke|Grundbeispiele|"
    r"Qualitätskriterien|Sicherheit & Freigaben|System-Prompt / Instruktionen|"
    r"Kurzbeschreibung|Übersicht|Empfohlener Tool-Stack|Quellen)\b",
    re.M,
)
GERMAN_HEADING_MARKERS = re.compile(
    r"\b(Zweck|Wann nutzen|Arbeitsablauf|Fallstricke|Grundbeispiele|Beispiel|Beispieldaten|"
    r"Praxisbeispiel|Qualitätskriterien|Kurzbeschreibung|Übersicht|Begründung|Einsatz|"
    r"Popularität|Freigaben)\b",
    re.I,
)
GERMAN_PATH_MARKERS = re.compile(
    r"(ä|ö|ü|ß|finanzen|automatisierung|bildung|daten-analytics|gesundheit-fitness|immobilien|"
    r"it-betrieb|(?<![a-z-])ki-ops(?![a-z-])|kommunikation|kundenservice|(?:^|/)medien/|office-dokumente|persoenlich|"
    r"projektmanagement|recherche-wissen|recht-verwaltung|reisen-events|wissenschaft-engineering|"
    r"software-entwicklung|vertrieb-crm|ernaehrung|buchhaltung|rechnungen|steuern|behoerden|"
    r"vertraege|fluege|reiseplanung|spielbibliotheken|untertitel|bearbeitung|bild-generierung|"
    r"dreid-|elektronik-diagnose|exposes|verwaltung-weg|identitaet-sso|lokale-modelle|"
    r"mcp-server-bau|meetings-transkription|sql-abfragen|spreadsheets-analyse|content-strategie|"
    r"plattform-deploy|cloud-kosten)",
    re.I,
)
GERMAN_MARKER_WORDS = re.compile(
    r"\b(Zweck|Arbeitsablauf|Grundbeispiele|Beispieldaten|Praxisbeispiel|Lieferobjekt|"
    r"Eingabe|Freigabe|Kurzbeschreibung|Implementierung|Reiseplanung|Nutzer|Dateien|"
    r"Katalog|Begründung|Fallstricke|Qualitätskriterien|Sicherheit|wurde|können|koennen|"
    r"Keine|keine|nicht|für|fuer)\b",
    re.I,
)


def split_frontmatter(text):
    if not text.startswith("---"):
        return None, text
    end = text.find("\n---", 3)
    if end == -1:
        return None, text
    body_start = end + 4
    if body_start < len(text) and text[body_start] == "\n":
        body_start += 1
    fm = text[3:end].strip()
    body = text[body_start:]
    return fm, body


def parse_scalar(value):
    value = value.strip()
    if not value:
        return ""
    if value in ("true", "True"):
        return True
    if value in ("false", "False"):
        return False
    if value in ("null", "~"):
        return None
    if value.startswith('"') and value.endswith('"'):
        return value[1:-1].replace('\\"', '"')
    if value.startswith("'") and value.endswith("'"):
        return value[1:-1]
    if re.fullmatch(r"-?\d+", value):
        return int(value)
    return value


def parse_block(lines, indent=0):
    result = {}
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip() or line.strip().startswith("#"):
            i += 1
            continue
        stripped = line.lstrip()
        cur_indent = len(line) - len(stripped)
        if cur_indent < indent:
            break
        if stripped.startswith("- "):
            break
        if ":" not in stripped:
            i += 1
            continue
        key, rest = stripped.split(":", 1)
        key = key.strip()
        rest = rest.strip()
        if rest:
            result[key] = parse_scalar(rest)
            i += 1
            continue
        items = []
        obj_lines = []
        j = i + 1
        while j < len(lines):
            nxt = lines[j]
            if not nxt.strip():
                j += 1
                continue
            nxt_stripped = nxt.lstrip()
            nxt_indent = len(nxt) - len(nxt_stripped)
            if nxt_indent <= cur_indent:
                break
            if nxt_stripped.startswith("- "):
                if obj_lines:
                    break
                item_text = nxt_stripped[2:].strip()
                if item_text and ":" in item_text and not item_text.startswith('"'):
                    block = [nxt_stripped[2:]]
                    k = j + 1
                    while k < len(lines):
                        inner = lines[k]
                        if not inner.strip():
                            k += 1
                            continue
                        inner_stripped = inner.lstrip()
                        inner_indent = len(inner) - len(inner_stripped)
                        if inner_indent <= nxt_indent:
                            break
                        if inner_stripped.startswith("- "):
                            break
                        block.append(inner_stripped)
                        k += 1
                    items.append(parse_block(block, 0))
                    j = k
                    continue
                items.append(parse_scalar(item_text))
                j += 1
                continue
            obj_lines.append(nxt_stripped)
            j += 1
        if items:
            result[key] = items
        elif obj_lines:
            result[key] = parse_block(obj_lines, cur_indent + 2)
        else:
            result[key] = []
        i = j
    return result


def parse_yaml_frontmatter(fm_text):
    lines = fm_text.splitlines()
    return parse_block(lines, 0)


def load_schema():
    with SCHEMA_PATH.open(encoding="utf-8") as f:
        return json.load(f)


def validate_type(value, t):
    if t == "string":
        return isinstance(value, str)
    if t == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if t == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    if t == "boolean":
        return isinstance(value, bool)
    if t == "array":
        return isinstance(value, list)
    if t == "object":
        return isinstance(value, dict)
    return True


def validate_value(value, schema, path="$"):
    errors = []
    if "enum" in schema:
        if value not in schema["enum"]:
            errors.append(f"{path}: value {value!r} not in enum {schema['enum']}")
    if "type" in schema:
        if not validate_type(value, schema["type"]):
            errors.append(f"{path}: expected {schema['type']}, got {type(value).__name__}")
            return errors
    if schema.get("type") == "string" and isinstance(value, str):
        if "minLength" in schema and len(value) < schema["minLength"]:
            errors.append(f"{path}: string shorter than minLength")
        if "maxLength" in schema and len(value) > schema["maxLength"]:
            errors.append(f"{path}: string longer than maxLength")
        if "pattern" in schema and not re.fullmatch(schema["pattern"], value):
            errors.append(f"{path}: does not match pattern {schema['pattern']}")
        if schema.get("format") == "date":
            try:
                datetime.strptime(value, "%Y-%m-%d")
            except ValueError:
                errors.append(f"{path}: invalid date format (YYYY-MM-DD)")
    if schema.get("type") == "integer" and isinstance(value, int):
        if "minimum" in schema and value < schema["minimum"]:
            errors.append(f"{path}: below minimum")
        if "maximum" in schema and value > schema["maximum"]:
            errors.append(f"{path}: above maximum")
    if schema.get("type") == "array" and isinstance(value, list):
        if "minItems" in schema and len(value) < schema["minItems"]:
            errors.append(f"{path}: array shorter than minItems")
        if "maxItems" in schema and len(value) > schema["maxItems"]:
            errors.append(f"{path}: array longer than maxItems")
        if schema.get("uniqueItems"):
            seen = []
            for item in value:
                key = json.dumps(item, sort_keys=True)
                if key in seen:
                    errors.append(f"{path}: duplicate items")
                    break
                seen.append(key)
        if "items" in schema:
            for i, item in enumerate(value):
                errors.extend(validate_value(item, schema["items"], f"{path}[{i}]"))
    if schema.get("type") == "object" and isinstance(value, dict):
        if schema.get("additionalProperties") is False:
            allowed = set(schema.get("properties", {}).keys())
            for key in value:
                if key not in allowed:
                    errors.append(f"{path}.{key}: additional property not allowed")
        for key, subschema in schema.get("properties", {}).items():
            if key in value:
                errors.extend(validate_value(value[key], subschema, f"{path}.{key}"))
        for req in schema.get("required", []):
            if req not in value:
                errors.append(f"{path}: missing required property '{req}'")
    return errors


def validate_frontmatter(data, schema):
    return validate_value(data, schema, "$")


def discover_templates():
    files = sorted(DOMAINS_DIR.glob("*/*/*.md"))
    return [p for p in files if p.name not in SKIP_NAMES and not p.name.startswith("_")]


def discover_category_meta():
    cats = set()
    for p in DOMAINS_DIR.glob("*/*/_category.md"):
        domain = p.parent.parent.name
        category = p.parent.name
        cats.add((domain, category))
    return cats


def required_body_sections():
    return [
        "## Purpose",
        "## When to use",
        "## Tool stack",
        "## System prompt",
        "## Workflow",
        "## Definition of done",
        "## Security",
        "## Pitfalls",
        "## Basic examples",
    ]


def extract_system_prompt_block(body):
    m = re.search(
        r"## System prompt\s+```(?:text)?\s*\n(.*?)```",
        body,
        re.S,
    )
    if not m:
        return None
    return m.group(1)


MIN_SYSTEM_PROMPT_CHARS = 350
MIN_SENTENCE_LIKE_LINES = 3
MIN_EXPECTED_OUTPUT_CHARS = 40
MAX_COLON_KEYWORD_WITHOUT_SENTENCES = (5, 5)

SENTENCE_LIKE_RE = re.compile(
    r"(^(You are\b)|(\b(must|should|never|always|Do not|will|When|If|Before|After)\b)|"
    r"(\b(the|a|an)\b.*\b(the|a|an)\b))",
    re.I,
)


def system_prompt_non_empty_lines(sp: str) -> list[str]:
    return [ln.strip() for ln in sp.splitlines() if ln.strip()]


def line_is_colon_keyword_fragment(line: str) -> bool:
    line = line.strip()
    if re.match(r"^Role:\s", line, re.I):
        return True
    return bool(
        re.match(r"^[A-Za-z][\w\s/&-]*:\s+\S", line) and len(line.split()) < 18
    )


def line_is_sentence_like(line: str) -> bool:
    line = line.strip()
    if line_is_colon_keyword_fragment(line):
        return False
    words = line.split()
    if len(words) < 8:
        return False
    if SENTENCE_LIKE_RE.search(line):
        return True
    if len(words) >= 14 and re.search(r"[.!?]\s*$", line):
        return True
    return False


def extract_basic_examples_expected_outputs(body: str) -> list[str]:
    if "## Basic examples" not in body:
        return []
    part = body.split("## Basic examples", 1)[1]
    outputs = []
    for pattern in (
        r"\*\*Expected result:\*\*\s*\n\n```(?:text|bash)?\s*\n(.*?)```",
        r"\*\*Expected result:\*\*\s+```(?:text|bash)?\s*\n(.*?)```",
    ):
        for m in re.finditer(pattern, part, re.S):
            outputs.append(m.group(1).strip())
    return outputs


def quality_content_checks(body):
    errors = []
    if re.search(r"\{slug\}|\{title\}|\{domain\}|\{category\}", body):
        errors.append("unrendered placeholder token in body")
    if re.search(r"Standard-.+-Aufgabe", body):
        errors.append("boilerplate Standard-*-Aufgabe marker")
    if "output/{slug}-demo" in body or (
        "Artefakt: output/" in body and "{slug}" in body
    ):
        errors.append("boilerplate demo output path")
    if re.search(r"Status: OK\s*\nArtefakt:", body):
        errors.append("boilerplate Status: OK / Artefakt")
    if re.search(r"You are a specialist for \w+ \(", body):
        errors.append("generic one-line system prompt opener")
    if "## Basic examples" in body:
        if not re.search(
            r"^### Example \d+ \(Example data \(self-written\)\)",
            body,
            re.M,
        ):
            errors.append(
                "Basic examples must use heading (Example data (self-written))"
            )
    sp = extract_system_prompt_block(body)
    if sp is None:
        errors.append("missing fenced system prompt block")
    elif len(system_prompt_non_empty_lines(sp)) < 10:
        errors.append("system prompt fewer than 10 non-empty lines")
    elif len(sp.strip()) < MIN_SYSTEM_PROMPT_CHARS:
        errors.append(
            f"system prompt shorter than {MIN_SYSTEM_PROMPT_CHARS} characters"
        )
    else:
        lines = system_prompt_non_empty_lines(sp)
        sentence_like = sum(1 for ln in lines if line_is_sentence_like(ln))
        colon_keyword = sum(1 for ln in lines if line_is_colon_keyword_fragment(ln))
        if sentence_like < MIN_SENTENCE_LIKE_LINES:
            errors.append(
                f"system prompt has fewer than {MIN_SENTENCE_LIKE_LINES} "
                "sentence-like lines (keyword-salad risk)"
            )
        min_colon, min_sent = MAX_COLON_KEYWORD_WITHOUT_SENTENCES
        if colon_keyword >= min_colon and sentence_like < min_sent:
            errors.append(
                "system prompt looks like keyword list (many Label: fragments)"
            )
    for idx, expected in enumerate(extract_basic_examples_expected_outputs(body), 1):
        if len(expected) < MIN_EXPECTED_OUTPUT_CHARS:
            errors.append(
                f"Example expected output {idx} shorter than "
                f"{MIN_EXPECTED_OUTPUT_CHARS} characters"
            )
    wf = body.split("## Workflow", 1)
    if len(wf) > 1:
        wf_part = wf[1].split("##", 1)[0]
        steps = re.findall(r"^\d+\.\s+", wf_part, re.M)
        if len(steps) < 5:
            errors.append("Workflow section has fewer than 5 numbered steps")
    pit = body.split("## Pitfalls", 1)
    if len(pit) > 1:
        pit_part = pit[1].split("##", 1)[0]
        bullets = re.findall(r"^\s*[-*]\s+", pit_part, re.M)
        if len(bullets) < 3:
            errors.append("Pitfalls section has fewer than 3 bullet items")
    return errors


def count_basic_examples(body):
    if "## Basic examples" not in body:
        return 0
    part = body.split("## Basic examples", 1)[1]
    return len(re.findall(r"^### Example \d+", part, re.M))


def text_has_german(text: str) -> bool:
    if not text or not text.strip():
        return False
    if GERMAN_UMLAUT.search(text):
        return True
    if LEGACY_GERMAN_HEADINGS.search(text):
        return True
    return bool(GERMAN_MARKER_WORDS.search(text))


def path_has_legacy_german(rel: str) -> bool:
    parts = Path(rel).parts
    if "domains" not in parts:
        return False
    i = parts.index("domains")
    for seg in parts[i + 1 :]:
        if GERMAN_UMLAUT.search(seg):
            return True
        if GERMAN_PATH_MARKERS.search(seg) and not re.fullmatch(r"3d-[a-z0-9-]+", seg):
            return True
    return False


def language_gate(rel: str, fm_text: str | None, data: dict | None, body: str, full_text: str):
    errors = []
    if path_has_legacy_german(rel):
        errors.append("language gate: German or legacy slug in file path")
    if fm_text and text_has_german(fm_text):
        errors.append("language gate: German text in frontmatter")
    if data:
        for field in ("domain", "category", "id", "title"):
            val = data.get(field)
            if isinstance(val, str) and text_has_german(val):
                errors.append(f"language gate: German in frontmatter {field}")
        for field in ("tags", "inputs", "outputs"):
            for val in data.get(field) or []:
                if isinstance(val, str) and text_has_german(val):
                    errors.append(f"language gate: German in frontmatter {field}")
        for tool in data.get("required_tools") or []:
            if isinstance(tool, dict):
                for key in ("name", "install", "version_notes"):
                    val = tool.get(key)
                    if isinstance(val, str) and text_has_german(val):
                        errors.append(f"language gate: German in required_tools.{key}")
    if LEGACY_GERMAN_HEADINGS.search(body):
        errors.append("language gate: legacy German section heading in body")
    for line in body.splitlines():
        if line.startswith("##") and text_has_german(line):
            errors.append(f"language gate: German section heading {line.strip()!r}")
    if text_has_german(body):
        errors.append("language gate: German text in body")
    return errors


def catalog_generated_at(templates: list[dict]) -> str:
    dates = [t["updated"] for t in templates if t.get("updated")]
    if not dates:
        return "1970-01-01T00:00:00Z"
    latest = max(dates)
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", latest):
        return f"{latest}T00:00:00Z"
    return latest


def main():
    schema = load_schema()
    templates = discover_templates()
    all_errors = []
    catalog = {
        "generated_at": None,
        "domains": [],
        "templates": [],
    }
    seen_ids = {}
    expected_cats = discover_category_meta()

    if not templates:
        print("No templates found under domains/", file=sys.stderr)
        return 1

    validated_templates = []

    for path in sorted(DOMAINS_DIR.rglob("*.md")):
        if path.name not in ("_domain.md", "_category.md"):
            continue
        rel = path.relative_to(ROOT)
        text = path.read_text(encoding="utf-8")
        lang_errs = language_gate(str(rel), None, None, text, text)
        if lang_errs:
            all_errors.extend([f"{rel}: {e}" for e in lang_errs])

    for path in templates:
        rel = path.relative_to(ROOT)
        text = path.read_text(encoding="utf-8")
        fm_text, body = split_frontmatter(text)
        if fm_text is None:
            all_errors.append(f"{rel}: missing YAML frontmatter")
            continue
        try:
            data = parse_yaml_frontmatter(fm_text)
        except Exception as exc:
            all_errors.append(f"{rel}: frontmatter parse error: {exc}")
            continue
        errs = validate_frontmatter(data, schema)
        errs.extend(language_gate(str(rel), fm_text, data, body, text))

        dom_folder = path.parts[path.parts.index("domains") + 1]
        cat_folder = path.parts[path.parts.index("domains") + 2]
        if data.get("domain") and data["domain"] != dom_folder:
            errs.append(f"domain mismatch folder {dom_folder}")
        if data.get("category") and data["category"] != cat_folder:
            errs.append(f"category mismatch folder {cat_folder}")
        tid = data.get("id")
        if tid:
            if tid in seen_ids:
                errs.append(f"duplicate id '{tid}' (also in {seen_ids[tid]})")
            else:
                seen_ids[tid] = str(rel)
        for section in required_body_sections():
            if section not in body:
                errs.append(f"missing section {section}")
        ec = data.get("example_count")
        found = count_basic_examples(body)
        if isinstance(ec, int) and found < ec:
            errs.append(f"Basic examples: found {found}, example_count {ec}")
        if isinstance(ec, int) and found < 2:
            errs.append("fewer than 2 Basic examples")
        errs.extend(quality_content_checks(body))
        if errs:
            all_errors.extend([f"{rel}: {e}" for e in errs])
        else:
            validated_templates.append((data, str(rel).replace("\\", "/")))

    for domain, category in sorted(expected_cats):
        cat_dir = DOMAINS_DIR / domain / category
        tpl_files = [
            p
            for p in cat_dir.glob("*.md")
            if p.name not in SKIP_NAMES and not p.name.startswith("_")
        ]
        if not tpl_files:
            all_errors.append(f"domains/{domain}/{category}: no template files")

    if all_errors:
        print("Validation failed:", file=sys.stderr)
        for e in all_errors:
            print(f"  - {e}", file=sys.stderr)
        return 1

    for data, relpath in validated_templates:
        catalog["templates"].append(
            {
                "id": data["id"],
                "title": data["title"],
                "domain": data["domain"],
                "category": data["category"],
                "tags": data["tags"],
                "target_agents": data["target_agents"],
                "risk_level": data["risk_level"],
                "example_count": data["example_count"],
                "version": data["version"],
                "updated": data["updated"],
                "path": relpath,
            }
        )

    catalog["templates"].sort(key=lambda x: (x["domain"], x["category"], x["id"]))
    catalog["generated_at"] = catalog_generated_at(catalog["templates"])

    by_domain = {}
    for t in catalog["templates"]:
        by_domain.setdefault(t["domain"], {}).setdefault(t["category"], []).append(t)

    for dom in sorted(by_domain.keys()):
        cats = []
        for cat in sorted(by_domain[dom].keys()):
            cats.append({"slug": cat, "template_count": len(by_domain[dom][cat])})
        catalog["domains"].append(
            {
                "slug": dom,
                "category_count": len(cats),
                "template_count": sum(c["template_count"] for c in cats),
                "categories": cats,
            }
        )

    catalog_path = ROOT / "catalog.json"
    with catalog_path.open("w", encoding="utf-8") as f:
        json.dump(catalog, f, indent=2, ensure_ascii=False)
        f.write("\n")

    lines = [
        "# Template index",
        "",
        f"Auto-generated. **{len(catalog['domains'])}** domains, **{len(expected_cats)}** categories, **{len(catalog['templates'])}** templates.",
        "",
    ]
    for dom in sorted(by_domain.keys()):
        dcount = sum(len(v) for v in by_domain[dom].values())
        lines.append(f"## Domain: `{dom}` ({dcount} templates)")
        lines.append("")
        for cat in sorted(by_domain[dom].keys()):
            tpls = by_domain[dom][cat]
            lines.append(f"### `{dom}/{cat}` ({len(tpls)})")
            lines.append("")
            lines.append("| id | title | agents | risk | examples |")
            lines.append("|----|-------|--------|------|----------|")
            for t in tpls:
                agents = ", ".join(t["target_agents"][:3])
                if len(t["target_agents"]) > 3:
                    agents += "…"
                lines.append(
                    f"| `{t['id']}` | {t['title']} | {agents} | {t['risk_level']} | {t['example_count']} |"
                )
            lines.append("")
    index_path = ROOT / "INDEX.md"
    index_path.write_text("\n".join(lines), encoding="utf-8")

    print(
        f"OK: {len(catalog['domains'])} domains, {len(expected_cats)} categories, {len(catalog['templates'])} templates."
    )
    print(f"Wrote {index_path.name} and {catalog_path.name}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())