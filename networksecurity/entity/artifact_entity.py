from dataclasses import dataclasses

@dataclass
class DataIngestionArtifact:
    trained_file_path:str
    test_file_path:str 
    