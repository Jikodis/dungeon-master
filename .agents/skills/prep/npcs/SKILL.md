---
name: npcs
description: Use when CREATING a new NPC, deeply UPDATING an NPC after a session, or researching what an NPC KNOWS about a topic. Reads context/npcs/_INDEX.md first, then drills in. Writes to context/npcs/<slug>.md and updates the index, after proposing the changes for user approval. NOT for at-the-table improvisation — use the live/improvise-npc skill instead.
---

# NPCs (prep skill)

## When to use
- "Create an NPC for <role/location>" — produces a new file with full sections.
- "Update <NPC> after session NN" — modifies frontmatter, appends history, may change status.
- "What does <NPC> know about <topic>?" — read-only, cross-references quests/, sessions/, world/.
- "Who in <region/faction> would know about <topic>?" — queries the index by tag, then drills in.

## When NOT to use
- The user is at the table and needs an NPC right now. Use `live/improvise-npc`.
- The user wants pure rules, statblocks, or combat tuning. Use `live/5e-rules` or `prep/encounters`.

## Inputs
- The user's request (what kind of NPC, what update, what query).
- `context/npcs/_INDEX.md` (always read first).
- `context/campaign.md` (for tone).
- The specific NPC file (for updates and "knows" queries).
- For "knows about" queries: relevant `context/quests/<slug>.md`, `context/world/factions/<slug>.md`, and matching `sessions/NNN-*.md`.

## Workflow

### Creating an NPC
1. Read `context/npcs/_INDEX.md` to avoid name collisions.
2. Read `context/campaign.md` and the relevant location file (where the NPC lives) for tone.
3. Draft the file with required sections (see "Output conventions").
4. **Propose** to the user: file path, frontmatter, section outline. Wait for approval.
5. On approval: write the file. Add the `<!-- last updated: sNN -->` footer (use `prep` if between sessions).
6. Update `context/npcs/_INDEX.md` with the new row.

### Updating an NPC after a session
1. Read the session file's "State deltas" section for the relevant `npc:<slug>` lines.
2. Read the existing NPC file.
3. Compute the diff (frontmatter changes; new "History" entry; possibly updated Secrets / Knows About).
4. **Propose** the diff to the user. Wait for approval.
5. On approval: write changes; update the footer; update the index's "Last touched" column.

### "What does X know about Y?"
1. Read the NPC file.
2. Grep `context/quests/_INDEX.md` and `context/world/factions/_INDEX.md` for related entities.
3. Read matching session State deltas (search by NPC slug).
4. Synthesize the answer into 3 categories: KNOWS (canon), SUSPECTS (inference), DOESN'T KNOW (gaps to be aware of).
5. NO file writes for queries.

## Output conventions

NPC files have these sections in this order:
1. Frontmatter (name, race, location, faction, status, tags, first_appeared, last_seen)
2. `## Description` — physical, 2-3 sentences
3. `## Voice` — speech pattern, 1-2 sentences (REQUIRED)
4. `## Motivations` — numbered list, 1-3 items
5. `## Secrets` — bulleted, each tagged with `(known: party | NPC | none)`
6. `## Knows about` — bulleted, what canon facts the NPC has
7. `## History` — bulleted, sNN-tagged appearances and changes
8. Footer: `<!-- last updated: sNN -->`

If a stat block is needed, add `## Stats` before History. Use 5e SRD references where possible.

## Update rules
- Always update `context/npcs/_INDEX.md` when writing a file.
- Always update the file's `<!-- last updated: sNN -->` footer.
- When status changes (e.g., wary → hostile), preserve the previous value in the History section ("s18: status wary → hostile").
