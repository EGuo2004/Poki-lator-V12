from tkinter import *
from tkinter import ttk
import math
import ourBaseFunc
from PIL import Image, ImageTk, ImageOps, ImageDraw
from functools import partial
import run_function

from functools import partial

from run_function import general_function
current_function = None
def go(streamer_name, target, ws):
    print("deleting")
    print(target)
    # clear screen
    for widgets in target.winfo_children():
        widgets.destroy()
    print(streamer_name)
    file = "k"
    # render bg image
    if (streamer_name == "poki"):
        import ourBaseFunc as file
    elif (streamer_name == "emiru"):
        import ourCalcFunc as file
    elif (streamer_name == "jodi"):
        import ourCalcFunc as file
    elif (streamer_name == "sykkuno"):
        import ourInverseTrig as file
    elif (streamer_name == "jodi"):
        import ourMiscFunc as file  
    elif (streamer_name == "toast"):
        import ourTrigFunc as file

    # create table with image
    functions = [f for _, f in file.__dict__.items() if callable(f)]
    print(functions)
    temp =[]
    index = 0
    for row in range(int(len(functions) / 3)):
        for col in range(3):
            if (row * col < len(functions)):
                print(f"{row},{col}")
                name =functions[index].__name__ 
                function_caller = Button(target,text=name, width= len(name), height=1, command=partial(run_function.create_general_function,streamer_name, file, functions[index], target))
                function_caller.grid(row=row, column=col,sticky='s')
                temp.append(function_caller)
                index += 1
    pass
    