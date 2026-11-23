#!/usr/bin/env python3
import json
import re
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = ROOT / "template.schema.json"
CATEGORIES_DIR = ROOT / "categories"
TEMPLATE_BASENAMES = {"TEMPLATE.md"}


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
            elif key in schema.get("required", []):
                errors.append(f"{path}: missing required property '{key}'")
        for req in schema.get("required", []):
            if req not in value:
                errors.append(f"{path}: missing required property '{req}'")
    return errors


def validate_frontmatter(data, schema):
    errors = validate_value(data, schema, "$")
    ids = set()
    if isinstance(data.get("id"), str):
        if data["id"] in ids:
            errors.append("duplicate id")
        ids.add(data["id"])
    return errors


def discover_templates():
    files = sorted(CATEGORIES_DIR.glob("*/*.md"))
    return [p for p in files if p.name not in TEMPLATE_BASENAMES]


def required_body_sections(body):
    return [
        "## Zweck",
        "## Wann nutzen",
        "## Tool-Stack",
        "## System-Prompt / Instruktionen",
        "## Arbeitsablauf",
        "## Qualitätskriterien / Definition of Done",
        "## Sicherheit & Freigaben",
        "## Beispiele",
    ]


def main():
    schema = load_schema()
    templates = discover_templates()
    all_errors = []
    catalog = {"generated_at": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"), "templates": []}
    seen_ids = {}

    if not templates:
        print("No templates found under categories/", file=sys.stderr)
        return 1

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
        cat_folder = path.parent.name
        if data.get("category") and data["category"] != cat_folder:
            errs.append(f"{rel}: category '{data['category']}' != folder '{cat_folder}'")
        tid = data.get("id")
        if tid:
            if tid in seen_ids:
                errs.append(f"{rel}: duplicate id '{tid}' (also in {seen_ids[tid]})")
            else:
                seen_ids[tid] = str(rel)
        for section in required_body_sections(body):
            if section not in body:
                errs.append(f"{rel}: missing section {section}")
        if errs:
            all_errors.extend([f"{rel}: {e}" for e in errs])
        else:
            catalog["templates"].append(
                {
                    "id": data["id"],
                    "title": data["title"],
                    "category": data["category"],
                    "tags": data["tags"],
                    "target_agents": data["target_agents"],
                    "risk_level": data["risk_level"],
                    "version": data["version"],
                    "updated": data["updated"],
                    "path": str(rel).replace("\\", "/"),
                }
            )

    if all_errors:
        print("Validation failed:", file=sys.stderr)
        for e in all_errors:
            print(f"  - {e}", file=sys.stderr)
        return 1

    catalog["templates"].sort(key=lambda x: (x["category"], x["id"]))
    catalog_path = ROOT / "catalog.json"
    with catalog_path.open("w", encoding="utf-8") as f:
        json.dump(catalog, f, indent=2, ensure_ascii=False)
        f.write("\n")

    by_cat = {}
    for t in catalog["templates"]:
        by_cat.setdefault(t["category"], []).append(t)

    lines = [
        "# Template-Index",
        "",
        f"Automatisch generiert. Anzahl Templates: **{len(catalog['templates'])}**.",
        "",
    ]
    for cat in sorted(by_cat.keys()):
        lines.append(f"## {cat}")
        lines.append("")
        lines.append("| id | title | agents | risk | version | updated |")
        lines.append("|----|-------|--------|------|---------|---------|")
        for t in by_cat[cat]:
            agents = ", ".join(t["target_agents"])
            lines.append(
                f"| `{t['id']}` | {t['title']} | {agents} | {t['risk_level']} | {t['version']} | {t['updated']} |"
            )
        lines.append("")
    index_path = ROOT / "INDEX.md"
    index_path.write_text("\n".join(lines), encoding="utf-8")

    print(f"OK: {len(catalog['templates'])} templates validated.")
    print(f"Wrote {index_path.relative_to(ROOT)} and {catalog_path.relative_to(ROOT)}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())