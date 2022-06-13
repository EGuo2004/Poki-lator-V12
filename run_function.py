from faulthandler import disable
from tkinter import *
from tkinter import ttk
import math
from turtle import width
from PIL import Image, ImageTk, ImageOps, ImageDraw

from functools import partial
# create object that shows equation for each math problem

alphabet = "abcdefgh"
class general_function:
    def __init__(self, file, func):
        self.func = func
        self.file = file
        self.name = func.__name__
        self.paras = file.params
        self.inputs = []
        # objects that show the type of all the paramers 
        #find how many paramaters i have 
        pass
    def render(self, target, x, y, w, h):
        self.canvas = Canvas(target, width=w*.75, height=h*.75)
        self.canvas.place(x=0, y=0, anchor=NW)
        function_image = Image.open(f"Pics/functions/{self.file.__name__}/{self.name}.png")
        function_image.resize((int(w*.75),int(h*.50)))
        img = ImageTk.PhotoImage(function_image)
        label = ttk.Label(self.canvas, image = img)
        label.image = img
        label.grid(row=0, column =0)
        # insert image in this grid
        inputs = Canvas(self.canvas, width=w*.75, height=h*.25)
        inputs.grid(row=1, column=0)
        # create table of params x 2
        for i in range(len(self.file.params[self.name])):
            letter_label = Label(inputs, text=alphabet[i], width= 1, height=1)
            letter_label.config(state=DISABLED)
            letter_label.grid(row=i, column=0, sticky="N")
            input_label = Entry(inputs)
            input_label.grid(row=i, column=1, sticky="N")
            self.inputs.append(input_label)
        
        pass

    def calc(self):
        # runs the function given all the info in the table
        pass

def create_general_function(person, file, func, target):
    size = (1500, 1000) 
    target.config(width = size[0])
    print(func)
    # clear screen
    print("deleting")
    print(target)
    # clear screen
    for widgets in target.winfo_children():
        widgets.destroy()

    # build function
    this_fun = general_function(file, func)
    
    # render

    this_fun.render(target, size[0]/2, size[1]/2, size[0], size[1])
    