from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
from src.end_to_end_textSummarizer.config.configuration import ConfigurationManager


class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_model_evaluation_config()

    def predict(self, text):
        # Debug prints for paths and types
        print(f"Model path value: {self.config.model_path}")
        print(f"Model path type: {type(self.config.model_path)}")
        print(f"Tokenizer path value: {self.config.tokenizer_path}")
        print(f"Tokenizer path type: {type(self.config.tokenizer_path)}")

        model_path = str(self.config.model_path)
        tokenizer_path = str(self.config.tokenizer_path)

        # Load tokenizer and model from specified paths
        tokenizer = AutoTokenizer.from_pretrained(tokenizer_path)
        model = AutoModelForSeq2SeqLM.from_pretrained(model_path)

        # Configure generation kwargs with safe defaults
        gen_kwargs = {
            "length_penalty": 0.8,
            "num_beams": 8,
            "max_length": 128,
            "min_length": 30,  # ensure minimum length to avoid empty outputs
            "no_repeat_ngram_size": 2,  # prevent repetition
            "early_stopping": True  # stop beam search early when optimal
        }

        pipe = pipeline("summarization", model=model, tokenizer=tokenizer)

        print("Input(Dialogue) Text:")
        print(text)

        # Validate input type
        if not isinstance(text, str):
            raise ValueError(f"Input text must be a string, got {type(text)}")

        # Call the summarization pipeline with generation params
        output = pipe(text, **gen_kwargs)
        print("Raw pipeline output:", output)
        summary = output[0]["summary_text"]  # type: ignore
        print("\nGenerated Summary:")
        print(summary)
        return summary

