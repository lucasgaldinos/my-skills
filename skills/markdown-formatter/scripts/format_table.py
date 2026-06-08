#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""
format_table.py — Validate and reformat markdown tables to compact style.

Checks (rule 8):
- Tables use compact style with minimal spacing (MD060 compact)
- Leading and trailing pipes on every row (MD055)
- Consistent column count across rows (MD056)

Modes:
- Default: report non-compact tables as findings
- --fix: reformat tables in-place to compact style

Run with:
  uv run format_table.py README.md            # validate only
  uv run format_table.py README.md --fix      # fix in-place
  uv run format_table.py README.md --json     # JSON output
"""

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

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


def _is_delimiter_row(line: str) -> bool:
    """Check if a line is a table delimiter row (|---|---|)."""
    return bool(re.match(r"^\s*\|[\s\-:|]+\|\s*$", line))


def _split_row(line: str) -> list[str]:
    """Split a table row into cells, stripping the outer pipes."""
    stripped = line.strip()
    if stripped.startswith("|"):
        stripped = stripped[1:]
    if stripped.endswith("|"):
        stripped = stripped[:-1]
    return [cell.strip() for cell in stripped.split("|")]


def _compact_row(cells: list[str]) -> str:
    """Format cells as compact: |cell1|cell2|cell3|."""
    return "|" + "|".join(cells) + "|"


def _compact_delimiter(cells: list[str]) -> str:
    """Format delimiter cells preserving alignment markers."""
    compact_cells: list[str] = []
    for cell in cells:
        cell = cell.strip()
        left = cell.startswith(":")
        right = cell.endswith(":")
        if left and right:
            compact_cells.append(":---:")
        elif left:
            compact_cells.append(":---")
        elif right:
            compact_cells.append("---:")
        else:
            compact_cells.append("---")
    return "|" + "|".join(compact_cells) + "|"


def _find_tables(lines: list[str]) -> list[tuple[int, int]]:
    """Find table blocks as (start_idx, end_idx) tuples (0-indexed, end exclusive).

    Skips tables inside code blocks.
    """
    tables: list[tuple[int, int]] = []
    in_code = False
    i = 0

    while i < len(lines):
        stripped = lines[i].strip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_code = not in_code
            i += 1
            continue
        if in_code:
            i += 1
            continue

        # A table row starts and ends with |
        if (
            stripped.startswith("|")
            and stripped.endswith("|")
            and stripped.count("|") >= 2
        ):
            start = i
            while i < len(lines):
                s = lines[i].strip()
                if s.startswith("|") and s.endswith("|") and s.count("|") >= 2:
                    i += 1
                else:
                    break
            end = i

            # Validate: need at least header + delimiter + 1 data row, and a delimiter row
            if end - start >= 2:
                has_delimiter = any(
                    _is_delimiter_row(lines[j]) for j in range(start, end)
                )
                if has_delimiter:
                    tables.append((start, end))
        else:
            i += 1

    return tables


def check_and_fix_tables(filepath: Path, *, fix: bool = False) -> list[Finding]:
    findings: list[Finding] = []
    fname = str(filepath)
    text = filepath.read_text(encoding="utf-8")
    lines = text.splitlines()

    tables = _find_tables(lines)
    if not tables:
        return findings

    new_lines = list(lines)
    modified = False

    for start, end in tables:
        # Parse expected column count from delimiter row
        delimiter_idx = None
        expected_cols = None
        for j in range(start, end):
            if _is_delimiter_row(lines[j]):
                delimiter_idx = j
                expected_cols = len(_split_row(lines[j]))
                break

        if delimiter_idx is None or expected_cols is None:
            continue

        for j in range(start, end):
            row = lines[j]
            cells = _split_row(row)
            line_num = j + 1

            # --- Column count consistency ---
            if len(cells) != expected_cols:
                findings.append(
                    Finding(
                        fname,
                        line_num,
                        "warning",
                        "table-column-count",
                        f"Row has {len(cells)} columns, expected {expected_cols}. (MD056)",
                    )
                )

            # --- Check compactness ---
            is_delimiter = _is_delimiter_row(row)
            if is_delimiter:
                compact = _compact_delimiter(cells)
            else:
                compact = _compact_row(cells)

            if row.strip() != compact:
                findings.append(
                    Finding(
                        fname,
                        line_num,
                        "warning",
                        "table-not-compact",
                        f"Table row is not compact. Expected: {compact}",
                    )
                )
                if fix:
                    # Preserve leading whitespace (indentation)
                    indent = len(row) - len(row.lstrip())
                    new_lines[j] = " " * indent + compact
                    modified = True

    if fix and modified:
        filepath.write_text("\n".join(new_lines) + "\n", encoding="utf-8")

    return findings


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Validate and reformat markdown tables to compact style"
    )
    parser.add_argument("files", nargs="+", type=Path, help="Markdown files to check")
    parser.add_argument(
        "--fix", action="store_true", help="Reformat non-compact tables in-place"
    )
    parser.add_argument(
        "--json", dest="as_json", action="store_true", help="Output findings as JSON"
    )
    args = parser.parse_args()

    all_findings: list[Finding] = []
    for f in args.files:
        if not f.exists():
            print(f"Error: {f} not found", file=sys.stderr)
            continue
        all_findings.extend(check_and_fix_tables(f, fix=args.fix))

    exit_code = print_findings(all_findings, as_json=args.as_json)

    if not args.as_json:
        if args.fix and all_findings:
            print(f"\033[32m✓\033[0m Fixed {len(all_findings)} table issues.")
        elif not all_findings:
            print(f"\033[32m✓\033[0m All files passed table validation.")

    sys.exit(exit_code)


if __name__ == "__main__":
    main()
