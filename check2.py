import easyocr
import cv2 as cv
import matplotlib.pyplot as plt
reader=easyocr.Reader(['en'])
final_digits=[]
def digit_recognition():
    output1=[]
    k=0
    for m in range(1,7,1):
        img=cv.imread(f"{m}.png")
        img=cv.resize(img,(120,120),cv.INTER_AREA)
        cv.imshow("image",img)
        output=reader.readtext(img,allowlist="0123456789")
        k=0
        cv.waitKey(0)
        for i in output:
            for j in i:
                k=k+1
                if k==2:
                    if(len(j)>1):
                        val=list(j)
                        final_digits.append(int(val[0]))
                    elif (j!=''):
                        final_digits.append(int(j))
                        print(j)
                 
def digit_extraction():
    x=5
    w=28
    #y=9
    #h=25
    y=5
    h=40
    #Capture image 6 values x=5 w=28 y=5 h=40
    #Capture image 6 values x=5 w=45 y=5 h=50
    #Capture image 5 values x=5 w=45 y=0 h=50
    #Capture image 4 values x=28 w=25 y=0 h=35
    #Capture image 3 values x=0 w=27 y=0 h=40
    #Capture image 2 values x=0 w=20 y=9 h=25
    #Capture x=0 w=17 y=0 h=15


    
    for i in range(1,7,1):
        img=cv.imread("meter_image.png")
        roi = img[y:y + h, x:x + w]
        x=x+w
        cv.imwrite(str(i) + '.png', roi)
    digit_recognition()  

def image_crop():
    img=cv.imread("Capture6.PNG")
    img=img[52:78,30:200]
    plt.imshow(img)
    plt.show()
    cv.waitKey(0)
    #img=img[90:140,56:343]Capture5
    #img=img[70:110,70:280]Capture 4
    #img=img[70:110,80:280]Capture3
    #img=img[70:90,80:180]Capture2
    #plt.imshow(img[90:130,25:175]) meter.jpg
    #img=img[90:130,25:175]
    cv.imwrite('meter_image.png', img)
    digit_extraction()
    
if __name__=="__main__":
    image_crop()
    with open('data.txt', 'w') as f:
        f.write(str(final_digits))