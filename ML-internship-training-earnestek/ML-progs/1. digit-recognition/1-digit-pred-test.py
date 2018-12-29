import tensorflow as tf
import matplotlib.pyplot as pyplot
import numpy as np

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

test_image_number = 60 #Muat be changed for testing other images. The value can be anywhere between 0 and 59999

#show image and the label (for my reference)
pyplot.imshow(x_test[test_image_number], cmap = pyplot.cm.binary)
pyplot.show()
print(y_test[test_image_number])

#load a previously trained model
trainedModel = tf.keras.models.load_model('digit-prediction.model')

predictions = trainedModel.predict([x_test])
print(np.argmax(predictions[test_image_number]))#to find number with highest probability
