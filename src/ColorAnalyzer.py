"""
import cv2
import numpy as np


class ColorAnalyzer:
    def __init__(self):
        pass

    def get_dominant_color(self, path: str):
        img = cv2.imread(path)
        if img is None:
            raise ValueError(f'Could not load image')

        img_resized = cv2.resize(img, (10, 10))

        avg_color = np.mean(img_resized, axis=(0, 1))
        blue, green, red = avg_color

        if red > green and red > blue:
            return 'red'
        elif green > red and green > blue:
            return 'green'
        else:
            return 'blue'
"""