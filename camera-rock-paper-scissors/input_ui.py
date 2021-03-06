###############
# Gather data #
###############

# Almost finished, just make the game playable

# Imports
import numpy as np
import tkinter as tk
import cv2
from PIL import ImageTk, Image
from random import randint
from build_model import build_model
from time import sleep

# Window setup
root = tk.Tk()
root.title('Rock, Paper, Scissors - Input')
root.config(background="#FFFFFF")
root.grid_rowconfigure(4, pad=10)

# Guidance message
message = tk.Label(root, text="Enter at least 20 samples of each gesture. There must be an equal number of samples.")
message.grid(row=0, column=0)

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
        progressText.set("Already Compiled")
    else:
        progressText.set("")
        # Shuffle the data
        for element in range(len(newDataset)):
            randIndex = randint(0, element)
            dataElem = newDataset.pop(randIndex)
            labelElem = newLabels.pop(randIndex)
            newDataset.append(dataElem)
            newLabels.append(labelElem)

        fullDataset = np.asarray(newDataset)
        fullLabels = np.asarray(newLabels)

# Progress button
progressText = tk.StringVar()
progressText.set("")
progressLabel = tk.Label(root, textvariable=progressText)
progressLabel.grid(row=2, column=3)
progress = tk.Button(root, text="compile dataset", command=compile_dataset)
progress.grid(row=3, column=1, columnspan=3)
progress.config(state="disabled")

# Graphics window
imageFrame = tk.Frame(root, width=600, height=500)
#imageFrame.grid(row=1, column=0, columnspan=4, padx=10, pady=2)
imageFrame.grid(row=1, rowspan=5,column=0, padx=10, pady=2)

# Capture video frames
lmain = tk.Label(imageFrame)
lmain.grid(row=0, column=0)
cap = cv2.VideoCapture(0)

def show_frame():
    frame = cap.read()[1]
    frame = cv2.flip(frame, 1)

    # Superpose a 128x128 rectangle in the middle of the frame
    midHeight = round(frame.shape[0]/2)
    midWidth = round(frame.shape[1]/2)
    x1 = midWidth - 128
    y1 = midHeight - 128
    x2 = midWidth + 128
    y2 = midHeight + 128
    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 3)

    # Put explanation text on the image
    font = cv2.FONT_HERSHEY_SIMPLEX
    text = 'Keep Gesture Within Box'
    textSize = cv2.getTextSize(text, font, 1, 2)[0]
    xt = midWidth - round(textSize[0]/2)
    cv2.putText(frame, text, (xt, 50), font, 1, (0, 0, 255), 2)

    # Display image and repeat
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

    # Capture the image within the box
    midHeight = round(image.shape[0]/2)
    midWidth = round(image.shape[1]/2)
    x1 = midWidth - 128
    y1 = midHeight - 128
    x2 = midWidth + 128
    y2 = midHeight + 128
    image = image[y1:y2, x1:x2]

    # Convert and add image to the dataset
    cv2image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    dataset.append(cv2image)

# Rock
rockDataset = []
rockLabels = []
rockText = tk.StringVar()
rockText.set("0")
rockLabel = tk.Label(root, textvariable=rockText)
#rockLabel.grid(row=2, column=0)
rockLabel.grid(row=1, column=1)
def input_rock():
    add_image(rockDataset)
    rockLabels.append(0)
    rockText.set(str(len(rockDataset)))
    if len(rockDataset) == len(paperDataset) == len(scissorsDataset) and len(rockDataset) >= 20:
        progress.config(state="normal")
    else:
        progress.config(state="disabled")
rock = tk.Button(root, text="rock", command=input_rock)
#rock.grid(row=3, column=0)
rock.grid(row=2, column=1)

# Paper
paperDataset = []
paperLabels = []
paperText = tk.StringVar()
paperText.set("0")
paperLabel = tk.Label(root, textvariable=paperText)
#paperLabel.grid(row=2, column=1)
paperLabel.grid(row=1, column=2)
def input_paper():
    add_image(paperDataset)
    paperLabels.append(1)
    paperText.set(str(len(paperDataset)))
    if len(rockDataset) == len(paperDataset) == len(scissorsDataset) and len(rockDataset) >= 20:
        progress.config(state="normal")
    else:
        progress.config(state="disabled")
paper = tk.Button(root, text="paper", command=input_paper)
#paper.grid(row=3, column=1)
paper.grid(row=2, column=2)

