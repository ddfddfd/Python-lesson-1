import pgzrun
from random import randint
WIDTH=600
HEIGHT=500

gojo=Actor("gojo")
message=""
def draw():
    screen.fill(color="navy")
    gojo.draw()
    screen.draw.text(message,center=(WIDTH//2,30),fontsize=30,color="green")
#crate  function to make gojo jump on random spots
def random_spot():
    gojo.x=randint(0,600)
    gojo.y=randint(0,500)


#this function will allow us ti click the gojoooo
def on_mouse_down(pos):
    global message
    random_spot()
    if gojo.collidepoint(pos):  
        message= "NICE 1!"
    else:
        message="YOU MISSED"





random_spot()
pgzrun.go()