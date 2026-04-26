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
