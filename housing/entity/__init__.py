from collections import namedtuple
from tkinter import Y




DataIngestionConfig =namedtuple("DataIngestionConfig",["datast_download_url","tgz_download_dir","raw_data_dir","ingested_test_dir"])


DataValidationConfig =namedtuple("DataValidationConfig",["schema_file_path"])

DtaTransformationConfig = namedtuple("DtaTransformationConfig", ["add_bedroom_per_room","transformed_train_dir","transform_test_dir","preprocessed_object_file_path"])




ModelTrainerConfig = namedtuple("ModelTrainerConfig",["train_model_path","base_accuracy"])


ModelEvaluationConfig = namedtuple("ModelEvaluationConfig",["model_evaluation_file_path","time_stamp"])
 

ModelPushConfig = namedtuple("ModelPushConfig", ["export_dir_path"])

