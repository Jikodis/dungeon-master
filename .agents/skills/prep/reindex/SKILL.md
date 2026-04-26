---
name: reindex
description: Use to rebuild a folder's _INDEX.md from the current files in that folder. Useful when an index has drifted out of sync with reality (rows missing, stale one-liners, deleted files still listed). Examples: "rebuild the npcs index", "reindex context/locations", "the sessions _INDEX.md is out of date". Proposes the rebuilt index for approval before writing. Does NOT touch entity files.
---

# Reindex (prep skill)

`_INDEX.md` files are the load-bearing read surface — every other skill queries the index before drilling into individual files. A stale index breaks search across the whole campaign. Most of the time, prep skills keep their indexes current as part of normal work. When they don't (manual edits, file moves, bulk imports, drift after long pauses), use this skill to rebuild from ground truth.

## When to use
- An `_INDEX.md` is missing rows for files that exist.
- An `_INDEX.md` lists files that no longer exist.
- One-liners or `Last touched` columns are stale and the user explicitly wants a refresh.
- After a manual reorganization or import.

## When NOT to use
- Routine entity edits — those should keep the index current via the entity skill (`prep/npcs`, `prep/locations`, etc.).
- A single missing row — just edit it inline; reindex is for bulk drift.
- Indexes outside `context/` and `sessions/` — out of scope.

## What this skill does (and doesn't)

**DOES:**
- Read every Markdown file in the target folder.
- Pull the entity name (from frontmatter or first heading) and a one-liner summary.
- Pull the last-touched session from the file's footer (`<!-- last updated: sNN -->`) when present, else infer from git or fall back to `prep`.
- Compose a fresh `_INDEX.md` matching the schema of the existing one (or the conventional schema for that folder type).
- **Propose the new index in chat for user approval before writing.**
- After approval, write `_INDEX.md` only.

**DOES NOT:**
- Touch entity files. Reindex never edits or deletes content files.
- Rebuild more than one folder per invocation. If multiple indexes are stale, ask for confirmation and process them one at a time so the user can review each.
- Recurse into subdirectories silently. If `context/locations/` is targeted, only its top-level `_INDEX.md` is rebuilt — `towns/_INDEX.md`, `dungeons/_INDEX.md`, `wilderness/_INDEX.md` are separate invocations.

## Workflow

1. **Confirm the target folder** with the user. Default to the folder they named.
2. **List the files** in the folder (Markdown only; ignore `_INDEX.md` itself).
3. **Read each file's frontmatter and footer.** Extract:
   - Entity name (frontmatter `name:` / `title:` / first H1).
   - One-line summary (frontmatter `summary:` if present, else synthesize from the entity's role from frontmatter fields like `status`, `location`, `disposition`, `tags`).
   - Last-touched session (footer `<!-- last updated: sNN -->`; fall back to `prep` if absent).
   - Tags (frontmatter `tags:`).
4. **Inspect the existing `_INDEX.md`** (if any) to learn its column schema. Match it. If no index exists, use the conventional schema for that folder type (see below).
5. **Compose the new index** — alphabetical by filename within each section, or by status if the folder uses a status grouping (e.g. `quests/` typically groups by `active` / `dormant` / `resolved`).
6. **Propose in chat:** show the new index as a fenced Markdown block, list any rows that changed (added / removed / one-liner-updated / last-touched-updated). Wait for approval.
7. **On approval:** write `_INDEX.md`. Confirm the path. Done.

## Schema cheat-sheet (when no existing index to match)

| Folder | Columns |
|---|---|
| `context/npcs/` | `\| File \| Name \| Location \| One-liner \| Last touched \|` |
| `context/locations/` (top level + subdirs) | `\| File \| Name \| Type \| One-liner \| Last touched \|` |
| `context/quests/` | `\| File \| Status \| One-liner \| Last touched \|` (group by status) |
| `context/pcs/` | `\| File \| PC \| Class/Level \| Arc state \| Last touched \|` |
| `context/world/` | `\| File \| One-liner \| Tags \| Last touched \|` |
| `context/world/factions/` | `\| File \| Faction \| Disposition \| Region \| Last touched \|` |
| `context/tables/` | `\| File \| Purpose \| Tags \| Last touched \|` |
| `sessions/` | `\| # \| Date \| Headline \| Linked entities \| Status \|` |

## Source of truth (REQUIRED)

- Every `*.md` file in the target folder (one read per file).
- The existing `_INDEX.md` in that folder (if any) — for schema matching.

DO NOT read:
- Sessions, unless `sessions/` is the target.
- Other folders' indexes.
- The vendored SRD.

## Hard rules

- ALWAYS propose before writing. No silent index rewrites.
- One folder per invocation.
- Do not edit entity files. If an entity file's metadata is wrong, that's a job for the entity skill (`prep/npcs`, etc.), not reindex.
- The output of a successful run is exactly one file written: the target `_INDEX.md`.
- If the proposed index is identical to the existing one, say "Already in sync — no changes needed" and write nothing.
