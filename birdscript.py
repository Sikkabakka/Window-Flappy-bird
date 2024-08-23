
from tkinter import *
from PIL import Image, ImageTk
from utils import *
import math


class Bird:
    def __init__(self, size, root):
        self.running = False
        self.monitor = getMonitorDimensions()
        self.size = 100
        self.window = root
        self.window.title("Bird")
        self.velocity = 0
        self.flap_strength = -10
        self.gravity = 0.5
        self.position = (int(self.monitor["width"]/10) , int(self.monitor["height"]/2)- self.size)
        self.startime = 0
        
    def spawn(self):
       
        bilde = Image.open("bilder/flappy_bird.png").resize((self.size, self.size))
        self.sprite = ImageTk.PhotoImage(bilde)
        self.label = Label(self.window, image = self.sprite, width= self.size, height=self.size)
        self.label.pack()
        
        self.window.bind("<space>", self.flap)
        self.window.geometry(f"{self.size}x{self.size}")
        self.window.geometry(f"+{self.position[0]}+{self.position[1]}")

       
    def remove_border(self):
        self.window.overrideredirect(True)
    def flap(self, event = None):
        self.velocity = self.flap_strength
  
        
    def update(self):
       
        self.velocity += self.gravity
        self.velocity = min(self.velocity, 10)
        
        self.position = (self.position[0], math.floor(self.position[1]+ self.velocity))
        self.window.geometry(f"+{self.position[0]}+{self.position[1]}")
    
        
    def check_out(self):
        if (self.position[1] +self.size > self.monitor["height"] or  self.position[1] <= 0):
            return True
            


          

