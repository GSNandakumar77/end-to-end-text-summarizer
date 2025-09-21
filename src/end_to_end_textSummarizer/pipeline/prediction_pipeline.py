from src.end_to_end_textSummarizer.config.configuration import ConfigurationManager
from transformers import AutoTokenizer,AutoModelForSeq2SeqLM
from transformers import pipeline


class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_model_evaluation_config()


    
    def predict(self, text):
        # Load model and tokenizer from the same path
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_path)
        model = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_path)
        
        gen_kwargs = {"length_penalty": 0.8, "num_beams": 8, "max_length": 128}

        pipe = pipeline("summarization", model=model, tokenizer=tokenizer)

        print("Dialogue:")
        print(text)

        output = pipe(text, **gen_kwargs)[0]["summary_text"]
        print("\nModel Summary:")
        print(output)

        return output