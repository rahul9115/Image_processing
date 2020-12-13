from PIL import Image
import os
img=Image.open("download.jpg").convert("L")
img.show()
filelist=["download.jpg","download (1).jpg"]
for i in filelist:
    o=os.path.splitext(i)[0]+".png"
    if i!=o:
        try:
            Image.open(i).save(o)
        except:
            print("Cannot convert the file")    