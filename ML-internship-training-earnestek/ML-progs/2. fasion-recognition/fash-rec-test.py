import tensorflow as tf
import matplotlib.pyplot as pyplot
import numpy as np

from tensorflow.keras.datasets import fashion_mnist

#load the dataset
(x_train, y_train) ,(x_test, y_test) = fashion_mnist.load_data()

test_image_number = 50 #This value must be changed for different pictures. Value can be anything between 0 and 59999

pyplot.imshow(x_test[test_image_number], cmap = pyplot.cm.binary)
pyplot.show()

trainedModel = tf.keras.models.load_model('fash-rec.model')

predictions = trainedModel.predict(x_test)

apparel_type = ["tshirt/top","trouser","pullover","dress","coat","sandal","shirt", "sneaker","bag","ankle boot"]
print(f"The apparel is a {apparel_type[np.argmax(predictions)]}")
