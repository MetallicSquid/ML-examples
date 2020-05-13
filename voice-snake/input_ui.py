from tkinter import *

root = Tk()
root.title('Record')

upEntry = Entry(root, width=10)
upEntry.pack(side=TOP)

leftEntry = Entry(root, width=10)
leftEntry.pack(side=LEFT)

rightEntry = Entry(root, width=10)
rightEntry.pack(side=RIGHT)

downEntry = Entry(root, width=10)
downEntry.pack(side=BOTTOM)

def record_up():
    pass

def record_left():
    pass

def record_right():
    pass

def record_down():
    pass

up = Button(root, text="record up", command=record_up)
up.pack(side=TOP)

left = Button(root, text="record left", command=record_left)
left.pack(side=LEFT)

right = Button(root, text="record right", command=record_right)
right.pack(side=RIGHT)

down = Button(root, text="record down", command=record_down)
down.pack(side=BOTTOM)

message = Label(root, text='press a each button, and record each direction')
message.pack(side=BOTTOM)
root=mainloop()


