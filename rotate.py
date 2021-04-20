import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('meter.jpg',0)
window_name = 'Image'
image = cv.rotate(img, cv.ROTATE_180) 
cv.imshow(window_name, image) 
cv.waitKey(0)