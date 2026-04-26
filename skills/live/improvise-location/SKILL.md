---
name: improvise-location
description: Use AT THE TABLE when the PCs go somewhere the DM didn't prep. Returns a 3-sentence description ending in one usable hook. Does NOT read sessions/. Does NOT write files. If the user wants to keep the location, they must invoke prep/locations after.
---

# Improvise Location (live skill)

## When to use
- Mid-session, party walks into a place the DM didn't prep.
- The location is probably incidental: a back-alley, a side room, a clearing.

## When NOT to use
- The location is a real prep target (a planned dungeon, a faction stronghold). Use `prep/locations`.

## Output format (REQUIRED — exactly this)

```
<3 sentences describing the place: what you see, what you hear/smell, who's there. The third sentence MUST end in a usable hook the DM can hand to players: someone strange in the corner, an odd object, an overheard line.>
```

That is the entire response. No headers. No bullet list.

## Source of truth (REQUIRED — read ONLY these)

- `context/world/_INDEX.md`
- `context/locations/_INDEX.md`
- `context/tables/tavern-events.md` if the location is a tavern (for hook flavor)

DO NOT read:
- Any individual location, NPC, quest, PC, or session file.

## Hard rules

- Output is a single paragraph of 3 sentences.
- Third sentence MUST contain a hook (a person, object, sound — something the players could pull on).
- NO file writes.
- NO preamble, no headers, no follow-up.
- Match tone to the region: Iron Reach is gritty, smoky, cold; Silent Coast is foggy, hushed, melancholic.
- If the user wants this location saved, they must invoke `prep/locations` separately. You may (in ≤1 line after the paragraph) say: "(To keep this location, invoke prep/locations.)"
