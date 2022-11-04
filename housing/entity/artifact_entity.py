from collections import namedtuple

DataIngestionArtifact = namedtuple("DataIngestionArtifact",["is_ingested","train_file_path","test_file_path","message"])

DataValidationArtifact = namedtuple("DataValidationArtifact",
["schema_file_path","report_file_path","report_page_file_path","is_validated","message"])

DataTransformationArtifact = namedtuple("DataTransformationArtifact",
["is_transformed","message","transformed_train_file_path","transformed_test_file_path","preprocessed_object_file_path"] )

