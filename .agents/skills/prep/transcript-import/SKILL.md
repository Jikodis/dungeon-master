---
name: transcript-import
description: Use after running tools/whisperx/transcribe.py on a session recording. Reads the raw transcript in transcripts/, translates speaker labels to player names if needed, and proposes a sessions/NNN-headline.md with a populated `## Raw notes` block ready for prep/sessions to recap. Does NOT draft Recap or State deltas — that's prep/sessions' job.
---

# Transcript Import (prep skill)

## When to use
- "Import the s19 transcript" / "fold transcripts/019-raw.md into sessions/" / "draft session 19 from the transcript".
- Any time `tools/whisperx/transcribe.py` has just produced a new `transcripts/NNN-raw.md`.

## When NOT to use
- For recapping an already-imported session — use `prep/sessions`.
- For mid-session capture — live skills don't write.
- If no transcript exists yet (point the user at `tools/whisperx/README.md`).

## Inputs (read in this order)
1. `transcripts/_INDEX.md` — find the row(s) with status `raw`.
2. The transcript file itself (`transcripts/NNN-raw.md`).
3. `sessions/_INDEX.md` — confirm the target session row exists; if not, prepare to add it.
4. `tools/whisperx/config.example.json` (or `config.json` if it exists) — for the canonical `speaker_map`. Use this only if the transcript still has raw `SPEAKER_XX` labels; `transcribe.py` usually translates them already.

## Workflow

1. **Identify** the transcript and target session number (from the filename, or ask the user if ambiguous).
2. **Read** the transcript. Note its rough length.
3. **Clean lightly** — propose, but don't apply silently:
   - If labels are still raw `SPEAKER_XX`, map them via `speaker_map`.
   - If transcript is very long (>~3000 lines), suggest a compression pass: drop pure backchannel ("yeah", "mm-hmm", "right") and merge same-speaker consecutive lines. Get user buy-in before applying.
4. **Draft** `sessions/NNN-headline.md` with:
   - **Frontmatter**: `session`, `date` (from the transcript or today's date), `pcs_present` (inferred from speakers seen in the transcript), `locations_visited: []` and `npcs_appeared: []` and `quests_touched: []` left blank for `prep/sessions` to fill in.
   - **`## Raw notes`**: the cleaned, attributed transcript. Each line: `**Speaker:** text` or `**[HH:MM:SS] Speaker:** text` if timestamps survived.
   - **No `## Recap`. No `## State deltas`.** Stop there.
   - Footer: `<!-- last updated: prep -->` (becomes `sNN` once `prep/sessions` runs).
5. **Headline:** ask the user for a 3–6-word headline for the filename (e.g., `019-sewers-east-descent.md`). Don't invent one — that's a creative call only the DM should make.
6. **Propose** the file path, the proposed `sessions/_INDEX.md` row, the `transcripts/_INDEX.md` status change (`raw` → `imported`), and the headline. Wait for approval.
7. **On approval**: write the session file, update both indexes.

## Hand-off

After writing, recommend the next step explicitly:

> Imported. Next: invoke `prep/sessions` with "Recap session NNN from the imported transcript" — it will read the Raw notes and propose Recap + State deltas.

## Update rules

- Always update `sessions/_INDEX.md` with the new row (status reflects what's done — Raw notes only, not yet recapped).
- Always update `transcripts/_INDEX.md` to flip the row's status from `raw` → `imported`.
- Never overwrite an existing `sessions/NNN-*.md` without flagging it. If one already exists for that session number, ask: append the Raw notes, replace, or pick a different number?
- Never silently drop content from the transcript. If you compress (collapse backchannel, merge consecutive lines), say so in the proposal.
- Speaker labels in Raw notes should match `context/pcs/_INDEX.md` (e.g., "Mira-sage" not "MIRA"); fall back to `speaker_map` for the DM.

## Hard rules

- This skill produces ONLY the `## Raw notes` block. The Recap and State deltas are explicitly out of scope. Hand off to `prep/sessions`.
- Propose-first; never write `sessions/` files without explicit user approval.
- If the transcript looks truncated, garbled, or has only one speaker labeled when multiple were expected, surface that as a warning rather than draft anyway.
