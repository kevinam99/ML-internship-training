import tensorflow as tf
import matplotlib.pyplot as pyplot
import numpy as np

from tensorflow.keras.datasets import fashion_mnist

def apparel(argmaxPred):
    apparel_type = {
        0: "tshirt/top",
        1: "trouser",
        2: "pullover",
        3: "dress",
        4: "coat",
        5: "sandal",
        6: "shirt",
        7: "sneaker",
        8: "bag",
        9: "ankle boot"
    }
    return apparel_type.get(argmaxPred)

#load the dataset

(x_train, y_train) ,(x_test, y_test) = fashion_mnist.load_data()

pyplot.imshow(x_test[40], cmap = pyplot.cm.binary)
pyplot.show()

trainedModel = tf.keras.models.load_model('fash-rec.model')

predictions = trainedModel.predict(x_test)

argMax = np.argmax(predictions[40])
print(f"The apparel is a {apparel(argMax)} muthafucka.")