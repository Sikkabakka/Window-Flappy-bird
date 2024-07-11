
import keyboard
import threading
import time
from birdscript import Bird
from pipeScript import Pipe

         
bird = Bird(100)

bird.spawn()
pipe = Pipe()
threading.Thread(target=Pipe.spawn)
pipe.spawn()


    
