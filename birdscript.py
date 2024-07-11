
from tkinter import *
import tkinter
from PIL import Image, ImageTk
from utils import *
import time 
import threading
import keyboard
import math


class Bird:
    def __init__(self, size):
        self.running = False
        self.size = size
        self.window = tkinter.Tk()
        self.window.title("Bird")
        self.velocity = 0
        self.flap_strength = -10
        self.gravity = 0.5
        self.monitor = getMonitorDimensions()
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
        self.run()
       
        
        self.window.mainloop()
        
    def flap(self, event = None):
        print("flapped")
        self.velocity = self.flap_strength
  
        
    def update(self):
       
        self.velocity += self.gravity
        self.velocity = min(self.velocity, 10)
        
        self.position = (self.position[0], math.floor(self.position[1]+ self.velocity))
        self.window.geometry(f"+{self.position[0]}+{self.position[1]}")
        self.startime = time.time()
        
        
    def main_loop(self):
        if self.running:
            self.update()
            self.check_out()
            self.window.after(16, self.main_loop)
        else:
            print("du tapte")   
            
    def check_out(self):
        if (self.position[1] +self.size > self.monitor["height"]):
            self.running = False
            

    def run(self):
        self.running = True
        self.main_loop()
          

