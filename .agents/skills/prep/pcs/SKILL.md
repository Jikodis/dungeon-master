---
name: pcs
description: Use to PULL hooks from PC backstories into upcoming session prep, TRACK per-PC arc state across sessions, and surface UNDER-SERVED PCs whose hooks haven't been touched recently. Reads context/pcs/ and recent sessions; updates PC files with approval.
---

# PCs (prep skill)

## When to use
- "Which PC hooks should I pull into session NN?" → recommends 1-3 hooks based on quest state and last touched.
- "Update <PC> after session NN" → writes arc-state changes proposed by `prep/sessions`.
- "Who's been under-served?" → surfaces PCs whose `hooks_active` haven't appeared in recent sessions.
- "Add a new active hook to <PC>" → new entry in `hooks_active`.

## When NOT to use
- For player-vs-DM stat questions. Use `live/5e-rules`.
- For session bookkeeping more broadly. Use `prep/sessions`.

## Inputs
- `context/pcs/_INDEX.md` and the specific PC files.
- `context/quests/_INDEX.md` (especially PC-tagged quests).
- Recent sessions/_INDEX.md and frontmatter (which PCs were present, which hooks pulled).

## Workflow

### Pulling hooks for prep
1. Read PC index.
2. For each PC, identify `hooks_active`.
3. Read related quest files for those hooks.
4. Cross-reference recent sessions to see which hooks have or haven't been touched.
5. Propose 1-3 hook-pulls for the upcoming session, tagged to the PC and quest.
6. Output is a recommendation — does NOT write files itself. The user takes the recommendation into `prep/sessions` for inclusion.

### Updating a PC after a session
1. Receive the State deltas from `prep/sessions` (typically `pc:<slug> → arc: <change>`).
2. Read the PC file.
3. Propose: arc_state change, hooks_active/hooks_resolved updates, append a brief "session NN" history note.
4. Wait for approval.
5. On approval: write changes; update footer; update `context/pcs/_INDEX.md` Last touched.

### "Under-served" query
1. Read PC index, get `hooks_active` for each.
2. Read recent N session frontmatter (default N=5).
3. For each PC, count how many of their hooks_active appeared in recent sessions.
4. Output a ranked table: PC | active hooks | last touched | recommendation.
5. NO file writes for queries.

## Output conventions
- PC files keep `arc_state` as a short imperative phrase (e.g., "searching-for-brother", "looking-for-purpose").
- `hooks_active` and `hooks_resolved` are kebab-case slugs that ideally match a quest slug.
- "Things she/he'd do that surprise the table" section is preserved across updates — don't rewrite it without prompting.

## Update rules
- Always update `context/pcs/_INDEX.md` when writing a PC file.
- Always write the footer.
- For "under-served" queries, no writes.
