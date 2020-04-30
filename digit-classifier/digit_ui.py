#from build_model import build_model # <--- basic model
from build_cnn import build_model # <--- cnn model
import tkinter
from tkinter import *
from PIL import ImageTk, Image, ImageOps
from _ast import Lambda
import math
from math import pow
#from PIL import ImageGrab # <--- For MacOS and Windows
import pyscreenshot as ImageGrab # <--- For linux
import numpy as np

prob_model = build_model(5)[2]

class_names = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

canvas_width=400
canvas_height=400

def paint(event):
    color= 'black'
    x1, y1 = (event.x-14.3) , (event.y-14.3)
    x2, y2 = (event.x+14.3) , (event.y+14.3)
    c.create_oval(x1,y1,x2,y2,fill=color, outline=color)

root = Tk()
root.title('Draw')

c = Canvas(root, width=canvas_width, height=canvas_height,
           bg='white')
c.pack(expand=YES, fill=BOTH)
c.bind('<B1-Motion>', paint )

def clear_screen():
    c.delete('all')

def quit_window():
    root.destroy()

def run_model():
    x=root.winfo_rootx()+c.winfo_x()
    y=root.winfo_rooty()+c.winfo_y()
    x1=x+c.winfo_width()
    y1=y+c.winfo_height()
    digit = ImageGrab.grab().crop((x,y,x1,y1)).convert('L')
    digit = ImageOps.invert(digit)
    digit.thumbnail((28,28), Image.ANTIALIAS)
    #digitArray = np.array(digit).reshape(1, 28, 28) / 255.0 # <--- basic model
    digitArray = np.array(digit).reshape(1, 28, 28, 1) / 255.0 # <--- cnn model
    prediction_array = prob_model.predict(digitArray)
    predicted_label = class_names[np.argmax(prediction_array)]
    print(predicted_label)

clear = Button(root, text="clear screen", command=clear_screen)
clear.pack(side=RIGHT)

quit = Button(root, text="quit", command=quit_window)
quit.pack(side=RIGHT)

run = Button(root, text="run model", command=run_model)
run.pack(side=RIGHT)

message = Label(root, text='Hold and Drag to draw')
message.pack(side=BOTTOM)
root.mainloop()
