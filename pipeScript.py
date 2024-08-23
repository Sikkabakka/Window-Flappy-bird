from tkinter import *
from random import randint
from utils import *
from PIL import Image, ImageTk

class Pipe:
    def __init__(self, root1, root2):
        self.monitor = getMonitorDimensions()
        self.size = self.monitor["width"]//20
        self.space = self.monitor["height"]//3
        self.top_position = randint(50, self.monitor["height"]-50 - self.space)
        self.top_pipe = root1
        self.bottom_pipe = root2
       
        self.width = round(self.size*2.44)
        self.x = self.monitor["width"] -self.width
        self.speed = 4
        self.running = False
        self.bilde = Image.open("bilder/pipe.png")
        self.tp_bilde = self.bilde.transpose(Image.FLIP_TOP_BOTTOM)
        self.tp_sprite = ImageTk.PhotoImage(self.tp_bilde, master =self.top_pipe)
        self.bp_sprite = ImageTk.PhotoImage(self.bilde, master= self.bottom_pipe)
    def remove_borders(self):
        self.top_pipe.overrideredirect(True)
        self.bottom_pipe.overrideredirect(True)
    def spawn(self): 
        
        
        self.top_pipe.geometry(f"{self.width}x{self.top_position}")
        self.top_pipe.geometry(f"+{self.x}+{0}")
        
        self.tp_label = Label(self.top_pipe, image = self.tp_sprite, width=self.width, height=1499)
        self.tp_label.place(x = 0, y=self.top_position-1499)
      
        
       
        self.bottom_pipe.geometry(f"{self.width}x{self.monitor["height"] -self.top_position +self.space}")
        self.bottom_pipe.geometry(f"+{self.x}+{self.top_position +self.space}")
        
        self.bp_label = Label(self.bottom_pipe, image = self.bp_sprite, width=self.width, height=1499)
        self.bp_label.place(x = 0, y=0)
      
    def destroyPipes(self):
        self.top_pipe.destroy()
        self.bottom_pipe.destroy()
        
    def update(self):
        self.x -= self.speed
        self.bottom_pipe.geometry(f"+{self.x}+{self.top_position +self.space}")
        self.top_pipe.geometry(f"+{self.x}+{0}")
    
    def check_out(self):
        if (self.x <= 0):
            return True

        
        
        
    
