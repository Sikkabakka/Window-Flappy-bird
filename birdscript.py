
from tkinter import *
import tkinter
from PIL import Image, ImageTk
from utils import *



class Bird:
    def __init__(self, size):
        self.size = size
        self.window = None
        self.position = ()
    
    def spawn(self):
        
        monitor = getMonitorDimensions()
        root = tkinter.Tk()
        root.title("Bird")
        
        self.window = root
        self.position = (int(monitor["width"]/10) , int(monitor["height"]/2)- self.size)
  
        
        bilde = Image.open("bilder/flappy_bird.png").resize((self.size, self.size))
        sprite = ImageTk.PhotoImage(bilde)
        label = Label(root, image = sprite, width= self.size, height=self.size)
        label.pack()
        
        
        root.geometry(f"{self.size}x{self.size}")
        root.geometry(f"+{self.position[0]}+{self.position[1]}")
     
        root.mainloop()
    def jump(self):
        
        print(self.window.winfo_x())
        return
          


