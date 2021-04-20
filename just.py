import cv2 as cv
import matplotlib.pyplot as plt
import easyocr
import pytesseract
import tensorflow as tf

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
reader=easyocr.Reader(['en'])
img=cv.imread("4.png")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("hola",img)
cv.waitKey(0)
ocr_result = pytesseract.image_to_string(img)
edges = cv.Canny(gray,100,200)







cv.imshow("yo",edges)
cv.waitKey(0)
output=reader.readtext(edges,allowlist="0123456789")
print(ocr_result,output)