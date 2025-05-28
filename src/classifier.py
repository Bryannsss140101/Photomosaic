import shutil
from pathlib import Path
from src.image import *


class Classifier:
    def __init__(self, directory):
        self.directory = Path(directory)

        for color in ["red", "green", "blue"]:
            folder = self.directory / color
            folder.mkdir(parents=True, exist_ok=True)

    def classify(self, directory, extensions=(".jpg", ".png", ".jpeg")):
        directory = Path(directory)

        if not directory.exists():
            raise (FileNotFoundError(f"The directory '{directory}' does not exist"))

        for file in directory.glob("*"):
            if file.suffix.lower() in extensions:
                image = Image(file)
                path = self.directory / image.get_color().name / Path(file).name
                shutil.copy(file, path)

    """
    def __init__(self, directory: str):
        self.directory = Path(directory)
        for color in ["red", "green", "blue"]:
            folder = self.directory / color
            folder.mkdir(parents=True, exist_ok=True)

    def classify(self, path: str, color: str):
        target_folder = self.output_directory / color
        target_path = target_folder / Path(path).name
        shutil.copy(path, target_path)
    """
