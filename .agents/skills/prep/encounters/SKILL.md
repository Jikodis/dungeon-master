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
