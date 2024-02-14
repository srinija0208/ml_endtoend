import pandas as pd
import numpy as np
from src.DimondPricePrediction.logger import logging
from src.DimondPricePrediction.exception import customexception

import os
import sys
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path

## configuration of the components

class DataIngestionConfig:
    raw_data_path:str=os.path.join("artifacts","raw.csv")
    train_data_path:str=os.path.join("artifacts","train.csv")
    test_data_path:str=os.path.join("artifacts","test.csv")


class DataIngestion():
    def __init__(self):
        ## object of data ingestion config
        self.ingestion_config=DataIngestionConfig()


class initiate_Data_Ingestion():
    def __init__(self):
        logging.info("data ingestion started")

        try:
            data=pd.read_csv(Path(os.path.join("notebooks/data","gemstone.csv")))
            logging.info("I have read the dataset as df")

            ## creating directory
            os.makedirs(os.path.dirname(raw_data_path),exist_ok=True)

            ## inside the dir saving data in the form of csv
            data.to_csv(self.ingestion_config.raw_data_path,index=False)
            logging.info("I have saved the raw dataset in artifacts folder")

            logging.info("I performed train test split")

            train_data,test_data=train_test_split(data,test_size=0.25)
            logging.info("train test split completed")

            ## saving the train and test data in csv
            train_data.to_csv(self.ingestion_config.train_data_path,index=False)
            test_data.to_csv(self.ingestion_config.test_data_path,index=False)

            logging.info("data ingestion part complted")

        except Exception as e:
            logging.info("exception occured at data ingestion stage")
            raise customexception(e,sys)

        