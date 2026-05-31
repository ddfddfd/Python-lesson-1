import pgzrun

HEIGHT=500
WIDTH=500

item=Actor("apple")
item2=Actor("watermelon")
item3=Actor("mango")

item2.pos=(200,0)
item3.pos=(300,0)
def draw():

    screen.fill(color="white")
    item2.draw()
    item3.draw()
    item.draw()
def update():
    item.y+=10
    item2.y+=10
    item3.y+=10
    if item.y > 500:
        item.pos=(100,0)
    if item2.y > 500:
        item2.pos=(300,0)
    if item3.y > 500:
        item3.pos=(400,0)


























pgzrun.go()