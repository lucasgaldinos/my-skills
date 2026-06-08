#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "markdown-it-py>=4.0.0",
#   "mdit-py-plugins>=0.4.0",
# ]
# ///
"""
check_footnotes.py — Validate footnote placement and size in markdown files.

Checks (rule 7):
- Footnote definitions are placed inline (after the referencing paragraph)
- Footnotes don't exceed ~2 lines / ~200 characters
- Orphaned references (no matching definition) and orphaned definitions
- Prefers descriptive identifiers over numeric ones for many-footnote docs

Run with: uv run check_footnotes.py README.md [--json]
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

SIZE_THRESHOLD_CHARS = 200
SIZE_THRESHOLD_LINES = 2
MANY_FOOTNOTES_THRESHOLD = 3

FOOTNOTE_DEF_RE = re.compile(r"^\[\^([^\]]+)\]:\s*(.*)")
FOOTNOTE_REF_RE = re.compile(r"\[\^([^\]]+)\](?!:)")


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


def check_footnotes(filepath: Path) -> list[Finding]:
    findings: list[Finding] = []
    fname = str(filepath)
    text = filepath.read_text(encoding="utf-8")
    lines = text.splitlines()

    # --- Collect definitions with content ---
    defs: dict[str, int] = {}  # id -> 1-indexed line number
    def_contents: dict[str, str] = {}  # id -> full content

    i = 0
    while i < len(lines):
        match = FOOTNOTE_DEF_RE.match(lines[i])
        if match:
            fid = match.group(1)
            content_parts = [match.group(2)]

            # Gather continuation lines (4-space indented or blank within block)
            j = i + 1
            while j < len(lines):
                continuation = lines[j]
                if continuation.startswith("    ") or (
                    continuation.strip() == ""
                    and j + 1 < len(lines)
                    and lines[j + 1].startswith("    ")
                ):
                    content_parts.append(continuation)
                    j += 1
                else:
                    break

            defs[fid] = i + 1
            def_contents[fid] = "\n".join(content_parts).strip()
            i = j
        else:
            i += 1

    # --- Collect references (skip code blocks and definition lines) ---
    refs: dict[str, list[int]] = {}  # id -> list of 1-indexed line numbers
    in_code = False

    for idx, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_code = not in_code
            continue
        if in_code:
            continue
        if FOOTNOTE_DEF_RE.match(line):
            continue

        for ref_match in FOOTNOTE_REF_RE.finditer(line):
            fid = ref_match.group(1)
            refs.setdefault(fid, []).append(idx + 1)

    # --- Check: definitions should come after their first reference ---
    for fid, ref_lines in refs.items():
        if fid in defs:
            first_ref = min(ref_lines)
            def_line = defs[fid]
            if def_line < first_ref:
                findings.append(
                    Finding(fname, def_line, "warning", "footnote-placement",
                            f"Footnote [^{fid}] definition (line {def_line}) appears before "
                            f"its first reference (line {first_ref}). Place definitions "
                            f"inline after the referencing paragraph.")
                )
        else:
            findings.append(
                Finding(fname, min(ref_lines), "warning", "footnote-orphan-ref",
                        f"Footnote reference [^{fid}] has no matching definition.")
            )

    # --- Check: orphaned definitions ---
    for fid, def_line in defs.items():
        if fid not in refs:
            findings.append(
                Finding(fname, def_line, "warning", "footnote-orphan-def",
                        f"Footnote definition [^{fid}] is never referenced.")
            )

    # --- Check: definition size ---
    for fid, content in def_contents.items():
        non_blank_lines = [ln for ln in content.splitlines() if ln.strip()]
        char_count = len(content)
        line_count = len(non_blank_lines)

        if char_count > SIZE_THRESHOLD_CHARS or line_count > SIZE_THRESHOLD_LINES:
            def_line = defs[fid]
            findings.append(
                Finding(fname, def_line, "warning", "footnote-too-long",
                        f"Footnote [^{fid}] is {char_count} chars / {line_count} lines. "
                        f"Consider converting to an admonition or subsection "
                        f"(threshold: ~{SIZE_THRESHOLD_CHARS} chars / "
                        f"~{SIZE_THRESHOLD_LINES} lines).")
            )

    # --- Check: identifier style ---
    numeric_ids = [fid for fid in defs if fid.isdigit()]
    total = len(defs)
    if total > MANY_FOOTNOTES_THRESHOLD and len(numeric_ids) > total // 2:
        findings.append(
            Finding(fname, 1, "info", "footnote-numeric-ids",
                    f"Most footnote identifiers are numeric ({len(numeric_ids)}/{total}). "
                    f"Prefer descriptive words (e.g., [^commonmark]) for documents "
                    f"with many footnotes.")
        )

    findings.sort(key=lambda f: f.line)
    return findings


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Validate footnote placement and size in markdown files"
    )
    parser.add_argument("files", nargs="+", type=Path, help="Markdown files to check")
    parser.add_argument("--json", dest="as_json", action="store_true",
                        help="Output findings as JSON")
    args = parser.parse_args()

    all_findings: list[Finding] = []
    for f in args.files:
        if not f.exists():
            print(f"Error: {f} not found", file=sys.stderr)
            continue
        all_findings.extend(check_footnotes(f))

    exit_code = print_findings(all_findings, as_json=args.as_json)
    if not all_findings and not args.as_json:
        print(f"\033[32m✓\033[0m All files passed footnote validation.")
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
