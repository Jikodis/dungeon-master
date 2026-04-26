# Dungeon Master Agentic OS

A campaign brain for a long-running D&D 5e game, built as Markdown content + Claude Code skills. The world lives in plain text, the skills do the repeatable DM work — both deskwork between sessions and quick rulings at the table — and you stay the DM.

Currently 18 sessions in on a single campaign, party at level 3, target ~150–200 sessions over the campaign's life.

## What's in here

- **`CLAUDE.md`** — project rules. Always loaded by Claude Code. Read this first if you want to understand how the skills are required to behave.
- **`context/`** — campaign canon. NPCs, locations, quests, factions, PCs, world bible, custom random tables, vendored 5e SRD, maps. The current state of the world.
- **`sessions/`** — chronological log, one Markdown file per session. Raw notes + recap + state deltas.
- **`.agents/skills/`** — the agent skills. Two families: `prep/` (deskwork, rich, propose-then-write) and `live/` (at-the-table, terse, never write files), plus `meta/` (skills about the OS itself, e.g. the onboarding tour). `.claude/skills` symlinks here so Claude Code auto-discovers them.
- **`docs/superpowers/`** — design spec and implementation plan (meta — not gameplay).
- **`TODO.md`** — upcoming features and known gaps.

## How it works

Two skill families, one campaign:

- **Prep skills** are slow and thoughtful. They read full context, produce structured output, and **propose every change to canon for your approval** before writing files. Use them for designing encounters, fleshing out NPCs, prepping or recapping a session, advancing PC arcs, growing the world bible.
- **Live skills** run at the table under time pressure. Output is ≤ 5–10 lines, formatted to a strict template. They **never write files** and **never read `sessions/`** (too slow). Use them for improvising an NPC, looking up a 5e rule or spell, pulling a monster stat block, scaling a fight, deciding who knows what.

Two non-negotiable rules: **propose-first writes** (no silent canon mutation) and **maintain `_INDEX.md`** (every folder has a one-row-per-file index that skills query before drilling into files).

## Getting started

Ask Claude: **"give me a tour of this DM OS"** — that fires the `tour` skill at `.agents/skills/meta/tour/SKILL.md`, which walks you through the layout, the rules, the session lifecycle, and a concrete first-30-minutes plan.

For the full design rationale, see [docs/superpowers/specs/](docs/superpowers/specs/).

## 5e SRD

`context/rules/srd/` vendors the [oldmanumby/dnd.srd](https://github.com/OldManUmby/dnd.srd) Markdown conversion of the official D&D 5.1 SRD (2014 rules + Nov 2018 errata), distributed under [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/legalcode). The `live/5e-rules`, `live/spell-lookup`, and `live/statblock` skills read from it directly so rulings cite real SRD text rather than relying on model recall.

## License

Project content (campaign data, skills, docs): see [LICENSE](LICENSE).
Vendored SRD content under `context/rules/srd/`: CC-BY-4.0, copyright Wizards of the Coast.
