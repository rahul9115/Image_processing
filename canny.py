import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('meter.jpg')
imggray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
edges = cv.Canny(imggray,100,200)
ret,thresh=cv.threshold(edges,127,255,0)
edges = cv.Canny(img,100,200)
idx = 0
BLACK_THRESHOLD = 200
THIN_THRESHOLD = 10
contours,hierarchy=cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
print(f'Number of contours are: {len(contours)}')
image=cv.drawContours(img,contours,110,(0,255,0),3)
for cnt in contours:
    idx += 1
    x, y, w, h = cv.boundingRect(cnt)
    
    roi = img[y:y + h, x:x + w]
    

    if h < THIN_THRESHOLD or w < THIN_THRESHOLD:
        continue
    if(idx==110):
        cv.imwrite(str(idx) + '.png', roi)
        cv.rectangle(img, (x, y), (x + w, y + h), (200, 0, 0), 2)
cv.imshow("Image",img)
cv.waitKey(0)