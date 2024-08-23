
import time
from birdscript import Bird
from pipeScript import Pipe 
from tkinter import *
import tkinter

root = tkinter.Tk()

bird = Bird(100, root)
  
bird.spawn()

 

score = 0
startime = time.time()
startInterval = time.time()
pipes = []

def check_for_collision():
    for each in pipes:
        if (bird.position[1] < each.top_position) or (bird.position[1] + bird.size > each.top_position + each.space):
            if (bird.position[0] > each.x - each.width/2 or bird.position[0] +bird.size > each.x + each.width/2): 
                root.destroy()
                

def spawn_score():
    scorewindow = tkinter.Tk()
    text_widget = tkinter.Text()
    text_widget.insert("1.0", f"Score: {score}")
    text_widget.pack()
def main_loop():
    global startInterval, pipes, score
    
    endInterval = time.time()
    if (startime-endInterval-16)<0:
        score = 0

    if (endInterval-startInterval) >= 4:
        print(score)
        pipe = Pipe(tkinter.Toplevel(root), tkinter.Toplevel(root))
        pipe.spawn()
        pipes.append(pipe)
        startInterval = endInterval
 
    if running:
        bird.update()
        if bird.check_out():
            root.destroy()
          
        check_for_collision()
        for pipen in pipes: 
            pipen.update()
            if pipen.check_out():
                pipen.destroyPipes()
                pipes.remove(pipen)
               
        
        root.after(16, main_loop)
    else:
        print("du tapte")
        print("score: ", score)   
        
running = True

    
main_loop()
root.mainloop()  