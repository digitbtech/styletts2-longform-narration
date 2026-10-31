# Models and evaluation

## Kept

| Model | Role and detail |
|---|---|
| StyleTTS 2 (full fine-tune) | Full fine-tune from the LibriTTS checkpoint, 771 MB in, 2.25 GB out including optimiser state |
| PL-BERT | 12 layers, 768 hidden, 178-token phoneme vocabulary, pretrained 1M steps on English Wikipedia |
| HiFi-GAN decoder | Upsample rates 10-5-3-2, product 300, equal to the mel hop |
| WavLM base+ | 13 layers at 16 kHz, adversarial naturalness signal in the final stage |
| JDC pitch extractor | F0 supervision, without the lambda_F0 term the contour flattens within a few epochs |
| ASR-based aligner | 80-mel input, 256 hidden, phased in at epoch 10 |

## Discarded

| Alternative | Why not |
|---|---|
| VALL-E / one-shot codec cloning | Clones identity from seconds of audio, but holding one identity across eleven continuous minutes is what it does not promise |
| YourTTS (zero-shot adaptation) | The cheap route for one target speaker, but its documented speaker-similarity ceiling is below what daily narration needs |
| VITS | No pretrained checkpoint matching the target acoustic conditions, which removes the only reason a tiny corpus works |
| Training from scratch | 12.4 minutes of audio, the pretrained checkpoint carries the whole prosody prior |

## Runs

| | First stage | Second stage |
|---|---|---|
| Epochs | 200 | 100 |
| Steps per epoch | 36 | 36 |
| Validation loss | 0.895 to 0.555 | 0.416 to 0.370 |
| Best validation | 0.542 at epoch 189 | 0.361 at epoch 68 |
| Active terms | mel only | all, per schedule |

Duration loss settled at 0.87 to 0.88 and F0 loss at 1.97 to 2.05, both flat for the last thirty epochs.

## Evaluation method

1. Loss is not the judge. By about epoch 40 the validation curve is flat within noise while audio still improves in ways mel loss does not price (consonant crispness, pause before a clause, whether a loanword lands the same way twice).
2. Checkpoints are compared by listening, A/B, on held-out sentences, from a notebook harness that reads the highest-numbered checkpoint.
3. Acceptance is long-form: one continuous generation, listened to in full. Result as stated on digitb.tech: **8 min 41 s in one pass, no stitching.**
4. UTMOS (predicted MOS) and NISQA (per-dimension quality, including a discontinuity axis for seam artefacts) are the intended no-reference checks. No scores from them are published.

## Honest finding

Checkpoints were saved every 50 epochs. The best validation loss, 0.361 at epoch 68, was never saved. The kept checkpoint scores 0.370. The gap is inside listening noise, but a rerun would use a tighter save interval.
