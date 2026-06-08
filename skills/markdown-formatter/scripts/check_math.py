#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "markdown-it-py>=4.0.0",
#   "mdit-py-plugins>=0.4.0",
# ]
# ///
"""
check_math.py — Validate KaTeX math in markdown files.

Checks (rule 11 + rule 13):
- Display math ($$) blocks contain a LaTeX environment (\\begin{env}...\\end{env})
- No forbidden commands: \\def, \\gdef, \\newcommand, \\href, \\url, etc.
- No \\[...\\] or \\(...\\) delimiters
- Bare words in math not wrapped in \\text{} (heuristic warning)
- Duplicate symbols in notation tables (rule 13)

Run with: uv run check_math.py README.md [--json]
"""

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

from markdown_it import MarkdownIt
from mdit_py_plugins.dollarmath import dollarmath_plugin

FORBIDDEN_COMMANDS = [
    r"\\def\b",
    r"\\gdef\b",
    r"\\newcommand\b",
    r"\\renewcommand\b",
    r"\\href\b",
    r"\\url\b",
    r"\\includegraphics\b",
    r"\\htmlClass\b",
    r"\\htmlId\b",
    r"\\htmlStyle\b",
    r"\\htmlData\b",
]

# Words that are valid bare in math mode (common LaTeX function names)
MATH_FUNCTIONS = frozenset({
    "sin", "cos", "tan", "log", "ln", "exp", "lim", "max", "min",
    "sup", "inf", "det", "dim", "mod", "gcd", "lcm", "arg",
    "hom", "ker", "deg", "sec", "csc", "cot",
    "sinh", "cosh", "tanh", "arcsin", "arccos", "arctan",
})

# LaTeX macro names that appear bare but are not "text" — skip these
MACRO_NAMES = frozenset({
    "begin", "end", "frac", "sqrt", "left", "right", "over",
    "cdot", "cdots", "ldots", "dots", "quad", "qquad", "hspace", "vspace",
    "text", "mathrm", "mathbf", "mathit", "mathcal", "mathbb", "mathfrak",
    "operatorname", "displaystyle", "textstyle", "scriptstyle",
    "textcolor", "color", "boxed", "cancel", "bcancel", "xcancel",
    "tag", "label", "notag", "nonumber", "textbf", "textit", "textrm",
    "overbrace", "underbrace", "overline", "underline", "widehat", "widetilde",
    "stackrel", "overset", "underset", "xleftarrow", "xrightarrow",
    "phantom", "hphantom", "vphantom", "smash",
})

# Regex to detect bare English words (4+ letters) in math
BARE_WORD_RE = re.compile(r"(?<![\\a-zA-Z])([a-zA-Z]{4,})(?![a-zA-Z{}])")

# Regex to strip \text{...}-style wrappers before bare-word detection
TEXT_WRAPPER_RE = re.compile(
    r"\\(?:text|mathrm|mathbf|mathit|mathsf|mathtt|mathcal|mathbb|mathfrak|"
    r"operatorname|textrm|textbf|textit|textsf|texttt)\{[^}]*\}"
)

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


def _check_forbidden(content: str, fname: str, line: int, context: str) -> list[Finding]:
    findings: list[Finding] = []
    for pattern in FORBIDDEN_COMMANDS:
        match = re.search(pattern, content)
        if match:
            cmd = match.group(0).lstrip("\\")
            findings.append(
                Finding(fname, line, "error", "math-forbidden-command",
                        f"Forbidden command '\\{cmd}' in {context} — "
                        f"breaks on GitHub and across renderers.")
            )
    return findings


def _check_bare_words(content: str, fname: str, line: int) -> list[Finding]:
    cleaned = TEXT_WRAPPER_RE.sub("", content)
    bare_words = BARE_WORD_RE.findall(cleaned)
    suspicious = [
        w for w in bare_words
        if w.lower() not in MATH_FUNCTIONS and w not in MACRO_NAMES
    ]
    if suspicious:
        sample = ", ".join(suspicious[:5])
        return [
            Finding(fname, line, "warning", "math-bare-words",
                    f"Possible bare words in math (wrap in \\text{{}}): {sample}")
        ]
    return []


