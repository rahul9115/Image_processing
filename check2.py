import easyocr
import cv2 as cv
reader=easyocr.Reader(['en'])

output1=[]
k=0
img=cv.imread("4.png")
img=cv.resize(img,(45,45),cv.INTER_AREA)
cv.imshow("image",img)
for m in range(1,6,1):
    img=cv.imread(f"{m}.png")
    img=cv.resize(img,(100,100),cv.INTER_AREA)
    cv.imshow("image",img)
    output=reader.readtext(img)
    k=0
    
    for i in output:
        for j in i:
            k=k+1
            if k==2:
                print(j)
cv.waitKey(0)