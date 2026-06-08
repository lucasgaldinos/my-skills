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
validate_all.py — Orchestrator: run all markdown validation checks in one command.

Imports check functions from each domain script (all have if __name__ == "__main__",
so they can still be run standalone). This script aggregates findings and exits
with code 1 if any errors are found, 0 otherwise.

Run with:
  uv run validate_all.py README.md                               # all checks
  uv run validate_all.py *.md                                    # multiple files
  uv run validate_all.py README.md --check frontmatter math      # specific checks
  uv run validate_all.py README.md --fix-tables                  # auto-fix tables
  uv run validate_all.py README.md --json                        # JSON output

Available checks: frontmatter, math, admonitions, codeblocks, footnotes, tables, xml
"""

import argparse
import json
import sys
from collections.abc import Set as AbstractSet
from dataclasses import asdict
from pathlib import Path
from typing import Any, Callable

# Make sibling scripts importable without installing them as packages.
# __file__ is the absolute path of this script when run via uv run --script.
sys.path.insert(0, str(Path(__file__).parent))

from check_admonitions import check_admonitions  # noqa: E402
from check_codeblocks import check_codeblocks  # noqa: E402
from check_footnotes import check_footnotes  # noqa: E402
from check_frontmatter import check_frontmatter  # noqa: E402
from check_math import check_math  # noqa: E402
from check_xml_tags import check_xml_tags  # noqa: E402
from format_table import check_and_fix_tables  # noqa: E402

COLORS = {
    "error": "\033[31m",
    "warning": "\033[33m",
    "info": "\033[36m",
    "reset": "\033[0m",
}


def _make_checks(fix_tables: bool = False) -> dict[str, Callable[[Path], list[Any]]]:
    return {
        "frontmatter": check_frontmatter,
        "math": check_math,
        "admonitions": check_admonitions,
        "codeblocks": check_codeblocks,
        "footnotes": check_footnotes,
        "tables": lambda f: check_and_fix_tables(f, fix=fix_tables),
        "xml": check_xml_tags,
    }


def run_all(
    filepath: Path,
    enabled: AbstractSet[str],
    fix_tables: bool = False,
) -> list[dict[str, Any]]:
    checks = _make_checks(fix_tables)
    all_findings: list[dict[str, Any]] = []

    for name, fn in checks.items():
        if name not in enabled:
            continue
        try:
            findings = fn(filepath)
            all_findings.extend(asdict(f) for f in findings)
        except Exception as exc:
            all_findings.append({
                "file": str(filepath),
                "line": 0,
                "severity": "error",
                "rule": f"check-{name}-crash",
                "message": f"Check '{name}' crashed unexpectedly: {type(exc).__name__}: {exc}",
            })

    all_findings.sort(key=lambda f: f["line"])
    return all_findings


def print_aggregate(findings: list[dict[str, Any]], *, as_json: bool = False) -> int:
    if as_json:
        print(json.dumps(findings, indent=2))
    else:
        prev_file = None
        for f in findings:
            if f["file"] != prev_file:
                prev_file = f["file"]
                print(f"\n\033[1m{f['file']}\033[0m")
            color = COLORS.get(f["severity"], "")
            reset = COLORS["reset"]
            print(f"  {color}{f['severity'].upper():7}{reset} :{f['line']} [{f['rule']}] {f['message']}")
    return 1 if any(f["severity"] == "error" for f in findings) else 0


ALL_CHECKS = ("frontmatter", "math", "admonitions", "codeblocks", "footnotes", "tables", "xml")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run all markdown validation checks in one command.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=f"Available checks: {', '.join(ALL_CHECKS)}",
    )
    parser.add_argument("files", nargs="+", type=Path, help="Markdown files to validate")
    parser.add_argument(
        "--check",
        metavar="NAME",
        dest="checks",
        action="append",
        choices=list(ALL_CHECKS),
        help="Enable specific check(s). Repeatable. Default: all checks.",
    )
    parser.add_argument(
        "--fix-tables",
        action="store_true",
        help="Auto-reformat non-compact tables in-place (tables check only).",
    )
    parser.add_argument("--json", dest="as_json", action="store_true",
                        help="Output findings as JSON array.")
    args = parser.parse_args()

    enabled = set(args.checks) if args.checks else set(ALL_CHECKS)

    all_findings: list[dict[str, Any]] = []
    for filepath in args.files:
        if not filepath.exists():
            print(f"Error: {filepath} not found", file=sys.stderr)
            continue
        all_findings.extend(run_all(filepath, enabled, fix_tables=args.fix_tables))

    exit_code = print_aggregate(all_findings, as_json=args.as_json)
    if not all_findings and not args.as_json:
        checks_run = ", ".join(sorted(enabled))
        print(f"\033[32m✓\033[0m All checks passed [{checks_run}].")
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
