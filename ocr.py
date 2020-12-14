# default imports
try:
    from PIL import Image
except ImportError:
    import Image
import re
import pytesseract
import cv2 as cv
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
ocr_result = pytesseract.image_to_string(Image.open('download (2).jpg'), lang='eng')
print(ocr_result)
img=cv.imread("download (2).jpg")
cv.imshow("Image",img)
cv.waitKey(0)