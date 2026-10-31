# Data

No audio, narrator text or transcripts are included in this repository. Only the specification and format are described.

## Intake specification

Corpus quality was decided by a written specification issued before recording, not by cleanup afterwards.

| Requirement | Reason |
|---|---|
| 48 kHz audio, no added noise | Room tone and handling noise survive segmentation and get learned as part of the voice |
| 1.5 to 2 hours in a single wav | Below this, style diffusion has too little variation to sample from |
| Matching transcript in text form | PL-BERT and the aligner consume the text side |
| 100 to 200 ms silence at head and tail | Clean cut points, and avoids learning abrupt starts |
| Clear, undisrupted pronunciation | Disfluencies create alignments the model cannot explain |
| Strictly one speaker | A second voice contaminates identity |

The specification was met on every axis except duration: 12.4 minutes were obtainable.

## SNR gate

Each candidate clip: FFmpeg to 16 kHz mono PCM, then WADA-SNR (blind estimate from the waveform amplitude distribution). The notebook prints each score next to an inline player. See `docs/figures/corpus-snr-colab.png`. A clean twelve minutes trains; a noisy hour teaches the decoder to reproduce the noise.

## Corpus

| Property | Value |
|---|---|
| Clips | 119 (108 train, 11 validation) |
| Duration | 12.4 min |
| Clip length | median 5.4 s, range 1.6 to 14.0 s |
| Format | 24 kHz, mono, 16-bit PCM |
| Speakers | 1 |
| Minimum length | 50 frames (`min_length`), shorter dropped, never padded |

## Transcript schema

Transcripts are stored phonemised, one line per clip, pipe-delimited:

```
<clip_filename>.wav|<espeak-ng IPA phonemes with stress marks>|<speaker_id>
```

`speaker_id` is `0` throughout. Files referenced by `data_params` in the config: `Data/train_list.txt`, `Data/val_list.txt`, `Data/OOD_texts.txt`, audio under `Data/wavs`.

## Out-of-distribution pool

`OOD_texts.txt`: 141,433 phonemised lines from LibriTTS train-clean-360. It gives the SLM discriminator text far outside the twelve in-domain minutes.

## Known data characteristic

Phonemisation uses the English espeak-ng voice. Loanwords fall back to English letter-to-sound guesses, so the data contains no Hebrew characters and no guttural phonemes. The model learns consistent English approximations, not Hebrew pronunciation.

## Helper

`code/tools/rename_clips.py` renames clips to a sequential zero-padded scheme (`wav-0001.wav`, ...). Edit the directory argument at the bottom before use.
