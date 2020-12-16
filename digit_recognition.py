import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from scipy import misc
from PIL import Image
mnist=tf.keras.datasets.mnist
(x_train,y_train),(x_test,y_test)=mnist.load_data()
x_train=tf.keras.utils.normalize(x_train,axis=1)
x_test=tf.keras.utils.normalize(x_test,axis=1)
img_size=28
x_trainr=np.array(x_train).reshape(-1,img_size,img_size,1)
x_testr=np.array(x_test).reshape(-1,img_size,img_size,1)
model=tf.keras.models.Sequential()
model.add(tf.keras.layers.Conv2D(64,(3,3),input_shape=x_trainr.shape[1:]))
model.add(tf.keras.layers.Activation("relu"))
model.add(tf.keras.layers.MaxPooling2D(pool_size=(2,2)))
model.add(tf.keras.layers.Conv2D(64,(3,3)))
model.add(tf.keras.layers.Activation("relu"))
model.add(tf.keras.layers.MaxPooling2D(pool_size=(2,2)))
model.add(tf.keras.layers.Conv2D(64,(3,3)))
model.add(tf.keras.layers.Activation("relu"))
model.add(tf.keras.layers.MaxPooling2D(pool_size=(2,2)))
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(32))
model.add(tf.keras.layers.Activation("relu"))
model.add(tf.keras.layers.Dense(10))
model.add(tf.keras.layers.Activation("softmax"))
model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
model.fit(x_trainr,y_train,epochs=3,validation_split=0.3)
accuracy,loss=model.evaluate(x_testr,y_test)
print(accuracy,loss)
model.save('digits.model')
new_model=tf.keras.models.load_model('digits.model')
for i in range(1,4,1):
    img=cv.imread(f"{i}.png")
    img=cv.resize(img,(28,28))
    img=tf.keras.utils.normalize(img,axis=1)
    print("The resized image is : ",np.asarray(img))
    data=np.array(img).reshape(-1,28,28,1)
    predictions=new_model.predict([data])
    print(f'The prdicted number is : {np.argmax(predictions[0])}')
    plt.imshow(img)
    plt.show()
        