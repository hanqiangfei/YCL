import pgzrun

WIDTH = 800
HEIGHT = 600
MAX_BULLETS=10
bullets=[]

player=Actor("actor/001") 
player.scale=2.0
player.pos=(300,500)

def draw():
    screen.clear()
    screen.draw.circle((400, 300), 30, 'white')
    player.draw()
    for bullet in bullets:
        bullet.draw()

def update():
    move_bullets()
    if keyboard.right:
        player.x=alien.x+1

def move_bullets():
    #pass
    for bullet in bullets:
        bullet.y = bullet.y - 6
        if bullet.y < 0:
            bullets.remove(bullet)

def on_key_down(key):
    if key==keys.SPACE and len(bullets) <MAX_BULLETS:        
        print("bullet")
        bullet=Actor("bullet",pos=(player.x,player.y))
        bullets.append(bullet)

pgzrun.go()