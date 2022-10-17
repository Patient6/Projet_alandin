import pgzrun
from pgzero.builtins import Actor

TITLE = 'Aladdin'
WIDTH = 686
HEIGHT = 490

genius = Actor('genie', midtop=(343, 245))
genius.x_direction = 1 # right
genius.y_direction = 1 # down
genius.speed = 2


def update():
    if genius.x+genius.width/2 >= WIDTH and genius.x_direction == 1:
        genius.x_direction = -1
    if genius.x-genius.width/2 <= 0 and genius.x_direction == -1:
        genius.x_direction = 1
    
    if genius.y+genius.height/2 >= HEIGHT and genius.y_direction == 1:
        genius.y_direction = -1
    if genius.y-genius.height/2 <= 0 and genius.y_direction == -1:
        genius.y_direction = 1
    genius.x += genius.x_direction * genius.speed
    genius.y += genius.y_direction * genius.speed
        
def draw():
    screen.blit('background', (0, 0))
    genius.draw()


pgzrun.go()
