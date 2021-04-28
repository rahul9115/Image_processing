import cv2 as cv
import matplotlib.pyplot as plt
img=cv.imread("Capture4.PNG")
plt.imshow(img)
img=img[70:110,70:280]
x=28
w=25
#y=9
#h=25
y=0
h=35
for i in range(1,7,1):
        
        roi = img[y:y + h, x:x + w]

        x=x+w
        cv.imwrite(str(i) + '.png', roi)
plt.imshow(img)
plt.show()