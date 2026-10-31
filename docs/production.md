# Production and operations

| Item | Detail |
|---|---|
| Corpus preparation | Google Colab, T4 GPU. FFmpeg normalisation, WADA-SNR scoring, manual listening |
| Training | Rented RunPod GPU, driven through JupyterLab |
| Batch / length | Batch size 3, max sequence length 500, 36 steps per epoch |
| Second-stage run | 100 epochs, 6 h 9 min wall clock (03:27 to 09:36) |
| Logging | TensorBoard, log interval 10. The 118 MB event file is mostly audio previews logged per validation pass |
| Checkpoints | Every 50 epochs (`save_freq: 50`), written as `epoch_2nd_<n>.pth` |
| Inference | Notebook harness reads the highest-numbered checkpoint, synthesises held-out sentences, NLTK sentence segmentation before phonemisation |
| Output | 24 kHz mono |

No cost figures or latency measurements are stated in the case study, so none are given here.

## Serving notes (not yet done)

- The fine-tuned checkpoint is 2.25 GB with optimiser state. Exporting weights only is the first step before serving.
- A pronunciation lexicon patching recurring transliterations ahead of espeak-ng is a cheaper fix than more audio.
- A rerun should use a tighter checkpoint interval and a corpus at the originally specified duration.
