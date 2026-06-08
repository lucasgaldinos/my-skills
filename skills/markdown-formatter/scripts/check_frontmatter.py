#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "markdown-it-py>=4.0.0",
#   "mdit-py-plugins>=0.4.0",
#   "pyyaml>=6.0",
# ]
# ///
"""
check_frontmatter.py — Validate YAML front matter in markdown files.

Checks (rule 0):
- Front matter block exists and is first in the file
- Required fields: title, tags, date_created, date_changed
- Dates are valid ISO 8601 (YYYY-MM-DD) and date_changed >= date_created
- Title approximately matches the document's H1 header

Run with: uv run check_frontmatter.py README.md [--json]
"""

import argparse
import json
import sys
from dataclasses import asdict, dataclass
from datetime import date
from pathlib import Path
from typing import Any, cast

import yaml
from markdown_it import MarkdownIt
from mdit_py_plugins.front_matter import front_matter_plugin

REQUIRED_FIELDS = ("title", "tags", "date_created", "date_changed")

COLORS = {
    "error": "\033[31m",
    "warning": "\033[33m",
    "info": "\033[36m",
    "reset": "\033[0m",
}


@dataclass
class Finding:
    file: str
    line: int
    severity: str
    rule: str
    message: str


def print_findings(findings: list[Finding], *, as_json: bool = False) -> int:
    if as_json:
        print(json.dumps([asdict(f) for f in findings], indent=2))
    else:
        for f in findings:
            color = COLORS.get(f.severity, "")
            reset = COLORS["reset"]
            print(f"{color}{f.severity.upper()}{reset} {f.file}:{f.line} [{f.rule}] {f.message}")
    return 1 if any(f.severity == "error" for f in findings) else 0


def _parse_date(value: object) -> date | None:
    try:
        if isinstance(value, date):
            return value
        return date.fromisoformat(str(value))
    except (ValueError, TypeError):
        return None


def check_frontmatter(filepath: Path) -> list[Finding]:
    findings: list[Finding] = []
    fname = str(filepath)
    text = filepath.read_text(encoding="utf-8")

    md = MarkdownIt("commonmark").use(front_matter_plugin)
    tokens = md.parse(text)

    # --- Presence check ---
    fm_tokens = [t for t in tokens if t.type == "front_matter"]
    if not fm_tokens:
        findings.append(
            Finding(fname, 1, "error", "frontmatter-missing",
                    "No YAML front matter found. Every file must start with a --- block.")
        )
        return findings

    fm_token = fm_tokens[0]
    fm_line = (fm_token.map[0] + 1) if fm_token.map else 1

    # --- Position check ---
    if tokens.index(fm_token) != 0:
        findings.append(
            Finding(fname, 1, "error", "frontmatter-position",
                    "Front matter must be the very first thing in the file.")
        )

    # --- YAML validity ---
    try:
        data = yaml.safe_load(fm_token.content)
    except yaml.YAMLError as exc:
        findings.append(
            Finding(fname, fm_line, "error", "frontmatter-invalid-yaml",
                    f"Invalid YAML in front matter: {exc}")
        )
        return findings

    if not isinstance(data, dict):
        findings.append(
            Finding(fname, fm_line, "error", "frontmatter-not-mapping",
                    "Front matter must be a YAML mapping (key: value pairs).")
        )
        return findings

    data = cast(dict[str, Any], data)

    # --- Required fields ---
    for field in REQUIRED_FIELDS:
        if field not in data:
            findings.append(
                Finding(fname, fm_line, "error", f"frontmatter-missing-{field}",
                        f"Required field '{field}' is missing from front matter.")
            )
        elif data[field] is None or (isinstance(data[field], str) and not data[field].strip()):
            findings.append(
                Finding(fname, fm_line, "error", f"frontmatter-empty-{field}",
                        f"Required field '{field}' is present but empty.")
            )

    # --- Date validation ---
    dc = _parse_date(data.get("date_created")) if "date_created" in data else None
    dch = _parse_date(data.get("date_changed")) if "date_changed" in data else None

    if "date_created" in data and dc is None:
        findings.append(
            Finding(fname, fm_line, "error", "frontmatter-date-format",
                    f"date_created '{data['date_created']}' is not a valid ISO 8601 date (YYYY-MM-DD).")
        )
    if "date_changed" in data and dch is None:
        findings.append(
            Finding(fname, fm_line, "error", "frontmatter-date-format",
                    f"date_changed '{data['date_changed']}' is not a valid ISO 8601 date (YYYY-MM-DD).")
        )
    if dc and dch and dch < dc:
        findings.append(
            Finding(fname, fm_line, "warning", "frontmatter-date-order",
                    f"date_changed ({dch}) is before date_created ({dc}).")
        )

    # --- Title vs H1 match ---
    title = data.get("title")
    if title and isinstance(title, str):
        h1_tokens = [t for t in tokens if t.type == "heading_open" and t.tag == "h1"]
        if h1_tokens:
            h1_idx = tokens.index(h1_tokens[0])
            if h1_idx + 1 < len(tokens) and tokens[h1_idx + 1].type == "inline":
                h1_text = tokens[h1_idx + 1].content.strip()
                if h1_text.lower() != title.strip().lower():
                    h1_line = (h1_tokens[0].map[0] + 1) if h1_tokens[0].map else 1
                    findings.append(
                        Finding(fname, h1_line, "warning", "frontmatter-title-mismatch",
                                f"Title '{title.strip()}' doesn't match H1 '{h1_text}'.")
                    )

    return findings


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate YAML front matter in markdown files")
    parser.add_argument("files", nargs="+", type=Path, help="Markdown files to check")
    parser.add_argument("--json", dest="as_json", action="store_true",
                        help="Output findings as JSON")
    args = parser.parse_args()

    all_findings: list[Finding] = []
    for f in args.files:
        if not f.exists():
            print(f"Error: {f} not found", file=sys.stderr)
            continue
        all_findings.extend(check_frontmatter(f))

    exit_code = print_findings(all_findings, as_json=args.as_json)
    if not all_findings and not args.as_json:
        print(f"\033[32m✓\033[0m All files passed front matter validation.")
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
