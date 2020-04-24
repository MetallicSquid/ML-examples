# The digit recognition model

# Necessary imports
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

from keras.datasets import mnist
def build_model(epochs=10):
    # Gather the dataset and split it into train and test sets, normalize this data between 0 and 1
    (image_train, label_train), (image_test, label_test) = mnist.load_data()
    image_train = image_train / 255.0
    image_test = image_test / 255.0

    # Build the model
    model = keras.Sequential([
        keras.layers.Flatten(input_shape=(28, 28)),
        keras.layers.Dense(128, activation='relu'),
        keras.layers.Dense(10)
    ])

    model.compile(optimizer='adam',
            loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
            metrics=['accuracy'])

    # Train the model on the train dataset and print the accuracy and loss
    model.fit(image_train, label_train, epochs=10)
    test_loss, test_acc = model.evaluate(image_test, label_test, verbose=2)

    print('\nTest accuracy: ', test_acc, '\nTest loss:', test_loss)

    # Make a predictor model
    prob_model = tf.keras.Sequential([model,
        tf.keras.layers.Softmax()])

    # Return the model as the output of the `build_model` function
    return [image_test, label_test, prob_model]
