# Imports
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras

def build_model(full_data, full_labels, epochs=10):
    # Load and split data
    full_data = np.load('data.npy')
    full_labels = np.load('labels.npy')

    trainLen = round(len(fullData) * 0.8)

    trainData = full_data[:trainLen] / 255.0
    trainLabels = full_labels[:trainLen]
    testData = full_data[trainLen:] / 255.0
    testLabels = full_labels[trainLen:]

    width = trainData[0].shape[0]
    height = trainData[0].shape[1]

    # Build the model
    model = keras.Sequential([
        keras.layers.Flatten(input_shape=(width, height)),
        keras.layers.Dense(256, activation='relu'),
        keras.layers.Dense(3)
    ])

    model.compile(optimizer='adam',
            loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
            metrics=['accuracy'])

    # Train the model on the train dataset and print the accuracy and loss
    model.fit(trainData, trainLabels, epochs=50)
    test_loss, test_acc = model.evaluate(testData, testLabels, verbose=2)

    print('\nTest accuracy: ',  test_acc, '\nTest loss:', test_loss)

    # Make a predictor model
    prob_model = tf.keras.Sequential([model,
        tf.keras.layers.Softmax()])

    # Return the model as the output of the `build_model` function
    return [testData, testLabels, prob_model]
