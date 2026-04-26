# WhisperX session transcription

Local, private, accurate transcription of D&D sessions. Produces speaker-attributed
Markdown transcripts that the `prep/transcript-import` skill can fold into the
`sessions/` canon.

## Why WhisperX

- **Whisper-large-v3** transcription accuracy.
- **pyannote-audio** speaker diarization (open-source gold standard).
- **Custom vocabulary** for NPC/place/cult names — auto-built from `context/` indexes.
- **Local + private** — no audio leaves the machine.

## One-time setup

1. **Install Python 3.10+** and (optionally) a CUDA-capable GPU. CPU works but is slow.
2. **Create a venv** in the repo root or your usual dev location:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r tools/whisperx/requirements.txt
   ```
3. **Get a HuggingFace token** at https://huggingface.co/settings/tokens (free).
   Accept the gated model terms at https://huggingface.co/pyannote/speaker-diarization-community-1.
4. **Export the token** in your shell profile (or a `.env` you don't commit):
   ```bash
   export HF_TOKEN="hf_..."
   ```
5. **Copy and edit the config**:
   ```bash
   cp tools/whisperx/config.example.json tools/whisperx/config.json
   ```
   Edit `speaker_map` to match your players. `config.json` is gitignored so personal
   tweaks (paths, GPU flags, player names) stay local.

## Usage

Drop a recording in `recordings/` (gitignored), then:

```bash
python tools/whisperx/transcribe.py recordings/session-019.wav
```

This will:
1. Build a hotword list from `context/` indexes + `tools/whisperx/extra_vocab.txt`.
2. Transcribe with Whisper-large-v3, biased by hotwords + initial_prompt.
3. Align word-level timestamps with wav2vec2.
4. Diarize with pyannote (5 speakers by default — tweak in `config.json`).
5. Map `SPEAKER_XX` → player names from `speaker_map`.
6. Write `transcripts/019-raw.md` (a plain attributed transcript).

Then in Claude Code:

```
> Import the s19 transcript.
```

The `prep/transcript-import` skill picks it up, proposes a `sessions/019-*.md` with
the cleaned transcript as `## Raw notes`, and you approve. From there, `prep/sessions`
turns Raw notes → Recap + State deltas as usual.

## Recording tips

- **Per-player mics destroy single-mic accuracy.** Even cheap USB lavaliers help a lot.
  If you can sum 5 channels into a single multi-track WAV, diarization is near-perfect.
- **Pin speaker count** in `config.json` (`num_speakers: 5` for DM + 4 players).
- **First session, label speakers manually once** — pyannote labels them
  `SPEAKER_00`, `SPEAKER_01`, etc. After mapping in `speaker_map`, save embeddings
  (`return_embeddings: true`) to keep labels stable across sessions. (Future work.)

## Files

| File | Purpose | Gitignored |
|---|---|---|
| `transcribe.py` | Main CLI: audio → transcript Markdown | no |
| `build_hotwords.py` | Walks `context/` to build hotword string + initial_prompt | no |
| `requirements.txt` | Pinned Python deps | no |
| `config.example.json` | Template config — copy to `config.json` and edit | no |
| `config.json` | Your local config (paths, speaker map, GPU flags) | **yes** |
| `extra_vocab.txt` | Hand-curated vocabulary not in indexes (cult terms, in-jokes) | no |
