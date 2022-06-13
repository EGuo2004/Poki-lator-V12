from tkinter import *
from tkinter import ttk
import math
from PIL import Image, ImageTk, ImageOps, ImageDraw

from functools import partial
# create object that shows equation for each math problem

alphabet = "abcdefgh"
class general_function:
    def __init__(self, function_name, target,x, y, w, h):
        self.canvas.pack(anchor=CENTER)
        self.name = function_name
        self.paras = []
        self.canvas = Canvas(target, width=w, height=h)
        self.canvas.place()

        # objects that show the type of all the paramers 
        #find how many paramaters i have 
        pass
    def render(self):

        # create table of params x 2
        for i in len(self.pars):
            letter_label = Text(self.canvas, text=alphabet[i], width= 1, height=1)
            letter_label.pack
        pass

    def calc(self):
        # runs the function given all the info in the table