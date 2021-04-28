import cv2 as cv
import matplotlib.pyplot as plt
img=cv.imread("Capture6.PNG")
plt.imshow(img)
img=img[52:78,30:200]
x=5
w=26
#y=9
#h=25
y=5
h=40
for i in range(1,7,1):
        
        roi = img[y:y + h, x:x + w]

        x=x+w
        cv.imwrite(str(i) + '.png', roi)
plt.imshow(img)
plt.show()