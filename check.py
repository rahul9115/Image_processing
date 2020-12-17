import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
# opencv loads the image in BGR, convert it to RGB
img=cv.imread("1.png")
img=cv.resize(img,(28,28))

plt.imshow(img)
plt.show()
