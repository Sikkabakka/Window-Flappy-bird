
import keyboard
import threading
import time
from birdscript import Bird

def check_for_spacebar():
    while True:
        print("waiting for space")
        keyboard.wait("space")
        bird.jump()
        print("pressed")
        
        
bird = Bird(100)
thread = threading.Thread(target=check_for_spacebar, daemon=True).start(  )
Running = True
bird.spawn()
print(bird)
