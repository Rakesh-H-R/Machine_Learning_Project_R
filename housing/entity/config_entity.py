from collections import namedtuple
from unicodedata import name

DataIngestionConfig = namedtuple(
    "DataIngestionConfig",
        ['dataset_download_url','tgz_download_dir','raw_data_dir','train_data_dir','test_Data_Dir']
    )

DataValidationConfig = namedtuple(
    "DataValidationConfig",
        ["schema_file_path","report_file_path","report_page_file_path"]
)

DataTranformationConfig = namedtuple(
    "DataTranformationConfig",
        ["add_bedroom_per_room","transformed_train_dir","transformed_test_dir","preprocessed_object_file_path"]
)

ModelTrainingConfig = namedtuple(
    "ModelTrainingConfig",
        ["trained_model_file_path","base_accuracy"]
)

ModelEvaluationCOnfig = namedtuple(
    "ModelEvaluationCOnfig",
        ["model_Evaluation_file_path","time_stamp"]
)

ModelPusherConfig = namedtuple(
    "ModelPusherConfig",
        ["export_dir_path"]
)

TrainingPipelineConfig = namedtuple(
    "TrainingPipelineConfig",
        ["artifact_dir"]
)