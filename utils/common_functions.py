import os
import pandas
from src.logger import get_logger
from src.custom_exception import CustomException
import yaml
import pandas as pd
logger=get_logger(__name__)

"""
A code to read the YAML file during data ingestion or data preprocessing.
"""
def read_yaml(file_path):
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError("File is not in the given path")
        
        with open(file_path,"r") as yaml_file:
            config=yaml.safe_load(yaml_file)
            logger.info("Successfully loaaded the YAML file")
            return config
        
    except Exception as e:
        logger.error("Error while reading the YAML file.")
        raise CustomException("Failed to read YAML file.",e)
    


def load_data(path):
    try:
        logger.info("Loading Data")
        chunks=pd.read_csv(path,chunksize=10000)
        df = pd.concat(chunks)                         # Combine to DataFrame
        return df


    except Exception as e:
        logger.error(f"Error while loading the data {e}")
        raise CustomException(f"Failed to load the data {e}")