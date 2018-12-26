import tensorflow as tf
import matplotlib.pyplot as plt

#import dataset
mnist = tf.keras.datasets.mnist

#load dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()
#print(x_train) #Return RGB value of each picture

#normalize the data
x_train = x_train/255.0#tf.keras.utils.normalize(x_train, axis = 1)
y_train = y_train/255.0#tf.keras.utils.normalize(y_train, axis = 1)

#print(x_train.shape())
#create a model, i.e, input layer

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten(input_shape = (28,28)))

#creating hidden layers
model.add(tf.keras.layers.Dense(300, activation = tf.nn.relu )) #args(no. of neurons, activation function)