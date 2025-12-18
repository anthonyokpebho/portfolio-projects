import pgzrun,random,pyautogui
print(pyautogui.size())
WIDTH,HEIGHT=pyautogui.size()
TITLE="SPACEBATTLE!"
w,h=WIDTH,HEIGHT
Score=0
Bullets=[]
Speed=5
Frequency=15
Villan=[]
GS="start"
spacejet=Actor("spacejet")
spacejet.pos=(1366,h/2)
def draw():
    screen.clear()
    screen.draw.text(f"score->{Score}",(w-100,40))
    spacejet.draw()
    if  GS=="start":
        screen.draw.text("Shoot the Villans by pressing the SPACE KEY \n Use ARROW KEYS to control the ship \n Press the SPACE KEY to start the Game",(w/4,h/3))
    if GS=="play":
        for i in Villan:
            i.draw()
        for i in Bullets:
            i.draw()
    if  GS=="Over":
            screen.draw.text("GAMEOVER",(w/2,h/2))

 
def update():
    global Score
    if GS=="play":
        for i in Villan:
            i.x+=Speed
            if i.x>h:
                Villan.remove(i)
        for i in Bullets: 
            i.x-=Speed
            if i.x<0:
                Bullets.remove(i)
            for j in Villan:
                if i.colliderect(j):
                    Score+=10
                    Villan.remove(j)
                    Bullets.remove(i)
                    print (Score)
        print(len(Bullets),len(Villan))

def on_key_down(key):
    global GS
    if GS=="start" and key==keys.SPACE:
        GS="play"
    elif GS=="play":
        if key==keys.LEFT:
            spacejet.x-=60
            if spacejet.x<0:
                spacejet.x=w
        if key==keys.RIGHT:
            spacejet.x+=60
            if spacejet.x>w:
                spacejet.x=0
        if key==keys.DOWN:
            spacejet.y+=60
            if spacejet.y>h:
                spacejet.y=h/2
        if key==keys.UP:
            spacejet.y-=60
            if spacejet.y<0:
                spacejet.y=h/2
        if key==keys.SPACE:
            bullet=Actor("bullet.png")
            bullet.pos=spacejet.x+40,spacejet.y
            Bullets.append(bullet)

def alienspaceshipwarehouse():
    alienspaceship=Actor("alienspaceship")
    alienspaceship.pos=-50,random.randint(0,h)
    Villan.append(alienspaceship)  

clock.schedule_interval(alienspaceshipwarehouse,5.0)


pgzrun.go()

