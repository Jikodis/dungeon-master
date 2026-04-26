# 5e SRD Index

Vendored from [OldManUmby/dnd.srd](https://github.com/OldManUmby/dnd.srd) — the official D&D 5.1 SRD (2014 PHB rules + Nov 2018 errata) converted to Markdown. License: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/legalcode).

**This is an index for skills.** Live rules/spell/statblock skills grep this file first to find the right SRD path, then read only the matching file. Do NOT read the entire SRD as context — it is 5+ MB.

## How to grep

- Rules questions (combat, conditions, exhaustion, surprise, hiding, etc.): look at the **Core rules** and **Conditions / hazards** tables.
- Spell lookup: every spell is one file under `Spells/<Spell Name>.md`.
- Monster stat block: every monster is one file under `Monsters/<Monster Name>.md`.
- Class / race features: `Classes/<class>.md` and `Races/<race>.md`.
- Equipment, treasure, magic items: `Equipment/`, `Treasure/`.

## Core rules (most-asked categories)

| Topic | File |
|---|---|
| Ability checks, saves, advantage/disadvantage, skills | `Gameplay/Abilities.md` |
| Adventuring (movement, rest, food/water, environment, vision/light) | `Gameplay/Adventuring.md` |
| Combat (initiative, actions, attacks, cover, grappling, opportunity attacks, mounted/underwater combat, damage/healing, death saves) | `Gameplay/Combat.md` |
| Spellcasting rules | `Spells/# Spellcasting.md` |

## Conditions, hazards, GM tables

| Topic | File |
|---|---|
| Conditions (blinded, charmed, exhausted, frightened, grappled, incapacitated, invisible, paralyzed, petrified, poisoned, prone, restrained, stunned, unconscious) | `Gamemastering/Conditions.md` |
| Diseases | `Gamemastering/Diseases.md` |
| Madness | `Gamemastering/Madness.md` |
| Objects (HP, AC, breaking) | `Gamemastering/Objects.md` |
| Pantheons (gods of various settings) | `Gamemastering/Pantheons.md` |
| Planes of existence | `Gamemastering/Planes.md` |
| Poisons | `Gamemastering/Poisons.md` |
| Traps | `Gamemastering/Traps.md` |

## Spells

322 individual spell files. Path pattern: `Spells/<Title Case Name>.md` (e.g. `Spells/Counterspell.md`, `Spells/Hold Person.md`, `Spells/Fireball.md`).

Spell list reference files:
- `Spells/# Spellcasting.md` — the rules for casting (slots, components, concentration, ritual)
- `Spells/## Spell Lists.md` — which classes get which spells
- `Spells/## Spell Lists (Wikilinked).md` — same with Obsidian-style links

## Monsters

319 individual monster stat block files. Path pattern: `Monsters/<Name>.md` (e.g. `Monsters/Goblin.md`, `Monsters/Cult Fanatic.md`, `Monsters/Adult Red Dragon.md`).

`Monsters (Alt)/` contains alternate-format versions of the same stat blocks (different table layout). Prefer `Monsters/` for skill reads.

## Classes, races, backgrounds

| Folder | Contains |
|---|---|
| `Classes/` | One file per SRD class (Barbarian, Bard, Cleric, Druid, Fighter, Monk, Paladin, Ranger, Rogue, Sorcerer, Warlock, Wizard). SRD includes one subclass per class. |
| `Races/` | One file per SRD race (Dwarf, Elf, Halfling, Human, Dragonborn, Gnome, Half-Elf, Half-Orc, Tiefling). |
| `Characterizations/` | Backgrounds, alignment, languages, inspiration. |

## Equipment, treasure, magic items

| Folder | Contains |
|---|---|
| `Equipment/` | Armor, weapons, gear, tools, mounts/transportation, trade goods, coinage, expenses |
| `Treasure/` | Magic item descriptions (`Magic Items A-Z.md`), treasure-by-CR tables, loot |
| `Treasure (Alt)/` | Alternate format |

## What's NOT in the SRD

The 5.1 SRD is a subset of the full PHB/DMG/MM. It does NOT include:
- Most subclasses (only one per class — e.g. Champion Fighter, Life Cleric, Evocation Wizard)
- Many spells from the full PHB (~320 of ~360)
- Many monsters from the full MM (~330 of ~450)
- Most playable races introduced after 2014
- Adventure modules, settings, or DMG variant rules beyond what's in `Gamemastering/`
- The 2024 PHB rules (this is 2014 + 2018 errata)

If a rules/spell/monster lookup misses, the `5e-rules` skill must label its fallback answer as `(unverified — not in SRD)` so the DM knows to double-check against their books.

## Attribution

Per CC-BY-4.0, attribution lives in `context/rules/srd/Legal.md` (vendored alongside) and in `README.md`.
