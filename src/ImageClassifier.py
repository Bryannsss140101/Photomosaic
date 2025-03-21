"""
import shutil
from pathlib import Path


class ImageClassifier:
    def __init__(self, output_directory: str):
        self.output_directory = Path(output_directory)
        self._prepare_directories()

    def _prepare_directories(self):
        for color in ['red', 'green', 'blue']:
            folder = self.output_directory / color
            folder.mkdir(parents=True, exist_ok=True)

    def classify(self, path: str, color: str):
        target_folder = self.output_directory / color
        target_path = target_folder / Path(path).name
        shutil.copy(path, target_path)
"""