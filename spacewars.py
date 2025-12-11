import pgzrun,random,pyautogui
print(pyautogui.size())
WIDTH,HEIGHT=pyautogui.size()
TITLE="SPACEWARS!"
w,h=WIDTH,HEIGHT
print(h)

GameState="start"
Chances=3
Score=0
Bullets=[]
Speed=2
Frequency=10
Villan=[]
spaceship=Actor("spaceship")
spaceship.pos=(w/2,h-100)

def draw():
    screen.clear()
    screen.draw.text(f"score->{Score}",(w-100,40))
    spaceship.draw()
    if  GameState=="start":
        screen.draw.text("Shoot the Villans by pressing the SPACE KEY \n Use ARROW KEYS to control the ship \n Press the SPACE KEY to start the Game",(w/4,h/3))
    if GameState=="play":
        for i in Villan:
            i.draw()
        for i in Bullets:
            i.draw()
    if  GameState=="Over":
            screen.draw.text("GAMEOVER",(w/2,h/2))
def update():
    global Score,GameState
    if GameState=="play":

        print("hello")
        for i in Villan:
            i.y+=Speed
            if i.y>h:
                Villan.remove(i)
            if i.colliderect(spaceship):
                Chances-=1
                if Chances==0:
                    GameState="Over"

        for i in Bullets: 
            i.y-=Speed
            if i.y<0:
                Bullets.remove(i)
            for j in Villan:
                if i.colliderect(j):
                    Score+=10
                    Villan.remove(j)
                    Bullets.remove(i)
                    print (Score)
        print(len(Bullets),len(Villan))

def on_key_down(key):
    global GameState
    if GameState=="start" and key==keys.SPACE:
        GameState="play"
    elif GameState=="play":
        if key==keys.LEFT:
            spaceship.x-=50
            if spaceship.x<0:
                spaceship.x=w
        if key==keys.RIGHT:
            spaceship.x+=50 
            if spaceship.x>w:
                spaceship.x=0
        if key==keys.SPACE:
            bullet=Actor("bullet.png")
            bullet.pos=spaceship.x,spaceship.y-30
            Bullets.append(bullet)


def alienwarehouse():
    if GameState=="play":
        global Villan
        alien=Actor("alien")
        alien.pos=random.randint(50,w-50),-50
        Villan.append(alien)  
clock.schedule_interval(alienwarehouse,5.0)
pgzrun.go()