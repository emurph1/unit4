#Emily Murphy
#2017-10-27
#bouncingBall.py - ball bounces in frame

from ggame import *
from random import randint

blue = Color(0x0000FF,1)
black = Color(0x000000,1)
white = Color(0xFFFFFF,1)

whiteOutline = LineStyle(1, white)
blackOutline = LineStyle(10, black)

blackRectangle = RectangleAsset(900, 600, blackOutline, black)


circle = blueCircle = CircleAsset(100, blackOutline, blue)

def moveCircle():
    banana.x = randint(0, COLS-1)*CELL_SIZE
    banana.y = randint(0, ROWS-1)*CELL_SIZE
    data['frames'] = 0

def step():
    data['frames'] += 1
    if data['frames'] == 200:
        moveBanana()

Sprite(blackRectangle)
Sprite(blueCircle,(200,300))

App().run(step)