# Scissors
scissorsDataset = []
scissorsLabels = []
scissorsText = tk.StringVar()
scissorsText.set("0")
scissorsLabel = tk.Label(root, textvariable=scissorsText)
#scissorsLabel.grid(row=2, column=2)
scissorsLabel.grid(row=1, column=3)
def input_scissors():
    add_image(scissorsDataset)
    scissorsLabels.append(2)
    scissorsText.set(str(len(scissorsDataset)))
    if len(rockDataset) == len(paperDataset) == len(scissorsDataset) and len(rockDataset) >= 20:
        progress.config(state="normal")
    else:
        progress.config(state="disabled")
scissors = tk.Button(root, text="scissors", command=input_scissors)
#scissors.grid(row=3, column=2)
scissors.grid(row=2, column=3)

# Horizontal line
#hLine = tk.Frame(root, height=1, width=600, bg="black")
#hLine.grid(row=4, column=0, columnspan=4)

# Vertical line
vLine1 = tk.Frame(root, height=500, width=1, bg="black")
vLine1.grid(row=1, column=4, rowspan=4, columnspan=2)

#############
# Run model #
#############

# Build the model when button is pressed
probModel= None
accuracy = ""
loss = ""

def run_model(data, labels, epochs):
    modelList = build_model(data, labels, epochs)
    # NB: the use of global variables here is unfortunate but hard to avoid
    global probModel
    global accuracy
    global loss
    probModel = modelList[2]
    accuracy = ("Accuracy: " + str(round(modelList[3], 2)))
    loss = ("Loss: " + str(round(modelList[4], 2)))
    accText.set(accuracy)
    lossText.set(loss)
    buildText.set("Model built")

build = tk.Button(root, text="build", command=lambda: run_model(fullDataset, fullLabels, 30))
#build.grid(row=5, column=0)
build.grid(row=1, column=6)
buildText = tk.StringVar()
buildText.set("")
buildLabel = tk.Label(root, textvariable=buildText)
#buildLabel.grid(row=6, column=0)
buildLabel.grid(row=2, column=6)
accText = tk.StringVar()
accText.set("")
accLabel = tk.Label(root, textvariable=accText)
#accLabel.grid(row=7, column=0)
accLabel.grid(row=3, column=6)
lossText = tk.StringVar()
lossText.set("")
lossLabel = tk.Label(root, textvariable=lossText)
#lossLabel.grid(row=8, column=0)
lossLabel.grid(row=4, column=6)

# Vertical line
vLine2 = tk.Frame(root, height=500, width=1, bg="black")
vLine2.grid(row=1, column=7, rowspan=4)

# Play a game
def cap_image():
    image = cap.read()[1]
    image = cv2.flip(image, 1)

    # Capture the image within the box
    midHeight = round(image.shape[0]/2)
    midWidth = round(image.shape[1]/2)
    x1 = midWidth - 128
    y1 = midHeight - 128
    x2 = midWidth + 128
    y2 = midHeight + 128
    image = image[y1:y2, x1:x2]

    # Convert and add image to the dataset
    cv2image = np.asarray(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY))/255.0
    cv2image = cv2image.reshape(1, 256, 256)
    return cv2image

playerScore = 0
computerScore = 0
verdict = ""

def play_round():
    # NB: the use of global variables is unfortunate, but difficult to avoid
    global playerScore
    global computerScore
    global verdict

    prediction = np.argmax(probModel.predict(cap_image()))
    optionList = ['rock', 'paper', 'scissors']
    textPrediction = optionList[prediction]
    pcText.set(textPrediction)
    computer = randint(0, 2)
    computerChoice = optionList[computer]
    ccText.set(computerChoice)

    # Decide who wins:
    if computer == (prediction+1) or computer == (prediction-2):
        computerScore += 1
        verdict = "Computer wins"
    elif computer == (prediction-1) or computer == (prediction+2):
        playerScore += 1
        verdict = "Player wins"
    else:
        verdict = "Draw"
    playerString = "Player score: " + str(playerScore)
    psText.set(playerString)
    computerString = "Computer score: " + str(computerScore)
    csText.set(computerString)
    verdictText.set(verdict)

play = tk.Button(root, text="Play", command=play_round)
play.grid(row=1, column=8, columnspan=2)
psText = tk.StringVar()
psLabel = tk.Label(root, textvariable=psText)
psLabel.grid(row=2, column=8)
csText = tk.StringVar()
csLabel = tk.Label(root, textvariable=csText)
csLabel.grid(row=3, column=8)
pcText = tk.StringVar()
pcLabel = tk.Label(root, textvariable=pcText)
pcLabel.grid(row=2, column=9)
ccText = tk.StringVar()
ccLabel = tk.Label(root, textvariable=ccText)
ccLabel.grid(row=3, column=9)
verdictText = tk.StringVar()
verdictLabel = tk.Label(root, textvariable=verdictText)
verdictLabel.grid(row=4, column=8, columnspan=2)

root.mainloop()
