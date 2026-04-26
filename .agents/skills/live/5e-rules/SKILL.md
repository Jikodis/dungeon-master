---
name: 5e-rules
description: Use AT THE TABLE for a quick 5e rules clarification (combat, conditions, hiding, grappling, rests, vision, environment, etc.). Returns one short paragraph + an SRD citation. Quotes the vendored SRD when possible; labels fallback model knowledge as unverified. Honors house-rules in context/house-rules.md when they apply. Does NOT write files. Does NOT do spell descriptions (use spell-lookup) or monster stats (use statblock).
---

# 5e Rules (live skill)

## When to use
- A rules question came up at the table and the DM needs a fast answer.

## When NOT to use
- "What does spell X do?" — use `live/spell-lookup` (also reads the SRD).
- "Stats for monster Y?" — use `live/statblock`.
- Encounter design or balance questions. Use `prep/encounters`.
- Anything narrative. Use `prep/sessions` or `live/improvise-*`.

## Output format (REQUIRED)

```
**Ruling:** <1-paragraph answer, ≤4 sentences, quoting or paraphrasing the SRD>
**Source:** <SRD path + section heading — e.g. "context/rules/srd/Gameplay/Combat.md → Grappling">
**House-rule note:** <if context/house-rules.md modifies this rule, what the house version is — otherwise omit>
```

≤4 lines total. NO prose around it.

## Workflow (REQUIRED)

1. **Read the SRD index:** `context/rules/srd/_INDEX.md`. Pick the most likely file for the topic.
2. **Read the matching SRD file** (one file, not the whole SRD). Find the relevant section by heading.
3. **Read** `context/house-rules.md` (always, one short read) to check for modifications.
4. **Compose the Ruling** by paraphrasing or briefly quoting the SRD text. Cite the file path and section heading on the **Source** line.
5. **Add the House-rule note** ONLY if `context/house-rules.md` modifies the answer.

## If the SRD doesn't cover it

Some things are not in the 5.1 SRD: post-2018 spells/subclasses, the 2024 rules update, many magic items, etc. If you can't find the topic in the SRD after checking the index and the most relevant file:

```
**Ruling:** (unverified — not in SRD) <model-knowledge answer, ≤4 sentences>
**Source:** Not in vendored SRD (2014 + Nov 2018 errata). Verify against your books.
```

The `(unverified — not in SRD)` prefix is REQUIRED in this case so the DM knows to double-check.

## Source of truth (REQUIRED — read ONLY these)

- `context/rules/srd/_INDEX.md` (always — one short read)
- ONE file under `context/rules/srd/` that matches the question (per the index)
- `context/house-rules.md` (always — one short read)

DO NOT read:
- Sessions, quests, NPCs, locations, world bible, PCs.
- The entire SRD tree (5+ MB — only read the one file the index points to).
- Multiple SRD files unless the first read clearly points elsewhere.

## Hard rules

- ≤4 sentences in the Ruling.
- ALWAYS include a Source line.
- ALWAYS prefix with `(unverified — not in SRD)` if the SRD doesn't cover the topic.
- ONLY include the House-rule note line if house rules actually modify the answer.
- If the question is ambiguous, ask ONE clarifying question (≤1 line) instead of guessing.
- NO file writes.

## Example

User: "How does grappling work?"

You read `context/rules/srd/_INDEX.md`, see grappling is in `Gameplay/Combat.md`. You read that file, find the Grappling section. House-rules has no grapple modification. Output:

```
**Ruling:** A grapple is a special melee attack that replaces one of your attacks; instead of damage, the target makes a Strength (Athletics) or Dexterity (Acrobatics) check contested by your Strength (Athletics). On success, the target is grappled (speed 0); they can use an action to escape with the same contested check. You must have at least one free hand and the target must be no more than one size larger than you.
**Source:** context/rules/srd/Gameplay/Combat.md → Making an Attack → Grappling
```
