from pathlib import Path


class ImageLoader:
    def __init__(self, directory: str):
        self.directory = Path(directory)

    def load_images(self, extensions=('.jpg', '.png', '.jpeg')):
        if not self.directory.exists():
            raise (FileNotFoundError
                   (f"The directory {self.directory} does not exist"))
        return [str(img)
                for img in self.directory.glob('*')
                if img.suffix.lower() in extensions]
