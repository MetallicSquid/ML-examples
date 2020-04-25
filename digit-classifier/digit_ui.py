import tkinter
from tkinter import *
from PIL import ImageTk, Image
from _ast import Lambda
import math
from math import pow

canvas_width=600
canvas_height=450

def paint(event):
    color= 'red'
    x1, y1 = (event.x-1) , (event.y-1)
    x2, y2 = (event.x+1) , (event.y+1)
    c.create_oval(x1,y1,x2,y2,fill=color, outline=color)

root = Tk()

root.title('Draw')

c = Canvas(root, width=canvas_width, height=canvas_height,
           bg='white')
c.pack(expand=YES, fill=BOTH)
c.bind('<B1-Motion>', paint )

def clear_screen():
    c.delete('all')






clear = Button(root, text="clear screen", command=clear_screen)
clear.pack(side=RIGHT)




message = Label(root, text='Hold and Drag to draw')
message.pack(side=BOTTOM)
root.mainloop()
