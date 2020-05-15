# Imports
import numpy as np
import tkinter as tk
import cv2
from PIL import ImageTk, Image

# Window setup
root = tk.Tk()
root.title('Rock, Paper, Scissors - Input')
root.config(background="#FFFFFF")

# Guidance message
message = tk.Label(root, text="Enter at least 20 samples of each gesture. There must be an equal number of samples.")
message.grid(row=0, column=0, columnspan=3)

# Quit
def quit_window():
    root.destroy()
quit = tk.Button(root, text="quit", command=quit_window)
quit.grid(row=0, column=3)

# Check progress, progression button
def check_progress():
    print('Next screen')


progress = tk.Button(root, text="Next", command=check_progress)
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
    cv2image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    dataset.append(cv2image)

progressFlag = False

# Rock
rockDataset = []
rockText = tk.StringVar()
rockText.set("0")
rockLabel = tk.Label(root, textvariable=rockText)
rockLabel.grid(row=2, column=0)
def input_rock():
    add_image(rockDataset)
    rockText.set(str(len(rockDataset)))
    if len(rockDataset) == len(paperDataset) == len(scissorsDataset) and len(rockDataset) >= 20:
        progress.config(state="normal")
    else:
        progress.config(state="disabled")
rock = tk.Button(root, text="rock", command=input_rock)
rock.grid(row=3, column=0)

# Paper
paperDataset = []
paperText = tk.StringVar()
paperText.set("0")
paperLabel = tk.Label(root, textvariable=paperText)
paperLabel.grid(row=2, column=1)
def input_paper():
    add_image(paperDataset)
    paperText.set(str(len(paperDataset)))
    if len(rockDataset) == len(paperDataset) == len(scissorsDataset) and len(rockDataset) >= 20:
        progress.config(state="normal")
    else:
        progress.config(state="disabled")
paper = tk.Button(root, text="paper", command=input_paper)
paper.grid(row=3, column=1)

# Scissors
scissorsDataset = []
scissorsText = tk.StringVar()
scissorsText.set("0")
scissorsLabel = tk.Label(root, textvariable=scissorsText)
scissorsLabel.grid(row=2, column=2)
def input_scissors():
    add_image(scissorsDataset)
    scissorsText.set(str(len(scissorsDataset)))
    if len(rockDataset) == len(paperDataset) == len(scissorsDataset) and len(rockDataset) >= 20:
        progress.config(state="normal")
    else:
        progress.config(state="disabled")
scissors = tk.Button(root, text="scissors", command=input_scissors)
scissors.grid(row=3, column=2)

# Create training and test datasets

root.mainloop()
