# Dungeon Master Agentic OS — Design

**Status:** Draft for implementation
**Date:** 2026-04-25
**Owner:** Jikodis

## Summary

A filesystem-based "agentic OS" for running a long-form D&D 5e campaign as a solo Dungeon Master. The system holds the user's campaign context as Markdown + images in a Git repo, and exposes 14 Claude Code skills (7 prep + 7 live) that handle the user's repeatable DM tasks across three phases: prep, live-at-the-table, and post-session.

The campaign is currently 18 sessions in, party at level 3, with an expected total of 150–200 sessions. The architecture must remain fast and maintainable at that scale.

## Goals

- Centralize campaign context (currently in OneNote) as Markdown in a Git repo so skills can read and update it.
- Provide skills covering all 22 repeatable DM tasks the user identified (prep, live, post).
- Keep at-the-table skills *fast and terse* — usable mid-session without breaking flow.
- Keep prep and post-session skills *rich and persistent* — they read full context and update files.
- Scale cleanly to ~200 sessions and hundreds of NPCs/locations without skill calls bloating in token cost.
- Build the POC with example/seed content; the user will do the OneNote → Markdown migration as a separate later step.

## Non-goals

- No live OneNote sync. One-time export only, done by the user later.
- No web UI / app. Filesystem + Claude Code only.
- No automated map parsing. Maps are committed images, referenced by skills but only "read" by Claude when explicitly asked.
- No other-edition support (5e only).
- No virtual tabletop integration (Roll20, Foundry, etc.).
- No initiative/HP tracking during combat — those tools already exist; this OS focuses on creative and bookkeeping work.

## Repo layout

```
dungeon-master/
├── CLAUDE.md                              # project-wide instructions, always loaded
├── README.md
│
├── context/                               # campaign data — read by skills, edited by skills (with approval)
│   ├── campaign.md                        # elevator pitch, tone, current arc
│   ├── house-rules.md
│   ├── timeline.md                        # in-world chronology
│   │
│   ├── world/                             # slow-changing world bible
│   │   ├── _INDEX.md
│   │   ├── geography.md
│   │   ├── history.md
│   │   ├── pantheon.md
│   │   └── factions/
│   │       ├── _INDEX.md
│   │       └── <faction>.md
│   │
│   ├── npcs/
│   │   ├── _INDEX.md
│   │   └── <npc-slug>.md
│   │
│   ├── locations/
│   │   ├── _INDEX.md
│   │   ├── towns/
│   │   ├── dungeons/
│   │   └── wilderness/
│   │
│   ├── quests/                            # active plot threads (high churn)
│   │   ├── _INDEX.md                      # status: active | dormant | resolved
│   │   └── <quest-slug>.md
│   │
│   ├── pcs/
│   │   ├── _INDEX.md
│   │   └── <pc-slug>.md                   # sheet, backstory, hooks pulled, arc state
│   │
│   ├── tables/                            # custom random tables
│   │   └── <table>.md
│   │
│   └── maps/                              # committed images
│       ├── world-overview.png
│       └── dungeons/
│
├── sessions/                              # chronological log; ~1 file per session, will reach 200
│   ├── _INDEX.md                          # # | date | one-line headline | linked entities
│   ├── 018-the-caravan-job.md             # raw notes + recap + state-deltas
│   └── 019-prep.md                        # prep doc for upcoming session
│
└── skills/
    ├── prep/                              # 7 rich skills — prep + post-session work
    │   ├── npcs/SKILL.md
    │   ├── encounters/SKILL.md
    │   ├── locations/SKILL.md
    │   ├── world-bible/SKILL.md
    │   ├── quests-and-threads/SKILL.md
    │   ├── sessions/SKILL.md
    │   └── pcs/SKILL.md
    │
    └── live/                              # 7 terse, at-the-table skills
        ├── improvise-npc/SKILL.md
        ├── improvise-location/SKILL.md
        ├── random-encounter/SKILL.md
        ├── region-names/SKILL.md
        ├── who-knows-what/SKILL.md
        ├── adjust-encounter/SKILL.md
        └── 5e-rules/SKILL.md
```

### Layout rationale

- **`_INDEX.md` in every folder** — every prep skill reads the index first, then drills into specific files. This is the load-bearing decision that keeps token cost flat as the campaign grows. A skill that "knows about all NPCs" reads `npcs/_INDEX.md` (one screen of one-liners), not all NPC files.
- **Frontmatter (YAML) on entity files** — gives skills structured fields (status, location, last_seen_session, tags) without forcing a strict schema. Body remains freeform Markdown.
- **`sessions/` at repo root, not under `context/`** — sessions are a chronological log of what *happened*; `context/` is the current state of the world. They're conceptually different and have different access patterns.
- **`world/` separated from `quests/`** — the world bible (geography, pantheon, factions) is slow-churn; active quests and plot threads change every session. Splitting them lets a "world expansion" skill not get confused by in-flight plot.
- **`maps/` as committed images** — Claude won't parse them by default. Skills mention them as references; the user opens them or asks Claude to look at a specific one.

## File conventions

### Frontmatter schema (entity files)

