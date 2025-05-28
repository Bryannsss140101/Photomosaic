import cv2
import numpy as np
from enum import Enum
from pathlib import Path


class Color(Enum):
    BLUE = 1
    GREEN = 2
    RED = 3


class Image:
    def __init__(self, file=None, matrix=None):
        if matrix is None:
            self.file = Path(file)
            self.img = cv2.imread(self.file)
        else:
            self.img = matrix

        if self.img is None:
            raise ValueError("Could not load the image")

        self.height, self.width = self.img.shape[:2]
        self.aspect_ratio = self.width / self.height

    def get_color(self):
        rimg = cv2.resize(
            self.img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR
        )

        avg_color = np.mean(rimg, axis=(0, 1))
        b, g, r = avg_color

        return max(
            (Color.BLUE, b), (Color.GREEN, g), (Color.RED, r), key=lambda x: x[1]
        )[0]

    def resize(self, width, height):
        self.img = cv2.resize(self.img, (width, height))
        self.height, self.width = width, height

    def overlap(self, image, x=0, y=0):
        if x + image.width > self.width or y + image.height > self.height:
            raise ValueError("The image cannot be overlaid")

        self.img[y : y + image.height, x : x + image.width] = image.img

    def show(self, name="Window"):
        cv2.imshow(name, self.img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
