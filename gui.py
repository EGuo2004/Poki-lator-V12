import tkinter as tk
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
    
  def getSquareRoot ():  
      x1 = entry1.get()
      
      label1 = tk.Label(ws, text= float(x1)**0.5)
      canvas1.create_window(200, 230, window=label1)
  button1 = tk.Button(text='Get the Square Root', command=getSquareRoot)
  canvas1.create_window(200, 180, window=button1)
  ws.mainloop()
