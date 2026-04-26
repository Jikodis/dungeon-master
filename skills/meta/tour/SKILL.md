---
name: tour
description: Use when the user is new to this DM Agentic OS or asks for a tour, walkthrough, onboarding, "how do I use this", "show me around", "what skills do I have", "getting started", or "explain how this repo works". Walks a Dungeon Master through the file layout, the prep vs live skill families, the propose-first and _INDEX rules, the session lifecycle, and a first-30-minutes plan.
---

# Tour: Onboard a Dungeon Master to this Agentic OS

You are giving a DM their first guided tour of this repository as a campaign brain. Be warm, concrete, and brief — show them where things are, what to type, and what will happen. Do not lecture. Use the section headings below in order. Pause for questions only at the marked checkpoints.

## What this is, in one breath

This repo is your campaign brain. The world lives in `context/` as Markdown. Past sessions live in `sessions/`. Skills under `skills/` do the repeatable DM work for you — both deskwork between sessions and quick rulings at the table. Nothing is auto-magic: you stay the DM, the OS just remembers, drafts, and proposes.

## The two skill families (the most important distinction)

There are two kinds of skills in this OS, and they behave very differently:

**Prep skills** (`skills/prep/`) are for **deskwork** — between sessions, with time to think.
- They read a lot of context and produce rich, structured output.
- They **propose changes to canon and wait for your approval** before writing files.
- Use them for: building NPCs, designing encounters, writing locations, growing the world bible, tracking quest threads, prepping or recapping a session, advancing PC arcs.

**Live skills** (`skills/live/`) are for **at the table** — mid-session, time pressure.
- Output is intentionally short (≤ 5–10 lines, strict template).
- They **never write files** and **never read `sessions/`** (too slow, too much context).
- Use them for: improvising an NPC, naming a region, rolling a random encounter, scaling an encounter on the fly, looking up a 5e rule, deciding who knows what.

**Rule of thumb:** if you mention being mid-session or want a quick answer, the live skill fires. If you say "let me prep" or "after the session", the prep skill fires.

## The two non-negotiable rules

### 1. Propose-first writes
Prep skills never silently mutate canon. They will:
1. Summarize all proposed changes in chat (one bullet per file, with what changes).
2. Wait for you to approve, edit, or reject.
3. Only on approval, write the files.

If a skill ever skips step 1 or 2, that's a bug — call it out.

### 2. `_INDEX.md` stays current
Every folder under `context/` and `sessions/` has an `_INDEX.md` table — one row per file with a one-liner and the last session that touched it. Skills query indexes first, then drill into specific files. Whenever a prep skill creates or edits an entity file, it must also update the matching `_INDEX.md`. Stale indexes break search across the whole campaign.

## The file layout

```
context/                     campaign canon — the current state of the world
  campaign.md                elevator pitch, tone, current arc
  house-rules.md             your table rules
  timeline.md                in-world chronology
  world/                     slow-changing world bible
    geography.md, history.md, pantheon.md
    factions/                one file per faction
  npcs/                      one file per NPC
  locations/{towns,dungeons,wilderness}/
  quests/                    active and dormant plot threads
  pcs/                       one file per player character
  tables/                    your custom random tables
  maps/                      committed image files

sessions/                    chronological log, one file per session
  NNN-headline.md            raw notes + recap + state deltas

skills/
  prep/                      7 deskwork skills (rich, propose-then-write)
  live/                      7 at-the-table skills (terse, no writes)
  meta/                      skills about the OS itself (this tour lives here)

docs/superpowers/            design and plan docs (meta — not gameplay)
CLAUDE.md                    project-wide instructions, always loaded
```

**Conventions worth knowing:**
- Entity files (NPCs, locations, quests, factions, PCs) start with YAML frontmatter and end with `<!-- last updated: sNN -->`.
- Slugs are kebab-case (`lord-verros.md`, `the-rusted-anchor.md`).
- Session files are zero-padded 3-digit (`018-the-caravan-hunt.md`).

**Checkpoint:** Ask the DM if they want to peek at any folder before continuing. If yes, run a quick `ls` and read one example file to make it concrete.

## The 14 skills, with their fire phrases

### Prep skills (7) — `skills/prep/`

| Skill | Fires when you say… |
|---|---|
| `npcs` | "draft an NPC", "flesh out Lord Verros", "update Mira after last session" |
| `encounters` | "design a tier-2 encounter", "build a puzzle for the sewers", "give me loot for a CR-3 fight" |
| `locations` | "write up a tavern", "design a 3-room dungeon", "describe the Black Crag wilderness" |
| `world-bible` | "expand the pantheon", "add a faction", "fill in northern history" |
| `quests-and-threads` | "design a new arc", "what threads are active?", "advance the cult quest" |
| `sessions` | "prep session 19", "recap session 18", "log what just happened" |
| `pcs` | "pull Kira's hooks", "advance Brand's arc", "what does Mira-Sage know about the cult?" |

