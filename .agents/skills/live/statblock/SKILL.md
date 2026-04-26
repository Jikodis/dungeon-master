---
name: statblock
description: Use AT THE TABLE to get a 5e monster stat block fast (e.g. "stats for a goblin", "AC and HP of a cult fanatic", "give me a young red dragon"). Returns a tight stat block from the vendored SRD. Does NOT write files. Does NOT do encounter design (use prep/encounters), spells (use spell-lookup), or general rules (use 5e-rules).
---

# Statblock (live skill)

## When to use
- The party engaged something and the DM needs the actual stats now.

## When NOT to use
- "Build me a tier-2 encounter" — use `prep/encounters`.
- "What does Sacred Flame do?" — use `live/spell-lookup`.
- "How does opportunity attack work?" — use `live/5e-rules`.

## Output format (REQUIRED)

```
**<Name>** — <size> <type>, <alignment>
**AC** <ac> | **HP** <hp> (<hit dice>) | **Speed** <speed>
**STR** <s> | **DEX** <d> | **CON** <c> | **INT** <i> | **WIS** <w> | **CHA** <ch>
**Saves:** <if any> | **Skills:** <if any> | **Senses:** <senses> | **Languages:** <langs> | **CR** <cr> (<xp> XP)
**Traits/Actions** (one line each, ≤5 lines total):
- <Trait or Action 1>: <one-line description>
- <…>
**Source:** context/rules/srd/Monsters/<Name>.md
```

≤10 lines of output total. Strip flavor text — the table needs combat numbers.

## Workflow (REQUIRED)

1. **Resolve the monster name to a file.** Monsters live at `context/rules/srd/Monsters/<Title Case Name>.md`. Try exact name first (e.g. `Goblin.md`, `Cult Fanatic.md`). If it fails, list the directory once and find the closest match.
2. **Read that one file.** Do not read the rest of the SRD.
3. **Extract** size/type/alignment, AC/HP/Speed, six abilities, saves/skills/senses/languages/CR.
4. **Summarize traits and actions** to one line each. Prioritize the ones that affect the fight (multiattack, special damage types, recharge powers, legendary actions, spellcasting). Drop pure flavor traits if you have to cut.
5. **Emit per the template above.** Cite the file path on the Source line.

## If the monster isn't in the SRD

The 5.1 SRD has ~319 monsters, not the full MM ~450. If the file doesn't exist:

```
**<Name>** — (unverified — not in SRD)
<best-guess stat block from model knowledge, same template>
**Source:** Not in vendored SRD (5.1, 2014 + Nov 2018 errata). Verify against your MM.
```

The `(unverified — not in SRD)` label is REQUIRED in this case.

## Variants

If the user asks for a tweak ("a goblin but with rogue tricks", "scale this up to CR 3"):

- Pull the base stat block first.
- Add ONE line at the bottom: `**Variant:** <one-sentence note on what you changed>`.
- Don't redesign — that's `prep/encounters` work.

## Source of truth (REQUIRED — read ONLY these)

- The single file `context/rules/srd/Monsters/<Name>.md`
- If you can't find the file: `ls context/rules/srd/Monsters/` once to locate it

DO NOT read:
- Sessions, quests, NPCs (these are campaign NPCs, not monster stats), locations, PCs, world bible.
- The entire monsters directory contents — one file only.

## Hard rules

- One monster per call. If the user asks for two, do the first and offer to pull the second.
- ≤10 lines of output.
- NO file writes.
- Source line is REQUIRED.
- Trim trait/action descriptions ruthlessly to one line each; combat-relevant first.

## Example

User: "give me a goblin"

You read `context/rules/srd/Monsters/Goblin.md`. Output:

```
**Goblin** — Small humanoid (goblinoid), neutral evil
**AC** 15 (leather, shield) | **HP** 7 (2d6) | **Speed** 30 ft
**STR** 8 | **DEX** 14 | **CON** 10 | **INT** 10 | **WIS** 8 | **CHA** 8
**Skills:** Stealth +6 | **Senses:** darkvision 60 ft, passive Perception 9 | **Languages:** Common, Goblin | **CR** 1/4 (50 XP)
**Traits/Actions:**
- Nimble Escape: Disengage or Hide as a bonus action.
- Scimitar (action): +4 to hit, 5 ft, 1d6+2 slashing.
- Shortbow (action): +4 to hit, 80/320 ft, 1d6+2 piercing.
**Source:** context/rules/srd/Monsters/Goblin.md
```
