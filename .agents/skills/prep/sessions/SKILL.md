---
name: sessions
description: Use BEFORE a session to draft the prep doc, or AFTER a session to generate the recap, state deltas, and propose updates to all affected files (NPCs, quests, factions, PCs). This is the campaign's main bookkeeping skill. Writes to sessions/ and (with approval) to multiple context/ files. Heaviest workflow in the OS — always operates in propose-then-apply mode.
---

# Sessions (prep skill)

## When to use
- "Draft prep for session NN" → new `sessions/NNN-prep.md`.
- "I just finished session NN, here are my notes" → produces recap + state deltas + proposed updates.
- "Generate a next-session seed" → looks at recent session deltas + active threads → drafts session NN+1's expected beats.

## When NOT to use
- During the session itself for in-the-moment improvisation. Use live skills.
- For pure quest design without a session context. Use `prep/quests-and-threads`.

## Inputs
- For PREP: active quests (`context/quests/_INDEX.md` filtered by status:active), PC index, recent session State deltas.
- For POST-SESSION: the user's raw session notes, plus all entity files mentioned.
- For NEXT-SESSION SEED: the most recent session's State deltas + open threads.

## Workflow

### Drafting prep for session NN
1. Read `context/quests/_INDEX.md` filtered to active quests.
2. Read `context/pcs/_INDEX.md` for PC arc-state.
3. Read the previous 1-2 sessions' State deltas.
4. Draft `sessions/NNN-prep.md` with: Goal of the session, Expected beats, Contingencies, Open questions to be ready for, PC hooks to maybe touch.
5. **Propose** the prep doc. Wait for approval.
6. On approval: write the file. (Prep docs do NOT update other files.)

### Post-session: recap + deltas + updates (THE BIG ONE)

1. Receive the user's raw session notes (the user has written them into `sessions/NNN-headline.md` under `## Raw notes`).
2. Read frontmatter to identify all NPCs, locations, quests touched.
3. Read each touched entity file.
4. Generate two sections in the session file:
   - `## Recap` — narrative summary, 2-3 paragraphs.
   - `## State deltas` — bulleted list of canonical changes, format: `<type>:<slug> → <change>`.
5. Compute proposed file updates from the State deltas:
   - Each NPC delta → propose changes to that NPC file (frontmatter + History section).
   - Each quest delta → propose changes to the quest file (status, last_touched, "What's known to the party").
   - Each faction delta → propose changes to the faction file (known_to_party, status).
   - Each PC delta → propose changes to the PC file (arc_state).
   - Each `world:` delta → propose changes to the relevant world-bible file.
6. **Propose-and-apply gate (REQUIRED)**:
   > "I'll update N files based on session NN. Approve?"
   > - bullet per file: path + summary of change
7. On user approval (whole batch or per-file):
   - Write the session file's Recap + State deltas first.
   - Then write all approved file updates.
   - Add `<!-- last updated: sNN -->` footer to every edited file.
   - Update each affected `_INDEX.md` Last touched column.
   - Update `sessions/_INDEX.md` with the new row.
8. If user rejects/edits a proposal, regenerate that single proposal and re-prompt.

### Generating a next-session seed
1. Read the most recent completed session's State deltas.
2. Read `context/quests/_INDEX.md` for active threads.
3. Suggest 3-5 candidate beats for next session, each tagged with which thread they advance.
4. Optional: offer to draft the prep file (which kicks back to "Drafting prep").

## Output conventions

### Recap section
- Narrative, past tense, 2-3 paragraphs.
- Names PCs by character name, not player name.
- Doesn't include DM-only information.

### State deltas section
- One line per change.
- Format: `<type>:<slug> → <change description>`
- Types: `npc`, `quest`, `pc`, `world`, `location`, `party-inventory`.
- Be SPECIFIC: not "Verros: changed", but "npc:lord-verros → status: hostile (was: wary)".

## Update rules
- ALWAYS propose before writing.
- ALWAYS update every affected `_INDEX.md`.
- ALWAYS update `sessions/_INDEX.md`.
- ALWAYS write footers.
- If the user rejects a proposed update, do NOT silently include it.
