# Recordings

Drop session audio files here (`*.wav`, `*.m4a`, `*.mp3`, etc).

**This folder is gitignored.** Only this README and `.gitkeep` are committed —
audio files are large, often contain unedited table chatter, and don't belong in
version control.

## Naming

Recommended: `session-NNN.wav` or `NNN-headline.wav` — e.g. `session-019.wav` or
`019-sewers-east.wav`. The `transcribe.py` script extracts the session number
from the first run of digits in the filename. You can also pass `--session N`
explicitly.

## Workflow

1. Record per-player if possible (per-player mics dramatically improve diarization).
2. Drop the file in this folder.
3. Run:
   ```bash
   python tools/whisperx/transcribe.py recordings/session-019.wav
   ```
4. The transcript is written to `transcripts/019-raw.md`.
5. In Claude Code: `Import the s19 transcript` to invoke `prep/transcript-import`.

See [`tools/whisperx/README.md`](../tools/whisperx/README.md) for full setup.
