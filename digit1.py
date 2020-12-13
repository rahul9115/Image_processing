from sklearn import datasets
from sklearn.svm import SVC
import cv2 as cv
from scipy import misc
import imageio
import skimage.util
digits=datasets.load_digits()
features=digits.data
labels=digits.target
clf=SVC(gamma=0.001)
clf.fit(features,labels)
img=imageio.imread("2.png")
img=img.astype(digits.images.dtype)
img=cv.resize(img,(8,8))
x_test=[]
print(clf.predict(img))
