"""
from ImageLoader import ImageLoader
from ColorAnalyzer import ColorAnalyzer
from ImageClassifier import ImageClassifier

loader: ImageLoader = ImageLoader('images/')
analyzer: ColorAnalyzer = ColorAnalyzer()
classifier: ImageClassifier = ImageClassifier('classifier')

images = loader.load_images()

for path_image in images:
    color_dominant = analyzer.get_dominant_color(path_image)
    classifier.classify(path_image, color_dominant)"
"""

from src.image import *
from pathlib import Path

img_1 = Image("Untitled.png")
img_2 = Image("1.png")

img_1.resize(400, 400)

divisions = 3

step_x, step_y = img_1.width // divisions, img_2.height // divisions


img_1.show()

for i in range(divisions):
    for j in range(divisions):
        x1, x2 = i * step_x, (i + 1) * step_x
        y1, y2 = j * step_y, (j + 1) * step_y

        region = img_1.img[y1:y2, x1:x2]

        sub_img = Image(matrix=region)

        sub_img.show("Region")

        print(sub_img.get_color())
