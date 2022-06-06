from tkinter import *
from PIL import Image, ImageTk

import ourBaseFunc
errorBound = 0.00001

# vision - poki slide show, each poki mood = a function
# sub moods for catagories 
# mad poki = trig functions
# violent poki = sin\
#if u on a slide, you can import paramaters into ui so our cal can solve it

relationships = {
  "poki" : "ourBaseFunc",
  "emru": "ourCalcFunc",
  "sykkuno": "ourInverseTrig",
  "jodi": "ourMiscFunc",
  "toast": "ourTrigFunc",
}


def init():
  global ws
  ws = Tk()
  ws.title("Poki-lator")
  
  #Get the current screen width and height of computer // not accurate
  global screen_width, screen_height
  screen_width = ws.winfo_screenwidth()
  screen_height = ws.winfo_screenheight()


  ws.geometry('%dx%d+%d+%d' % (screen_width, screen_height, 0, 0))
  
  print(f"{screen_width}, {screen_height}")
  #init main drawable canvas
  canvas = Canvas(ws, width=screen_width, height=screen_height, bg='yellow')
  canvas.pack(anchor = CENTER)
  # start off in homepage
  home(canvas)

def home(target):
  title = Text(target, width=screen_width, height=1)
  title.tag_configure("Title", justify='center')

  title.pack(anchor=N)
  title.insert(END, "Homepage")
  title.config(state=DISABLED)
  title.tag_add("Title", "1.0", "end")

  # image slideshow layer
  
  slideshow_base = Canvas(target, width = screen_width//2, height = screen_height//2)   
  slideshow_base.configure(bg='blue')   
  
  img = PhotoImage(file="Pics/Poki-Pics/POKI.png")
  slideshow_base.pack(anchor=CENTER)  
  ws.update()

  slideshow_base.create_oval(0, 0, slideshow_base.winfo_width(), slideshow_base.winfo_height())
  # image will be centered in the center of the page
  # print('%d, %d' % (canvas.winfo_width()//2, canvas.winfo_height()//2))
  slideshow_base.create_image(slideshow_base.winfo_width()//2, slideshow_base.winfo_height()//2, anchor=CENTER, image=img)   
  
  ws.mainloop()

  
  
