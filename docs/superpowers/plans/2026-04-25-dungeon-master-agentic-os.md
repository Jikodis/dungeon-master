# Dungeon Master Agentic OS — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Scaffold a filesystem-based "agentic OS" for a D&D 5e DM — `CLAUDE.md` + `context/` (Markdown campaign data) + `sessions/` (chronological log) + `skills/prep/` (7 rich skills) + `skills/live/` (7 terse skills) — populated with consistent seed content so every skill can be exercised end-to-end.

**Architecture:** Each entity type lives in its own folder under `context/` with a YAML-frontmatter Markdown file per entity and a `_INDEX.md` table of one-liners. Skills read indexes first, drill into specific files, and (for prep skills) propose changes for user approval before writing. Live skills are bound by hard rules in their own bodies (no file writes, ≤5–10 lines of output, no reading `sessions/`).

**Tech Stack:** Markdown, YAML frontmatter, Git, Claude Code skills. No code, no runtime, no build step.

**Spec:** [docs/superpowers/specs/2026-04-25-dungeon-master-agentic-os-design.md](../specs/2026-04-25-dungeon-master-agentic-os-design.md)

**Verification model:** This project produces no runnable code. "Tests" are file-existence + grep-for-required-content checks. Each task ends with a verification command and an explicit expected output, then a commit.

**Seed world (used consistently across all seed files):**

