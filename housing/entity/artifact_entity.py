from collections import namedtuple

DataIngestionArtifact = namedtuple("DataIngestionArtifact",["is_ingested","train_file_path","test_file_path","message"])

DataValidationArtifact = namedtuple("DataValidationArtifact",
["schema_file_path","report_file_path","report_page_file_path","is_validated","message"])

