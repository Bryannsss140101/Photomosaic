from ImageLoader import ImageLoader
from ColorAnalyzer import ColorAnalyzer
from ImageClassifier import ImageClassifier

loader: ImageLoader = ImageLoader('images/')
analyzer: ColorAnalyzer = ColorAnalyzer()
classifier: ImageClassifier = ImageClassifier('classifier')

images = loader.load_images()

for path_image in images:
    color_dominant = analyzer.get_dominant_color(path_image)
    classifier.classify(path_image, color_dominant)