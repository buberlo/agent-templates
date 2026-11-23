#!/usr/bin/env python3
import json
import re
import sys
from datetime import UTC, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = ROOT / "template.schema.json"
DOMAINS_DIR = ROOT / "domains"
SKIP_NAMES = {"_category.md", "_domain.md", "TEMPLATE.md"}


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
        "## Zweck",
        "## Wann nutzen",
        "## Tool-Stack",
        "## System-Prompt / Instruktionen",
        "## Arbeitsablauf",
        "## Qualitätskriterien / Definition of Done",
        "## Sicherheit & Freigaben",
        "## Fallstricke",
        "## Grundbeispiele",
    ]


def extract_system_prompt_block(body):
    m = re.search(
        r"## System-Prompt / Instruktionen\s+```(?:text)?\s*\n(.*?)```",
        body,
        re.S,
    )
    if not m:
        return None
    return m.group(1)


def quality_content_checks(body):
    errors = []
    if re.search(r"\{slug\}|\{title\}|\{domain\}|\{category\}", body):
        errors.append("unrendered placeholder token in body")
    if re.search(r"Standard-.+-Aufgabe", body):
        errors.append("boilerplate Standard-*-Aufgabe")
    if "output/{slug}-demo" in body or (
        "Artefakt: output/" in body and "{slug}" in body
    ):
        errors.append("boilerplate demo output path")
    if re.search(r"Status: OK\s*\nArtefakt:", body):
        errors.append("boilerplate Status: OK / Artefakt")
    if re.search(r"You are a specialist for \w+ \(", body):
        errors.append("generic one-line system prompt opener")
    sp = extract_system_prompt_block(body)
    if sp is None:
        errors.append("missing fenced system prompt block")
    elif len([ln for ln in sp.splitlines() if ln.strip()]) < 10:
        errors.append("system prompt fewer than 10 non-empty lines")
    wf = body.split("## Arbeitsablauf", 1)
    if len(wf) > 1:
        wf_part = wf[1].split("##", 1)[0]
        steps = re.findall(r"^\d+\.\s+", wf_part, re.M)
        if len(steps) < 5:
            errors.append("Arbeitsablauf fewer than 5 numbered steps")
    pit = body.split("## Fallstricke", 1)
    if len(pit) > 1:
        pit_part = pit[1].split("##", 1)[0]
        bullets = re.findall(r"^\s*[-*]\s+", pit_part, re.M)
        if len(bullets) < 3:
            errors.append("Fallstricke fewer than 3 bullet items")
    return errors


def count_grundbeispiele(body):
    if "## Grundbeispiele" not in body:
        return 0
    part = body.split("## Grundbeispiele", 1)[1]
    return len(re.findall(r"^### Beispiel \d+", part, re.M))


def main():
    schema = load_schema()
    templates = discover_templates()
    all_errors = []
    catalog = {
        "generated_at": datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "domains": [],
        "templates": [],
    }
    seen_ids = {}
    category_tpl_count = {}
    domains_seen = {}

    if not templates:
        print("No templates found under domains/", file=sys.stderr)
        return 1

    expected_cats = discover_category_meta()

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
        found = count_grundbeispiele(body)
        if isinstance(ec, int) and found < ec:
            errs.append(f"Grundbeispiele: found {found}, example_count {ec}")
        if isinstance(ec, int) and found < 2:
            errs.append("fewer than 2 Grundbeispiele")
        errs.extend(quality_content_checks(body))
        if errs:
            all_errors.extend([f"{rel}: {e}" for e in errs])
        else:
            key = (data["domain"], data["category"])
            category_tpl_count[key] = category_tpl_count.get(key, 0) + 1
            domains_seen[data["domain"]] = domains_seen.get(data["domain"], 0) + 1
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
                    "path": str(rel).replace("\\", "/"),
                }
            )

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

    catalog["templates"].sort(key=lambda x: (x["domain"], x["category"], x["id"]))
    by_domain = {}
    for t in catalog["templates"]:
        by_domain.setdefault(t["domain"], {}).setdefault(t["category"], []).append(t)

    for dom in sorted(by_domain.keys()):
        cats = []
        for cat in sorted(by_domain[dom].keys()):
            cats.append({"slug": cat, "template_count": len(by_domain[dom][cat])})
        catalog["domains"].append(
            {"slug": dom, "category_count": len(cats), "template_count": sum(c["template_count"] for c in cats), "categories": cats}
        )

    catalog_path = ROOT / "catalog.json"
    with catalog_path.open("w", encoding="utf-8") as f:
        json.dump(catalog, f, indent=2, ensure_ascii=False)
        f.write("\n")

    lines = [
        "# Template-Index",
        "",
        f"Automatisch generiert. **{len(catalog['domains'])}** Domains, **{len(expected_cats)}** Kategorien, **{len(catalog['templates'])}** Templates.",
        "",
    ]
    for dom in sorted(by_domain.keys()):
        dcount = sum(len(v) for v in by_domain[dom].values())
        lines.append(f"## Domain: `{dom}` ({dcount} Templates)")
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

    print(f"OK: {len(catalog['domains'])} domains, {len(expected_cats)} categories, {len(catalog['templates'])} templates.")
    print(f"Wrote {index_path.name} and {catalog_path.name}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())