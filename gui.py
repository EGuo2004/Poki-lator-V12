from cmath import pi
from tkinter import *
from tkinter import ttk
import math
from PIL import Image, ImageTk
from functools import partial

import ourBaseFunc
errorBound = 0.00001

# vision - poki slide show, each poki mood = a function
# sub moods for catagories 
# mad poki = trig functions
# violent poki = sin\
#if u on a slide, you can import paramaters into ui so our cal can solve it

streamers = {
  "poki" : "ourBaseFunc",
  "emiru": "ourCalcFunc",
  "sykkuno": "ourInverseTrig",
  "jodi": "ourMiscFunc",
  "toast": "ourTrigFunc",
}
home_order = list(streamers.keys())

def init():
  global ws
  ws = Tk()
  ws.title("Poki-lator")
  # ws.attributes('-fullscreen', True)

  #Get the current screen width and height of computer // not accurate
  global screen_width, screen_height
  screen_width = ws.winfo_screenwidth()
  screen_height = ws.winfo_screenheight()
  # screen_width = 2000
  # screen_height = 1000  
  ws.geometry('%dx%d+%d+%d' % (screen_width, screen_height, 0, 0))
  
  print(f"{screen_width}, {screen_height}")
  #init main drawable canvas
  canvas = Canvas(ws, width=screen_width, height=screen_height, bg='yellow')
  canvas.pack(fill=Y, side=TOP, expand=True, anchor = CENTER)
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
  slideshow_ratio = 2/3
  slideshow_base = Canvas(target, width = screen_width * slideshow_ratio, height = screen_height *slideshow_ratio)   
  slideshow_base.configure(bg='blue')   
  
  slideshow_base.pack(anchor=CENTER)  
  slideshow_base.place(anchor=CENTER, x=screen_width /2, y=screen_height/2)
  ws.update()
  # a and b values of the slideshow oval
  oval_margin_percentage = .2
  slideshow_a = slideshow_base.winfo_width() * (1-2*oval_margin_percentage)
  slideshow_b = slideshow_base.winfo_height() * (1-2*oval_margin_percentage)
  slideshow_base.create_oval(slideshow_base.winfo_width()*oval_margin_percentage, slideshow_base.winfo_height()*oval_margin_percentage, slideshow_base.winfo_width()*(1-oval_margin_percentage),  slideshow_base.winfo_height()*(1-oval_margin_percentage))
  # image will be centered in the center of the page
  # print('%d, %d' % (canvas.winfo_width()//2, canvas.winfo_height()//2))

  delta_theta = 2 * math.pi / len(home_order)
  streamer_index = 0
  starting_theta = -3/2 * math.pi # start at downwards angle
  starting_y = slideshow_b/2 * math.sin(delta_theta * streamer_index + starting_theta) + slideshow_base.winfo_height()/2 
  streamer_buttons = []
  for streamer_name in home_order:
    # find location along the elipse
    image_x = slideshow_a/2 * math.cos(delta_theta * streamer_index + starting_theta) + slideshow_base.winfo_width()/2 
    image_y = slideshow_b/2 * math.sin(delta_theta * streamer_index + starting_theta) + slideshow_base.winfo_height()/2 
    # render image according to streamer name
    print(f"Pics/{streamer_name}-Pics/home.png" )
    image = Image.open(f"Pics/{streamer_name}-Pics/home.png")
    # Resize the image based on y distance from bottom of screen
    y_dist = (starting_y - image_y + 1) / 60
    decay_constant = 1.15
    print(f"y_dist {y_dist}")
    image_max_x = 300
    image_max_y = 500
    image_dimensions = (int(image_max_x * pow(decay_constant, -y_dist)), int(image_max_y * pow(decay_constant, -y_dist)))
    print("%d, %d" % image_dimensions)

    resize_image = image.resize( image_dimensions ) 

    # test the computer locations along the ellipse

    def buttonPressed(streamer_name):
      print(f"{streamer_name} Pressed")


    img = ImageTk.PhotoImage(resize_image)

    # btn = None
    btn = ttk.Button(
      slideshow_base,
      text = 'Click Me !',
      command = partial(buttonPressed, streamer_name),
      image = img,
    )
    btn.streamer_name = streamer_name
    btn.image = img
    btn.place(x=image_x, y=image_y, anchor=CENTER)
    streamer_buttons.append(btn)
    
    streamer_index += 1
 
  ws.mainloop()

  
  
