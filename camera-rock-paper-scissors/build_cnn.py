# Imports
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras

ori_data = np.load('data.npy')
full_data = []
for element in range(len(ori_data)):
    width = int(ori_data[0].shape[0]/10.0)
    height = int(ori_data[0].shape[1]/10.0)
    array = ori_data[element]
    print(ori_data[element])
    full_data.append(array.resize((width, height)))

print(ori_data[0].shape)

full_labels = np.load('labels.npy')

def build_model(full_data, full_labels, epochs=10):
    # Load and split data

    trainLen = round(len(full_data) * 0.8)

    trainData = full_data[:trainLen] / 255.0
    trainLabels = full_labels[:trainLen]
    testData = full_data[trainLen:] / 255.0
    testLabels = full_labels[trainLen:]

    trainRows = trainData[0].shape[0]
    trainCols = trainData[0].shape[1]
    print(trainRows, trainCols)
    trainData = trainData.reshape(trainData.shape[0], trainRows, trainCols, 1)
    testData = testData.reshape(testData.shape[0], trainRows, trainCols, 1)

    # Build the model
    # Set up base layers
    model = keras.Sequential()
    model.add(keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(trainRows, trainCols, 1)))
    model.add(keras.layers.MaxPooling2D((2, 2)))
    model.add(keras.layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(keras.layers.MaxPooling2D((2, 2)))
    model.add(keras.layers.Conv2D(64, (3, 3), activation='relu'))

    # Set up the dense layers
    model.add(keras.layers.Flatten())
    model.add(keras.layers.Dense(128, activation='relu'))
    model.add(keras.layers.Dense(3))
    print(model.summary())

    # Compile the model
    model.compile(optimizer='adam',
            loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
            metrics=['accuracy'])

    # Train the model
    model.fit(trainData, trainLabels, epochs=epochs, validation_data=(testData, testLabels))
    print(model.evaluate(testData, testLabels, verbose=2))

    # Evaluate the accuracy
    test_loss, test_acc = model.evaluate(testData, testLabels, verbose=2)
    print('\nTest accuracy: ', test_acc, '\nTest loss:', test_loss)

    # Make a predictor model
    prob_model = tf.keras.Sequential([model,
        tf.keras.layers.Softmax()])

    # Return the model as the output of the `build_model` function
    return [testData, testLabels, prob_model]

# This runs up against the memory constraits, resize the image inputs
#build_model(full_data, full_labels, epochs=10)
