#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "markdown-it-py>=4.0.0",
# ]
# ///
"""
check_admonitions.py — Enforce admonition-only blockquotes in markdown files.

Checks (rules 4, 9):
- Every blockquote must use GitHub admonition syntax: > [!TYPE]
- TYPE must be one of: NOTE, TIP, IMPORTANT, WARNING, CAUTION
- Consecutive blockquotes must be separated by a blank line

Run with: uv run check_admonitions.py README.md [--json]
"""

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

from markdown_it import MarkdownIt

VALID_TYPES = frozenset({"NOTE", "TIP", "IMPORTANT", "WARNING", "CAUTION"})

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


def check_admonitions(filepath: Path) -> list[Finding]:
    findings: list[Finding] = []
    fname = str(filepath)
    text = filepath.read_text(encoding="utf-8")

    md = MarkdownIt("commonmark")
    tokens = md.parse(text)

    prev_bq_end_line: int | None = None
    admonition_re = re.compile(r"^\[!(\w+)\]")

    i = 0
    while i < len(tokens):
        token = tokens[i]

        if token.type == "blockquote_open":
            bq_start = (token.map[0] + 1) if token.map else 0

            # --- Consecutive blockquote separation ---
            if prev_bq_end_line is not None and token.map is not None:
                # map[0] is 0-indexed start line of this blockquote
                gap = token.map[0] - prev_bq_end_line
                if gap < 1:
                    findings.append(
                        Finding(fname, bq_start, "error", "admonition-separation",
                                "Consecutive blockquotes must be separated by a blank line.")
                    )

            # --- Walk forward to find first inline content at depth 1 ---
            j = i + 1
            depth = 1
            first_inline = None
            bq_end_line = token.map[1] if token.map else 0

            while j < len(tokens) and depth > 0:
                t = tokens[j]
                if t.type == "blockquote_open":
                    depth += 1
                elif t.type == "blockquote_close":
                    depth -= 1
                    if depth == 0:
                        bq_end_line = t.map[1] if t.map else bq_end_line
                        break
                elif t.type == "inline" and first_inline is None and depth == 1:
                    first_inline = t
                j += 1

            prev_bq_end_line = bq_end_line

            # --- Check for admonition marker ---
            if first_inline is not None:
                content = first_inline.content.strip()
                admon_match = admonition_re.match(content)
                if not admon_match:
                    preview = content[:60].replace("\n", " ")
                    findings.append(
                        Finding(fname, bq_start, "error", "blockquote-no-admonition",
                                f"Plain blockquotes are not allowed. All blockquotes must use "
                                f"admonition syntax: > [!TYPE]. "
                                f"Content starts with: \"{preview}\"")
                    )
                else:
                    admon_type = admon_match.group(1).upper()
                    if admon_type not in VALID_TYPES:
                        valid = ", ".join(sorted(VALID_TYPES))
                        findings.append(
                            Finding(fname, bq_start, "error", "admonition-invalid-type",
                                    f"Invalid admonition type '[!{admon_type}]'. "
                                    f"Allowed types: {valid}.")
                        )
            else:
                # Empty blockquote — no inline content found
                findings.append(
                    Finding(fname, bq_start, "warning", "blockquote-empty",
                            "Empty blockquote found. Remove or add admonition content.")
                )

            i = j + 1
        else:
            # Reset consecutive tracking when non-blockquote content appears
            if token.type not in ("paragraph_open", "paragraph_close",
                                  "inline", "softbreak", "hardbreak"):
                if token.map is not None and prev_bq_end_line is not None:
                    # Only reset if there's real content between blockquotes
                    if token.map[0] > prev_bq_end_line:
                        prev_bq_end_line = None
            i += 1

    return findings


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Enforce admonition-only blockquotes in markdown files"
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
        all_findings.extend(check_admonitions(f))

    exit_code = print_findings(all_findings, as_json=args.as_json)
    if not all_findings and not args.as_json:
        print(f"\033[32m✓\033[0m All files passed admonition validation.")
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
