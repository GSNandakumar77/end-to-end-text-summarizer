from src.end_to_end_textSummarizer.config.configuration import ConfigurationManager, DataIngestionConfig
from src.end_to_end_textSummarizer.components.data_ingestion import DataIngestion
from src.end_to_end_textSummarizer.logging import logger


class DataIngestionPipeline:
    def __init__(self):
        pass
    def initiate_data_ingestion(self):
        config=ConfigurationManager()
        data_ingestion_config=config.get_data_ingestion_config()
        data_ingestion=DataIngestion(config=data_ingestion_config)
        data_ingestion.extract_zip_file()