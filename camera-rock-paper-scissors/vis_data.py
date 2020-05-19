# Command to visualise the data
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

full_data = np.load("data.npy")
full_labels = np.load("labels.npy")


plt.imshow(full_data[0], interpolation='nearest')

for i in range(10):
    print(full_labels[i])
    plt.imshow(full_data[i], interpolation='nearest')
    plt.show()
