import tkinter as tk
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
  ws = tk.Tk()
  ws.title("Poki-lator")
  ws.geometry('400x600')
  greeting = tk.Label(text="Hello, Tkinter")
  greeting.pack(side=tk.TOP)

  canvas1 = tk.Canvas(ws, width = 400, height = 300)
  entry1 = tk.Entry (ws) 
  canvas1.create_window(200, 140, window=entry1)
  canvas1.pack()
  
  canvas = tk.Canvas(ws, width = 300, height = 300)      
  canvas.pack()      
  img = tk.PhotoImage(file="Poki-Pics/POKI.png")    
  N = tk.N
  W = tk.W
  canvas.create_image(100,100,anchor=tk.CENTER, image=img)     

  
  canvas1.create_window(200, 180, window=button1)
  ws.mainloop()
