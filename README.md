# cog-IDEFICS


[![Replicate](https://replicate.com/cjwbw/idefics/badge)](https://replicate.com/cjwbw/idefics) 

IDEFICS (**I**mage-aware **D**ecoder **E**nhanced à la **F**lamingo with **I**nterleaved **C**ross-attention**S**) is an open-access reproduction of [Flamingo](https://huggingface.co/papers/2204.14198), a closed-source visual language model developed by Deepmind. Like GPT-4, the multimodal model accepts arbitrary sequences of image and text inputs and produces text outputs. IDEFICS is built solely on publicly available data and models.

The model can answer questions about images, describe visual contents, create stories grounded on multiple images, or simply behave as a pure language model without visual inputs.

IDEFICS is on par with the original closed-source model on various image-text benchmarks, including visual question answering (open-ended and multiple choice), image captioning, and image classification when evaluated with in-context few-shot learning. It comes into two variants: a large [80 billion parameters](https://huggingface.co/HuggingFaceM4/idefics-80b) version and a [9 billion parameters](https://huggingface.co/HuggingFaceM4/idefics-9b) version.

We also fine-tune the base models on a mixture of supervised and instruction fine-tuning datasets, which boosts the downstream performance while making the models more usable in conversational settings: [idefics-80b-instruct](https://huggingface.co/HuggingFaceM4/idefics-80b-instruct) and [idefics-9b-instruct](https://huggingface.co/HuggingFaceM4/idefics-9b-instruct). As they reach higher performance, we recommend using these instructed versions first.

Learn more about some of the technical challenges we encountered while training IDEFICS [here](https://github.com/huggingface/m4-logs/blob/master/memos/README.md).

# License

The model is built on top of two pre-trained models: [laion/CLIP-ViT-H-14-laion2B-s32B-b79K](https://huggingface.co/laion/CLIP-ViT-H-14-laion2B-s32B-b79K) and [huggyllama/llama-65b](https://huggingface.co/huggyllama/llama-65b). The first was released under an MIT license, while the second was released under a specific non-commercial license focused on research purposes. As such, users should comply with that license by applying directly to [Meta's form](https://docs.google.com/forms/d/e/1FAIpQLSfqNECQnMkycAp2jP4Z9TFX0cGR4uf7b_fBxjY_OjhJILlKGA/viewform).

The two pre-trained models are connected to each other with newly initialized parameters that we train. These are not based on any of the two base frozen models forming the composite model. We release the additional weights we trained under an MIT license.

# Citation

**BibTeX:**

```bibtex
@misc{laurencon2023obelics,
      title={OBELICS: An Open Web-Scale Filtered Dataset of Interleaved Image-Text Documents},
      author={Hugo Laurençon and Lucile Saulnier and Léo Tronchon and Stas Bekman and Amanpreet Singh and Anton Lozhkov and Thomas Wang and Siddharth Karamcheti and Alexander M. Rush and Douwe Kiela and Matthieu Cord and Victor Sanh},
      year={2023},
      eprint={2306.16527},
      archivePrefix={arXiv},
      primaryClass={cs.IR}
}
```