import cv2 as cv
import numpy as np
import sys

img = cv.imread("img/green.png")

if img is None:
    sys.exit("Could not read the images.")

cv.imshow("Display window", img)

avg_row = np.average(img, axis=0)
avg = np.average(avg_row, axis=0)
avg_round = np.ceil(avg)

print("avg = " + str(avg_round))
