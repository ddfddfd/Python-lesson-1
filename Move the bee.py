import pgzrun
from random import randint
WIDTH=600
HEIGHT  = 500
TITLE="Bee Game"
score=0
flower=Actor("flower")
flower.pos=70,70

bee=Actor("bee")
bee.pos=250,250
def draw():

    screen.blit("bg",(0,0)) 
    flower.draw()
    bee.draw()
    screen.draw.text(str(score),color="black",topright=(500,10))
    

def update():

    global score
    
    if keyboard.a:
        bee.x-=5
    if keyboard.d:
        bee.x+=5
    if keyboard.w:
        bee.y-=5
    if keyboard.s:
        bee.y+=5
    if bee.colliderect(flower):
        score+=10
        flower.x=randint(0,600)
        flower.y=randint(0,500)


pgzrun.go()
