import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


class LLM:
    def __init__(self):
        model_name = "google/flan-t5-small"  # smaller than large
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        self.device="mps" if torch.backends.mps.is_available() else "cpu"
        self.model.to(self.device)

    def generate_answer(self, prompt):
        inputs = self.tokenizer(
            prompt,
            return_tensors="pt",
        ).to(self.device)

        outputs = self.model.generate(
            **inputs,
        )
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)