- World: **Velara** (low-magic gritty fantasy)
- Region: **Iron Reach** — mountainous mining region, gruff dwarven culture
- Town: **Hollowgate** — fortified mining town in Iron Reach
- Antagonist faction: **Silent Flame** — cult operating in the shadows
- Ally faction: **Iron Reach Merchant Guild** — trying to clean up smuggling
- Key NPCs: **Lord Verros** (smuggler-king, secret cultist), **Tavernkeep Mira** (Rusted Anchor owner, ally), **High Priest Aldon** (cult leader, unseen), **Sergeant Brenna** (city watch, neutral)
- PCs (level 3, party of 4): **Kira** (elf ranger), **Brand** (human fighter), **Mira-sage** (half-elf wizard), **Thorn** (halfling rogue)
- Locations: **Hollowgate** (town), **The Rusted Anchor** (tavern), **Sewers East** (dungeon), **The Black Crag** (wilderness)
- Active quests: **The Missing Caravan**, **Cult of the Silent Flame**; dormant: **The Stolen Bow** (Kira's brother)
- Sessions: 16 (first cult contact), 17 (Hollowgate investigation), 18 (Black Crag caravan hunt), 19-prep (sewers descent planned)

---

## File Structure

The following files are created in this plan, grouped by responsibility:

**Project root**
- `CLAUDE.md` — project-wide rules (skill families, propose-first, index maintenance)
- `.gitignore` — ignore `.superpowers/` and OS noise
- `README.md` — already exists from brainstorm; will be expanded

**Top-level context** (`context/`)
- `context/campaign.md`, `context/house-rules.md`, `context/timeline.md`

**World bible** (`context/world/`, slow churn)
- `_INDEX.md`, `geography.md`, `history.md`, `pantheon.md`
- `factions/_INDEX.md`, `factions/silent-flame.md`, `factions/iron-reach-merchant-guild.md`

**Entities** (`context/{npcs,locations,quests,pcs,tables,maps}/`, varying churn)
- 4 NPC files + index
- 1 town + 1 dungeon + 1 wilderness file + indexes
- 3 quest files + index
- 4 PC files + index
- 2 table files + index
- `maps/` (empty placeholder dir + `.gitkeep`)

**Sessions** (`sessions/`, chronological log)
- `_INDEX.md`, `016-the-cult-symbol.md`, `017-asking-around-hollowgate.md`, `018-the-caravan-hunt.md`, `019-prep.md`

**Prep skills** (`skills/prep/<name>/SKILL.md`)
- `npcs`, `encounters`, `locations`, `world-bible`, `quests-and-threads`, `sessions`, `pcs`

**Live skills** (`skills/live/<name>/SKILL.md`)
- `improvise-npc`, `improvise-location`, `random-encounter`, `region-names`, `who-knows-what`, `adjust-encounter`, `5e-rules`

---

## Task 1: Scaffold directory structure and .gitignore

**Files:**
- Create: directory tree under `context/`, `sessions/`, `skills/prep/`, `skills/live/`
- Modify: `.gitignore` (already exists with `.superpowers/` and `.DS_Store` from brainstorm)

- [ ] **Step 1: Create the directory tree**

```bash
mkdir -p context/world/factions \
         context/npcs \
         context/locations/towns \
         context/locations/dungeons \
         context/locations/wilderness \
         context/quests \
         context/pcs \
         context/tables \
         context/maps/dungeons \
         sessions \
         skills/prep/npcs \
         skills/prep/encounters \
         skills/prep/locations \
         skills/prep/world-bible \
         skills/prep/quests-and-threads \
         skills/prep/sessions \
         skills/prep/pcs \
         skills/live/improvise-npc \
         skills/live/improvise-location \
         skills/live/random-encounter \
         skills/live/region-names \
         skills/live/who-knows-what \
         skills/live/adjust-encounter \
         skills/live/5e-rules
```

- [ ] **Step 2: Add a placeholder so `maps/` survives in git**

```bash
touch context/maps/.gitkeep
touch context/maps/dungeons/.gitkeep
```

- [ ] **Step 3: Verify the tree**

Run: `find . -type d -not -path '*/.*' -not -path './docs*' | sort`
Expected: includes all 24 directories above (plus `.`, `./context`, `./sessions`, `./skills`, etc.)

- [ ] **Step 4: Commit**

```bash
git add -A
git commit -m "Scaffold directory structure for context, sessions, and skills"
```

---

## Task 2: Create empty `_INDEX.md` files

Empty index files let `git` track the directories and let early skills find them even before content exists.

**Files:**
- Create: `_INDEX.md` in every folder that will hold entity files

- [ ] **Step 1: Write all index files with their headers**

Each index file gets a `# <Name> Index` heading and a stub table. Run this script (in the project root):

```bash
cat > context/world/_INDEX.md <<'EOF'
# World Bible Index

| File | One-liner | Tags | Last touched |
|------|-----------|------|--------------|
EOF

cat > context/world/factions/_INDEX.md <<'EOF'
# Factions Index

| File | One-liner | Tags | Last touched |
|------|-----------|------|--------------|
EOF

cat > context/npcs/_INDEX.md <<'EOF'
# NPCs Index

| File | One-liner | Tags | Last touched |
|------|-----------|------|--------------|
EOF

cat > context/locations/_INDEX.md <<'EOF'
# Locations Index

| File | One-liner | Tags | Last touched |
|------|-----------|------|--------------|
EOF

cat > context/quests/_INDEX.md <<'EOF'
# Quests Index

| File | One-liner | Status | Tags | Last touched |
|------|-----------|--------|------|--------------|
EOF

cat > context/pcs/_INDEX.md <<'EOF'
# PCs Index

| File | One-liner | Player | Last touched |
|------|-----------|--------|--------------|
EOF

cat > context/tables/_INDEX.md <<'EOF'
# Tables Index

| File | Purpose | Tags |
|------|---------|------|
EOF

cat > sessions/_INDEX.md <<'EOF'
# Sessions Index

| # | Date | Headline | PCs present | Locations | NPCs | Quests touched |
|---|------|----------|-------------|-----------|------|----------------|
EOF
```

- [ ] **Step 2: Verify all 8 indexes exist**

Run: `find . -name '_INDEX.md' | sort`
Expected: 8 files listed (world, factions, npcs, locations, quests, pcs, tables, sessions).

- [ ] **Step 3: Commit**

```bash
git add -A
git commit -m "Add empty _INDEX.md files for every context and sessions folder"
```

---

## Task 3: Write the root CLAUDE.md

**Files:**
- Create: `CLAUDE.md`

- [ ] **Step 1: Write CLAUDE.md**

Write the following to `CLAUDE.md`:

```markdown
# Dungeon Master Agentic OS

This repo is the campaign brain for a long-running D&D 5e campaign (currently 18 sessions in, party at level 3, target ~150–200 sessions). It holds the campaign as Markdown so Claude Code skills can read and update it.

## Where things live

- `context/` — campaign canon (world, NPCs, locations, quests, PCs, tables, maps). The current state of the world.
- `sessions/` — chronological log of what happened, one file per session. Source of truth for past events.
- `skills/prep/` — 7 rich skills for deskwork: prep before a session, bookkeeping after.
- `skills/live/` — 7 terse skills for at-the-table use during play.
- `docs/superpowers/` — design docs and implementation plans (meta, not gameplay).

## Two skill families

**Prep skills** (`skills/prep/`) are deliberate. They read full context, produce rich output (multiple paragraphs, structured Markdown), and **propose changes to canon for user approval before writing files**.

**Live skills** (`skills/live/`) run at the table. They are intentionally constrained:
- Output ≤ 5–10 lines, formatted to a strict template.
- They **must not read `sessions/`** (too slow, too much context).
- They **must not write files**.
- If the user wants to persist what a live skill produced, they invoke the corresponding prep skill.

When a request could match either family, prefer the live skill if the user mentions being mid-session, time pressure, or short output.

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
```

- [ ] **Step 2: Verify CLAUDE.md exists and contains the key rules**

Run: `grep -c "Propose-first" CLAUDE.md && grep -c "_INDEX.md" CLAUDE.md`
Expected: each command outputs at least `1` (both rules are present).

- [ ] **Step 3: Commit**

```bash
git add CLAUDE.md
git commit -m "Add root CLAUDE.md with skill families, propose-first, and index rules"
```

---

## Task 4: Top-level context files (campaign, house-rules, timeline)

**Files:**
- Create: `context/campaign.md`, `context/house-rules.md`, `context/timeline.md`

- [ ] **Step 1: Write `context/campaign.md`**

```markdown
# Velara Campaign

## Pitch
A gritty low-magic campaign in the world of Velara, currently centered on the Iron Reach — a mountainous mining region run by ruthless guilds and creeping with a hidden cult called the Silent Flame. The party (level 3) has stumbled into the cult's edges while doing odd jobs out of the town of Hollowgate.

## Tone
- Low magic, money matters, healing is rare.
- Faction politics over kicking-down-doors.
- Consequences stick. NPCs remember.
- Gallows humor at the table is welcome.

## Current arc (as of session 18)
The party has uncovered a cult symbol in a missing caravan's wreckage out in the Black Crag. They suspect Lord Verros (whose smuggling operation the caravan was raiding) is connected. Tavernkeep Mira at the Rusted Anchor is helping them quietly. Next session: descending into Sewers East under Hollowgate to find the cult's safehouse.

## Session cadence
- Roughly weekly, ~3 hour sessions.
- Target: 150–200 total sessions.

<!-- last updated: prep -->
```

- [ ] **Step 2: Write `context/house-rules.md`**

```markdown
# House Rules

## Combat
- **Critical hits:** max die + roll, not double dice.
- **Death saves are private.** DM rolls behind the screen.
- **Inspiration:** awarded for in-character moments, not cleverness alone. Stacks up to 3.

## Resting
- **Long rest** requires a safe location and 8 hours. Wilderness alone is not safe.
- **Short rest** is 1 hour and assumes downtime; can't be done mid-combat or while pursued.

## Magic
- **Identify** still requires the spell or ritual; magic items are not auto-identified on touch.
- **Healing potions** are a bonus action to drink, action to administer to another.

## Social
- **Persuasion is not mind control.** A good roll moves attitude one step at most.

<!-- last updated: prep -->
```

- [ ] **Step 3: Write `context/timeline.md`**

```markdown
# Velaran Timeline

In-world chronology. Dates are in the Velaran calendar — *Year of Iron 847 (YoI 847)* is "now" at the start of session 18.

## Distant past
- **YoI 0** — The Iron Reach mines opened; the dwarven holds rose.
- **YoI ~200** — The Hollowgate fortification built.
- **YoI 612** — The "Quiet War" between the Merchant Guild and the old nobility ended in the Guild's favor.

## Recent
- **YoI 845** — Cult of the Silent Flame first whispered about in eastern villages.
- **YoI 846 (last winter)** — Three caravans vanish on the Black Crag road; Guild offers bounties.
- **YoI 847, Spring** — The party arrives in Hollowgate (campaign session 1).

## Current arc
- **YoI 847, late spring (s16)** — Party finds the cult symbol in a wrecked caravan.
- **YoI 847, late spring (s18)** — Party links Verros to the missing caravans.

<!-- last updated: prep -->
```

- [ ] **Step 4: Verify all three files**

Run: `ls -1 context/campaign.md context/house-rules.md context/timeline.md`
Expected: three lines, all present.

Run: `grep -l "last updated" context/*.md`
Expected: all three files listed.

- [ ] **Step 5: Commit**

```bash
git add context/campaign.md context/house-rules.md context/timeline.md
git commit -m "Add top-level context: campaign pitch, house rules, in-world timeline"
```

---

## Task 5: World bible (geography, history, pantheon)

**Files:**
- Create: `context/world/geography.md`, `context/world/history.md`, `context/world/pantheon.md`

- [ ] **Step 1: Write `context/world/geography.md`**

```markdown
---
type: world-reference
section: geography
---

# Geography of Velara

## Continents
Velara is a single mid-sized continent, roughly 2,000 miles east-to-west.

## Major regions

### The Iron Reach (current campaign region)
- Mountainous mining region in the central north.
- Ruled in name by the old Mountain Kings, in practice by the Iron Reach Merchant Guild.
- Climate: cold, harsh winters, short summers.
- Economy: iron, silver, smuggled luxury goods, mercenary work.
- Notable: **Hollowgate** (fortified mining town), **The Black Crag** (wilderness north of Hollowgate), **The Spine** (the great mountain ridge).

### The Silent Coast (east)
- Forested, foggy, scattered fishing villages.
- Where the Silent Flame cult was first heard of.
- Largely outside Guild influence.

### The Goldlands (south)
- Wealthy plains, the political heart of Velara.
- The party hasn't been here. Rumors say the Merchant Guild's true power sits in the Goldland city of **Aurelle**.

### The Burnt Wastes (west)
- Volcanic, hostile, ringed by dead cities.
- Folklore says the Silent Flame originated here.

<!-- last updated: prep -->
```

- [ ] **Step 2: Write `context/world/history.md`**

```markdown
---
type: world-reference
section: history
---

# History of Velara (broad strokes)

## The Old Kingdoms (YoI 0 – ~500)
A patchwork of dwarven mountain holds and human petty kingdoms. The Iron Reach mines were the wealth engine.

## The Quiet War (YoI 600 – 612)
A 12-year economic and shadow war between the Iron Reach Merchant Guild and the old Mountain Kings. Ended without major battles — the Kings were paid off, exiled, or quietly killed. The Guild has effectively ruled the Iron Reach since.

## The Long Peace (YoI 612 – 845)
Mostly stable. The Guild expanded south into the Goldlands. Trade routes flourished. The Silent Coast was largely abandoned to fog and small villages.

## The Stirring (YoI 845 – present)
- Cult of the Silent Flame begins surfacing in Silent Coast villages.
- Caravans on the Black Crag road start vanishing.
- Hollowgate's underworld grows bolder.
- The Guild is distracted by Goldlands politics and slow to respond.

<!-- last updated: prep -->
```

- [ ] **Step 3: Write `context/world/pantheon.md`**

```markdown
---
type: world-reference
section: pantheon
---

# The Velaran Pantheon

Velara has a small, practical pantheon. Most folk worship one or two gods sincerely and acknowledge the rest.

## The Six

| God | Domain | Symbol | Followers |
|-----|--------|--------|-----------|
| **Korren** | Stone, mountains, oaths | A hammer over a mountain | Dwarves, miners, masons |
| **Vesna** | Hearth, harvest, family | A grain stalk in a doorway | Most townsfolk |
| **Talen** | Trade, roads, fortune | A coin between two clasped hands | Merchants, the Guild |
| **The Pale Lady** | Death, memory, endings | A white moth | Everyone, eventually |
| **Drenn** | War, courage, honor | A red spear | Soldiers, mercenaries |
| **Sela** | Sea, weather, change | A wave with three crests | Coastal folk, sailors |

## The Silent Flame (heretical)
Not part of the Six. A cult god (or thing-pretending-to-be-a-god). Worshippers claim it offers "release from the burden of memory." Most Velarans find this terrifying. Symbol: an inverted candle with a black flame.

<!-- last updated: prep -->
```

- [ ] **Step 4: Verify the three files**

Run: `ls -1 context/world/*.md`
Expected: `geography.md`, `history.md`, `pantheon.md`, plus `_INDEX.md` (still empty for now — populated in Task 12).

- [ ] **Step 5: Commit**

```bash
git add context/world/geography.md context/world/history.md context/world/pantheon.md
git commit -m "Add world bible: geography, history, pantheon"
```

---

## Task 6: Faction files

**Files:**
- Create: `context/world/factions/silent-flame.md`, `context/world/factions/iron-reach-merchant-guild.md`

- [ ] **Step 1: Write the antagonist faction**

`context/world/factions/silent-flame.md`:

```markdown
---
name: Silent Flame
type: cult
disposition: hostile
region: silent-coast, iron-reach (recently)
status: active-and-spreading
known_to_party: rumor + symbol-evidence (as of s18)
tags: [cult, antagonist, silent-flame]
---

# The Silent Flame

## What they claim to be
A movement offering "release from the burden of memory." Followers describe a profound peace after initiation.

## What they actually are
A cult worshipping (or being used by) something that erases the minds of its converts. Initiates are docile, useful, and forget who they were. Higher tiers know more — and choose to keep going anyway.

## Structure (best current intel)
- **Embers** — newest converts, mind-wiped, used as labor.
- **Wicks** — knowing followers, mid-tier, recruit and protect.
- **The Lit** — leadership cadre. Names not known to the party.
- **High Priest Aldon** — the only named figure. Never seen by the party.

## What they want
Unclear. The cult is spreading; that's all the party knows.

## Known operations
- **Silent Coast villages** — original recruiting ground (rumor).
- **Iron Reach** — recent infiltration. Tied to Lord Verros's smuggling routes (s18 evidence).

## Symbol
An inverted candle with a black flame. Marked on the wrecked caravan in s16.

## Cross-references
- See `context/npcs/lord-verros.md` (suspected Wick or higher).
- See `context/quests/cult-of-the-silent-flame.md` (active investigation).

<!-- last updated: s18 -->
```

- [ ] **Step 2: Write the ally faction**

`context/world/factions/iron-reach-merchant-guild.md`:

```markdown
---
name: Iron Reach Merchant Guild
type: trade-political-organization
disposition: neutral-leaning-ally
region: iron-reach (HQ in Hollowgate; influence in Aurelle)
status: dominant-but-distracted
known_to_party: extensively
tags: [guild, ally, iron-reach]
---

# Iron Reach Merchant Guild

## What they are
The de facto government of the Iron Reach. Originally a trade cartel; after the Quiet War (YoI 612) they absorbed the political functions of the displaced Mountain Kings. Run by a council of "Factors."

## Structure
- **The Council of Factors** — ~12 senior merchants. Meets in Aurelle quarterly.
- **Factor-Hollowgate** — the local boss in Hollowgate. Currently **Factor Renn**.
- **Caravan-marshals** — guild-employed enforcers protecting trade.
- **Guild scribes** — keep records, hire freelancers (the party has done jobs for them).

## What they want
- Stable trade routes.
- Smuggling shut down (it competes with their margin).
- The Goldlands kept happy.

## Where they're weak
- Slow to act on threats they don't yet measure financially. The Silent Flame doesn't show up on a ledger.
- Internal politics: not all Factors agree on Iron Reach priorities.

## Relationship with the party
- Have hired the party 3 times for caravan escort and 1 time for "investigation" (s14).
- Factor Renn knows their names. Trusts them moderately.
- If shown cult evidence, would likely fund pursuit — but slowly.

## Cross-references
- See `context/npcs/lord-verros.md` (Guild's #1 smuggling target).
- See `context/quests/the-missing-caravan.md` (Guild-funded bounty).

<!-- last updated: s18 -->
```

- [ ] **Step 3: Verify the faction files**

Run: `ls -1 context/world/factions/*.md`
Expected: `iron-reach-merchant-guild.md`, `silent-flame.md`, plus `_INDEX.md`.

Run: `grep -c "^---$" context/world/factions/silent-flame.md`
Expected: `2` (frontmatter open + close).

- [ ] **Step 4: Commit**

```bash
git add context/world/factions/silent-flame.md context/world/factions/iron-reach-merchant-guild.md
git commit -m "Add faction files: Silent Flame (antagonist) and Merchant Guild (ally)"
```

---

## Task 7: NPC files (4 NPCs)

**Files:**
- Create: `context/npcs/lord-verros.md`, `context/npcs/tavernkeep-mira.md`, `context/npcs/high-priest-aldon.md`, `context/npcs/sergeant-brenna.md`

- [ ] **Step 1: Write Lord Verros (antagonist)**

`context/npcs/lord-verros.md`:

```markdown
---
name: Lord Verros
race: human
location: hollowgate
faction: silent-flame
status: hostile
tags: [iron-reach, antagonist, smuggler, silent-flame]
first_appeared: s12
last_seen: s18
---

# Lord Verros

## Description
Late forties, tall, gaunt. Always immaculately dressed in dark colors. Wears black gloves indoors. Speaks in deliberate, measured sentences.

## Voice
Low, dry, never raises it. Pauses before answering questions, as if rehearsing the answer.

## Motivations
1. Expand his smuggling network across the Iron Reach.
2. (Hidden) Serve the Silent Flame and bring more converts to it.

## Secrets
- (known: party-suspects-not-confirmed) He runs the smuggling that the missing caravans were stealing from.
- (known: none) He is at minimum a Wick of the Silent Flame and is recruiting from his crew.
- (known: none) High Priest Aldon visits Verros's manor monthly.

## Knows about
- The cult's Iron Reach operations (extensively).
- Smuggling routes through the Black Crag.
- Which Hollowgate guards take bribes (most of them).

## History
- **s12** — First met the party in passing at a Guild reception.
- **s15** — Party did an unrelated job near his warehouse; he noticed.
- **s18** — Party found his smuggling brand on the caravan wreckage, alongside the cult symbol.

<!-- last updated: s18 -->
```

- [ ] **Step 2: Write Tavernkeep Mira (ally)**

`context/npcs/tavernkeep-mira.md`:

```markdown
---
name: Tavernkeep Mira
race: half-elf
location: hollowgate
faction: none
status: ally
tags: [iron-reach, ally, hollowgate, information-broker]
first_appeared: s2
last_seen: s17
---

# Tavernkeep Mira

## Description
Mid-forties, grey-streaked black hair, sharp eyes. Owner of the Rusted Anchor, the central tavern in Hollowgate. Knows everyone.

## Voice
Warm but never gushing. Drops her voice low when sharing real information. Calls everyone "love" except the people she despises.

## Motivations
1. Keep the Rusted Anchor solvent and her staff safe.
2. Push back, quietly, against the cult and the worst of the smuggling.
3. Repay the party for protecting her niece in s7.

## Secrets
- (known: party) She runs a low-key information network across Hollowgate's working class.
- (known: none) Her late husband was a Guild caravan-marshal killed by smugglers in YoI 843. She has reasons to want Verros dead.

## Knows about
- Which Hollowgate guards are clean.
- Most of the named regulars in town and what they do for a living.
- Rumors at the level of "I heard from a barmaid who heard from..."

## History
- **s2** — Party's first stop in Hollowgate. Sized them up; let them stay on the cuff.
- **s7** — Party stopped a brawl that would have hurt her niece; she's owed them since.
- **s17** — Party brought her the cult symbol; she went quiet, then started asking around.

<!-- last updated: s17 -->
```

- [ ] **Step 3: Write High Priest Aldon (off-screen antagonist)**

`context/npcs/high-priest-aldon.md`:

```markdown
---
name: High Priest Aldon
race: unknown
location: unknown
faction: silent-flame
status: hostile-unseen
tags: [silent-flame, antagonist, off-screen]
first_appeared: never (rumor only)
last_seen: never
---

# High Priest Aldon

## Description
Unknown. The party has only heard the name in fragments — once from a Silent Coast survivor (s11), once scratched into the ledger found in the wrecked caravan (s16).

## Voice
Unknown.

## Motivations
1. Lead the Silent Flame to whatever it is they're aiming at.
2. (Speculation) Personal investment in the Iron Reach expansion.

## Secrets
- Everything. The party doesn't know if Aldon is human, where they are, or what they want.

## Knows about
- The cult's actual purpose.
- Probably the party's existence (Verros has reported them by now).

## History
- **s11** — Name first heard from a frightened survivor of a Silent Coast village.
- **s16** — Name appeared in the caravan-driver's ledger as "*Aldon's people pay double*."

<!-- last updated: s16 -->
```

- [ ] **Step 4: Write Sergeant Brenna (neutral)**

`context/npcs/sergeant-brenna.md`:

```markdown
---
name: Sergeant Brenna
race: dwarf
location: hollowgate
faction: hollowgate-watch
status: neutral
tags: [iron-reach, neutral, watch, hollowgate]
first_appeared: s4
last_seen: s17
---

# Sergeant Brenna

## Description
Stocky dwarven woman, fifties, scarred forearms. Sergeant of the Hollowgate Watch's eastern district. Honest, by Iron Reach standards.

## Voice
Clipped, direct. Doesn't waste words. Uses old dwarven oaths under her breath.

## Motivations
1. Keep her district from descending into chaos.
2. Make Watch sergeant-major before she retires in three years.

## Secrets
- (known: none) She knows three of her own watchmen take bribes from Verros. She's saving the proof.

## Knows about
- Who's in the Hollowgate Watch and which ones can be trusted (a short list).
- Recent crimes in the eastern district — including unreported ones.

## History
- **s4** — Detained the party briefly after a tavern fight; let them go when their story checked.
- **s11** — Hired the party off the books to investigate a missing watchman (resolved in s12 — he had run off).
- **s17** — Mira asked Brenna a question about the cult symbol; Brenna asked the party what they knew. Polite, not hostile.

<!-- last updated: s17 -->
```

- [ ] **Step 5: Verify NPCs**

Run: `ls -1 context/npcs/*.md`
Expected: 4 NPC files + `_INDEX.md`.

Run: `grep -l "^---$" context/npcs/*.md | wc -l`
Expected: `5` (4 NPC files + index — though the index has no frontmatter, this is a loose check; the real check is below).

Run: `grep -c "^name:" context/npcs/lord-verros.md context/npcs/tavernkeep-mira.md context/npcs/high-priest-aldon.md context/npcs/sergeant-brenna.md`
Expected: each file shows `1`.

- [ ] **Step 6: Commit**

```bash
git add context/npcs/*.md
git commit -m "Add NPC seed: Verros, Mira, Aldon, Brenna"
```

---

## Task 8: Location files (1 town, 1 dungeon, 1 wilderness)

**Files:**
- Create: `context/locations/towns/hollowgate.md`, `context/locations/towns/the-rusted-anchor.md`, `context/locations/dungeons/sewers-east.md`, `context/locations/wilderness/the-black-crag.md`

- [ ] **Step 1: Write Hollowgate (town)**

`context/locations/towns/hollowgate.md`:

```markdown
---
name: Hollowgate
type: town
region: iron-reach
population: ~4,500
governance: Guild Factor + Watch
tags: [town, iron-reach, current-base]
---

# Hollowgate

## Overview
Fortified mining town, the largest settlement in the Iron Reach outside of capital-equivalent dwarven holds. Built around the Hollow Gate itself — a massive iron-banded portcullis at the foot of the Spine. Cold, smoky, busy.

## Districts
- **The Hollow** — old town inside the original walls. Guild offices, merchants, the Rusted Anchor.
- **East District** — workers' quarter, miners' tenements, where most trouble starts. Sergeant Brenna's beat.
- **The Cuts** — slums on the outer slope. Watch rarely goes here.
- **Stonecradle** — wealthy district uphill. Lord Verros's manor.

## Notable locations
- **The Rusted Anchor** (Mira's tavern) — see file.
- **The Hollow Forge** — the main Guild forge and warehouse.
- **The Watch House (East)** — Brenna's posting.
- **Verros Manor** — in Stonecradle.
- **Sewers East entrance** — manhole behind the Watch House. See dungeon file.

## Mood
Smoke from a hundred forge-fires. The smell of iron in the rain. Watchmen in green tabards. Dwarves arguing prices in the street.

## Hooks the party hasn't used
- A miner in the East District is offering reward for finding his missing son (filed in s14, untouched).
- A Stonecradle widow wants someone followed; she suspects her son is involved with the cult (Mira mentioned this in s17).

<!-- last updated: s17 -->
```

- [ ] **Step 2: Write The Rusted Anchor (sub-location)**

`context/locations/towns/the-rusted-anchor.md`:

```markdown
---
name: The Rusted Anchor
type: tavern
region: iron-reach
parent_location: hollowgate
tags: [tavern, hollowgate, ally-base]
---

# The Rusted Anchor

## Description
Two-story stone-and-timber tavern in the Hollow district. The "Anchor" of the name is a literal rusted ship's anchor mounted above the door — nobody remembers why. Warm, low-beamed common room. Private booths along the back wall. Mira lives upstairs with her niece.

## Who's there
- **Mira** — the owner. Always around at night.
- **Halt** — the bouncer, ex-Watch, doesn't talk much.
- **Fenna** — Mira's niece, 17, runs food.
- **Regulars** — a rotating cast of miners, off-duty watchmen, low-tier Guild scribes, the occasional caravan crew.

## Why the party comes here
- It's their unofficial HQ in Hollowgate (since s2).
- Mira lets them stay on the cuff when broke (currently owe her 8gp).
- She's their best information broker.

## Notable details
- Back booth (third from the left) is where she takes "private" conversations.
- The cellar door behind the bar — she's never let the party down there. They've never asked why.

<!-- last updated: s17 -->
```

- [ ] **Step 3: Write Sewers East (dungeon)**

`context/locations/dungeons/sewers-east.md`:

```markdown
---
name: Sewers East
type: dungeon
region: iron-reach
parent_location: hollowgate
status: party-planning-to-enter-s19
tier: 1
tags: [dungeon, hollowgate, cult-presence-suspected]
---

# Sewers East (under Hollowgate)

## Overview
The eastern wing of Hollowgate's underground sewer system. Built atop older mine shafts that predate the town. Damp, cold, smells like you'd expect. The party has reason to suspect a Silent Flame safehouse is hidden in here (per Mira's information, s17).

## Layout (DM-known; party hasn't entered)

### Entry
- Manhole behind the East Watch House. Brenna knows it exists. Party has the cover key.
- Drops 12 feet to a maintenance ledge.

### Main shaft
- Runs east under the East District for ~600 feet.
- Six side passages branch off — most are dead ends or active sewer flow.

### The fork (decision point)
- 400 feet in, the shaft splits. Left passage: collapsed in YoI 832 (officially). Right: continues to the river outflow.
- The "collapse" is fake — clearable in 10 minutes. Hides the cult passage.

### Cult chamber (the goal, if party finds it)
- Small octagonal stone chamber, predates the sewer system.
- 2-4 Wicks usually present (per Mira's intel).
- A locked iron door on the east wall — leads somewhere unmapped.

## Hazards
- **Sewer slime** in standing pools (CR 1/4 each, 2-3 patches).
- **Bad air pockets** in the older sections (Con save DC 11 to avoid 1 level of exhaustion).
- **The fake collapse** — finding it requires Investigation 14 or following someone in.

## Encounters (suggested)
- 1 patrol of 2 Wicks (use cultist statblock) and 1 Ember (use commoner with 1 extra HD).
- Optional: rival smugglers if the party is loud.

<!-- last updated: s18 -->
```

- [ ] **Step 4: Write The Black Crag (wilderness)**

`context/locations/wilderness/the-black-crag.md`:

```markdown
---
name: The Black Crag
type: wilderness
region: iron-reach
parent_location: none
tier: 1-2
tags: [wilderness, iron-reach, caravan-route]
---

# The Black Crag

## Overview
A jagged ridge of dark volcanic stone running north-south, three days' ride north of Hollowgate. The Black Crag Road is the only viable trade route between Hollowgate and the northern holds. Three caravans have vanished here in the last year.

## Terrain
- Narrow switchback road clinging to the western slope.
- Pine forest on the lower slopes; bare stone above.
- Cold even in summer. Snow on the upper passes year-round.

## Notable points
- **The Cairn Pass** — the road's high point. Old burial cairns, said to be from the Quiet War.
- **The Watcher's Tower** — abandoned Guild waystation halfway up. Roofless, useful as shelter.
- **The Wreck** (s16) — where the party found the missing caravan. Three days' ride from Hollowgate, just past the Cairn Pass.

## Inhabitants
- Wolves (not unusual, common encounters).
- Brigands — a small ring works the upper switchbacks (see encounter table).
- Smugglers — Verros's people. They know the side trails.
- Whatever runs the Silent Flame's operations up here. Unknown.

## Encounters
- See `context/tables/encounters-iron-reach-tier1.md` for the rolling table.

<!-- last updated: s18 -->
```

- [ ] **Step 5: Verify locations**

Run: `find context/locations -name '*.md' -not -name '_INDEX.md' | sort`
Expected: 4 location files in their respective subfolders.

- [ ] **Step 6: Commit**

```bash
git add context/locations/towns/*.md context/locations/dungeons/*.md context/locations/wilderness/*.md
git commit -m "Add location seed: Hollowgate, Rusted Anchor, Sewers East, Black Crag"
```

---

## Task 9: Quest files (3 quests)

**Files:**
- Create: `context/quests/the-missing-caravan.md`, `context/quests/cult-of-the-silent-flame.md`, `context/quests/the-stolen-bow.md`

- [ ] **Step 1: Write the active investigation quest**

`context/quests/the-missing-caravan.md`:

```markdown
---
title: The Missing Caravan
status: active
tier: 1
related_npcs: [lord-verros, tavernkeep-mira, sergeant-brenna]
related_locations: [the-black-crag, hollowgate]
opened: s14
last_touched: s18
tags: [active, iron-reach, ties-to-cult]
---

# The Missing Caravan

## Hook
Factor Renn (Merchant Guild) posted a 200gp bounty for information on the third missing caravan of the year. Party took it in s14.

## What's known to the party
- The caravan was Guild-registered, carrying iron and silver (s14).
- They tracked the route in s15 and found nothing.
- In s16 they found the wreckage in the Black Crag, three days north — and a cult symbol painted in dried blood inside one of the wagons.
- In s17 Mira confirmed the symbol matches a cult called the Silent Flame.
- In s18 they found Verros's smuggler brand on a recovered crate. They suspect Verros raided the caravan and the cult was involved somehow.

## What's actually going on (DM-only)
The caravan was raided by Verros's people for the cult's funding. The cult symbol was left intentionally — Verros is testing whether anyone in Hollowgate can read it.

## Open threads
- Tell the Guild what they've found? (party hasn't decided)
- Confront Verros directly? (would be very dangerous at level 3)
- Follow the cult lead through Sewers East? (planned for s19)

## Bounty
- 200gp on completion (Guild).
- Mira would owe them another favor if they take Verros down quietly.

<!-- last updated: s18 -->
```

- [ ] **Step 2: Write the slow-burn cult quest**

`context/quests/cult-of-the-silent-flame.md`:

```markdown
---
title: Cult of the Silent Flame
status: active
tier: 1-3 (will scale)
related_npcs: [lord-verros, high-priest-aldon, tavernkeep-mira]
related_locations: [silent-coast, hollowgate, the-black-crag]
opened: s11
last_touched: s18
tags: [active, campaign-arc, silent-flame]
---

# Cult of the Silent Flame

## Hook
A Silent Coast survivor in s11 mentioned the name "Aldon" in connection with a cult that "takes your memories." The party filed it; it became urgent again in s16 when the cult symbol turned up on the caravan.

## What's known to the party
- Cult exists; calls themselves the Silent Flame.
- Symbol: inverted candle with black flame.
- Active in Silent Coast and (recently) Iron Reach.
- A figure named "Aldon" or "High Priest Aldon" leads it.
- Recruits are docile and forgetful afterward (per the Silent Coast survivor).
- Mira is now quietly investigating on their behalf.

## What's actually going on (DM-only)
See `context/world/factions/silent-flame.md` for the full picture. Short version: the cult worships something that erases identity. The party will need to climb the tier ladder (Embers → Wicks → Lit → Aldon) over the campaign.

## Current situation
- Mira's quiet asking-around will produce 1-2 leads by s20.
- The Sewers East safehouse (planned s19) is the next step on the Wick tier.

## Long arc
This is the campaign's central thread. Resolution is many sessions away.

<!-- last updated: s18 -->
```

- [ ] **Step 3: Write the dormant PC-personal quest**

`context/quests/the-stolen-bow.md`:

```markdown
---
title: The Stolen Bow (Kira's brother)
status: dormant
tier: 1
related_npcs: []
related_locations: []
related_pcs: [kira]
opened: s1
last_touched: s9
tags: [dormant, pc-hook, kira]
---

# The Stolen Bow

## Hook
Kira's backstory: her older brother **Vael** disappeared two years ago after writing a letter saying he'd "found something worth dying for in the east." Kira's elven longbow (a family heirloom) went with him. Kira has been looking for him on and off.

## What's known
- Vael was last confirmed in a Silent Coast village in YoI 845.
- A trader in s9 said he'd seen "an elf carrying a fine bow" pass through Hollowgate that summer. Lead went cold.

## DM-only / planned reveal
Vael was an early Silent Flame convert and is now an Ember somewhere in Iron Reach. The bow was sold; it's currently in a Stonecradle collector's house. (Foreshadowed but not yet hit.)

## Status
Dormant since s9. Will reactivate once the cult investigation produces a "missing converts" lead.

<!-- last updated: s9 -->
```

- [ ] **Step 4: Verify quests**

Run: `ls -1 context/quests/*.md`
Expected: 3 quest files + `_INDEX.md`.

Run: `grep -l "^status: active" context/quests/*.md | wc -l`
Expected: `2`.

- [ ] **Step 5: Commit**

```bash
git add context/quests/*.md
git commit -m "Add quest seed: missing caravan (active), cult arc (active), stolen bow (dormant)"
```

---

## Task 10: PC files (4 PCs)

**Files:**
- Create: `context/pcs/kira.md`, `context/pcs/brand.md`, `context/pcs/mira-sage.md`, `context/pcs/thorn.md`

- [ ] **Step 1: Write Kira (ranger)**

`context/pcs/kira.md`:

```markdown
---
name: Kira
class: ranger
race: elf
level: 3
player: PLAYER-1
arc_state: searching-for-brother (currently dormant lead)
hooks_active: [the-stolen-bow]
hooks_resolved: []
tags: [pc, ranger, elf, kira]
---

# Kira

## Quick stats
Ranger 3, AC 15, HP 27. Longbow + shortswords. Favored Enemy: humanoids. Favored Terrain: forest.

## Personality
Quiet, watchful, unsentimental. Speaks Elvish to herself when stressed. Trusts Brand more than the rest of the party.

## Backstory hook
Brother **Vael** missing two years (see `context/quests/the-stolen-bow.md`). Carries a notebook with his last letter copied in.

## Arc state
Currently dormant — last lead went cold in s9. Player has hinted they want this back on the table eventually. Plant a "missing converts" lead through the cult investigation.

## Things she'd do that surprise the table
- Spare an enemy who reminds her of Vael.
- Push HARD on any clue about the Silent Coast.

<!-- last updated: prep -->
```

- [ ] **Step 2: Write Brand (fighter)**

`context/pcs/brand.md`:

```markdown
---
name: Brand
class: fighter
race: human
level: 3
player: PLAYER-2
arc_state: looking-for-purpose
hooks_active: [ex-soldier-guild-connections]
hooks_resolved: [first-mentor-revealed-s11]
tags: [pc, fighter, human, brand]
---

# Brand

## Quick stats
Fighter 3 (Battle Master), AC 18, HP 30. Longsword + shield. Maneuvers: Trip Attack, Riposte, Disarming Attack.

## Personality
Steady, quiet competence. Old soldier. Tries to mediate when the party argues. Drinks too much when off-duty.

## Backstory hook
Ex-Guild caravan-marshal (5 years out). Knows the system from inside. Lost his squad to brigands in YoI 843; carries that.

## Arc state
Looking for something worth being good at again. The cult investigation is starting to fill that hole.

## Things he'd do that surprise the table
- Refuse to leave a wounded ally even at huge cost.
- Take a Guild offer the party should be skeptical of, just to feel useful.

<!-- last updated: prep -->
```

- [ ] **Step 3: Write Mira-sage (wizard) — note name disambiguates from Tavernkeep Mira**

`context/pcs/mira-sage.md`:

```markdown
---
name: Mira (the sage; tagged "Mira-sage" to distinguish from Tavernkeep Mira)
class: wizard
race: half-elf
level: 3
player: PLAYER-3
arc_state: chasing-the-real-history
hooks_active: [forbidden-knowledge, family-name-erased]
hooks_resolved: []
tags: [pc, wizard, half-elf, mira-sage]
---

# Mira (sage)

## Quick stats
Wizard 3 (School of Divination), AC 12, HP 18. Spells prepared: Detect Magic, Identify, Mage Armor, Magic Missile, Misty Step, Suggestion, plus 2 cantrips.

## Personality
Eager, a bit too eager. Asks NPCs questions other party members consider rude. Keeps a research journal.

## Backstory hook
Family name was struck from a noble register two generations ago for reasons no one will tell her. She's been digging through libraries for years.

## Arc state
The cult's "memory erasure" angle is uncomfortably close to her family mystery. Player hasn't said this out loud yet but has been steering toward it.

## Things she'd do that surprise the table
- Bargain with a captured cultist for "just one question" the party would rather not ask.
- Steal a book from the Guild library if she could get away with it.

<!-- last updated: prep -->
```

- [ ] **Step 4: Write Thorn (rogue)**

`context/pcs/thorn.md`:

```markdown
---
name: Thorn
class: rogue
race: halfling
level: 3
player: PLAYER-4
arc_state: enjoying-the-ride
hooks_active: [thieves-guild-old-debt]
hooks_resolved: []
tags: [pc, rogue, halfling, thorn]
---

# Thorn

## Quick stats
Rogue 3 (Thief), AC 14, HP 22. Shortsword + daggers + shortbow. Sneak Attack 2d6.

## Personality
Charming chaos goblin. Picks pockets for fun. Genuinely loyal to the party.

## Backstory hook
Owes a real debt to a thieves' guild in Aurelle (Goldlands). Has been outrunning it for two years; they don't yet know she's in Hollowgate.

## Arc state
Mostly along for the ride and the loot. Player likes it that way. The Aurelle debt will catch up eventually — not soon.

## Things she'd do that surprise the table
- Refuse a job that involves robbing a working family (lines in the sand).
- Quietly slip a useful item into Mira-sage's pocket because she likes her.

<!-- last updated: prep -->
```

- [ ] **Step 5: Verify PCs**

Run: `ls -1 context/pcs/*.md`
Expected: 4 PC files + `_INDEX.md`.

Run: `grep -c "^class:" context/pcs/kira.md context/pcs/brand.md context/pcs/mira-sage.md context/pcs/thorn.md`
Expected: each file shows `1`.

- [ ] **Step 6: Commit**

```bash
git add context/pcs/*.md
git commit -m "Add PC seed: Kira (ranger), Brand (fighter), Mira-sage (wizard), Thorn (rogue)"
```

---

## Task 11: Random tables (2 tables)

**Files:**
- Create: `context/tables/encounters-iron-reach-tier1.md`, `context/tables/tavern-events.md`

- [ ] **Step 1: Write the encounter table**

`context/tables/encounters-iron-reach-tier1.md`:

```markdown
---
type: encounter-table
region: iron-reach
tier: 1
intended_for: live/random-encounter skill
tags: [iron-reach, tier1, encounter-table]
---

# Iron Reach — Tier 1 Encounters

Roll d12. Bias toward the Black Crag wilderness; the dungeon entries can be remixed for Sewers East.

| Roll | Encounter | Notes |
|------|-----------|-------|
| 1 | 2d4 wolves | Hungry, pack tactics. Will retreat below half. |
| 2 | 1 brown bear | Defending a kill. Avoidable with stealth or food. |
| 3 | 1d4+1 brigands | Want coin and weapons. Will surrender if outmatched. |
| 4 | 1 Verros smuggler scout (spy stat) + 1d3 thugs | Doesn't want a fight. Will try to slip away to warn. |
| 5 | Lone trapper | Friendly, info on local wildlife (and a rumor: roll once on tavern-events). |
| 6 | Ruined wagon (no people) | Loot: 2d10gp + a clue if you're feeling generous. |
| 7 | Cairn pass shrine | Old. Korren's symbol. Religion DC 12 to recall the Quiet War. |
| 8 | 1 Wick + 2 Embers (cultist + 2 commoners) | If the party isn't expecting cult presence yet, hide their nature. |
| 9 | Heavy snow / fog (encounter-as-weather) | Visibility 30 ft. Survival DC 12 to stay on path. |
| 10 | A small caravan, friendly | Trade, gossip, possible escort job for tier 2. |
| 11 | 2 Hollowgate watchmen, off-duty | Could be friendly (Brenna's) or corrupt (Verros's). DM choice. |
| 12 | A single elf, lost | If the party asks the right questions, this is a Vael lead. Use sparingly. |

## How to use
- The `live/random-encounter` skill rolls d12 and reports just the encounter line + 1 short flavor note.
- The `prep/encounters` skill picks intentionally and writes a full encounter file.

<!-- last updated: prep -->
```

- [ ] **Step 2: Write the tavern events table**

`context/tables/tavern-events.md`:

```markdown
---
type: event-table
region: any (defaults to Iron Reach flavor)
tier: any
intended_for: live skills, scene-flavor
tags: [tavern, scene-flavor]
---

# Tavern Events — d10

Use whenever the party enters a tavern and you want a vibe beyond "it's a tavern."

| Roll | Event |
|------|-------|
| 1 | A drunk is being thrown out by the bouncer. He's shouting about being cheated at dice. |
| 2 | Two off-duty watchmen are arguing quietly in a corner. They go silent when the party enters. |
| 3 | A lone bard is failing badly. Locals are politely ignoring her. She's actually a decent information source. |
| 4 | A merchant is paying out a generous round to celebrate a sale. He'll talk about anything. |
| 5 | Someone the party recognizes (DM choice) is here, badly trying not to be recognized. |
| 6 | Fight in the back. 1d4 rounds. Bouncer breaks it up unless the party intervenes. |
| 7 | A child is asleep under a table near the fire. Nobody is watching her. |
| 8 | A traveling priest of Vesna is offering a hearth-blessing for a copper. Genuine. |
| 9 | A guard is reading a wanted poster aloud. The party recognizes the name (DM choice — Verros associate, ideally). |
| 10 | Quiet night. Just the regulars. Mira / barkeep gives the party a rumor on the house. |

<!-- last updated: prep -->
```

- [ ] **Step 3: Verify tables**

Run: `ls -1 context/tables/*.md`
Expected: 2 tables + `_INDEX.md`.

- [ ] **Step 4: Commit**

```bash
git add context/tables/*.md
git commit -m "Add random tables: Iron Reach tier 1 encounters, tavern events"
```

---

## Task 12: Populate all `_INDEX.md` files

**Files:**
- Modify: `context/world/_INDEX.md`, `context/world/factions/_INDEX.md`, `context/npcs/_INDEX.md`, `context/locations/_INDEX.md`, `context/quests/_INDEX.md`, `context/pcs/_INDEX.md`, `context/tables/_INDEX.md`

(`sessions/_INDEX.md` is populated in Task 13.)

- [ ] **Step 1: World index**

Overwrite `context/world/_INDEX.md`:

```markdown
# World Bible Index

| File | One-liner | Tags | Last touched |
|------|-----------|------|--------------|
| geography.md | Continent of Velara: Iron Reach (current), Silent Coast, Goldlands, Burnt Wastes | geography | prep |
| history.md | Old Kingdoms → Quiet War (YoI 612) → Long Peace → The Stirring (current) | history | prep |
| pantheon.md | The Six (Korren, Vesna, Talen, Pale Lady, Drenn, Sela) + heretical Silent Flame | pantheon | prep |
| factions/ | See factions/_INDEX.md | factions | s18 |
```

- [ ] **Step 2: Factions index**

Overwrite `context/world/factions/_INDEX.md`:

```markdown
# Factions Index

| File | One-liner | Tags | Last touched |
|------|-----------|------|--------------|
| silent-flame.md | Cult that erases memory; antagonist; spreading from Silent Coast into Iron Reach | cult, antagonist, silent-flame | s18 |
| iron-reach-merchant-guild.md | De facto government of the Iron Reach; Guild of merchants and Factors | guild, ally, iron-reach | s18 |
```

- [ ] **Step 3: NPCs index**

Overwrite `context/npcs/_INDEX.md`:

```markdown
# NPCs Index

| File | One-liner | Tags | Last touched |
|------|-----------|------|--------------|
| lord-verros.md | Smuggler-king of Iron Reach, secretly Silent Flame Wick (or higher) | iron-reach, antagonist, smuggler, silent-flame | s18 |
| tavernkeep-mira.md | Owner of the Rusted Anchor in Hollowgate; ally; quiet info network | iron-reach, ally, hollowgate, information-broker | s17 |
| high-priest-aldon.md | Unseen leader of the Silent Flame; name-only so far | silent-flame, antagonist, off-screen | s16 |
| sergeant-brenna.md | Hollowgate Watch sergeant (East); honest by Iron Reach standards | iron-reach, neutral, watch, hollowgate | s17 |
```

- [ ] **Step 4: Locations index**

Overwrite `context/locations/_INDEX.md`:

```markdown
# Locations Index

| File | One-liner | Tags | Last touched |
|------|-----------|------|--------------|
| towns/hollowgate.md | Fortified mining town in the Iron Reach; party's current base | town, iron-reach, current-base | s17 |
| towns/the-rusted-anchor.md | Tavern in Hollowgate; Mira's; party's unofficial HQ | tavern, hollowgate, ally-base | s17 |
| dungeons/sewers-east.md | Sewers under Hollowgate's East District; suspected cult safehouse | dungeon, hollowgate, cult-presence-suspected | s18 |
| wilderness/the-black-crag.md | Volcanic ridge north of Hollowgate; caravan route; site of the wreck | wilderness, iron-reach, caravan-route | s18 |
```

- [ ] **Step 5: Quests index**

Overwrite `context/quests/_INDEX.md`:

```markdown
# Quests Index

| File | One-liner | Status | Tags | Last touched |
|------|-----------|--------|------|--------------|
| the-missing-caravan.md | Track the third missing caravan; ties to Verros and the cult | active | active, iron-reach, ties-to-cult | s18 |
| cult-of-the-silent-flame.md | Long-arc investigation of the cult; campaign central thread | active | active, campaign-arc, silent-flame | s18 |
| the-stolen-bow.md | Kira's missing brother Vael; lead currently cold | dormant | dormant, pc-hook, kira | s9 |
```

- [ ] **Step 6: PCs index**

Overwrite `context/pcs/_INDEX.md`:

```markdown
# PCs Index

| File | One-liner | Player | Last touched |
|------|-----------|--------|--------------|
| kira.md | Elf ranger 3; brother Vael missing; quiet, watchful | PLAYER-1 | prep |
| brand.md | Human fighter 3 (Battle Master); ex-Guild caravan-marshal | PLAYER-2 | prep |
| mira-sage.md | Half-elf wizard 3 (Divination); chasing erased family history | PLAYER-3 | prep |
| thorn.md | Halfling rogue 3 (Thief); old Aurelle thieves'-guild debt looming | PLAYER-4 | prep |
```

- [ ] **Step 7: Tables index**

Overwrite `context/tables/_INDEX.md`:

```markdown
# Tables Index

| File | Purpose | Tags |
|------|---------|------|
| encounters-iron-reach-tier1.md | d12 random encounter table for Iron Reach wilderness/dungeon at tier 1 | iron-reach, tier1, encounter-table |
| tavern-events.md | d10 tavern scene-flavor table | tavern, scene-flavor |
```

- [ ] **Step 8: Verify all indexes are non-empty and contain real rows**

Run: `wc -l context/world/_INDEX.md context/world/factions/_INDEX.md context/npcs/_INDEX.md context/locations/_INDEX.md context/quests/_INDEX.md context/pcs/_INDEX.md context/tables/_INDEX.md`
Expected: every file has at least 5 lines (header + table header + ≥1 row).

- [ ] **Step 9: Commit**

```bash
git add context/world/_INDEX.md context/world/factions/_INDEX.md context/npcs/_INDEX.md context/locations/_INDEX.md context/quests/_INDEX.md context/pcs/_INDEX.md context/tables/_INDEX.md
git commit -m "Populate _INDEX.md tables for all context folders"
```

---

## Task 13: Session files (3 completed + 1 prep) and sessions index

**Files:**
- Create: `sessions/016-the-cult-symbol.md`, `sessions/017-asking-around-hollowgate.md`, `sessions/018-the-caravan-hunt.md`, `sessions/019-prep.md`
- Modify: `sessions/_INDEX.md`

- [ ] **Step 1: Session 016**

`sessions/016-the-cult-symbol.md`:

```markdown
---
session: 16
date: 2026-04-04
pcs_present: [kira, brand, mira-sage, thorn]
locations_visited: [the-black-crag]
npcs_appeared: []
quests_touched: [the-missing-caravan]
---

## Raw notes
Three days into the Black Crag tracking the caravan. Hit snow on day 2, lost half a day. Day 3 morning found the wreckage in a draw off the road, just past the Cairn Pass. Wagons burned. Two bodies, one driver one guard, both stripped. Mira-sage Detect Magic'd the site, faint abjuration on the lead wagon's iron rim — odd. Brand spotted painted symbol inside the lead wagon: inverted candle, black flame, painted in dried blood. Nobody recognized it. Thorn pocketed the driver's ledger (water-damaged but legible). Kira found a single set of boot prints leading away east — 1 person walked out of here.

## Recap
The party reached the wrecked caravan after three hard days in the Black Crag. The cargo was stripped, two bodies left where they fell. Inside the lead wagon Brand spotted a strange symbol — an inverted candle with a black flame, painted in dried blood. The driver's ledger came back with them. Kira's tracking suggested one person walked away from the scene heading east, alone.

## State deltas
- quest:the-missing-caravan → status remains active; new evidence: cult symbol + ledger
- quest:cult-of-the-silent-flame → reactivated (was dormant since s11); tied to the caravan
- location:the-black-crag → mark "the wreck" location

<!-- last updated: s16 -->
```

- [ ] **Step 2: Session 017**

`sessions/017-asking-around-hollowgate.md`:

```markdown
---
session: 17
date: 2026-04-11
pcs_present: [kira, brand, mira-sage, thorn]
locations_visited: [hollowgate, the-rusted-anchor]
npcs_appeared: [tavernkeep-mira, sergeant-brenna]
quests_touched: [the-missing-caravan, cult-of-the-silent-flame]
---

## Raw notes
Back to Hollowgate, a day's faster ride than out. Spent two days in town. Showed Mira the symbol — she went quiet, told them to come back at midnight. At midnight she said the symbol matches a cult called the Silent Flame, that an elf named Aldon leads it (matched what they heard in s11). She offered to ask around. Mira-sage spent the second day at the Guild scribe's office cross-referencing Black Crag manifests; found two prior caravans had similar Verros-route timing. Brand chatted with Brenna in the Watch House — Brenna asked what they knew about the symbol; Mira had asked Brenna a question. Brenna offered nothing herself but seemed to be measuring them. Thorn picked Verros's manor steward's pocket on a whim (3sp, a wax seal). Mira-sage Identified the wax — it's Verros's personal seal, valid for low-level smuggler correspondence.

## Recap
The party returned to Hollowgate to puzzle out the symbol. Mira recognized it: the Silent Flame, a cult led by a figure called Aldon. Mira agreed to ask around quietly. Mira-sage's research at the Guild scribe's office turned up two prior caravans on the Verros smuggling route. Brand had a careful conversation with Sergeant Brenna, who's also clearly heard something. Thorn lifted Verros's personal seal off his steward.

## State deltas
- npc:tavernkeep-mira → quietly investigating cult on the party's behalf
- npc:sergeant-brenna → "measuring" — neutral but knows something is up
- npc:lord-verros → confirmed link to missing caravans (party's deduction, not yet proven to Guild)
- quest:cult-of-the-silent-flame → status active; Mira investigating
- party-inventory → +Verros's wax seal (Thorn)

<!-- last updated: s17 -->
```

- [ ] **Step 3: Session 018**

`sessions/018-the-caravan-hunt.md`:

```markdown
---
session: 18
date: 2026-04-18
pcs_present: [kira, brand, mira-sage, thorn]
locations_visited: [the-black-crag, hollowgate, the-rusted-anchor]
npcs_appeared: [tavernkeep-mira]
quests_touched: [the-missing-caravan, cult-of-the-silent-flame]
---

## Raw notes
Returned to the Black Crag for a closer look at the wreck site. Wolves on day 2 (rolled #1 — chased them off, no damage). At the wreck, Kira found one crate they'd missed first time, half-buried. Inside: silver bars stamped with Verros's smuggler brand. The cult symbol was painted on the inside of the crate lid, fresh-looking. Mira-sage Detect Magic'd the bars — clean. They brought a bar back. Mira saw the brand and confirmed it's Verros's. She told them she's been asked by an East District tinker if his apprentice has been to the Rusted Anchor — the apprentice has been "different" for two weeks, and the apprentice goes to Sewers East at night. That's the lead. Mira said she'll get them the manhole key from a friend at the Watch.

## Recap
A second visit to the wreck site turned up a buried crate of silver bars stamped with Lord Verros's smuggler brand, with a fresh cult symbol painted inside the lid. The case against Verros tightened. Back in Hollowgate, Mira shared a new lead: an East District tinker's apprentice has been "different" for two weeks and visits Sewers East at night. The party intends to follow the apprentice next session.

## State deltas
- npc:lord-verros → status: hostile (was: wary); evidence is now physical, not just deduction
- quest:the-missing-caravan → new lead: cult-Verros physical proof (crate)
- quest:cult-of-the-silent-flame → new lead: tinker's apprentice + Sewers East
- world:silent-flame → revealed: cult operates in Iron Reach (was: rumor only); upgrade in faction file
- party-inventory → +1 silver bar (Verros-branded)

<!-- last updated: s18 -->
```

- [ ] **Step 4: Session 019 prep doc**

`sessions/019-prep.md`:

```markdown
---
session: 19
date: 2026-04-25
status: prep
expected_locations: [hollowgate, sewers-east]
expected_npcs: [tavernkeep-mira, possibly: tinker, possibly: apprentice, cult-patrol]
quests_touched: [cult-of-the-silent-flame, the-missing-caravan]
---

## Goal of the session
Get the party into Sewers East and let them find (or fail to find) the cult chamber. First time they fight or face Wicks directly.

## Expected beats
1. Open at the Rusted Anchor. Mira hands over the manhole key + intel.
2. Optional: stake out the apprentice. Roll Stealth/Insight.
3. Descent into Sewers East — see `context/locations/dungeons/sewers-east.md`.
4. The fork (decision point): figure out the false collapse.
5. Cult chamber encounter — 1 Wick + 2 Embers (use cultist + commoner stats).
6. Either escape with intel or get caught.

## Contingencies
- If they go LOUD: rival smugglers from the table (#4) join in.
- If they refuse the dungeon and confront Verros directly: NOT a level-3 party fight. Mira will warn them off; if they push, dramatic consequence-not-combat.
- If they spend too long preparing in town: Mira gets attacked by a Wick that night to put them on the clock.

## Open questions to be ready for
- "Can we tell the Guild?" → Yes, but slow; Renn would want proof; Verros would notice.
- "Can we use the seal Thorn lifted in s17?" → A forged note carries a Wick or two but won't fool Verros himself.
- "What does the apprentice know?" → Ember-tier: knows safehouse exists, doesn't know what it's for.

## PC hooks to maybe touch
- Mira-sage might recognize cult symbology language (she's been reading).
- Kira: if any cultist looks elven, hesitate — possible Vael lead.

<!-- last updated: prep -->
```

- [ ] **Step 5: Populate `sessions/_INDEX.md`**

Overwrite `sessions/_INDEX.md`:

```markdown
# Sessions Index

| # | Date | Headline | PCs present | Locations | NPCs | Quests touched |
|---|------|----------|-------------|-----------|------|----------------|
| 016 | 2026-04-04 | Found the wrecked caravan and the cult symbol | kira, brand, mira-sage, thorn | the-black-crag | — | the-missing-caravan |
| 017 | 2026-04-11 | Mira IDs the symbol; Brenna is watching; Verros's seal lifted | kira, brand, mira-sage, thorn | hollowgate, the-rusted-anchor | tavernkeep-mira, sergeant-brenna | the-missing-caravan, cult-of-the-silent-flame |
| 018 | 2026-04-18 | Verros-branded silver crate with cult symbol; Sewers East lead | kira, brand, mira-sage, thorn | the-black-crag, hollowgate, the-rusted-anchor | tavernkeep-mira | the-missing-caravan, cult-of-the-silent-flame |
| 019 | 2026-04-25 | (PREP) Sewers East descent | — | hollowgate, sewers-east | (planned) | cult-of-the-silent-flame |
```

- [ ] **Step 6: Verify sessions**

Run: `ls -1 sessions/*.md`
Expected: 4 session files + `_INDEX.md`.

Run: `grep -c "## Raw notes" sessions/016-*.md sessions/017-*.md sessions/018-*.md`
Expected: each shows `1`.

- [ ] **Step 7: Commit**

```bash
git add sessions/
git commit -m "Add session seed: 3 completed sessions (16-18) + session 19 prep doc"
```

---

## Task 14: Prep skill — `npcs`

**Files:**
- Create: `skills/prep/npcs/SKILL.md`

- [ ] **Step 1: Write the skill**

`skills/prep/npcs/SKILL.md`:

```markdown
---
name: npcs
description: Use when CREATING a new NPC, deeply UPDATING an NPC after a session, or researching what an NPC KNOWS about a topic. Reads context/npcs/_INDEX.md first, then drills in. Writes to context/npcs/<slug>.md and updates the index, after proposing the changes for user approval. NOT for at-the-table improvisation — use the live/improvise-npc skill instead.
---

# NPCs (prep skill)

## When to use
- "Create an NPC for <role/location>" — produces a new file with full sections.
- "Update <NPC> after session NN" — modifies frontmatter, appends history, may change status.
- "What does <NPC> know about <topic>?" — read-only, cross-references quests/, sessions/, world/.
- "Who in <region/faction> would know about <topic>?" — queries the index by tag, then drills in.

## When NOT to use
- The user is at the table and needs an NPC right now. Use `live/improvise-npc`.
- The user wants pure rules, statblocks, or combat tuning. Use `live/5e-rules` or `prep/encounters`.

## Inputs
- The user's request (what kind of NPC, what update, what query).
- `context/npcs/_INDEX.md` (always read first).
- `context/campaign.md` (for tone).
- The specific NPC file (for updates and "knows" queries).
- For "knows about" queries: relevant `context/quests/<slug>.md`, `context/world/factions/<slug>.md`, and matching `sessions/NNN-*.md`.

## Workflow

### Creating an NPC
1. Read `context/npcs/_INDEX.md` to avoid name collisions.
2. Read `context/campaign.md` and the relevant location file (where the NPC lives) for tone.
3. Draft the file with required sections (see "Output conventions").
4. **Propose** to the user: file path, frontmatter, section outline. Wait for approval.
5. On approval: write the file. Add the `<!-- last updated: sNN -->` footer (use `prep` if between sessions).
6. Update `context/npcs/_INDEX.md` with the new row.

### Updating an NPC after a session
1. Read the session file's "State deltas" section for the relevant `npc:<slug>` lines.
2. Read the existing NPC file.
3. Compute the diff (frontmatter changes; new "History" entry; possibly updated Secrets / Knows About).
4. **Propose** the diff to the user. Wait for approval.
5. On approval: write changes; update the footer; update the index's "Last touched" column.

### "What does X know about Y?"
1. Read the NPC file.
2. Grep `context/quests/_INDEX.md` and `context/world/factions/_INDEX.md` for related entities.
3. Read matching session State deltas (search by NPC slug).
4. Synthesize the answer into 3 categories: KNOWS (canon), SUSPECTS (inference), DOESN'T KNOW (gaps to be aware of).
5. NO file writes for queries.

## Output conventions

NPC files have these sections in this order:
1. Frontmatter (name, race, location, faction, status, tags, first_appeared, last_seen)
2. `## Description` — physical, 2-3 sentences
3. `## Voice` — speech pattern, 1-2 sentences (REQUIRED)
4. `## Motivations` — numbered list, 1-3 items
5. `## Secrets` — bulleted, each tagged with `(known: party | NPC | none)`
6. `## Knows about` — bulleted, what canon facts the NPC has
7. `## History` — bulleted, sNN-tagged appearances and changes
8. Footer: `<!-- last updated: sNN -->`

If a stat block is needed, add `## Stats` before History. Use 5e SRD references where possible.

## Update rules
- Always update `context/npcs/_INDEX.md` when writing a file.
- Always update the file's `<!-- last updated: sNN -->` footer.
- When status changes (e.g., wary → hostile), preserve the previous value in the History section ("s18: status wary → hostile").
```

- [ ] **Step 2: Verify the skill file**

Run: `grep -c "^name: npcs$" skills/prep/npcs/SKILL.md && grep -c "^description:" skills/prep/npcs/SKILL.md`
Expected: each `1`.

Run: `grep -c "Propose" skills/prep/npcs/SKILL.md`
Expected: `≥ 2` (mentioned multiple times — propose-first is core).

- [ ] **Step 3: Commit**

```bash
git add skills/prep/npcs/SKILL.md
git commit -m "Add prep skill: npcs (create, update, who-knows-what)"
```

---

## Task 15: Prep skill — `encounters`

**Files:**
- Create: `skills/prep/encounters/SKILL.md`

- [ ] **Step 1: Write the skill**

`skills/prep/encounters/SKILL.md`:

```markdown
---
name: encounters
description: Use when DESIGNING a balanced 5e encounter, generating treasure/loot, or designing puzzles and traps for a planned session. Reads party context (PCs, level), location, and tier. Produces a structured encounter document. Does NOT replace random rolls at the table — use live/random-encounter for that, or live/adjust-encounter for mid-fight tuning.
---

# Encounters (prep skill)

## When to use
- "Design an encounter for the party at <location>" — full balanced encounter.
- "Generate a hoard for a CR <N> encounter" — treasure roll-up.
- "I need a puzzle for <location>" — solvable, multi-path puzzle.
- "Design a trap for <location>" — mechanically described trap with detection / disable / damage.

## When NOT to use
- At the table. Use live skills.
- Designing the entire dungeon's encounter set. Do them one at a time; coherence is your job, not the skill's.

## Inputs
- Party composition: `context/pcs/_INDEX.md` then individual PC files.
- Location file (for terrain, theme).
- House rules: `context/house-rules.md` (e.g., crit rules affect encounter math slightly).
- Optional: `context/tables/encounters-<region>-tier<N>.md` for thematic flavor.

## Workflow

### Designing an encounter
1. Read PC index → get party level and class composition.
2. Read the location file for terrain, lighting, escape routes, themed enemies.
3. Compute encounter difficulty target (DMG XP budget for the party level). Show the math in your output.
4. Propose 1-3 encounter compositions (e.g., "A) 1 elite + 2 minions, B) 4 medium-tier all of one type, C) ambush from environment").
5. On user pick, write the full encounter into `sessions/NNN-prep.md` (under an "Encounters" section) OR a freestanding scratch file the user names. **Propose first; never write silently.**
6. Include: enemy stats reference, terrain notes, tactics, scaling notes (what to do if party is doing too well or too poorly).

### Generating treasure
1. Read party level and the encounter's CR.
2. Use DMG hoard tables OR a custom roll appropriate to the campaign's low-magic tone.
3. Propose; on approval, write into the prep doc.

### Designing a puzzle
1. Puzzle MUST have at least 2 valid solutions (or 1 solution + 1 escape valve).
2. Propose with: setup, what the players see, mechanism, all valid solutions, what failure looks like.
3. On approval, write into the prep doc.

### Designing a trap
1. Specify: trigger, detection DC, disable DC, effect, damage.
2. Always include a "warning sign" the players can spot before triggering.
3. Propose first; write to the prep doc on approval.

## Output conventions
- Always use 5e SRD stat references when possible (e.g., "MM cultist", "MM brown bear").
- Always show the XP math.
- Always include scaling notes for both directions ("if too hard: ...", "if too easy: ...").

## Update rules
- Encounters live inside the relevant `sessions/NNN-prep.md` file (or a freestanding scratch file). They are not standalone entities and don't get their own index.
- Treasure given to PCs after a session is recorded in the session file's State deltas (the `sessions` skill handles that).
```

- [ ] **Step 2: Verify**

Run: `grep -c "^name: encounters$" skills/prep/encounters/SKILL.md`
Expected: `1`.

- [ ] **Step 3: Commit**

```bash
git add skills/prep/encounters/SKILL.md
git commit -m "Add prep skill: encounters (design, treasure, puzzles, traps)"
```

---

## Task 16: Prep skill — `locations`

**Files:**
- Create: `skills/prep/locations/SKILL.md`

- [ ] **Step 1: Write the skill**

`skills/prep/locations/SKILL.md`:

```markdown
---
name: locations
description: Use when DESIGNING a new location (tavern, dungeon, town, wilderness area) or expanding an existing one with sub-locations or detail. Reads campaign tone and parent region for consistency. Writes to context/locations/<type>/<slug>.md after proposing changes.
---

# Locations (prep skill)

## When to use
- "Create a tavern in <town>" → file in `context/locations/towns/`.
- "Design a dungeon for <quest>" → file in `context/locations/dungeons/`.
- "Expand <existing location> with more detail" → modifies the existing file.
- "Add a sub-location to <town>" → new file with `parent_location` set.

## When NOT to use
- At the table when you need a place to drop the party that doesn't matter long-term. Use `live/improvise-location`.
- For maps as images. Maps go in `context/maps/`; this skill only handles the textual location notes.

## Inputs
- `context/campaign.md` — tone.
- `context/world/geography.md` — regional context.
- The parent location file if one exists.
- Related quest files if the location ties to a quest.

## Workflow

### New location
1. Read campaign tone + region.
2. Read parent location (if any) and any tied quest.
3. Draft frontmatter + sections.
4. **Propose** the file path, frontmatter, and section outline. Wait for approval.
5. On approval: write the file with the `<!-- last updated: sNN -->` footer (use `prep` if between sessions). Update `context/locations/_INDEX.md`.

### Expanding an existing location
1. Read existing file.
2. Identify what's being added (sub-locations, encounter hooks, history).
3. Propose the diff. Wait for approval.
4. On approval: write changes; update the footer.

## Output conventions

Location files have these sections (vary slightly by type):
1. Frontmatter (name, type, region, parent_location, tags; type-specific: population, governance, tier)
2. `## Overview` — 2-3 sentences setting the place
3. `## Districts` (towns) / `## Layout` (dungeons) / `## Terrain` (wilderness)
4. `## Notable locations` (towns/dungeons) — list of sub-points
5. `## Mood` (towns) — sensory; what does it feel like
6. `## Inhabitants` / `## Who's there` — who's around
7. `## Hooks` or `## Encounters` — uses for play
8. Footer.

For dungeons specifically:
- Always include hazards section.
- Always include "DM-known" content marked separately from player-discoverable.

## Update rules
- Always update `context/locations/_INDEX.md` when writing a file.
- Always update the footer.
- When a location's status changes (e.g., destroyed, captured by faction X), preserve previous status in a History section.
```

- [ ] **Step 2: Verify**

Run: `grep -c "^name: locations$" skills/prep/locations/SKILL.md`
Expected: `1`.

- [ ] **Step 3: Commit**

```bash
git add skills/prep/locations/SKILL.md
git commit -m "Add prep skill: locations (towns, dungeons, wilderness)"
```

---

## Task 17: Prep skill — `world-bible`

**Files:**
- Create: `skills/prep/world-bible/SKILL.md`

- [ ] **Step 1: Write the skill**

`skills/prep/world-bible/SKILL.md`:

```markdown
---
name: world-bible
description: Use when EXPANDING the slow-changing world bible — geography, history, pantheon, factions. This is for canon-level worldbuilding, not active plot threads. For quests and active threads, use prep/quests-and-threads instead. Writes to context/world/ after proposing changes.
---

# World bible (prep skill)

## When to use
- "Expand on the history of <region>" → modifies `context/world/history.md`.
- "Add a new faction" → new file in `context/world/factions/`.
- "Tell me more about <god>" → expand `context/world/pantheon.md`.
- "Build out the geography of <region we haven't visited>" → modifies `geography.md`.

## When NOT to use
- For an active plot thread or quest. Use `prep/quests-and-threads`.
- For a single location (town, dungeon). Use `prep/locations`.
- For an NPC. Use `prep/npcs`.

## Inputs
- `context/campaign.md` — tone.
- The existing world bible files (always read what exists before adding).
- `context/timeline.md` — anything you write about history must align.

## Workflow

### Expanding existing files
1. Read the existing file (`geography.md`, `history.md`, or `pantheon.md`) entirely.
2. Identify what's being added.
3. Propose the diff. Wait for approval.
4. On approval: write the change; update the footer; update `context/world/_INDEX.md` if the file's one-liner has shifted.

### New faction file
1. Read existing factions to avoid name/concept collision.
2. Read related quest/NPC files (factions usually appear because of a story need).
3. Draft frontmatter + sections (see Output conventions).
4. **Propose**. Wait for approval.
5. On approval: write file; update `context/world/factions/_INDEX.md`.

## Output conventions

### Faction files
1. Frontmatter (name, type, disposition, region, status, known_to_party, tags)
2. `## What they claim to be` — public face
3. `## What they actually are` — DM truth
4. `## Structure` — leadership / hierarchy
5. `## What they want` — goals
6. `## Where they're weak` — exploitable for PCs
7. `## Relationship with the party` — current
8. `## Cross-references` — links to NPCs, quests, locations
9. Footer.

### History additions
- Anchor everything to the YoI (Year of Iron) calendar.
- If you're adding to "The Stirring" (current era), make sure it's consistent with `context/timeline.md`.

## Update rules
- Always update `context/world/_INDEX.md` if a file's one-liner shifts.
- For factions, update `context/world/factions/_INDEX.md`.
- Always update the footer.
- If you reveal something about a faction, also update `known_to_party:` in the frontmatter.
```

- [ ] **Step 2: Verify**

Run: `grep -c "^name: world-bible$" skills/prep/world-bible/SKILL.md`
Expected: `1`.

- [ ] **Step 3: Commit**

```bash
git add skills/prep/world-bible/SKILL.md
git commit -m "Add prep skill: world-bible (geography, history, pantheon, factions)"
```

---

## Task 18: Prep skill — `quests-and-threads`

**Files:**
- Create: `skills/prep/quests-and-threads/SKILL.md`

- [ ] **Step 1: Write the skill**

`skills/prep/quests-and-threads/SKILL.md`:

```markdown
---
name: quests-and-threads
description: Use when DESIGNING a new quest, REVISING an existing quest's structure, or doing thread bookkeeping (mark active/dormant/resolved, list stale threads, surface neglected hooks). Operates on context/quests/ — high-churn content that lives separate from the slow world-bible.
---

# Quests and threads (prep skill)

## When to use
- "Design a quest about <X>" → new file in `context/quests/`.
- "What threads are active right now?" → reads `context/quests/_INDEX.md`, summarizes.
- "What threads have gone stale?" → finds quests where `last_touched` is far behind current session.
- "Mark <quest> resolved" → status change + final-state writeup.
- "Surface neglected PC hooks" → cross-reference quests where `related_pcs` is set but `last_touched` is old.

## When NOT to use
- For a single NPC interaction. Use `prep/npcs`.
- For canon worldbuilding (faction lore, history). Use `prep/world-bible`.
- For session-by-session bookkeeping (recap, deltas). Use `prep/sessions`.

## Inputs
- `context/quests/_INDEX.md` (always read first).
- The specific quest file(s) for revisions.
- `context/pcs/_INDEX.md` for PC-tied quests.
- Related NPC and faction files.
- Recent session files (for "what's stale" queries).

## Workflow

### Designing a new quest
1. Identify the hook source (Guild bounty, NPC ask, PC backstory, faction-driven).
2. Read related NPCs, factions, locations.
3. Draft frontmatter + sections (see Output conventions).
4. **Propose** the quest summary, branches, and DM-only twist. Wait for approval.
5. On approval: write file; update `context/quests/_INDEX.md`.

### Thread bookkeeping query
1. Read the quests index.
2. Filter / sort by status, last_touched, tags.
3. Output a short summary table — no file changes needed for queries.

### Marking a quest resolved
1. Read the quest file.
2. Compute the change: `status: resolved`, append a "Resolution" section summarizing what happened.
3. Propose. Wait for approval.
4. On approval: write changes; update the index row.

## Output conventions

Quest files have these sections:
1. Frontmatter (title, status, tier, related_npcs, related_locations, related_pcs, opened, last_touched, tags)
2. `## Hook` — how the party got pulled in
3. `## What's known to the party` — current player-side state
4. `## What's actually going on (DM-only)` — the truth
5. `## Open threads` (active) OR `## Resolution` (resolved)
6. `## Bounty` / `## Reward` — what completion pays
7. Footer.

## Update rules
- Always update `context/quests/_INDEX.md`. The status column is critical.
- Always update `last_touched` in frontmatter and the index.
- When a quest goes dormant → active or vice versa, mention the trigger in the file.
```

- [ ] **Step 2: Verify**

Run: `grep -c "^name: quests-and-threads$" skills/prep/quests-and-threads/SKILL.md`
Expected: `1`.

- [ ] **Step 3: Commit**

```bash
git add skills/prep/quests-and-threads/SKILL.md
git commit -m "Add prep skill: quests-and-threads (design + thread bookkeeping)"
```

---

## Task 19: Prep skill — `sessions` (the heaviest skill)

**Files:**
- Create: `skills/prep/sessions/SKILL.md`

- [ ] **Step 1: Write the skill**

`skills/prep/sessions/SKILL.md`:

```markdown
---
name: sessions
description: Use BEFORE a session to draft the prep doc, or AFTER a session to generate the recap, state deltas, and propose updates to all affected files (NPCs, quests, factions, PCs). This is the campaign's main bookkeeping skill. Writes to sessions/ and (with approval) to multiple context/ files. Heaviest workflow in the OS — always operates in propose-then-apply mode.
---

# Sessions (prep skill)

## When to use
- "Draft prep for session NN" → new `sessions/NNN-prep.md`.
- "I just finished session NN, here are my notes" → produces recap + state deltas + proposed updates.
- "Generate a next-session seed" → looks at recent session deltas + active threads → drafts session NN+1's expected beats.

## When NOT to use
- During the session itself for in-the-moment improvisation. Use live skills.
- For pure quest design without a session context. Use `prep/quests-and-threads`.

## Inputs
- For PREP: active quests (`context/quests/_INDEX.md` filtered by status:active), PC index, recent session State deltas.
- For POST-SESSION: the user's raw session notes, plus all entity files mentioned.
- For NEXT-SESSION SEED: the most recent session's State deltas + open threads.

## Workflow

### Drafting prep for session NN
1. Read `context/quests/_INDEX.md` filtered to active quests.
2. Read `context/pcs/_INDEX.md` for PC arc-state.
3. Read the previous 1-2 sessions' State deltas.
4. Draft `sessions/NNN-prep.md` with: Goal of the session, Expected beats, Contingencies, Open questions to be ready for, PC hooks to maybe touch.
5. **Propose** the prep doc. Wait for approval.
6. On approval: write the file. (Prep docs do NOT update other files.)

### Post-session: recap + deltas + updates (THE BIG ONE)

1. Receive the user's raw session notes (the user has written them into `sessions/NNN-headline.md` under `## Raw notes`).
2. Read frontmatter to identify all NPCs, locations, quests touched.
3. Read each touched entity file.
4. Generate two sections in the session file:
   - `## Recap` — narrative summary, 2-3 paragraphs.
   - `## State deltas` — bulleted list of canonical changes, format: `<type>:<slug> → <change>`.
5. Compute proposed file updates from the State deltas:
   - Each NPC delta → propose changes to that NPC file (frontmatter + History section).
   - Each quest delta → propose changes to the quest file (status, last_touched, "What's known to the party").
   - Each faction delta → propose changes to the faction file (known_to_party, status).
   - Each PC delta → propose changes to the PC file (arc_state).
   - Each `world:` delta → propose changes to the relevant world-bible file.
6. **Propose-and-apply gate (REQUIRED)**:
   > "I'll update N files based on session NN. Approve?"
   > - bullet per file: path + summary of change
7. On user approval (whole batch or per-file):
   - Write the session file's Recap + State deltas first.
   - Then write all approved file updates.
   - Add `<!-- last updated: sNN -->` footer to every edited file.
   - Update each affected `_INDEX.md` Last touched column.
   - Update `sessions/_INDEX.md` with the new row.
8. If user rejects/edits a proposal, regenerate that single proposal and re-prompt.

### Generating a next-session seed
1. Read the most recent completed session's State deltas.
2. Read `context/quests/_INDEX.md` for active threads.
3. Suggest 3-5 candidate beats for next session, each tagged with which thread they advance.
4. Optional: offer to draft the prep file (which kicks back to "Drafting prep").

## Output conventions

### Recap section
- Narrative, past tense, 2-3 paragraphs.
- Names PCs by character name, not player name.
- Doesn't include DM-only information.

### State deltas section
- One line per change.
- Format: `<type>:<slug> → <change description>`
- Types: `npc`, `quest`, `pc`, `world`, `location`, `party-inventory`.
- Be SPECIFIC: not "Verros: changed", but "npc:lord-verros → status: hostile (was: wary)".

## Update rules
- ALWAYS propose before writing.
- ALWAYS update every affected `_INDEX.md`.
- ALWAYS update `sessions/_INDEX.md`.
- ALWAYS write footers.
- If the user rejects a proposed update, do NOT silently include it.
```

- [ ] **Step 2: Verify**

Run: `grep -c "^name: sessions$" skills/prep/sessions/SKILL.md`
Expected: `1`.

Run: `grep -c "Propose" skills/prep/sessions/SKILL.md`
Expected: `≥ 4` (this skill must enforce propose-first heavily).

- [ ] **Step 3: Commit**

```bash
git add skills/prep/sessions/SKILL.md
git commit -m "Add prep skill: sessions (prep doc, recap+deltas+propose updates, next-seed)"
```

---

## Task 20: Prep skill — `pcs`

**Files:**
- Create: `skills/prep/pcs/SKILL.md`

- [ ] **Step 1: Write the skill**

`skills/prep/pcs/SKILL.md`:

```markdown
---
name: pcs
description: Use to PULL hooks from PC backstories into upcoming session prep, TRACK per-PC arc state across sessions, and surface UNDER-SERVED PCs whose hooks haven't been touched recently. Reads context/pcs/ and recent sessions; updates PC files with approval.
---

# PCs (prep skill)

## When to use
- "Which PC hooks should I pull into session NN?" → recommends 1-3 hooks based on quest state and last touched.
- "Update <PC> after session NN" → writes arc-state changes proposed by `prep/sessions`.
- "Who's been under-served?" → surfaces PCs whose `hooks_active` haven't appeared in recent sessions.
- "Add a new active hook to <PC>" → new entry in `hooks_active`.

## When NOT to use
- For player-vs-DM stat questions. Use `live/5e-rules`.
- For session bookkeeping more broadly. Use `prep/sessions`.

## Inputs
- `context/pcs/_INDEX.md` and the specific PC files.
- `context/quests/_INDEX.md` (especially PC-tagged quests).
- Recent sessions/_INDEX.md and frontmatter (which PCs were present, which hooks pulled).

## Workflow

### Pulling hooks for prep
1. Read PC index.
2. For each PC, identify `hooks_active`.
3. Read related quest files for those hooks.
4. Cross-reference recent sessions to see which hooks have or haven't been touched.
5. Propose 1-3 hook-pulls for the upcoming session, tagged to the PC and quest.
6. Output is a recommendation — does NOT write files itself. The user takes the recommendation into `prep/sessions` for inclusion.

### Updating a PC after a session
1. Receive the State deltas from `prep/sessions` (typically `pc:<slug> → arc: <change>`).
2. Read the PC file.
3. Propose: arc_state change, hooks_active/hooks_resolved updates, append a brief "session NN" history note.
4. Wait for approval.
5. On approval: write changes; update footer; update `context/pcs/_INDEX.md` Last touched.

### "Under-served" query
1. Read PC index, get `hooks_active` for each.
2. Read recent N session frontmatter (default N=5).
3. For each PC, count how many of their hooks_active appeared in recent sessions.
4. Output a ranked table: PC | active hooks | last touched | recommendation.
5. NO file writes for queries.

## Output conventions
- PC files keep `arc_state` as a short imperative phrase (e.g., "searching-for-brother", "looking-for-purpose").
- `hooks_active` and `hooks_resolved` are kebab-case slugs that ideally match a quest slug.
- "Things she/he'd do that surprise the table" section is preserved across updates — don't rewrite it without prompting.

## Update rules
- Always update `context/pcs/_INDEX.md` when writing a PC file.
- Always write the footer.
- For "under-served" queries, no writes.
```

- [ ] **Step 2: Verify**

Run: `grep -c "^name: pcs$" skills/prep/pcs/SKILL.md`
Expected: `1`.

- [ ] **Step 3: Commit**

```bash
git add skills/prep/pcs/SKILL.md
git commit -m "Add prep skill: pcs (hook-pulling, arc updates, under-served query)"
```

---

## Task 21: Live skill — `improvise-npc`

**Files:**
- Create: `skills/live/improvise-npc/SKILL.md`

- [ ] **Step 1: Write the skill**

`skills/live/improvise-npc/SKILL.md`:

```markdown
---
name: improvise-npc
description: Use AT THE TABLE when the PCs interact with someone the DM didn't prep. Returns Name / Look / Voice / Wants / Secret in 5 lines, region-flavored. Does NOT read sessions/. Does NOT write files. If the user wants to keep the NPC, they must invoke prep/npcs after.
---

# Improvise NPC (live skill)

## When to use
- The DM is mid-session and needs an NPC NOW.
- The NPC is incidental: a barmaid, a guard, a passerby with a line.

## When NOT to use
- The NPC will be recurring. Use `prep/npcs` after the session, OR ask the user to confirm the NPC should be saved (then point them to `prep/npcs`).
- The user is at their desk between sessions. Use `prep/npcs` for a richer NPC.

## Output format (REQUIRED — terse, exactly this template)

```
**Name:** <name>
**Look:** <one phrase>
**Voice:** <one phrase>
**Wants:** <one short clause>
**Secret:** <one short clause>
```

That is the entire response. No prose before or after. No headers. No explanation.

## Source of truth (REQUIRED — read ONLY these)

- `context/world/_INDEX.md` (for region flavor)
- `context/locations/_INDEX.md` (for the current region's flavor)
- The current region's faction `_INDEX.md` if the user named a faction in the request

DO NOT read:
- Any individual NPC file
- `sessions/` (any file)
- Any quest file
- Any PC file
- Any world-bible file other than the indexes

## Hard rules

- Output ≤ 5 lines, exactly the template above.
- NO file writes, ever.
- NO prose, no preamble, no follow-up offer.
- Match the NPC's name flavor to the region: Iron Reach skews dwarven/gruff (Korr, Bren, Halt); Silent Coast skews softer/elvish (Vael, Aelric); Goldlands fancy (Velorian, Aurene).
- If the user wants this NPC saved, they must invoke `prep/npcs` separately. You may (in ≤1 line, after the template) say: "(To keep this NPC, invoke prep/npcs.)"
```

- [ ] **Step 2: Verify**

Run: `grep -c "^name: improvise-npc$" skills/live/improvise-npc/SKILL.md`
Expected: `1`.

Run: `grep -c "NO file writes" skills/live/improvise-npc/SKILL.md`
Expected: `≥ 1`.

- [ ] **Step 3: Commit**

```bash
git add skills/live/improvise-npc/SKILL.md
git commit -m "Add live skill: improvise-npc (5-line template, no file writes)"
```

---

## Task 22: Live skill — `improvise-location`

**Files:**
- Create: `skills/live/improvise-location/SKILL.md`

- [ ] **Step 1: Write the skill**

`skills/live/improvise-location/SKILL.md`:

```markdown
---
name: improvise-location
description: Use AT THE TABLE when the PCs go somewhere the DM didn't prep. Returns a 3-sentence description ending in one usable hook. Does NOT read sessions/. Does NOT write files. If the user wants to keep the location, they must invoke prep/locations after.
---

# Improvise Location (live skill)

## When to use
- Mid-session, party walks into a place the DM didn't prep.
- The location is probably incidental: a back-alley, a side room, a clearing.

## When NOT to use
- The location is a real prep target (a planned dungeon, a faction stronghold). Use `prep/locations`.

## Output format (REQUIRED — exactly this)

```
<3 sentences describing the place: what you see, what you hear/smell, who's there. The third sentence MUST end in a usable hook the DM can hand to players: someone strange in the corner, an odd object, an overheard line.>
```

That is the entire response. No headers. No bullet list.

## Source of truth (REQUIRED — read ONLY these)

- `context/world/_INDEX.md`
- `context/locations/_INDEX.md`
- `context/tables/tavern-events.md` if the location is a tavern (for hook flavor)

DO NOT read:
- Any individual location, NPC, quest, PC, or session file.

## Hard rules

- Output is a single paragraph of 3 sentences.
- Third sentence MUST contain a hook (a person, object, sound — something the players could pull on).
- NO file writes.
- NO preamble, no headers, no follow-up.
- Match tone to the region: Iron Reach is gritty, smoky, cold; Silent Coast is foggy, hushed, melancholic.
- If the user wants this location saved, they must invoke `prep/locations` separately. You may (in ≤1 line after the paragraph) say: "(To keep this location, invoke prep/locations.)"
```

- [ ] **Step 2: Verify**

Run: `grep -c "^name: improvise-location$" skills/live/improvise-location/SKILL.md`
Expected: `1`.

- [ ] **Step 3: Commit**

```bash
git add skills/live/improvise-location/SKILL.md
git commit -m "Add live skill: improvise-location (3-sentence with hook)"
```

---

## Task 23: Live skill — `random-encounter`

**Files:**
- Create: `skills/live/random-encounter/SKILL.md`

- [ ] **Step 1: Write the skill**

`skills/live/random-encounter/SKILL.md`:

```markdown
---
name: random-encounter
description: Use AT THE TABLE for a random encounter roll. Reads ONLY the matching context/tables/ file, rolls the die, and reports the encounter line + 1 short flavor note. Does NOT design encounters. Does NOT scale them. Does NOT write files.
---

# Random Encounter (live skill)

## When to use
- Mid-session, the DM wants a random encounter from a region+tier.
- The DM has accepted whatever the table rolls.

## When NOT to use
- The DM wants a designed, balanced encounter. Use `prep/encounters`.
- The DM wants to adjust an in-progress fight. Use `live/adjust-encounter`.

## Output format (REQUIRED)

```
**Roll:** <d#> = <result>
**Encounter:** <text from the table row>
**Flavor:** <one short sentence to set the scene>
```

3 lines exactly. No prose around it.

## Source of truth (REQUIRED — read ONLY this)

- The single matching table file: `context/tables/encounters-<region>-tier<N>.md`
- If no exact match exists, ask the user to specify region and tier in 1 short line, then look again.

DO NOT read:
- Other table files
- Any NPC, location, quest, PC, world, or session file

## Hard rules

- 3-line output, exactly.
- The Roll line shows actual rolled value (you generate the random number).
- The Encounter line is the table text verbatim.
- The Flavor line is ONE sentence, no more.
- NO file writes.
- If the rolled result references "DM choice", surface that fact in the Flavor line ("DM choice — pick the corrupt watchmen if you want this to escalate") instead of making the choice yourself.
```

- [ ] **Step 2: Verify**

Run: `grep -c "^name: random-encounter$" skills/live/random-encounter/SKILL.md`
Expected: `1`.

- [ ] **Step 3: Commit**

```bash
git add skills/live/random-encounter/SKILL.md
git commit -m "Add live skill: random-encounter (table roll, 3-line output)"
```

---

## Task 24: Live skill — `region-names`

**Files:**
- Create: `skills/live/region-names/SKILL.md`

- [ ] **Step 1: Write the skill**

`skills/live/region-names/SKILL.md`:

```markdown
---
name: region-names
description: Use AT THE TABLE when the DM needs N names with a regional flavor (e.g., "give me 5 dwarven names from the Iron Reach"). Returns a numbered list. Does NOT read sessions/. Does NOT write files.
---

# Region Names (live skill)

## When to use
- Mid-session, the DM needs names — for an improvised NPC, a roster, a list of suspects.

## Output format (REQUIRED)

```
1. <name>
2. <name>
3. <name>
4. <name>
5. <name>
```

Default N is 5. If the user asks for a different N, use that. NO prose.

## Source of truth (REQUIRED — read ONLY these)

- `context/world/geography.md` (for the region's cultural flavor)
- `context/world/_INDEX.md`

DO NOT read anything else.

## Hard rules

- Output is just the numbered list. Nothing else.
- Match flavor to region:
  - **Iron Reach**: dwarven/gruff (one or two syllables, hard consonants — Korr, Bren, Halt, Tova, Drennick).
  - **Silent Coast**: soft, elvish-tinged (Vael, Aelric, Sira, Mereth, Cael).
  - **Goldlands**: ornate, latinate (Velorian, Aurene, Mariposa, Castan, Lirielle).
  - **Burnt Wastes**: harsh, monosyllabic, often single-name (Ash, Krin, Vor, Slag, Thirst).
- If the region the user named isn't in the world bible, use the closest match and (in ≤1 line BEFORE the list) say: "(Closest match: <region>)".
- NO file writes.
```

- [ ] **Step 2: Verify**

Run: `grep -c "^name: region-names$" skills/live/region-names/SKILL.md`
Expected: `1`.

- [ ] **Step 3: Commit**

```bash
git add skills/live/region-names/SKILL.md
git commit -m "Add live skill: region-names (numbered list, region-flavored)"
```

---

## Task 25: Live skill — `who-knows-what`

**Files:**
- Create: `skills/live/who-knows-what/SKILL.md`

- [ ] **Step 1: Write the skill**

`skills/live/who-knows-what/SKILL.md`:

```markdown
---
name: who-knows-what
description: Use AT THE TABLE when the DM needs to know what a specific NPC knows about a topic, fast. Returns 1-3 bullets. Reads only that NPC's file plus the relevant index. Does NOT read sessions/. Does NOT write files.
---

# Who Knows What (live skill)

## When to use
- Mid-session, the DM is about to roleplay an NPC and needs to know what that NPC knows.
- Quick cross-reference: "Mira knows about the cult — what specifically?"

## When NOT to use
- The DM wants the deeper answer with sources and uncertainty. Use `prep/npcs` ("what does X know about Y?") between sessions.

## Output format (REQUIRED)

```
**<NPC name> knows about <topic>:**
- <fact 1>
- <fact 2>
- <fact 3>
```

1-3 bullets, no more. No prose around it. If the NPC genuinely doesn't know anything, output:

```
**<NPC name> knows about <topic>:**
- Nothing relevant.
```

## Source of truth (REQUIRED — read ONLY these)

- `context/npcs/<npc-slug>.md` (specifically the "Knows about" section)
- `context/npcs/_INDEX.md` (to resolve the slug if needed)

DO NOT read:
- Sessions
- Quests (the NPC's "Knows about" section is the canonical source)
- Other NPCs

## Hard rules

- Output is the template, nothing else.
- 1-3 bullets max. Pick the most relevant if more facts exist.
- Each bullet is one short clause.
- NO file writes.
- If the NPC's "Knows about" section doesn't address the topic, output the "Nothing relevant" form. DO NOT speculate.
```

- [ ] **Step 2: Verify**

Run: `grep -c "^name: who-knows-what$" skills/live/who-knows-what/SKILL.md`
Expected: `1`.

- [ ] **Step 3: Commit**

```bash
git add skills/live/who-knows-what/SKILL.md
git commit -m "Add live skill: who-knows-what (1-3 bullets, NPC-only source)"
```

---

## Task 26: Live skill — `adjust-encounter`

**Files:**
- Create: `skills/live/adjust-encounter/SKILL.md`

- [ ] **Step 1: Write the skill**

`skills/live/adjust-encounter/SKILL.md`:

```markdown
---
name: adjust-encounter
description: Use AT THE TABLE mid-fight when an encounter is going too easy or too hard. Returns ONE adjustment — either a reinforcement or an environmental complication — appropriate to the location and tier. Does NOT redesign the encounter. Does NOT write files.
---

# Adjust Encounter (live skill)

## When to use
- Combat is in round 2-3 and is clearly too easy → introduce something.
- Combat is in round 2-3 and the party is in real danger → introduce a complication that gives them an out (or a non-combat resolution path).

## When NOT to use
- Designing an encounter from scratch. Use `prep/encounters`.
- Rolling a random encounter. Use `live/random-encounter`.

## Output format (REQUIRED)

```
**Adjustment type:** [Reinforcement | Complication]
**What appears:** <1-2 sentence description>
**Mechanical effect:** <stat reference + relevant numbers>
**Why it makes sense here:** <1 sentence — terrain, faction, narrative tie>
```

4 lines exactly. No prose around it.

## Source of truth (REQUIRED — read ONLY these)

- The current location file (the user must name it, or you may infer from a recent prep doc — but you may NOT scan all locations).
- `context/tables/encounters-<region>-tier<N>.md` for thematic flavor.

DO NOT read:
- Sessions
- NPC files in detail (you may glance at the index for a name)
- Quest files

## Hard rules

- ONE adjustment. Not two. Not a menu. The user asked for help, not options.
- If the user said "too easy" → Reinforcement. If "too hard" → Complication that opens an escape valve, not more enemies.
- Mechanical effect MUST reference SRD stats (e.g., "MM cultist, CR 1/8, AC 12, HP 9").
- NO file writes.
```

- [ ] **Step 2: Verify**

Run: `grep -c "^name: adjust-encounter$" skills/live/adjust-encounter/SKILL.md`
Expected: `1`.

- [ ] **Step 3: Commit**

```bash
git add skills/live/adjust-encounter/SKILL.md
git commit -m "Add live skill: adjust-encounter (one mid-fight adjustment, 4-line output)"
```

---

## Task 27: Live skill — `5e-rules`

**Files:**
- Create: `skills/live/5e-rules/SKILL.md`

- [ ] **Step 1: Write the skill**

`skills/live/5e-rules/SKILL.md`:

```markdown
---
name: 5e-rules
description: Use AT THE TABLE for a quick 5e rules clarification. Returns one short paragraph + an SRD reference. Honors house-rules in context/house-rules.md when they apply. Does NOT write files.
---

# 5e Rules (live skill)

## When to use
- A rules question came up at the table and the DM needs a fast answer.

## When NOT to use
- Encounter design or balance questions. Use `prep/encounters`.
- Anything narrative. Use `prep/sessions` or `live/improvise-*`.

## Output format (REQUIRED)

```
**Ruling:** <1-paragraph answer, ≤4 sentences>
**Source:** <SRD section / page reference>
**House-rule note:** <if context/house-rules.md modifies this rule, what the house version is — otherwise omit this line>
```

≤4 lines total. NO prose around it.

## Source of truth (REQUIRED)

- 5e SRD knowledge (you have this).
- `context/house-rules.md` (always check; one short read).

DO NOT read:
- Sessions, quests, NPCs, locations.

## Hard rules

- ≤4 sentences in the Ruling.
- ALWAYS include a Source line.
- ONLY include the House-rule note line if house rules actually modify the answer.
- If the question is ambiguous, ask ONE clarifying question (≤1 line) instead of guessing.
- NO file writes.
```

- [ ] **Step 2: Verify**

Run: `grep -c "^name: 5e-rules$" skills/live/5e-rules/SKILL.md`
Expected: `1`.

- [ ] **Step 3: Commit**

```bash
git add skills/live/5e-rules/SKILL.md
git commit -m "Add live skill: 5e-rules (1-paragraph ruling + SRD reference + house-rule check)"
```

---

## Task 28: Smoke-test verification

**Files:** None (verification only).

This task is a structural sanity check across the whole repo. It catches missing files, broken frontmatter, and missing index rows.

- [ ] **Step 1: Verify directory structure is complete**

Run: `find . -type d -not -path '*/.git*' -not -path '*/.superpowers*' -not -path './docs*' | sort`

Expected (sorted):
```
.
./context
./context/locations
./context/locations/dungeons
./context/locations/towns
./context/locations/wilderness
./context/maps
./context/maps/dungeons
./context/npcs
./context/pcs
./context/quests
./context/tables
./context/world
./context/world/factions
./sessions
./skills
./skills/live
./skills/live/5e-rules
./skills/live/adjust-encounter
./skills/live/improvise-location
./skills/live/improvise-npc
./skills/live/random-encounter
./skills/live/region-names
./skills/live/who-knows-what
./skills/prep
./skills/prep/encounters
./skills/prep/locations
./skills/prep/npcs
./skills/prep/pcs
./skills/prep/quests-and-threads
./skills/prep/sessions
./skills/prep/world-bible
```

- [ ] **Step 2: Verify all 14 SKILL.md files exist**

Run: `find skills -name SKILL.md | wc -l`
Expected: `14`.

- [ ] **Step 3: Verify every SKILL.md has both `name:` and `description:` frontmatter fields**

Run: `for f in $(find skills -name SKILL.md); do echo "$f"; grep -c "^name:" "$f"; grep -c "^description:" "$f"; done`
Expected: every `name:` and `description:` line shows `1`.

- [ ] **Step 4: Verify every live SKILL.md mentions the no-file-writes rule**

Run: `for f in $(find skills/live -name SKILL.md); do echo -n "$f: "; grep -c "NO file writes\|no file writes\|Does NOT write files\|does not write" "$f"; done`
Expected: every file shows ≥ 1 match.

- [ ] **Step 5: Verify every `_INDEX.md` is non-empty and contains at least one data row**

Run: `for f in $(find . -name '_INDEX.md' -not -path '*/.git*'); do lines=$(wc -l < "$f"); echo "$lines $f"; done | sort -n`
Expected: every file ≥ 5 lines (8 indexes total: world, factions, npcs, locations, quests, pcs, tables, sessions).

- [ ] **Step 6: Verify every entity file has YAML frontmatter (opens with `---`)**

Run: `for f in $(find context -name '*.md' -not -name '_INDEX.md'); do head -1 "$f" | grep -q '^---$' || echo "MISSING FRONTMATTER: $f"; done`
Expected: no output (all files have frontmatter).

Run: `for f in $(find sessions -name '*.md' -not -name '_INDEX.md'); do head -1 "$f" | grep -q '^---$' || echo "MISSING FRONTMATTER: $f"; done`
Expected: no output.

- [ ] **Step 7: Verify every entity file has the `<!-- last updated:` footer**

Run: `for f in $(find context sessions -name '*.md' -not -name '_INDEX.md'); do tail -3 "$f" | grep -q '<!-- last updated:' || echo "MISSING FOOTER: $f"; done`
Expected: no output.

- [ ] **Step 8: Verify CLAUDE.md mentions both load-bearing rules**

Run: `grep -c "Propose-first\|propose.first\|Propose " CLAUDE.md && grep -c "_INDEX.md" CLAUDE.md`
Expected: each ≥ 1.

- [ ] **Step 9: Final commit (if there are any uncommitted changes — there shouldn't be)**

```bash
git status
```
Expected: `nothing to commit, working tree clean`.

If anything's uncommitted, fix it and commit before declaring done:
```bash
git add -A
git commit -m "Smoke-test fixups"
```

- [ ] **Step 10: Print the full file inventory for the user**

Run: `find . -type f -not -path '*/.git*' -not -path '*/.superpowers*' | sort`

Expected: a complete listing including CLAUDE.md, all context files, all sessions, all 14 SKILL.md files, plus the docs/ spec and plan files. Hand this to the user as proof of completion.

---

## Self-review notes (post-write)

This plan was self-reviewed against the spec:

- **Spec coverage:** All 22 user-identified tasks are covered across the 7 prep + 7 live skills (verified by re-reading the spec's "Skill anatomy" section). All folder layout, frontmatter conventions, propose-first rule, and index-maintenance rule are encoded in CLAUDE.md and reinforced in every prep skill.
- **Placeholder scan:** No "TBD", "TODO", or "fill in later" remain. Every code block is concrete. Verification commands show expected output.
- **Type/name consistency:** Skill names match between spec and plan. PC name "Mira-sage" disambiguates from "Tavernkeep Mira" consistently. Slug conventions are kebab-case throughout. The session file naming (`NNN-headline.md`) is consistent across CLAUDE.md, the spec, and the seed sessions.
- **Scope check:** This is a single cohesive subsystem, single plan is appropriate.