NPCs:
```yaml
---
name: Lord Verros
race: human
location: iron-reach
faction: silent-flame   # optional
status: hostile         # ally | friendly | neutral | wary | hostile | dead
tags: [smuggler, antagonist, iron-reach]
first_appeared: s12
last_seen: s19
---
```

Quests:
```yaml
---
title: The Missing Caravan
status: active          # active | dormant | resolved
tier: 1
related_npcs: [lord-verros, tavernkeep-mira]
related_locations: [iron-reach, sewers-east]
opened: s17
last_touched: s19
---
```

PCs:
```yaml
---
name: Kira
class: ranger
race: elf
level: 3
player: <real-name>
arc_state: confronting-brother
hooks_active: [missing-brother, stolen-bow]
hooks_resolved: []
---
```

Sessions:
```yaml
---
session: 19
date: 2026-04-26
pcs_present: [kira, brand, mira-sage]
locations_visited: [the-rusted-anchor, sewers-east]
npcs_appeared: [tavernkeep-mira, lord-verros]
quests_touched: [the-missing-caravan]
---
```

### `_INDEX.md` format

Every index file is a Markdown table the same shape:

```markdown
# NPCs Index

| File | One-liner | Tags | Last touched |
|------|-----------|------|--------------|
| lord-verros.md | Smuggler-king of Iron Reach, secretly Silent Flame cultist | iron-reach, antagonist | s19 |
| tavernkeep-mira.md | Owner of the Rusted Anchor, knows everyone in Iron Reach | iron-reach, ally | s18 |
```

Prep skills are **required** to update the relevant `_INDEX.md` whenever they create or edit a file. CLAUDE.md encodes this rule.

### Session file structure

Each `sessions/NNN-headline.md`:

```markdown
---
<frontmatter as above>
---

## Raw notes
(user's stream-of-consciousness during play; user-authored)

## Recap
(generated by `sessions` skill — narrative summary)

## State deltas
(generated by `sessions` skill — explicit list of what changed in canon)
- npc:lord-verros → status: hostile (was: wary)
- quest:the-missing-caravan → new lead: cult symbol on driver's neck
- pc:kira → arc: confronted brother for the first time
- world:silent-flame → revealed: cult operates in Iron Reach (was: rumor only)
```

The "State deltas" section is the canonical changelog and the input to all downstream file updates.

## CLAUDE.md (root)

CLAUDE.md is short and points at conventions rather than replicating context:

- Project purpose (one paragraph).
- Where to find things (link to layout above).
- The two skill families (prep vs live) and when each is appropriate.
- The propose-first update rule (skills must summarize proposed file changes and get user approval before writing).
- The `_INDEX.md` maintenance rule (any skill that writes to `context/<dir>/<file>.md` must also update `context/<dir>/_INDEX.md`).
- The "live skills are terse" contract (≤5–10 lines of output, no file writes, no reading `sessions/`).
- The `<!-- last updated: sNN -->` footer convention on edited entity files.

CLAUDE.md does NOT contain campaign content. That stays in `context/`.

## Skill anatomy

### Prep skills (7)

Each prep skill has a `SKILL.md` with:
- **Frontmatter:** `name`, `description` (the auto-trigger — describes when to invoke).
- **When to use:** explicit list of user requests this skill handles.
- **Workflow:** numbered steps including which `_INDEX.md` files to read first, which entity files to drill into, what to write.
- **Output conventions:** the expected file structure / sections produced.
- **Update rules:** which other files must be updated as side effects (e.g., `_INDEX.md`, footer line).

The 7 prep skills and their primary tasks:

| Skill | Primary tasks |
|-------|---------------|
| `npcs` | Create NPC, deeply update NPC after a session, "what does NPC know about X?" |
| `encounters` | Design balanced encounter, generate treasure/loot, design puzzles & traps |
| `locations` | Design taverns, dungeons, towns, wilderness areas |
| `world-bible` | Expand lore, factions, pantheon, history, geography |
| `quests-and-threads` | Design quests/plot, track active/dormant/resolved threads |
| `sessions` | Pre-session prep outline, post-session recap + state deltas + propose updates, generate next-session seed |
| `pcs` | Pull hooks from PC backstories into prep, track per-PC arc state |

### Live skills (7)

Each live skill has a `SKILL.md` with:
- **Frontmatter** with a description that explicitly says "use AT THE TABLE".
- **Output format (REQUIRED):** strict template (e.g., 5 fields, one phrase each).
- **Source of truth:** which (small) files it may read. Live skills MUST NOT read `sessions/`.
- **Hard rules:** explicit constraints — max output lines, no file writes, etc.

The 7 live skills:

| Skill | Output |
|-------|--------|
| `improvise-npc` | Name / Look / Voice / Wants / Secret — 5 lines |
| `improvise-location` | 3-sentence description with one hook |
| `random-encounter` | 1 encounter pulled from `tables/` matched to tier+region |
| `region-names` | 5 names matching the region's flavor |
| `who-knows-what` | 1–3 bullets: what the NPC knows, how they learned it |
| `adjust-encounter` | 1 reinforcement OR 1 environmental complication |
| `5e-rules` | 1-paragraph rules answer with SRD reference |

