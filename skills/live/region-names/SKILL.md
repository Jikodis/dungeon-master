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