def check_math_tokens(filepath: Path) -> list[Finding]:
    findings: list[Finding] = []
    fname = str(filepath)
    text = filepath.read_text(encoding="utf-8")

    md = MarkdownIt("commonmark").use(dollarmath_plugin, double_inline=False)
    tokens = md.parse(text)

    for token in tokens:
        line = (token.map[0] + 1) if token.map else 0
        content = token.content.strip()

        # --- Display math: must have \begin{env}...\end{env} ---
        if token.type in ("math_block", "math_block_label"):
            env_match = re.search(r"\\begin\{(\w+\*?)\}", content)
            if not env_match:
                preview = content[:60].replace("\n", " ")
                findings.append(
                    Finding(fname, line, "error", "math-no-environment",
                            f"Display math ($$) must contain a LaTeX environment "
                            f"(\\begin{{env}}...\\end{{env}}). Got: {preview}...")
                )
            else:
                env_name = env_match.group(1)
                end_pattern = rf"\\end\{{{re.escape(env_name)}\}}"
                if not re.search(end_pattern, content):
                    findings.append(
                        Finding(fname, line, "error", "math-unclosed-env",
                                f"Environment \\begin{{{env_name}}} has no matching "
                                f"\\end{{{env_name}}}.")
                    )

            findings.extend(_check_forbidden(content, fname, line, "display math"))
            findings.extend(_check_bare_words(content, fname, line))

        # --- Inline math: check forbidden commands + bare words ---
        elif token.type == "math_inline":
            findings.extend(_check_forbidden(content, fname, line, "inline math"))
            findings.extend(_check_bare_words(content, fname, line))

    return findings


def check_wrong_delimiters(filepath: Path) -> list[Finding]:
    """Detect \\[...\\] or \\(...\\) delimiters (line-based, skips code blocks)."""
    findings: list[Finding] = []
    fname = str(filepath)
    lines = filepath.read_text(encoding="utf-8").splitlines()

    in_code = False
    for i, raw_line in enumerate(lines):
        stripped = raw_line.strip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_code = not in_code
            continue
        if in_code:
            continue
        if re.search(r"(?<!\\)\\\[", raw_line) or re.search(r"(?<!\\)\\\(", raw_line):
            findings.append(
                Finding(fname, i + 1, "error", "math-wrong-delimiter",
                        "Do not use \\[...\\] or \\(...\\) delimiters — "
                        "unsupported on GitHub. Use $...$ or $$...$$."))
    return findings


def check_notation_table_duplicates(filepath: Path) -> list[Finding]:
    """Check for duplicate entries in math notation tables (rule 13)."""
    findings: list[Finding] = []
    fname = str(filepath)
    lines = filepath.read_text(encoding="utf-8").splitlines()

    in_code = False
    in_table = False
    is_notation_table = False
    seen_delimiter = False
    first_col_values: dict[str, int] = {}

    for i, raw_line in enumerate(lines):
        stripped = raw_line.strip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_code = not in_code
            continue
        if in_code:
            continue

        if stripped.startswith("|") and stripped.count("|") >= 2:
            if not in_table:
                # Starting a new table — check if header suggests notation table
                in_table = True
                seen_delimiter = False
                first_col_values.clear()
                header_lower = stripped.lower()
                is_notation_table = (
                    ("symbol" in header_lower or "notation" in header_lower)
                    and ("meaning" in header_lower or "description" in header_lower)
                )
            elif not seen_delimiter:
                # Delimiter row
                if re.match(r"^\|[\s\-:|]+\|$", stripped):
                    seen_delimiter = True
            elif is_notation_table:
                parts = stripped.split("|")
                if len(parts) >= 3:
                    first_col = parts[1].strip()
                    if first_col:
                        if first_col in first_col_values:
                            findings.append(
                                Finding(fname, i + 1, "warning", "math-duplicate-symbol",
                                        f"Duplicate symbol '{first_col}' in notation table "
                                        f"(first defined at line {first_col_values[first_col]}).")
                            )
                        else:
                            first_col_values[first_col] = i + 1
        else:
            in_table = False

    return findings


def check_math(filepath: Path) -> list[Finding]:
    findings: list[Finding] = []
    findings.extend(check_math_tokens(filepath))
    findings.extend(check_wrong_delimiters(filepath))
    findings.extend(check_notation_table_duplicates(filepath))
    findings.sort(key=lambda f: f.line)
    return findings


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate KaTeX math in markdown files")
    parser.add_argument("files", nargs="+", type=Path, help="Markdown files to check")
    parser.add_argument("--json", dest="as_json", action="store_true",
                        help="Output findings as JSON")
    args = parser.parse_args()

    all_findings: list[Finding] = []
    for f in args.files:
        if not f.exists():
            print(f"Error: {f} not found", file=sys.stderr)
            continue
        all_findings.extend(check_math(f))

    exit_code = print_findings(all_findings, as_json=args.as_json)
    if not all_findings and not args.as_json:
        print(f"\033[32m✓\033[0m All files passed math validation.")
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
