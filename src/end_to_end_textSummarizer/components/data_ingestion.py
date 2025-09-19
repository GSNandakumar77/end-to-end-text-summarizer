import os
import zipfile
from src.end_to_end_textSummarizer.logging import logger
from src.end_to_end_textSummarizer.entity import DataIngestionConfig

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config

    def extract_zip_file(self):
        '''
        zip_file_path
        extracts the zip file into data directory'''

        unzip_file_path=self.config.unzip_dir
        os.makedirs(unzip_file_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_file_path)
