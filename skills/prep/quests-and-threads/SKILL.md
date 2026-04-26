---
name: quests-and-threads
description: Use when DESIGNING a new quest, REVISING an existing quest's structure, or doing thread bookkeeping (mark active/dormant/resolved, list stale threads, surface neglected hooks). Operates on context/quests/ — high-churn content that lives separate from the slow world-bible.
---

# Quests and threads (prep skill)

## When to use
- "Design a quest about <X>" → new file in `context/quests/`.
- "What threads are active right now?" → reads `context/quests/_INDEX.md`, summarizes.
- "What threads have gone stale?" → finds quests where `last_touched` is far behind current session.
- "Mark <quest> resolved" → status change + final-state writeup.
- "Surface neglected PC hooks" → cross-reference quests where `related_pcs` is set but `last_touched` is old.

## When NOT to use
- For a single NPC interaction. Use `prep/npcs`.
- For canon worldbuilding (faction lore, history). Use `prep/world-bible`.
- For session-by-session bookkeeping (recap, deltas). Use `prep/sessions`.

## Inputs
- `context/quests/_INDEX.md` (always read first).
- The specific quest file(s) for revisions.
- `context/pcs/_INDEX.md` for PC-tied quests.
- Related NPC and faction files.
- Recent session files (for "what's stale" queries).

## Workflow

### Designing a new quest
1. Identify the hook source (Guild bounty, NPC ask, PC backstory, faction-driven).
2. Read related NPCs, factions, locations.
3. Draft frontmatter + sections (see Output conventions).
4. **Propose** the quest summary, branches, and DM-only twist. Wait for approval.
5. On approval: write file; update `context/quests/_INDEX.md`.

### Thread bookkeeping query
1. Read the quests index.
2. Filter / sort by status, last_touched, tags.
3. Output a short summary table — no file changes needed for queries.

### Marking a quest resolved
1. Read the quest file.
2. Compute the change: `status: resolved`, append a "Resolution" section summarizing what happened.
3. Propose. Wait for approval.
4. On approval: write changes; update the index row.

## Output conventions

Quest files have these sections:
1. Frontmatter (title, status, tier, related_npcs, related_locations, related_pcs, opened, last_touched, tags)
2. `## Hook` — how the party got pulled in
3. `## What's known to the party` — current player-side state
4. `## What's actually going on (DM-only)` — the truth
5. `## Open threads` (active) OR `## Resolution` (resolved)
6. `## Bounty` / `## Reward` — what completion pays
7. Footer.

## Update rules
- Always update `context/quests/_INDEX.md`. The status column is critical.
- Always update `last_touched` in frontmatter and the index.
- When a quest goes dormant → active or vice versa, mention the trigger in the file.
