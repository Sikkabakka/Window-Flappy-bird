
import keyboard
import threading
import time
from birdscript import Bird

def check_for_spacebar():
    while True:
        if (keyboard.is_pressed("space")):
            bird.flap()
            time.sleep(0.1)
        
        
        
bird = Bird(100)
threading.Thread(target=check_for_spacebar, daemon=True).start()
def main_loop():
    Running = True
    while Running:
        print("hwlloe")
        bird.update()
        
        
threading.Thread(target=main_loop, daemon=True).start()
bird.spawn()




    
