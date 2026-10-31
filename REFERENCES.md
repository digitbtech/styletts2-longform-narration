# References

## Papers

| Paper | Link | Role here |
|---|---|---|
| StyleTTS 2: Towards Human-Level Text-to-Speech | https://arxiv.org/abs/2306.07691 | Method: style diffusion and SLM adversarial training |
| StyleTTS: A Style-Based Generative Model for Natural and Diverse Text-to-Speech Synthesis | https://arxiv.org/abs/2205.15439 | Origin of the style vector and AdaIN conditioning |
| HiFi-GAN | https://arxiv.org/abs/2010.05646 | Waveform decoding from mel spectrograms |
| WavLM: Large-Scale Self-Supervised Pre-Training for Full Stack Speech Processing | https://arxiv.org/abs/2110.13900 | Why an SSL speech model makes a usable discriminator |
| LibriTTS: A Corpus Derived from LibriSpeech for Text-to-Speech | https://arxiv.org/abs/1904.02882 | Corpus behind the pretrained checkpoint |
| Glow-TTS | https://arxiv.org/abs/2005.11129 | Monotonic alignment objective scheduled in at epoch 10 |
| FastSpeech 2 | https://arxiv.org/abs/2006.04558 | Duration, pitch and energy as explicit targets |
| VITS | https://arxiv.org/abs/2106.06103 | Alternative architecture, not taken |
| VALL-E | https://arxiv.org/abs/2301.02111 | One-shot alternative, not used |
| NaturalSpeech 2 | https://arxiv.org/abs/2304.09116 | Diffusion for prosody and one-shot identity transfer |
| YourTTS | https://arxiv.org/abs/2112.02418 | Zero-shot adaptation baseline |
| UTMOS | https://arxiv.org/abs/2204.02152 | Automatic MOS prediction |
| WADA-SNR (Kim and Stern, Interspeech 2008) | https://www.cs.cmu.edu/~robust/Papers/KimSternIS08.pdf | Blind SNR scoring of candidate clips |

## Models and code

- StyleTTS 2 (upstream, MIT): https://github.com/yl4579/StyleTTS2
- StyleTTS: https://github.com/yl4579/StyleTTS
- PL-BERT: https://github.com/yl4579/PL-BERT
- WavLM base+: https://huggingface.co/microsoft/wavlm-base-plus
- LibriTTS corpus (OpenSLR 60): https://www.openslr.org/60/

## Tools

- espeak-ng: https://github.com/espeak-ng/espeak-ng
- phonemizer: https://github.com/bootphon/phonemizer
- NLTK: https://www.nltk.org/
- Hugging Face Transformers: https://github.com/huggingface/transformers
- NISQA: https://github.com/gabrielmittag/NISQA
- TensorBoard: https://www.tensorflow.org/tensorboard
- RunPod: https://www.runpod.io/
- Hugging Face Hub: https://huggingface.co/

## Related work by DigitB

- This project's case study: https://digitb.tech/case-study/hebrew-tts/
- Chimera Studio (image synthesis research): https://digitb.tech/case-study/chimera-studio/
