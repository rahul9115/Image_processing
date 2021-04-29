import cv2 as cv
import matplotlib.pyplot as plt
img=cv.imread("Capture2.PNG")
plt.imshow(img)
img=img[70:90,80:180]
x=0
w=20
#y=9
#h=25
y=0
h=20
for i in range(1,6,1):
        
        roi = img[y:y + h, x:x + w]

        x=x+w
        cv.imwrite(str(i) + '.png', roi)
plt.imshow(img)
plt.show()