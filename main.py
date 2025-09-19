from src.end_to_end_textSummarizer.logging import logger
from src.end_to_end_textSummarizer.pipeline.stage_1_data_ingestion_pipeline import DataIngestionPipeline



STAGE_NAME="Data Ingestion stage"

try:
    logger.info(f"stage {STAGE_NAME} initiated")
    data_ingestion_pipeline=DataIngestionPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info(f"stage {STAGE_NAME} Completed")

except Exception as e:
    logger.exception(e)
    raise e