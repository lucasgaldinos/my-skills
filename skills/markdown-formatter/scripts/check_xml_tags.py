#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""
check_xml_tags.py — Validate XML tags in agent customization files.

Checks (rule 12):
- No HTML tag names used as XML semantic tags
- Blank line after opening tags and before closing tags
- Matching open/close tags (no unclosed or mismatched tags)
- Nesting depth <= 3
- Only checks agent files: .instructions.md, .prompt.md, SKILL.md,
  AGENTS.md, .agent.md

Run with: uv run check_xml_tags.py SKILL.md [--json]
"""

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

# HTML tag names that must not be used as semantic XML tags in agent files
HTML_TAGS = frozenset(
    {
        "div",
        "p",
        "span",
        "b",
        "i",
        "em",
        "strong",
        "code",
        "pre",
        "a",
        "img",
        "table",
        "tr",
        "td",
        "th",
        "thead",
        "tbody",
        "tfoot",
        "script",
        "style",
        "ul",
        "ol",
        "li",
        "h1",
        "h2",
        "h3",
        "h4",
        "h5",
        "h6",
        "br",
        "hr",
        "section",
        "article",
        "header",
        "footer",
        "nav",
        "main",
        "aside",
        "figure",
        "figcaption",
        "blockquote",
        "cite",
        "abbr",
        "address",
        "details",
        "summary",
        "mark",
        "small",
        "sub",
        "sup",
        "dl",
        "dt",
        "dd",
        "form",
        "button",
        "select",
        "option",
        "textarea",
        "label",
        "fieldset",
        "legend",
        "iframe",
        "video",
        "audio",
        "source",
        "canvas",
        "svg",
        "path",
    }
)

# Canonical semantic tags for agent skills
CANONICAL_TAGS = frozenset(
    {
        "instructions",
        "context",
        "rules",
        "constraints",
        "examples",
        "example",
        "input",
        "output",
        "warning",
        "output_format",
        "gotchas",
        "validation",
        "checkpoint",
        "recovery",
        "command",
        "template",
        "criteria",
        "prerequisites",
        "error_handling",
        "steps",
        "step",
        "documents",
        "document",
        "document_content",
        "source",
        "category",
    }
)

# Agent file extensions and names
AGENT_EXTENSIONS = {".instructions.md", ".prompt.md", ".agent.md"}
AGENT_FILENAMES = {"SKILL.md", "AGENTS.md"}

# Match a standalone XML tag on its own line (opening or closing)
TAG_RE = re.compile(r"^<(/?)(\w[\w-]*)(?:\s[^>]*)?>$")

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


def _is_agent_file(filepath: Path) -> bool:
    name = filepath.name
    if name in AGENT_FILENAMES:
        return True
    return any(name.endswith(ext) for ext in AGENT_EXTENSIONS)


def check_xml_tags(filepath: Path) -> list[Finding]:
    findings: list[Finding] = []
    fname = str(filepath)

    if not _is_agent_file(filepath):
        return findings

    text = filepath.read_text(encoding="utf-8")
    lines = text.splitlines()

    in_code = False
    tag_stack: list[tuple[str, int]] = []  # (tag_name, 1-indexed line)

    for i, raw_line in enumerate(lines):
        stripped = raw_line.strip()

        # Track code blocks
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_code = not in_code
            continue
        if in_code:
            continue

        # Skip HTML comments
        if stripped.startswith("<!--"):
            continue

        match = TAG_RE.match(stripped)
        if not match:
            continue

        is_closing = match.group(1) == "/"
        tag_name = match.group(2).lower()
        line_num = i + 1

        # --- HTML tag collision ---
        if tag_name in HTML_TAGS:
            findings.append(
                Finding(
                    fname,
                    line_num,
                    "error",
                    "xml-html-tag",
                    f"Tag <{tag_name}> is an HTML tag name — markdown renderers will "
                    f"strip it. Use a semantic domain-specific name instead.",
                )
            )
            continue

        if is_closing:
            # --- Blank line before closing tag ---
            if i > 0 and lines[i - 1].strip() != "":
                findings.append(
                    Finding(
                        fname,
                        line_num,
                        "warning",
                        "xml-no-blank-before-close",
                        f"Insert a blank line before </{tag_name}> for readability.",
                    )
                )

            # --- Matching open/close ---
            if tag_stack and tag_stack[-1][0] == tag_name:
                tag_stack.pop()
            elif tag_stack:
                open_tag, open_line = tag_stack[-1]
                findings.append(
                    Finding(
                        fname,
                        line_num,
                        "error",
                        "xml-mismatched-close",
                        f"Closing </{tag_name}> doesn't match opening <{open_tag}> "
                        f"at line {open_line}.",
                    )
                )
            else:
                findings.append(
                    Finding(
                        fname,
                        line_num,
                        "error",
                        "xml-unexpected-close",
                        f"Closing </{tag_name}> has no matching opening tag.",
                    )
                )
        else:
            # Opening tag
            # --- Blank line after opening tag ---
            if i + 1 < len(lines) and lines[i + 1].strip() != "":
                findings.append(
                    Finding(
                        fname,
                        line_num,
                        "warning",
                        "xml-no-blank-after-open",
                        f"Insert a blank line after <{tag_name}> for readability.",
                    )
                )

            tag_stack.append((tag_name, line_num))

            # --- Nesting depth ---
            if len(tag_stack) > 3:
                findings.append(
                    Finding(
                        fname,
                        line_num,
                        "warning",
                        "xml-deep-nesting",
                        f"XML tag nesting is {len(tag_stack)} levels deep. "
                        f"Keep to 2–3 levels maximum.",
                    )
                )

    # --- Unclosed tags ---
    for tag_name, open_line in tag_stack:
        findings.append(
            Finding(
                fname,
                open_line,
                "error",
                "xml-unclosed-tag",
                f"Tag <{tag_name}> at line {open_line} is never closed.",
            )
        )

    return findings


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Validate XML tags in agent customization files"
    )
    parser.add_argument("files", nargs="+", type=Path, help="Files to check")
    parser.add_argument(
        "--json", dest="as_json", action="store_true", help="Output findings as JSON"
    )
    args = parser.parse_args()

    all_findings: list[Finding] = []
    for f in args.files:
        if not f.exists():
            print(f"Error: {f} not found", file=sys.stderr)
            continue
        all_findings.extend(check_xml_tags(f))

    exit_code = print_findings(all_findings, as_json=args.as_json)
    if not all_findings and not args.as_json:
        print(f"\033[32m✓\033[0m All files passed XML tag validation.")
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
