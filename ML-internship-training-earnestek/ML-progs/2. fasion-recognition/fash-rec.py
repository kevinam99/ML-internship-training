import tensorflow as tf
import matplotlib.pyplot as pyplot

from keras.datasets import fashion_mnist

print('check1')
#load the datasets
(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()
print("check!")
#normalise
x_train = tf.keras.utils.normalize(x_train, axis =1)
x_test = tf.keras.utils.normalize(x_test, axis = 1)

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten(input_shape = (28,28)))

#creating layers
model.add(tf.keras.layers.Dense(100, activation = tf.nn.relu)) #input
model.add(tf.keras.layers.Dense(100, activation = tf.nn.relu))
model.add(tf.keras.layers.Dense(100, activation = tf.nn.relu))
model.add(tf.keras.layers.Dense(10, activation = tf.nn.softmax))#output

model.compile(optimizer = 'adam', loss = "sparse_categorical_crossentropy", metrics = ['accuracy'])
model.fit(x_train, y_train, epochs = 20)

model.save('fash-rec.model')

