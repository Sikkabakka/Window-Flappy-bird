
from tkinter import *
import tkinter
from PIL import Image, ImageTk
from utils import *



class Bird:
    def __init__(self, size):
        self.size = size
        self.window = tkinter.Tk()
        self.window.title("Bird")
        self.velocity = 10
        monitor = getMonitorDimensions()
        self.position = (int(monitor["width"]/10) , int(monitor["height"]/2)- self.size)
        
    def spawn(self):
       
        bilde = Image.open("bilder/flappy_bird.png").resize((self.size, self.size))
        sprite = ImageTk.PhotoImage(bilde)
        label = Label(self.window, image = sprite, width= self.size, height=self.size)
        label.pack()
        
        
        self.window.geometry(f"{self.size}x{self.size}")
        self.window.geometry(f"+{self.position[0]}+{self.position[1]}")
        self.window.mainloop()
        
    def flap(self):
        self.velocity = -10
        return

       
        
    def update(self):
        self.position = (self.position[0], self.position[1]+self.velocity)
        self.window.geometry(f"+{self.position[0]}+{self.position[1]}")
        
     
          


