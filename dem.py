from insurance.pipeline.pipeline import Pipeline
from insurance.exception import InsuranceException
from insurance.logger import logging
from insurance.config.configuration import Configuartion
from insurance.components.data_transformation import DataTransformation
from insurance.constant import CONFIG_DIR, get_current_time_stamp
import os, sys

ROOT_DIR = os.getcwd()
# log dir issue fiexed
LOG_FOLDER_NAME = "logs"
PIPELINE_FOLDER_NAME = "insurance"
SAVED_MODELS_DIR_NAME = "saved_models"
MODEL_CONFIG_FILE_PATH = os.path.join(ROOT_DIR, CONFIG_DIR, "model.yaml")
LOG_DIR = os.path.join(ROOT_DIR, LOG_FOLDER_NAME)
PIPELINE_DIR = os.path.join(ROOT_DIR, PIPELINE_FOLDER_NAME)
MODEL_DIR = os.path.join(ROOT_DIR, SAVED_MODELS_DIR_NAME)
CONFIG_FILE_PATH = os.path.join(ROOT_DIR, CONFIG_DIR, "config.yaml")


def main():
    try:
        pipeline = Pipeline(config=Configuartion(current_time_stamp=get_current_time_stamp()))
        pipeline.run_pipeline()
        
    except Exception as e:
        logging.error(f"{e}")
        print(e)



if __name__=="__main__":
    main()