Live skills NEVER write to disk. If the user wants to persist something an improvise skill produced, they invoke the corresponding prep skill.

## State mutation pattern

**Propose-then-apply.** Prep skills that mutate canon never write silently. The flow:

1. User invokes the skill (commonly `sessions` after a session).
2. Skill reads relevant context.
3. Skill produces a **proposed-changes summary** in chat:
   > "I'll update 4 files based on session 19. Approve?"
   > - `context/npcs/lord-verros.md` — change status `wary → hostile`, append history entry
   > - `context/quests/the-missing-caravan.md` — add new lead (cult symbol on driver's neck)
   > - `context/pcs/kira-rangerelf.md` — append arc beat (confronted brother)
   > - `context/world/factions/silent-flame.md` — promote rumor to confirmed
4. User approves, edits, or rejects.
5. On approval, skill writes all files atomically:
   - Updates the entity file's frontmatter and body sections.
   - Appends `<!-- last updated: s19 -->` footer to each edited file.
   - Updates each affected `_INDEX.md` row's "Last touched" column.

**Why propose-first:** at the table the user trusts the AI for transient improvisation. For canon updates, a human gate prevents bad facts from compounding across 200 sessions.

## Indexing strategy at scale

`_INDEX.md` files are the queryable surface for the entire context. They are:
- **One-liner per file** — fits in a single screen even at 200+ entries per type.
- **Tagged** — skills can filter by tag (e.g., `iron-reach`, `antagonist`).
- **Last-touched column** — lets skills find recently relevant entities without scanning sessions.

When a skill needs cross-cutting info ("who in Iron Reach knows about the Silent Flame?"), it:
1. Greps `context/npcs/_INDEX.md` for `iron-reach` tag.
2. For matching NPCs, reads only their files (small set).
3. Cross-references `context/world/factions/silent-flame.md`.

Token cost remains roughly constant in campaign size, scaling with the *result set*, not the corpus.

## Seed content for the POC

Because the OneNote migration is deferred, the POC ships with example seed data sufficient to exercise every skill end-to-end:

- `campaign.md` — example campaign pitch and tone
- `house-rules.md` — a couple of example house rules
- `world/geography.md`, `world/history.md`, `world/pantheon.md` — short example entries
- `world/factions/` — 2 example factions (one ally, one antagonist)
- `npcs/` — 4 example NPCs with full frontmatter and sections
- `locations/towns/` — 1 example town with 2 sub-locations
- `locations/dungeons/` — 1 example dungeon (keyed)
- `locations/wilderness/` — 1 example region
- `quests/` — 2 active quests, 1 dormant
- `pcs/` — 4 example PCs at level 3
- `tables/` — 2 example random tables
- `sessions/` — 3 example completed sessions (16, 17, 18) with raw notes + recap + state deltas, plus 1 prep doc for session 19
- `_INDEX.md` files in every folder, populated for the seed content

Seed content uses placeholder names (Iron Reach, Silent Flame, Lord Verros, Kira, etc.) consistent across files so the cross-reference behaviors are demonstrable.

## Component summary

| Component | Purpose | Inputs | Outputs |
|-----------|---------|--------|---------|
| `CLAUDE.md` | Project-wide rules and conventions | (always loaded) | (instructions to all skills) |
| `context/` | Campaign canon | edited by user + prep skills (with approval) | read by all skills |
| `sessions/` | Chronological session log | user (raw notes), `sessions` skill (recap + deltas) | read by prep skills for state-delta application |
| 7 prep skills | Rich prep + post-session work | `context/`, `sessions/` | proposed file changes + user-facing rich output |
| 7 live skills | Fast at-the-table improvisation | small slices of `context/` | terse text output, no file writes |
| `_INDEX.md` files | Queryable summaries per folder | maintained by prep skills on every write | the primary read surface for skills |

## Build sequence (high level — for the planning step)

1. Scaffold repo: `CLAUDE.md`, `README.md`, all directories with empty `_INDEX.md` files.
2. Write seed content for `context/` (the example data described above).
3. Write the 3 example completed session files + 1 prep file.
4. Write all 7 prep `SKILL.md` files.
5. Write all 7 live `SKILL.md` files.
6. End-to-end smoke test: invoke one live skill (e.g., `improvise-npc`) and one prep skill (e.g., `sessions` post-session flow on session 18) against the seed content.

The detailed implementation plan is the next step (writing-plans skill).

## Open questions / future work

- **Map parsing.** Skills currently treat maps as opaque references. If desired, a future skill could call vision tools to describe a battle map.
- **Player-facing handouts.** No skill yet generates handouts (letters, posters, journal entries the players see). Could be added under `prep/handouts`.
- **Campaign analytics.** Once 50+ sessions exist, a `campaign-analytics` skill could surface "PCs we've under-served," "threads stale > 5 sessions," etc. Out of POC scope.
- **OneNote migration tooling.** User will do the export manually; no helper skill yet. If migration is painful, a `migrate-onenote-page` skill could parse exported HTML.
