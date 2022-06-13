from tkinter import *
from tkinter import ttk
import math
from PIL import Image, ImageTk, ImageOps, ImageDraw

from functools import partial
import listFunctions

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
  scrollbar = Scrollbar ( ws)
  scrollbar.pack( side = RIGHT, fill = Y )

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
  slideshow_ratio = 3/4 # how big of the width and heigh should the main area be
  slideshow_base = Canvas(target, width = screen_width * slideshow_ratio, height = screen_height *slideshow_ratio)   
  slideshow_base.configure(bg='blue')   
  slideshow_offset_y = -screen_height * slideshow_ratio * 1/9
  slideshow_base.pack(anchor=CENTER)  
  slideshow_base.place(anchor=CENTER, x=screen_width /2, y=screen_height/2)
  ws.update()
  # a and b values of the slideshow oval
  oval_margin_percentage = .2
  slideshow_a = slideshow_base.winfo_width() * (1-2*oval_margin_percentage)
  slideshow_b = slideshow_base.winfo_height() * (1-2*oval_margin_percentage)
  # image will be centered in the center of the page
  # print('%d, %d' % (canvas.winfo_width()//2, canvas.winfo_height()//2))

  delta_theta = 2 * math.pi / len(home_order)
  streamer_index = 0
  starting_theta = -3/2 * math.pi # start at downwards angle
  first = True
  streamer_buttons = []
  streamer_images = []
  directional_arrows = []
  for streamer_name in home_order:
    # find location along the elipse
    image_x = slideshow_a/2 * math.cos(delta_theta * streamer_index + starting_theta) + slideshow_base.winfo_width()/2 
    image_y = slideshow_b/2 * math.sin(delta_theta * streamer_index + starting_theta) + slideshow_base.winfo_height()/2 
    image_max_x = 300
    image_max_y = 500
    if first:
      starting_y = image_y
      starting_x = image_x




    # render image according to streamer name
    image = Image.open(f"Pics/{streamer_name}-Pics/home.png")
    # (first time)add to streamer_images
    # Resize the image based on y distance from bottom of screen
    y_dist = (starting_y - image_y + 1) / 60
    decay_constant = 1.08
    decay_factor = pow(decay_constant, -y_dist)


    image_width = int(image_max_x * decay_factor)
    image_height = int(image_max_y * decay_factor)
    image_dimensions = (image_width, image_height)
    name_tage = Label(slideshow_base, text=streamer_name, width=len(streamer_name), height=1)
    if (first):
      name_tage.place(anchor=CENTER, x=image_x, y=image_y - image_height*5/6)
      name_tage.config(state=DISABLED)

    print("%d, %d" % image_dimensions)
    max_image_dimensions = (image_max_x, image_max_y)
    resize_image = image.resize( max_image_dimensions)

    mask = Image.new('L', max_image_dimensions, 0)
    draw = ImageDraw.Draw(mask) 
    draw.ellipse((0, 0) + max_image_dimensions, fill=255)

    im = resize_image

    resize_image = ImageOps.fit(im, mask.size, centering=(0.5, 0.5))
    resize_image.putalpha(mask)

    streamer_images.append(resize_image)
    resize_image = image.resize( image_dimensions ) 
    # test the computer locations along the ellipse

    def buttonPressed(streamer_name):
      __first = True
      print(f"{streamer_name} Pressed")

      index = home_order.index(streamer_name)
      def new_index(index, offset):
        index += offset
        if index >= len(home_order):
          # wrap around
          index -= len(home_order)
        elif(index < 0):
          index += len(home_order)
        return index
      print(directional_arrows)
      directional_arrows[0][0].configure(command = partial(buttonPressed, home_order[new_index(index, directional_arrows[0][1])]))
      directional_arrows[1][0].configure(command = partial(buttonPressed, home_order[new_index(index, directional_arrows[1][1])]))
      for i in range(len(home_order)):
        # i is counting from bottom, counter countwise
        # curr is i offset by where we clicked on
        curr = index + i
        if curr >= len(home_order):
          # wrap around
          curr -= len(home_order)
        print(curr)
        # cur button
        cur_button = streamer_buttons[i][0]
        image_dimensions = streamer_buttons[i][1]
        mytext = streamer_buttons[i][2]
        # change image
        image = streamer_images[curr]
        resize_image = image.resize( image_dimensions ) 
        img =ImageTk.PhotoImage(resize_image)
        cur_button.configure(image=img)
        cur_button.image = img 

        # change callback

        if (__first):
          cur_button.configure(command = partial(listFunctions.go, streamer_name, target, ws))
        else:
          cur_button.configure(command = partial(buttonPressed, home_order[curr]))
          cur_button.streamer_name = home_order[curr]
        # change text
        mytext["text"] = home_order[curr]
        mytext["width"] = len(home_order[curr])
        __first = False


    img = ImageTk.PhotoImage(resize_image)
    if (first):
      # add left and right button
      left = Image.open(f"Pics/home/left.png")
      right = ImageOps.mirror(left)
      right_image = ImageTk.PhotoImage(right)
      left_image = ImageTk.PhotoImage(left)
      left_offset = 1
      right_offset = -1
      right_button = ttk.Button(
        slideshow_base,
        command = partial(buttonPressed, home_order[home_order.index(streamer_name) +right_offset]),
        image = right_image,  
      )
      left_button = ttk.Button(
        slideshow_base,
        command = partial(buttonPressed, home_order[home_order.index(streamer_name) +left_offset]),
        image = left_image,  
      )


      left_button.place(anchor=CENTER,x= image_x-image_max_x,y= image_y)
      left_button.image = left_image
      right_button.place(anchor=CENTER,x= image_x + image_max_x,y= image_y)
      right_button.image = right_image
      directional_arrows.append((left_button,left_offset))
      directional_arrows.append((right_button, right_offset))


    # btn = None

    btn = ttk.Button(
      slideshow_base,
      text = 'Click Me !',
      command = partial(buttonPressed, streamer_name),
      image = img,  
    )
    if (first):
      btn.configure(command = partial(listFunctions.go, streamer_name, target, ws))
    btn.streamer_name = streamer_name
    btn.image = img
    btn.place(x=image_x, y=image_y+slideshow_offset_y, anchor=CENTER)
    streamer_buttons.append((btn, image_dimensions, name_tage))

    first = False
    streamer_index += 1
  # build the status box
  # status_box = Canvas(target, width=1000, height=300, bg='green')
  # status_box.place(x=starting_x, y=starting_y + image_max_y /2, anchor=CENTER)
  
  # cur_name_label = Label(status_box, text=home_order[0], width=len(home_order[0]), height=1)
  # cur_name_label.grid(row=0, column=0, sticky='s')
  # go_image = Image.open(f"Pics/general/go.png")
  # go_image= go_image.resize((300, 300))
  # go_button = Button(status_box, command= partial(listFunctions.go, home_order[0]))

  # go_button.grid(column=1, row=0, sticky='S')
  
  ws.mainloop()

  
  
