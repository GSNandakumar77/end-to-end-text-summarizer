from src.end_to_end_textSummarizer.config.configuration import ConfigurationManager
from src.end_to_end_textSummarizer.components.model_evaluation import ModelEvaluation
from src.end_to_end_textSummarizer.logging import logger

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass
    def initiate_model_evaluation(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.evaluate()