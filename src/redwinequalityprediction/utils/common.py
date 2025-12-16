import os
import yaml
import joblib
import json
from typing import Any, List
from pathlib import Path
from box import ConfigBox
from box.exceptions import BoxValueError
from ensure import ensure_annotations
from redwinequalityprediction import logger


@ensure_annotations
def create_directories(dir_paths: List[str]) -> None:
    """
    Create multiple directories if they don't exist.
    Args:
        dir_paths (List[str]): List of directory paths to create.
    """
    for path in dir_paths:
        os.makedirs(path, exist_ok=True)
        logger.info(f"Directory created at: {path}")


@ensure_annotations
def read_yaml(file_path: str) -> ConfigBox:
    """
    Read a YAML file and return its contents as a ConfigBox (dict-like).
    Args:
        file_path (str): Path to the YAML file.
    Returns:
        ConfigBox: Parsed YAML content.
    """
    try:
        with open(file_path, "r") as f:
            content = yaml.safe_load(f)
        logger.info(f"YAML file loaded successfully from: {file_path}")
        return ConfigBox(content)
    except BoxValueError as e:
        logger.error(f"Error reading YAML file {file_path}: {e}")
        raise e


@ensure_annotations
def save_json(file_path: str, data: dict) -> None:
    """Save a dictionary to a JSON file."""
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"JSON file saved at: {file_path}")


@ensure_annotations
def save_object(file_path: str, obj: Any) -> None:
    """Save a Python object (like a model) using joblib."""
    joblib.dump(obj, file_path)
    logger.info(f"Object saved at: {file_path}")


@ensure_annotations
def load_object(file_path: str) -> Any:
    """Load a Python object (like a model) using joblib."""
    obj = joblib.load(file_path)
    logger.info(f"Object loaded from: {file_path}")
    return obj