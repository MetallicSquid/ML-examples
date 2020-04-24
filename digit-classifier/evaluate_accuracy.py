# Evaluate the accuracy of the model's predictions

# Import the `build_model` function from `build_model.py`
from build_model import build_model
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# Load the built model
image_test, label_test, prob_model = build_model()

predictions = prob_model.predict(image_test)

# A list of class names
class_names = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

# Plot the predictions (taken from tensorflow classification tutorial)
def plot_image(i, predictions_array, true_label, img):
    predictions_array, true_label, img = predictions_array, true_label[i], img[i]
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])

    plt.imshow(img, cmap=plt.cm.binary)

    predicted_label = np.argmax(predictions_array)
    if predicted_label == true_label:
        colour = 'blue'
    else:
        colour = 'red'

    plt.xlabel("{} {:2.0f} ({})".format(class_names[predicted_label],
        100*np.max(predictions_array),
        class_names[true_label]),
        color=colour)

def plot_value_array(i, predictions_array, true_label):
    predictions_array, true_label = predictions_array, true_label[i]
    plt.grid(False)
    plt.xticks(range(10))
    plt.yticks([])
    thisplot = plt.bar(range(10), predictions_array, color='#777777')
    plt.ylim([0, 1])
    predicted_label = np.argmax(predictions_array)

    thisplot[predicted_label].set_color('red')
    thisplot[true_label].set_color('blue')

# NB: Press 'q' to move to the next digit in the prediction
for i in range(25):
    plt.figure(figsize=(6, 3))
    plt.subplot(1, 2, 1)
    plot_image(i, predictions[i], label_test, image_test)
    plt.subplot(1, 2, 2)
    plot_value_array(i, predictions[i], label_test)
    plt.show()
