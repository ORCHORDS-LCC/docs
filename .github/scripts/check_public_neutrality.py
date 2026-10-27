#!/usr/bin/env python3
"""Reject project/private identifiers in public Markdown text and paths."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

# Boundary-aware so legitimate public technical terms such as OWASP are not
# mistaken for a standalone private product acronym.
PRIVATE_NAME_RE = re.compile(
    r"(?i)(?:^|[^A-Za-z0-9])"
    r"(?:W\.?A\.?S\.?P\.?|thewam|searabbit|retmo|cutshit|roomtoneoptimiser|mrorchords|mr\.orchords)"
    r"(?:$|[^A-Za-z0-9])"
)
PRIVATE_REPO_RE = re.compile(
    r"(?i)(?:"
    r"https?://(?:www\.)?github\.com/(?:ORCHORDS|sapperskills)/(?!docs(?:[/?#]|$))|"
    r"https?://raw\.githubusercontent\.com/(?:ORCHORDS|sapperskills)/|"
    r"https?://api\.github\.com/repos/(?:ORCHORDS|sapperskills)/|"
    r"git@github\.com:(?:ORCHORDS|sapperskills)/(?!docs(?:\.git)?(?:\s|$))|"
    r"\b(?:ORCHORDS|sapperskills)/(?!docs\b)[A-Za-z0-9_.-]+\b"
    r")"
)
SOURCE_PATH_RE = re.compile(r"(?i)(?:^|[\\/])(?:knowledge_base|\.fleet)[\\/]")
# A home directory must start the path it appears in, and the POSIX home
# directory names are literally "/home" and "/Users". A lowercase
# "/users/..." is a URL path segment, not a home directory.
ABSOLUTE_PRIVATE_PATH_RE = re.compile(
    r"(?:"
    r"(?<![A-Za-z0-9_./~-])/home/[^/\s]+/|"
    r"(?<![A-Za-z0-9_./~-])/Users/[^/\s]+/|"
    r"(?<=://)/home/[^/\s]+/|"
    r"(?<=://)/Users/[^/\s]+/|"
    r"(?<![A-Za-z0-9_./~-])/_work/[^/\s]+/[^/\s]+|"
    r"(?i:/mnt/data/[^\s)]+)|"
    r"(?i:[A-Z]:\\Users\\[^\\\s]+\\)"
    r")"
)


def main() -> int:
    errors: list[str] = []
    markdown = sorted(ROOT.rglob("*.md"))
    for path in markdown:
        rel = path.relative_to(ROOT).as_posix()
        text = path.read_text(encoding="utf-8")
        if PRIVATE_NAME_RE.search(rel):
            errors.append(f"{rel}: project-specific identifier in public path")
        if PRIVATE_NAME_RE.search(text):
            errors.append(f"{rel}: project-specific identifier in public text")
        if PRIVATE_REPO_RE.search(text):
            errors.append(f"{rel}: private/project repository reference")
        if SOURCE_PATH_RE.search(text):
            errors.append(f"{rel}: private source workspace path")
        if ABSOLUTE_PRIVATE_PATH_RE.search(text):
            errors.append(f"{rel}: absolute private/workspace path")

    if errors:
        print("Public neutrality checks failed:")
        for error in errors:
            print(f" - {error}")
        return 1
    print(f"Public neutrality checks passed for {len(markdown)} Markdown files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
