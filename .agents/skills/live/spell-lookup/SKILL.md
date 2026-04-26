---
name: spell-lookup
description: Use AT THE TABLE to get the rules text of a specific 5e spell (e.g. "what does Hypnotic Pattern do", "Hold Person — give me the text", "fireball details"). Returns the spell block in a tight format from the vendored SRD. Does NOT write files. Does NOT do general rules questions (use 5e-rules) or monster stats (use statblock).
---

# Spell Lookup (live skill)

## When to use
- The DM or a player needs the actual rules text of a named spell, fast.

## When NOT to use
- General rules questions ("how does concentration work?") — use `live/5e-rules`.
- Monster stat blocks — use `live/statblock`.
- Spell selection / build advice — out of scope; defer to player.

## Output format (REQUIRED)

```
**<Spell Name>** — <level> <school> (<casting time>)
**Range:** <range> | **Components:** <V/S/M> | **Duration:** <duration>
<one-paragraph effect, ≤4 sentences, paraphrased or briefly quoted>
**At higher levels:** <one line if the spell scales — otherwise omit>
**Source:** context/rules/srd/Spells/<Spell Name>.md
```

≤6 lines total. NO prose around it.

## Workflow (REQUIRED)

1. **Resolve the spell name to a file.** Spells live at `context/rules/srd/Spells/<Title Case Name>.md`. Try the exact name first (e.g. `Hypnotic Pattern.md`). If that fails, list the directory once and find the closest match.
2. **Read that one file.** Do not read the rest of the SRD.
3. **Extract** the level/school/casting time, range/components/duration, the effect paragraph, and the "At Higher Levels" note (if present).
4. **Format and emit** per the template above.

## If the spell isn't in the SRD

The 5.1 SRD has ~322 spells, not the full PHB ~360. If the spell file doesn't exist:

```
**<Spell Name>** — (unverified — not in SRD)
<model-knowledge summary, ≤3 sentences>
**Source:** Not in vendored SRD (5.1, 2014 + Nov 2018 errata). Verify against your books.
```

The `(unverified — not in SRD)` label is REQUIRED in this case.

## Source of truth (REQUIRED — read ONLY these)

- The single file `context/rules/srd/Spells/<Spell Name>.md`
- If you can't find the file: `ls context/rules/srd/Spells/` once to locate it

DO NOT read:
- Sessions, quests, NPCs, locations, PCs, world bible.
- The entire spells directory contents — one file only.
- `context/house-rules.md` (this skill is rules-text-only; if the DM houses a spell, they'll mention it).

## Hard rules

- One spell per call. If the user asks for two, say "one at a time" and pick the first.
- ≤6 lines of output total.
- NO file writes.
- The Source line is REQUIRED.
- If you guess a name, say `(closest match: <name>)` on the first line.

## Example

User: "what does Hypnotic Pattern do?"

You read `context/rules/srd/Spells/Hypnotic Pattern.md`. Output:

```
**Hypnotic Pattern** — 3rd-level illusion (1 action)
**Range:** 120 ft | **Components:** S, M (a glowing stick of incense or a crystal vial filled with phosphorescent material) | **Duration:** Concentration, up to 1 minute
You create a twisting pattern in a 30-foot cube within range. Each creature in the area that can see it must make a Wisdom save or be charmed for the duration — incapacitated and with speed 0. Damage breaks the effect; another creature can shake them awake with an action.
**At higher levels:** Does not scale.
**Source:** context/rules/srd/Spells/Hypnotic Pattern.md
```
