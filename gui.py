from tkinter import *
import math
from PIL import Image, ImageTk

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
  
  # testing centering + image rendering
  img = PhotoImage(file="Pics/poki-Pics/POKI.png")
  slideshow_base.pack(anchor=CENTER)  
  ws.update()
  slideshow_base.create_image(slideshow_base.winfo_width()//2, slideshow_base.winfo_height()//2, anchor=CENTER, image=img)   
  # a and b values of the slideshow oval
  slideshow_a = slideshow_base.winfo_width()
  slideshow_b = slideshow_base.winfo_height()
  slideshow_base.create_oval(0, 0, slideshow_a, slideshow_b)
  # image will be centered in the center of the page
  # print('%d, %d' % (canvas.winfo_width()//2, canvas.winfo_height()//2))

  
  delta_theta = 2 * math.pi / len(home_order)
  streamer_index = 0
  starting_theta = 0
  for streamer_name in home_order:
    # find location along the elipse
    image_x = slideshow_a * math.cos(delta_theta * streamer_index + starting_theta)
    image_y = slideshow_b * math.sin(delta_theta * streamer_index + starting_theta)
    # render image according to streamer name
    # Read the Image
    print(f"Pics/{streamer_name}-Pics/home.png" )
    image = Image.open(f"Pics/{streamer_name}-Pics/home.png")
    # Resize the image using resize() method
    resize_image = image.resize((40, 60))
    # resize_image.show()
    img = ImageTk.PhotoImage(resize_image)

    def buttonPressed():
      print("button Pressed")
    
    btn = Button(slideshow_base, text = 'Click Me !', command=buttonPressed, image = img)
    btn.place(x=image_x, y= image_y)

    # slideshow_base.create_image(image_x, image_y, anchor=CENTER, image=img)   
    streamer_index += 1
    
  ws.update()
  
  ws.mainloop()

  
  
