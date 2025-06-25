from src.data_ingestion import DataIngestion
from src.data_preprocessing import DataProcessor
from src.model_training import ModelTraining
from config.paths_config import *
from utils.common_functions import read_yaml


if __name__=="__main__":

    ## Data Ingestion
    data_ingestion=DataIngestion(read_yaml(config_path))
    data_ingestion.run()

    ## Data Preprocessing
    processor=DataProcessor(TRAIN_FILE_PATH,TEST_FILE_PATH,PROCESSED_DIR,config_path)
    processor.process()

    ##Model Training
    trainer=ModelTraining(PROCESSED_TRAIN_DATA_PATH,PROCESSED_TEST_DATA_PATH,MODEL_OUTPUT_PATH)
    trainer.run()