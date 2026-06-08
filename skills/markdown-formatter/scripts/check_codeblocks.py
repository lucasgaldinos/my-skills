#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "markdown-it-py>=4.0.0",
# ]
# ///
"""
check_codeblocks.py — Validate fenced code blocks in markdown files.

Checks (rule 3):
- Every fenced code block must specify a language
- Backtick fences only — no tilde fences (MD048)

Run with: uv run check_codeblocks.py README.md [--json]
"""

import argparse
import json
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

from markdown_it import MarkdownIt

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
            print(
                f"{color}{f.severity.upper()}{reset} {f.file}:{f.line} [{f.rule}] {f.message}"
            )
    return 1 if any(f.severity == "error" for f in findings) else 0


def check_codeblocks(filepath: Path) -> list[Finding]:
    findings: list[Finding] = []
    fname = str(filepath)
    text = filepath.read_text(encoding="utf-8")

    md = MarkdownIt("commonmark")
    tokens = md.parse(text)

    for token in tokens:
        if token.type != "fence":
            continue

        line = (token.map[0] + 1) if token.map else 0
        info = token.info.strip()

        # --- Language specifier required ---
        if not info:
            findings.append(
                Finding(
                    fname,
                    line,
                    "error",
                    "codeblock-no-language",
                    "Fenced code block must specify a language. (MD040)",
                )
            )

        # --- Backtick fences only ---
        if token.markup.startswith("~"):
            findings.append(
                Finding(
                    fname,
                    line,
                    "warning",
                    "codeblock-tilde-fence",
                    "Use backtick fences (```), not tilde fences (~~~). (MD048)",
                )
            )

    return findings


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Validate fenced code blocks in markdown files"
    )
    parser.add_argument("files", nargs="+", type=Path, help="Markdown files to check")
    parser.add_argument(
        "--json", dest="as_json", action="store_true", help="Output findings as JSON"
    )
    args = parser.parse_args()

    all_findings: list[Finding] = []
    for f in args.files:
        if not f.exists():
            print(f"Error: {f} not found", file=sys.stderr)
            continue
        all_findings.extend(check_codeblocks(f))

    exit_code = print_findings(all_findings, as_json=args.as_json)
    if not all_findings and not args.as_json:
        print(f"\033[32m✓\033[0m All files passed code block validation.")
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
