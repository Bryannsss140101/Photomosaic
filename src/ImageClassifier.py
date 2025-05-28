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

from pathlib import Path


class ImageLoader:
    def __init__(self, directory: str):
        self.directory = Path(directory)

    def load_images(self, ):
        if not self.directory.exists():
            raise (FileNotFoundError
                   (f"The directory {self.directory} does not exist"))
        return [str(img)
                for img in self.directory.glob('*')
                if img.suffix.lower() in extensions]
"""