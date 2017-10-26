#Emily Murphy
#2017-10-26
#bubbles.py - opens window and click causes bubbles to appear
from ggame import *

red = Color(0xFF0000,1)
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)
black = Color(0x000000,1)
white = Color(0xFFFFFF,1)
yellow = Color(0xFFFF33,1)


whiteOutline = LineStyle(10, white)


def mouseClick(Event):
    num = randint(1,4)
    if num == 1:
        greenCircle = CircleAsset(100, whiteOutline, green)
    elif num == 2:
        blueCircle = CircleAsset(100, whiteOutline, blue)
    elif num == 3:
        redCircle = CircleAsset(100, whiteOutline, red)
    elif num == 4:
        yellowCircle = CircleAsset(100, whiteOutline, yellow)
    x = randint(200,800)
    y = randint(200,800)
    Sprite(yellowCircle,(x,y))
        

App().listenMouseEvent('click',mouseClick)
App().run()