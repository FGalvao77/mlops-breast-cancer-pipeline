from __future__ import annotations
from pathlib import Path
import yaml 

def load_config(file_path:str | Path, default:dict=None) -> dict:
    try:
        with open(file=file_path, mode='r', encoding='utf-8') as file:
            config = yaml.safe_load(stream=file)
    except FileNotFoundError:
        fp = Path(file_path)
        if not fp.is_absolute():
            alt = Path(__file__).parent / fp
            with open(file=alt, mode='r', encoding='utf-8') as file:
                config = yaml.safe_load(stream=file)
        else:
            raise
    
    if config is None:
        config = default
    
    return config   