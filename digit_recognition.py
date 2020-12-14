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
model=tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten(input_shape=(28,28)))
model.add(tf.keras.layers.Dense(units=128,activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(units=128,activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(units=10,activation=tf.nn.softmax))
model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
model.fit(x_train,y_train,epochs=3)
accuracy,loss=model.evaluate(x_test,y_test)
print(accuracy,loss)
model.save('digits.model')
new_model=tf.keras.models.load_model('digits.model')
for i in range(0,4,1):
    '''
    img=cv.imread(f"{i}.png")
    img=cv.resize(img,(28,28))
    print("The resized image is : ",np.asarray(img))
    data=np.asarray(img)
    data=data.reshape(3,28,28)
    '''
    predictions=new_model.predict([x_test])
    print(f'The prdicted number is : {np.argmax(predictions[i])}')
    plt.imshow(x_test[i])
    plt.show()
        