from errno import EXDEV
from heapq import heappush
import logging
from tkinter import E

from sklearn.metrics import homogeneity_score
from housing.entity.config_entity import DataIngestionConfig, DataValidationConfig, \
                                        DataTranformationConfig, ModelTrainingConfig, ModelEvaluationCOnfig, \
                                        ModelPusherConfig, TrainingPipelineConfig, TrainingPipelineConfig
from housing.util.util import read_yaml_file
import sys, os
from housing.constants import *
from housing.exception import HousingException
from housing.logger import logging


class Configuration:

    def __init__(self, config_file_path: str =CONFIG_FILE_PATH, current_time_stamp:str = CURRENT_TIME_STAMP) -> None:
        try:
            self.config_info = read_yaml_file(file_path=config_file_path)
            self.training_pipeline_config = self.get_training_pipeline_config()
            self.time_stamp = current_time_stamp
        except Exception as e:
            raise HousingException(e, sys) from e

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        try:
            data_ingestion_config = self.config_info[DATA_INGESTION_CONFIG_KEY]
            data_ingestion_artifact_dir = os.path.join(
                self.training_pipeline_config.artifact_dir, 
                DATA_INGESTION_ARTIFACT_DIR, 
                self.time_stamp)
            dataset_download_url = data_ingestion_config[DATA_INGESTION_DOWNLOAD_URL_KEY]
            tgz_download_dir = os.path.join(
                data_ingestion_artifact_dir, data_ingestion_config[DATA_INGESTION_TGZ_DOWNLOAD_DIR_KEY]
                )
            raw_data_dir = os.path.join(
                data_ingestion_artifact_dir, data_ingestion_config[DATA_INGESTION_RAW_DATA_DIR_KEY]
            )
            ingested_data_dir = os.path.join(
                data_ingestion_artifact_dir, DATA_INGESTION_INGESTED_DIR_NAME_KEY
            )
            train_data_dir = os.path.join(
                ingested_data_dir, data_ingestion_config[DATA_INGESTION_TRAIN_DIR_KEY]
            )
            test_Data_Dir = os.path.join(
                ingested_data_dir, data_ingestion_config[DATA_INGESTION_TEST_DIR_KEY]
            )
            data_ingestion_config = DataIngestionConfig(
                dataset_download_url=dataset_download_url,
                tgz_download_dir = tgz_download_dir,
                raw_data_dir= raw_data_dir,
                train_data_dir= train_data_dir,
                test_Data_Dir= test_Data_Dir
            )
            logging.info(f"The data ingestion config : {data_ingestion_config}")
            return data_ingestion_config
        except Exception as e:
            raise HousingException(e,sys) from e
        
    def get_data_validation_config(self) -> DataValidationConfig:
        try:
            data_validation_config = self.config_info[DATA_VALIDATION_CONFIG_KEY]
            data_validation_artifact_dir = os.path.join(
                self.training_pipeline_config.artifact_dir, 
                data_validation_config[DATA_VALIDATION_ARTIFACT_DIR_NAME],
                self.time_stamp
            )
            schema_file_path = os.path.join(
                data_validation_artifact_dir, 
                
            )
            data_validation_config = DataValidationConfig(schema_file_path = schema_file_path)
            logging.info(f"The Data Validation Config : {data_validation_config}")
            return data_validation_config
        except Exception as e:
            raise HousingException(e,sys) from e

    def get_data_tranformation_config(self) -> DataTranformationConfig:
        try:
            pass
        except Exception as e:
            raise HousingException(e, sys) from e

    def get_model_trainer_config(self) -> ModelTrainingConfig:
        try:
            pass
        except Exception as e:
            raise HousingException(e, sys) from e

    def get_model_validation_config(self) -> ModelEvaluationCOnfig:
        try:
            pass
        except Exception as e:
            raise HousingException(e, sys) from e

    def get_model_pusher_config(self) -> ModelPusherConfig:
        try:
            pass
        except Exception as e:
            raise HousingException(e, sys) from e

    def get_training_pipeline_config(self) -> TrainingPipelineConfig:
        try:
            training_pipeline_config = self.config_info[TRAINING_PIPELINE_CONFIG_KEY]
            artifact_dir = os.path.join(ROOT_DIR, 
                                        training_pipeline_config[TRAINING_PIPELINE_NAME_KEY],
                                        training_pipeline_config[TRAINING_PIPELINE_ARTIFACT_DIR_KEY])
            training_pipeline_config = TrainingPipelineConfig(artifact_dir= artifact_dir)
            logging.info(f"Training pipeline config : {training_pipeline_config}")
            return training_pipeline_config
        except Exception as e:
            raise HousingException(e,sys) from e