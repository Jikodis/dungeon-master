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
