from dataclasses import dataclass 
from pathlib import Path

@dataclass## with @dataclass, Python automatically generates: constructor , __init___ and all 
class DataIngestionConfig:
    root_dir: Path
    local_data_file: Path
    unzip_dir: Path