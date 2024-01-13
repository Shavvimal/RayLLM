from ray import serve
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import torch


class FlanT5Base:
    def __init__(self):
        self.model_name = 'google/flan-t5-base'
        self.model = AutoModelForSeq2SeqLM.from_pretrained(self.model_name, torch_dtype=torch.bfloat16)
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)

    def generate(self, prompt, max_new_tokens=200) -> str:
        inputs = self.tokenizer(prompt, return_tensors='pt')
        # Run inference
        output = self.tokenizer.decode(
            self.model.generate(
                inputs["input_ids"],
                max_new_tokens=max_new_tokens,
            )[0],
            skip_special_tokens=True
        )
        return output


@serve.deployment()
class FlanT5(FlanT5Base):
    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    prompt = "What is the meaning of life?"
    flan = FlanT5Base()
    print(flan.generate(prompt))
