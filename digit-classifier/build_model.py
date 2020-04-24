# Necessary imports
from keras.datasets import mnist

# Gather the dataset and split it into train and test sets
(image_train, label_train), (image_test, label_test) = mnist.load_data()

