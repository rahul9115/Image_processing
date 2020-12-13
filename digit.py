import os
import gzip
import urllib.request
import numpy as np
import matplotlib as pl
import matplotlib.pyplot as plt
def load_dataset():
    def download(filename,source="http://yann.lecun.com/exdb/mnist/"):
        print("Downloading",filename)
        urllib.request.urlretrieve(source+filename,filename)
    def load_mnist_images(filename):
        if not os.path.exists(filename):
            download(filename)
        with gzip.open(filename,"rb") as f:
            data=np.frombuffer(f.read(),np.uint8,offset=16)
            #boiler plate to extract data from the zip file
            data=data.reshape(-1,1,28,28)
        return data/np.float32(256) 
    def load_mnist_labels(filename):
        if not os.path.exists(filename):
            download(filename)
        with gzip.open(filename,"rb") as f:
            data=np.frombuffer(f.read(),np.uint8,offset=8)
            #boiler plate to extract data from the zip file

        return data
    X_train=load_mnist_images("train-images-idx3-ubyte.gz")
    Y_train=load_mnist_labels("train-labels-idx1-ubyte.gz")
    X_test=load_mnist_images("t10k-images-idx3-ubyte.gz")
    Y_test=load_mnist_labels("t10k-labels-idx1-ubyte.gz")
    return X_train,Y_train,X_test,Y_test
X_train,Y_train,X_test,Y_test=load_dataset()
pl.use("TkAgg")
plt.imshow(X_train[3][0])
plt.show()    