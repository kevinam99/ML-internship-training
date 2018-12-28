import tensorflow as tf
import matplotlib.pyplot as pyplot
import numpy as np

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

#show image and the label (for my reference)
pyplot.imshow(x_test[60], cmap = pyplot.cm.binary)
pyplot.show()
print(y_test[60])

#load a previously trained model
trainedModel = tf.keras.models.load_model('digit-prediction.model')

predictions = trainedModel.predict([x_test])
print(np.argmax(predictions[60]))#to find number with highest probability
