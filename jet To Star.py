import pgzrun
from random import randint
WIDTH=600
HEIGHT  = 500
TITLE="Jet to Star!"
score=0
star=Actor("star")
star.pos=(70,70)

jet=Actor("jet")
jet.pos=(250,250)
def draw():

    screen.fill(color="white") 
    star.draw()
    jet.draw()
    screen.draw.text(str(score),color="black",topright=(500,10))
    

def update():

    global score
    
    if keyboard.a:
        jet.x-=5
    if keyboard.d:
        jet.x+=5
    if keyboard.w:
        jet.y-=5
    if keyboard.s:
        jet.y+=5
    if jet.colliderect(star):
        score+=10
        star.x=randint(0,600)
        star.y=randint(0,500)


pgzrun.go()
