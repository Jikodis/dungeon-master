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
