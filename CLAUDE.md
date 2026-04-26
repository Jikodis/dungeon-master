# Dungeon Master Agentic OS

This repo is the campaign brain for a long-running D&D 5e campaign (currently 18 sessions in, party at level 3, target ~150–200 sessions). It holds the campaign as Markdown so Claude Code skills can read and update it.

## Where things live

- `context/` — campaign canon (world, NPCs, locations, quests, PCs, tables, maps). The current state of the world.
- `sessions/` — chronological log of what happened, one file per session. Source of truth for past events.
- `.agents/skills/prep/` — rich skills for deskwork: prep before a session, bookkeeping after. (Also discoverable as `.claude/skills/prep/` via symlink.)
- `.agents/skills/live/` — terse skills for at-the-table use during play.
- `.agents/skills/meta/` — skills about the OS itself (e.g., the tour onboarding skill).
- `context/rules/srd/` — vendored 5e SRD (CC-BY-4.0, oldmanumby/dnd.srd). Read by rules/spell/statblock live skills.
- `docs/superpowers/` — design docs and implementation plans (meta, not gameplay).
- `tools/whisperx/` — local WhisperX transcription pipeline (audio → speaker-attributed Markdown). See `tools/whisperx/README.md`.
- `recordings/` — session audio (gitignored). Drop files here for transcription.
- `transcripts/` — committed text transcripts produced by `tools/whisperx/transcribe.py`. Input to the `prep/transcript-import` skill.

## Two skill families

**Prep skills** (`.agents/skills/prep/`) are deliberate. They read full context, produce rich output (multiple paragraphs, structured Markdown), and **propose changes to canon for user approval before writing files**.

**Live skills** (`.agents/skills/live/`) run at the table. They are intentionally constrained:
- Output ≤ 5–10 lines, formatted to a strict template.
- They **must not read `sessions/`** (too slow, too much context).
- They **must not write files**.
- If the user wants to persist what a live skill produced, they invoke the corresponding prep skill.

When a request could match either family, prefer the live skill if the user mentions being mid-session, time pressure, or short output.

**Live-skill freshness assumption.** Live skills read `context/` snapshots only — they trust that canon is current as of the last completed prep/sessions run. If the table just learned something that hasn't been propagated to entity files yet, a live skill may give stale info. After running a live skill mid-session, treat its output as advisory until the post-session `prep/sessions` recap propagates the deltas.

## Two non-negotiable rules

### 1. Propose-first writes

Prep skills NEVER silently mutate canon. Before writing any file in `context/` or `sessions/`, the skill must:

1. Summarize all proposed changes in chat (one bullet per file, with what changes).
2. Wait for the user to approve, edit, or reject.
3. Only on approval, write the files.

### 2. Maintain `_INDEX.md`

Every folder under `context/` (and `sessions/`) has a `_INDEX.md` table with one row per file. Whenever a prep skill creates or edits an entity file, it MUST also update the corresponding `_INDEX.md`:

- Update the "One-liner" if the entity's role has shifted.
- Update the "Last touched" column to the current session number (e.g., `s19`).
- Add a row for new files; never silently leave a stale or missing row.

Indexes are the load-bearing read surface — skills query them before drilling into individual files. A stale index breaks search across the whole campaign.

## File conventions

- All entity files have YAML frontmatter at the top (schema is per-type; see the spec).
- Edited entity files get a footer line: `<!-- last updated: sNN -->` where `NN` is the session number (or `prep` for between-session edits).
- Slugs are kebab-case (`lord-verros.md`, `the-rusted-anchor.md`).
- Session files are named `NNN-headline.md` with zero-padded 3-digit session number.

## Maps

`context/maps/` holds committed image files. Skills should reference them by filename but not attempt to parse them unless the user explicitly asks Claude to look at one.
