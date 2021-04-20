import cv2 as cv
import matplotlib.pyplot as plt
import easyocr
img=cv.imread("hola.png")

reader=easyocr.Reader(['en'])

plt.imshow(img)
plt.show()
cv.waitKey(0)
x=72
w=21
y1=20
y2=92
final_digits=[]
def digit_recognition(img1):
    img1=cv.resize(img1,(100,100),cv.INTER_AREA)
    img1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
    cv.imshow("image",img1)
    cv.waitKey(0)
    
    output=reader.readtext(img1)
    print(output)
    k=0
    for i in output:
        for j in i:
            k=k+1
            if k==2:
                final_digits.append(int(j))
                print(j)
    return final_digits            
for i in range(1,6,1):
    img1=img[y1:y2,x:x+w]
    cv.imwrite(str(i)+".png",img1)
    digit_recognition(img1)
    x=x+w
print(final_digits)    
    
    



    