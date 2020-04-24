# Function to gather the MNIST handwritten digits dataset and split it train and test sets
from keras.datasets import mnist

def gather_dataset():
    (image_train, label_train), (image_test, label_test) = mnist.load_data()

    return [image_train, label_train, image_test, label_test]

print(gather_dataset())
