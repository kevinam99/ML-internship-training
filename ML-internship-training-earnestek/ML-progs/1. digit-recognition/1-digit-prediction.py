import tensorflow as tf
import matplotlib.pyplot as pyplot

#import dataset
mnist = tf.keras.datasets.mnist

#load dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

pyplot.imshow(x_train[10000], cmap = pyplot.cm.binary)
pyplot.show()
print(y_train[10000])
#print(x_train) #Return RGB value of each picture

""" #normalize the data
x_train = x_train/255.0
x_test = y_train/255.0
 """
x_train = tf.keras.utils.normalize(x_train, axis = 1)
x_test = tf.keras.utils.normalize(x_test, axis = 1)


print(x_train.shape)
#define the neural network

model = tf.keras.models.Sequential() #Sequential - Type of neural network to be built
model.add(tf.keras.layers.Flatten(input_shape = (28,28)))

#creating hidden layers
model.add(tf.keras.layers.Dense(128, activation = tf.nn.relu )) #args(no. of neurons, activation function)
model.add(tf.keras.layers.Dense(128, activation = tf.nn.relu ))
model.add(tf.keras.layers.Dense(10, activation = tf.nn.softmax )) #10 neurons since there are only ten digits in total to be predicted

model.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])#compiles the neural network
model.fit(x_train, y_train, epochs = 3)#gives the data and tells the neural network to run the number of epochs.

val_loss, val_acc = model.evaluate(x_test, y_test)
print(val_loss, val_acc)

model.save('digit-prediction.model')