### Live skills (7) — `skills/live/`

| Skill | Fires when you say… |
|---|---|
| `improvise-npc` | "they walked into a shop I didn't prep — give me a shopkeeper, fast" |
| `improvise-location` | "they wandered off the map — quick description of a roadside shrine" |
| `random-encounter` | "roll an encounter for tier-1 Iron Reach, party of 4" |
| `region-names` | "name three villages in the lowlands" |
| `who-knows-what` | "would Kira recognize the cult symbol?" |
| `adjust-encounter` | "they're getting steamrolled — scale this fight down" |
| `5e-rules` | "how does grappling interact with reach?" |

If a request is ambiguous, the OS prefers the live skill when you mention time pressure, being mid-session, or want short output.

## The session lifecycle

This is the loop the OS is built around. Live it once and the rest will make sense.

1. **Before the session — prep**
   - Invoke the `sessions` prep skill: "prep session 19".
   - It reads `sessions/_INDEX.md`, the latest few session files, active quests, and PC hook state. Then it proposes a `019-prep.md` with: open threads to push, scenes ready to run, NPCs likely to appear, contingencies, hooks-to-pull per PC.
   - You approve / edit / reject. On approval it writes the file and updates `sessions/_INDEX.md`.

2. **During the session — play**
   - Keep the prep doc open. When the players go off-script, call live skills:
     - "improvise an NPC for the ferry crossing"
     - "roll a random encounter"
     - "would Brand know that name?"
   - Live skills give you 5–10 lines and never touch the files.
   - Jot rough notes anywhere — a scratch buffer, a notepad, even chat with Claude.

3. **After the session — recap + deltas**
   - Invoke `sessions`: "recap session 18 from these notes: ...".
   - The skill drafts a session file with three sections: **Raw notes**, **Recap** (2–4 paragraphs in the campaign's voice), and **State deltas** (a list like "Lord Verros now suspects the party", "the Rusted Anchor was burned down").
   - You approve. It writes `sessions/018-the-caravan-hunt.md`, then proposes the entity file edits implied by the deltas (NPCs, locations, quests, PCs, timeline). You approve those, it writes them and updates every affected `_INDEX.md`.

4. **Between sessions — grow the world**
   - Use `world-bible`, `locations`, `npcs`, `quests-and-threads`, `pcs` ad-hoc as you build new content.

## Your first 30 minutes

A concrete walkthrough to try right now:

1. **Read `CLAUDE.md`** (60 seconds). It's the project-wide brief Claude reloads every conversation.
2. **Skim `context/campaign.md` and `context/timeline.md`** — see the current arc and where the campaign is.
3. **Open one of each entity type** to learn the shape:
   - `context/npcs/lord-verros.md`
   - `context/locations/towns/hollowgate.md`
   - `context/quests/the-missing-caravan.md`
   - `context/pcs/kira.md`
4. **Glance at `sessions/_INDEX.md`** then read `sessions/018-the-caravan-hunt.md` to see the Raw / Recap / Deltas pattern.
5. **Open one prep skill** (e.g. `skills/prep/sessions/SKILL.md`) and **one live skill** (e.g. `skills/live/improvise-npc/SKILL.md`). Compare their length and tone — that contrast is the OS's spine.
6. **Try a live skill cold:** ask "improvise an NPC: drunk dockhand at the Rusted Anchor." You should get ~6 lines, no files touched.
7. **Try a prep skill:** ask "draft an NPC: a retired bounty hunter who runs the Hollowgate stables." It should propose a file path and full content, then wait for your approval.
8. **Approve the proposal** and watch it write `context/npcs/<slug>.md` plus a one-row update to `context/npcs/_INDEX.md`. That's the loop.

After this, you know the whole system.

## When something feels off

- **A live skill is writing files.** That's a bug. Stop and ask Claude to read the live-skill rule in `CLAUDE.md`.
- **A prep skill wrote without asking.** Same — that violates the propose-first rule.
- **Search feels broken.** Check the relevant `_INDEX.md` — a missing or stale row is almost always the cause.
- **You're at the table and the answer is too long.** Say "live skill, short answer" — that re-routes to the constrained family.

## Closing

You are still the DM. The OS is a memory and a pair of hands, not a co-author of your judgment. Lean on it for bookkeeping and improv scaffolding so you can spend your attention on the table.

Welcome aboard.
