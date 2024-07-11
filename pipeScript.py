import tkinter 
from tkinter import *
from random import randint
from utils import *
from PIL import Image, ImageTk

class Pipe:
    def __init__(self):
        self.size = 100
        self.monitor = getMonitorDimensions()
        self.space = self.monitor["height"]//4
        self.top_position = randint(50, self.monitor["height"]-50 - self.space)
        self.top_pipe = tkinter.Tk()
        self.bottom_pipe = tkinter.Tk()
        self.width = 244
        self.x = self.monitor["width"]
        self.speed = 3
        self.running = False
        self.bilde = Image.open("bilder/pipe.png")
        self.tp_bilde = self.bilde.transpose(Image.FLIP_TOP_BOTTOM)
        self.tp_sprite = ImageTk.PhotoImage(self.tp_bilde, master =self.top_pipe)
        self.bp_sprite = ImageTk.PhotoImage(self.bilde, master= self.bottom_pipe)
    def spawn(self): 
        
        print("hello")
        self.top_pipe.geometry(f"{self.width}x{self.top_position}")
        self.top_pipe.geometry(f"+{self.x}+{0}")
        
        self.tp_label = Label(self.top_pipe, image = self.tp_sprite, width=self.width, height=1499)
        self.tp_label.place(x = 0, y=self.top_position-1499)
      
        
        
        self.bottom_pipe.geometry(f"{self.width}x{self.monitor["height"] -self.top_position +self.space}")
        self.bottom_pipe.geometry(f"+{self.x}+{self.top_position +self.space}")
        
        self.bp_label = Label(self.bottom_pipe, image = self.tp_sprite, width=self.width, height=1499)
        
        self.bp_label.place(x = 0, y=self.top_position-1499)
      
        
        
        self.run()
        self.top_pipe.mainloop()
        self.bottom_pipe.mainloop()

    def update(self):
        print("update")
        self.x -= self.speed
        self.bottom_pipe.geometry(f"+{self.x}+{self.top_position +self.space}")
        self.top_pipe.geometry(f"+{self.x}+{0}")
    
    def check_outside(self):
        if (self.x <= 0):
            self.running = False
    def  main_loop(self):
        if self.running:
            self.update()
            self.check_outside()
            self.top_pipe.after(16, self.main_loop)
        
    def run(self):
        self.running = True
        self.main_loop()   
        
        
        
        
        
pipe = Pipe()
pipe.spawn()
