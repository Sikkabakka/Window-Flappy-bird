
import tkinter
import keyboard
import threading
import time
# root = tkinter.Tk()
# root.mainloop()


def check_for_spacebar():
    while True:
        print("waiting for space")
        keyboard.wait("space")
        print("pressed")
        
class Bird:
    def __init__(self, size):
        self.size = size
    position = 10
    
          
bird = Bird(100)
thread = threading.Thread(target=check_for_spacebar, daemon=True).start(  )
Running = True
while Running:
    bird.position -= 1  
    time.sleep(1)
    if (bird.position < 0):
        Running = False 
    print(bird.position) 