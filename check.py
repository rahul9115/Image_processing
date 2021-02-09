import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
# opencv loads the image in BGR, convert it to RGB
img=cv.imread("meter.jpg")
plt.imshow(img[90:130,25:175])
img=img[90:130,25:175]

cv.imwrite('meter_image.png', img)
plt.show()
