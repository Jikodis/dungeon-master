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
