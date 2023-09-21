# Prediction interface for Cog ⚙️
# https://github.com/replicate/cog/blob/main/docs/python.md


import torch
from PIL import Image
from transformers import IdeficsForVisionText2Text, AutoProcessor
from cog import BasePredictor, Input, Path


class Predictor(BasePredictor):
    def setup(self) -> None:
        """Load the model into memory to make running multiple predictions efficient"""
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

        checkpoint = "HuggingFaceM4/idefics-9b"
        self.model = IdeficsForVisionText2Text.from_pretrained(
            checkpoint, cache_dir="model_cache", torch_dtype=torch.bfloat16
        ).to(self.device)
        self.processor = AutoProcessor.from_pretrained(checkpoint)

    def predict(
        self,
        image: Path = Input(description="Input image"),
        text: str = Input(description="Input text"),
        max_new_tokens: int = Input(
            description="Maximum number of new tokens to generate.",
            default=512,
            ge=8,
            le=1024,
        ),
        repetition_penalty: float = Input(
            description="Repetition penalty, 1.0 is equivalent to no penalty",
            default=2.0,
            ge=0.01,
            le=5,
        ),
        decoding_strategy: str = Input(
            choices=[
                "Greedy",
                "Top P Sampling",
            ],
            default="Greedy",
            description="Choose the decoding strategy.",
        ),
        temperature: float = Input(
            description="Sampling temperature. Valid for Top P Sampling. Higher values will produce more diverse outputs.",
            default=0.4,
            ge=0,
            le=5,
        ),
        top_p: float = Input(
            description="Valid for Top P Sampling. Higher values is equivalent to sampling more low-probability tokens.",
            default=0.8,
            ge=0.01,
            le=0.99,
        ),
    ) -> str:
        """Run a single prediction on the model"""
        prompt = [Image.open(str(image)), text]
        inputs = self.processor(prompt, return_tensors="pt").to(self.device)

        generation_args = {
            "max_new_tokens": max_new_tokens,
            "repetition_penalty": repetition_penalty,
            # "stop_sequences": ["<end_of_utterance>", "\nUser:"],
            "do_sample": False,
        }

        if decoding_strategy == "Top P Sampling":
            generation_args["temperature"] = temperature
            generation_args["do_sample"] = True
            generation_args["top_p"] = top_p

        # Generation args
        bad_words_ids = self.processor.tokenizer(
            ["<image>", "<fake_token_around_image>"], add_special_tokens=False
        ).input_ids

        generated_ids = self.model.generate(
            **inputs,
            **generation_args,
            bad_words_ids=bad_words_ids,
        )
        generated_text = self.processor.batch_decode(
            generated_ids, skip_special_tokens=True
        )
        out_text = generated_text[0]
        if out_text.startswith(text):
            out_text = out_text[len(text) :].strip()
        return out_text
