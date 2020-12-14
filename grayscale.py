from PIL import Image
import os
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
img=cv.imread("download.png")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Original image',img)
cv.imshow('Gray image', gray)
cv.waitKey(0)