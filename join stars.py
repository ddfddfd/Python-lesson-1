
import pgzrun
import random
WIDTH=800
HEIGHT=600

number_of_star=13


starsList=[]

def star_maker():# fun draws stars
    for i in range(0,number_of_star):#repeats 8 times
      star=Actor("star")
      star.pos=(random.randint(50,750),random.randint(50,550))
      starsList.append(star)


def draw():
    screen.blit("space",(0,0))
    for star in starsList:
       star.draw()

   
def update():
   pass







star_maker()
pgzrun.go()