from src.image import *
from src.classifier import *
import random

# classifier = Classifier("classifier")
# classifier.classify("images")


# -----------


def calcular_promedio(img_path):
    img = cv2.imread(str(img_path))
    return tuple(np.mean(img, axis=(0, 1)))


def distancia_rgb(c1, c2):
    return np.linalg.norm(np.array(c1) - np.array(c2))


def obtener_mejor_match(color_objetivo, base_colores):
    return min(base_colores, key=lambda x: distancia_rgb(x[1], color_objetivo))[0]


# -----------

grid = 70

background = Image("images/cute.jpg")

x = background.width // grid
y = background.height // grid

background.show()

base_colores = [
    (ruta, calcular_promedio(ruta))
    for ruta in Path("classifier").rglob("*")
    if ruta.suffix.lower() in [".jpg", ".jpeg", ".png"]
]

for i in range(grid):
    for j in range(grid):
        x_1, x_2 = i * x, (i + 1) * x
        y_1, y_2 = j * y, (j + 1) * y

        matrix = background.img[y_1:y_2, x_1:x_2]
        sub_image = Image(matrix=matrix)

        bgr_avg = np.mean(sub_image.img, axis=(0, 1))
        random_file = obtener_mejor_match(bgr_avg, base_colores)

        new_image = Image(random_file)

        new_image.resize(sub_image.width, sub_image.height)

        background.overlap(new_image, x_1, y_1)

background.show()
cv2.imwrite("images/output.png", background.img)

# random_file = random.choice(
#    list(Path(f"classifier/{sub_image.get_color().name}").glob("*"))
# )
