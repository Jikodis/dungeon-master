---
name: who-knows-what
description: Use AT THE TABLE when the DM needs to know what a specific NPC knows about a topic, fast. Returns 1-3 bullets. Reads only that NPC's file plus the relevant index. Does NOT read sessions/. Does NOT write files.
---

# Who Knows What (live skill)

## When to use
- Mid-session, the DM is about to roleplay an NPC and needs to know what that NPC knows.
- Quick cross-reference: "Mira knows about the cult — what specifically?"

## When NOT to use
- The DM wants the deeper answer with sources and uncertainty. Use `prep/npcs` ("what does X know about Y?") between sessions.

## Output format (REQUIRED)

```
**<NPC name> knows about <topic>:**
- <fact 1>
- <fact 2>
- <fact 3>
```

1-3 bullets, no more. No prose around it. If the NPC genuinely doesn't know anything, output:

```
**<NPC name> knows about <topic>:**
- Nothing relevant.
```

## Source of truth (REQUIRED — read ONLY these)

- `context/npcs/<npc-slug>.md` (specifically the "Knows about" section)
- `context/npcs/_INDEX.md` (to resolve the slug if needed)

DO NOT read:
- Sessions
- Quests (the NPC's "Knows about" section is the canonical source)
- Other NPCs

## Hard rules

- Output is the template, nothing else.
- 1-3 bullets max. Pick the most relevant if more facts exist.
- Each bullet is one short clause.
- NO file writes.
- If the NPC's "Knows about" section doesn't address the topic, output the "Nothing relevant" form. DO NOT speculate.
