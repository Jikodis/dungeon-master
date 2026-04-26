#!/usr/bin/env python3
"""Build a WhisperX hotword string + initial_prompt from the campaign's context/ indexes.

Walks every entity file under context/ (npcs, pcs, locations, quests, world/factions)
and pulls the first H1 heading as the canonical name. Adds hand-curated extras from
extra_vocab.txt. Outputs a JSON object with `hotwords` (space-separated) and
`initial_prompt` (a sentence-style prompt suitable for Whisper's decoder context).

Usage:
    python tools/whisperx/build_hotwords.py            # prints JSON to stdout
    python tools/whisperx/build_hotwords.py --hotwords # prints just the hotword string
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
CONTEXT = REPO_ROOT / "context"

# Folders to walk for H1 extraction. The first H1 in each file is the entity's name.
ENTITY_GLOBS = [
    "npcs/*.md",
    "pcs/*.md",
    "locations/**/*.md",
    "quests/*.md",
    "world/factions/*.md",
]

H1_RE = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)
PARENS_RE = re.compile(r"\s*\(.*?\)\s*")
SEMICOLON_RE = re.compile(r"\s*;.*$")


def extract_h1(md_path: Path) -> str | None:
    """Return the first H1 heading of a Markdown file, cleaned of parentheticals."""
    try:
        text = md_path.read_text(encoding="utf-8")
    except OSError:
        return None
    m = H1_RE.search(text)
    if not m:
        return None
    name = m.group(1).strip()
    # Strip "(the sage; tagged "Mira-sage")" style decorations to leave the bare name.
    name = PARENS_RE.sub(" ", name).strip()
    name = SEMICOLON_RE.sub("", name).strip()
    return name or None


def collect_entity_names() -> list[str]:
    names: list[str] = []
    for pattern in ENTITY_GLOBS:
        for path in sorted(CONTEXT.glob(pattern)):
            if path.name == "_INDEX.md":
                continue
            name = extract_h1(path)
            if name:
                names.append(name)
    return names


def collect_extra_vocab(extra_path: Path) -> list[str]:
    if not extra_path.exists():
        return []
    out: list[str] = []
    for line in extra_path.read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        out.append(s)
    return out


_STRIP_CHARS = ",.;:!?\"'"


def to_hotwords(terms: list[str]) -> str:
    """WhisperX/faster-whisper hotwords is a space-separated string of single
    tokens. Split multi-word terms into constituent words and dedupe
    case-insensitively. The joined form is redundant — the tokenizer would
    re-split it anyway."""
    seen: set[str] = set()
    ordered: list[str] = []
    for term in terms:
        for word in term.split():
            t = word.strip(_STRIP_CHARS)
            if not t or t.lower() in seen:
                continue
            # Drop pure stopwords that add no proper-noun signal.
            if t.lower() in {"of", "the", "and", "a", "an", "in", "on"}:
                continue
            seen.add(t.lower())
            ordered.append(t)
    return " ".join(ordered)


def to_initial_prompt(blurb: str, names: list[str], pcs: list[str]) -> str:
    parts = [blurb.strip().rstrip(".") + "."] if blurb.strip() else []
    if pcs:
        parts.append("Player characters: " + ", ".join(pcs) + ".")
    if names:
        # Cap the prompt size — Whisper's prompt context is finite.
        sample = names[:30]
        parts.append("Recurring proper nouns include: " + ", ".join(sample) + ".")
    return " ".join(parts)


def collect_pc_names() -> list[str]:
    pcs = []
    for path in sorted((CONTEXT / "pcs").glob("*.md")):
        if path.name == "_INDEX.md":
            continue
        name = extract_h1(path)
        if name:
            pcs.append(name)
    return pcs


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--extra-vocab",
        type=Path,
        default=Path(__file__).parent / "extra_vocab.txt",
        help="Path to hand-curated vocabulary file",
    )
    parser.add_argument(
        "--blurb",
        default="A Dungeons and Dragons session.",
        help="Campaign blurb to seed initial_prompt",
    )
    parser.add_argument(
        "--hotwords",
        action="store_true",
        help="Print only the hotword string (for shell piping)",
    )
    args = parser.parse_args()

    entity_names = collect_entity_names()
    pc_names = collect_pc_names()
    extras = collect_extra_vocab(args.extra_vocab)

    all_terms = entity_names + extras
    hotwords = to_hotwords(all_terms)
    initial_prompt = to_initial_prompt(args.blurb, all_terms, pc_names)

    if args.hotwords:
        print(hotwords)
        return 0

    json.dump(
        {
            "hotwords": hotwords,
            "initial_prompt": initial_prompt,
            "entity_count": len(entity_names),
            "extra_count": len(extras),
        },
        sys.stdout,
        indent=2,
    )
    print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
