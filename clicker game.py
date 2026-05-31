import pgzrun 
import random
WIDTH=700   
HEIGHT=600
CENTRE=(WIDTH/2,HEIGHT/2)
FINAL_LEVEL=4
START_SPEED=1
ITEMS=["blackbomb","redbomb","yellowbomb","pinkbomb"]

game_over=False
game_complete=False
current_level=1
items=[]
animations=[]

def draw():

    screen.clear()
    screen.fill(color="black")
    if game_over:
        display_message("GAME OVER","YOU LOSE")
    elif game_complete:
        display_message("you WIN!","GAME OVER")
    else:
        for item in items:
            item.draw()


def update():
    global items
    if not items:
        items=make_items(current_level)
def make_items(level):
    item_names=["apple"]+[random.choice(ITEMS)for _ in range(level)]
    new_items=[Actor(name)for name in item_names]   
    gap=WIDTH/(len(new_items)+1)

    random.shuffle(new_items)
    for i,item in enumerate(new_items):
        item.x=(i+1)*gap
        item.y=0
        item.anchor = ("center","bottom")
        anim=animate(
            item,
            duration=max(1,START_SPEED-current_level),
            y=HEIGHT,
            on_finished=game_over_fun())
        animations.append(anim)
    return new_items   
        
def game_over_fun():
    global game_over
    game_over=True
def on_mouse_down(pos):
    for item in items:
        if item.collidepoint(pos):
            if "apple" in item.image:
                game_complete_fun()
            else:
                game_over_fun()
            break
def game_complete_fun():
    global current_level,items,animations,game_complete
    for anim in animations:
        if anim.running:
            anim.stop()
    if current_level==FINAL_LEVEL:
        game_complete=True
    else:
        current_level+=1
        items.clear()
        animations.clear()
def display_message(title,subtitle):
    screen.draw.text(title,fontsize=50,center=CENTRE,color="white")
    screen.draw.text(subtitle,fontsize=35,center=(CENTRE[0],CENTRE[1]+30),color="white")
pgzrun.go()
