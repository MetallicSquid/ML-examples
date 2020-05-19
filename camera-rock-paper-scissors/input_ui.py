###############
# Gather data #
###############

# Imports
import numpy as np
import tkinter as tk
import cv2
from PIL import ImageTk, Image
from random import randint

# Window setup
root = tk.Tk()
root.title('Rock, Paper, Scissors - Input')
root.config(background="#FFFFFF")
root.grid_rowconfigure(4, pad=10)

# Guidance message
message = tk.Label(root, text="Enter at least 20 samples of each gesture. There must be an equal number of samples.")
message.grid(row=0, column=0, columnspan=3)

# Quit
def quit_window():
    root.destroy()
quit = tk.Button(root, text="quit", command=quit_window)
quit.grid(row=0, column=3)

# Create training and test datasets
fullDataset = []
fullLabels = []

def compile_dataset():
    # NB: The use of a global variable is unfortunate but difficult to avoid
    global fullDataset
    global fullLabels

    newDataset = rockDataset + paperDataset + scissorsDataset
    newLabels = rockLabels + paperLabels + scissorsLabels
    if len(fullDataset) == len(newDataset):
        print("Already compiled")
    else:
        # Shuffle the data
        for element in range(len(newDataset)):
            randIndex = randint(0, element)
            dataElem = newDataset.pop(randIndex)
            labelElem = newLabels.pop(randIndex)
            newDataset.append(dataElem)
            newLabels.append(labelElem)

        fullDataset = np.asarray(newDataset)
        fullLabels = np.asarray(newLabels)

        print(fullDataset)
        print(fullLabels)

        # TEMP
        np.save('data.npy', fullDataset)
        np.save('labels.npy', fullLabels)


# Progress button
progress = tk.Button(root, text="compile dataset", command=compile_dataset)
progress.grid(row=3, column=3)
progress.config(state="disabled")

# Graphics window
imageFrame = tk.Frame(root, width=600, height=500)
imageFrame.grid(row=1, column=0, columnspan=4, padx=10, pady=2)

# Capture video frames
lmain = tk.Label(imageFrame)
lmain.grid(row=0, column=0)
cap = cv2.VideoCapture(0)

def show_frame():
    frame = cap.read()[1]
    frame = cv2.flip(frame, 1)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame)
show_frame()

def add_image(dataset):
    image = cap.read()[1]
    image = cv2.flip(image, 1)
    cv2image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    cv2image.resize((128, 128))
    dataset.append(cv2image)
    print(cv2image.shape)

# Rock
rockDataset = []
rockLabels = []
rockText = tk.StringVar()
rockText.set("0")
rockLabel = tk.Label(root, textvariable=rockText)
rockLabel.grid(row=2, column=0)
def input_rock():
    add_image(rockDataset)
    rockLabels.append(0)
    rockText.set(str(len(rockDataset)))
    if len(rockDataset) == len(paperDataset) == len(scissorsDataset) and len(rockDataset) >= 20:
        progress.config(state="normal")
    else:
        progress.config(state="disabled")
rock = tk.Button(root, text="rock", command=input_rock)
rock.grid(row=3, column=0)

# Paper
paperDataset = []
paperLabels = []
paperText = tk.StringVar()
paperText.set("0")
paperLabel = tk.Label(root, textvariable=paperText)
paperLabel.grid(row=2, column=1)
def input_paper():
    add_image(paperDataset)
    paperLabels.append(1)
    paperText.set(str(len(paperDataset)))
    if len(rockDataset) == len(paperDataset) == len(scissorsDataset) and len(rockDataset) >= 20:
        progress.config(state="normal")
    else:
        progress.config(state="disabled")
paper = tk.Button(root, text="paper", command=input_paper)
paper.grid(row=3, column=1)

# Scissors
scissorsDataset = []
scissorsLabels = []
scissorsText = tk.StringVar()
scissorsText.set("0")
scissorsLabel = tk.Label(root, textvariable=scissorsText)
scissorsLabel.grid(row=2, column=2)
def input_scissors():
    add_image(scissorsDataset)
    scissorsLabels.append(2)
    scissorsText.set(str(len(scissorsDataset)))
    if len(rockDataset) == len(paperDataset) == len(scissorsDataset) and len(rockDataset) >= 20:
        progress.config(state="normal")
    else:
        progress.config(state="disabled")
scissors = tk.Button(root, text="scissors", command=input_scissors)
scissors.grid(row=3, column=2)

hLine = tk.Frame(root, height=1, width=600, bg="black")
hLine.grid(row=4, column=0, columnspan=4)

#############
# Run model #
#############



root.mainloop()
