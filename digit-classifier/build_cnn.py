# The digit recognition model

# Necessary imports
import tensorflow as tf
from tensorflow import keras
import numpy as np

from keras.datasets import mnist
def build_model(epochs=10):
    # Gather the dataset and split it into train and test sets, normalize this data between 0 and 1
    (image_train, label_train), (image_test, label_test) = mnist.load_data()
    image_train = image_train / 255.0
    image_test = image_test / 255.0

    train_rows = image_train[0].shape[0]
    train_cols = image_train[0].shape[1]
    image_train = image_train.reshape(image_train.shape[0], train_rows, train_cols, 1)
    image_test = image_test.reshape(image_test.shape[0], train_rows, train_cols, 1)

    # Build the model
    # Set up base layers
    model = keras.Sequential()
    model.add(keras.layers.Conv2D(28, (3, 3), activation='relu', input_shape=(train_rows, train_cols, 1)))
    model.add(keras.layers.MaxPooling2D((2, 2)))
    model.add(keras.layers.Conv2D(56, (3, 3), activation='relu'))
    model.add(keras.layers.MaxPooling2D((2, 2)))
    model.add(keras.layers.Conv2D(56, (3, 3), activation='relu'))

    # Set up the dense layers
    model.add(keras.layers.Flatten())
    model.add(keras.layers.Dense(112, activation='relu'))
    model.add(keras.layers.Dense(10))
    #print(model.summary())

    # Compile the model
    model.compile(optimizer='adam',
            loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
            metrics=['accuracy'])

    # Train the model
    model.fit(image_train, label_train, epochs=epochs, validation_data=(image_test, label_test))

    print(model.evaluate(image_test, label_test, verbose=2))

    # Evaluate the accuracy
    test_loss, test_acc = model.evaluate(image_test, label_test, verbose=2)
    print('\nTest accuracy: ', test_acc, '\nTest loss:', test_loss)

    # Make a predictor model
    prob_model = tf.keras.Sequential([model,
        tf.keras.layers.Softmax()])

    # Return the model as the output of the `build_model` function
    return [image_test, label_test, prob_model]
