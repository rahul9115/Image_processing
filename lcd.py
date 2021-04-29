import cv2 as cv
import matplotlib.pyplot as plt
img=cv.imread("gas_meter1.jpeg")

img=img[331:421,200:720]
plt.imshow(img)
x=0
w=60
#y=9
#h=25
y=0
h=100
for i in range(1,9,1):
        
        roi = img[y:y + h, x:x + w]

        x=x+w
        cv.imwrite(str(i) + '.png', roi)
plt.imshow(img)
plt.show()