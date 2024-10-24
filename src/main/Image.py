import cv2 as cv
import numpy as np
import sys
import Color as RGB

img = cv.imread("../../img/random.jpg")

if img is None:
    sys.exit("Could not read the images.")

#cv.imshow("Display window", img)

#cv.waitKey(0)

avg_row = np.average(img, axis=0)
avg = np.average(avg_row, axis=0)

color = RGB.Color(avg)

print(color)
print(color.predominant_value())
print(color.predominant_chanel())