import easyocr
import cv2 as cv
import matplotlib.pyplot as plt
reader=easyocr.Reader(['en'])
final_digits=[]
def digit_recognition():
    output1=[]
    k=0
    for m in range(1,6,1):
        img=cv.imread(f"{m}.png")
        img=cv.resize(img,(100,100),cv.INTER_AREA)
        cv.imshow("image",img)
        output=reader.readtext(img)
        k=0
        cv.waitKey(0)
        for i in output:
            for j in i:
                k=k+1
                if k==2:
                    if(len(j)>1):
                        val=list(j)
                        final_digits.append(int(val[0]))
                    else:
                        final_digits.append(int(j))
                        print(j)
                 
def digit_extraction():
    x=2
    w=30
    y=9
    h=25
    for i in range(1,6,1):
        img=cv.imread("meter_image.png")
        roi = img[y:y + h, x:x + w]
        x=x+30
        cv.imwrite(str(i) + '.png', roi)
    digit_recognition()  

def image_crop():
    img=cv.imread("meter.jpg")
    plt.imshow(img[90:130,25:175])
    img=img[90:130,25:175]
    cv.imwrite('meter_image.png', img)
    digit_extraction()
    
if __name__=="__main__":
    image_crop()
    with open('data.txt', 'w') as f:
        f.write(str(final_digits))
   


