# Transcripts Index

Raw and lightly-cleaned per-session transcripts from the WhisperX pipeline
(see [`tools/whisperx/`](../tools/whisperx/README.md)). These are the *input* to
the `prep/transcript-import` skill, which folds them into `sessions/` canon.

Transcripts are committed (text, small) so the conversion to canon is
auditable. The source audio files in `recordings/` are gitignored.

| File | Session | Date | Length | Status |
|------|---------|------|--------|--------|
| _(none yet)_ | | | | |

## Status values

- **raw** — fresh from `transcribe.py`, not yet imported into a session file.
- **imported** — `prep/transcript-import` has produced the matching `sessions/NNN-*.md` Raw notes block.
- **archived** — kept for reference; the corresponding session file has been recapped.
