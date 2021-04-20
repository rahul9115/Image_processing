import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('hola.png')
imggray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
edges = cv.Canny(imggray,100,200)
ret,thresh=cv.threshold(edges,127,255,0)
edges = cv.Canny(img,100,200)
idx = 0
BLACK_THRESHOLD = 200
THIN_THRESHOLD = 10
contours,hierarchy=cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
print(f'Number of contours are: {len(contours)}')
x=2
w=30
y=9
h=25
for i in range(1,6,1):
    roi = img[y:y + h, x:x + w]
    x=x+30
    cv.imwrite(str(i) + '.png', roi)
    
plt.imshow(img)
cv.waitKey(0)