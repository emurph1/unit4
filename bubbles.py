#Emily Murphy
#2017-10-26
#bubbles.py - opens window and click causes bubbles to appear
from ggame import *
from random import randint

red = Color(0xFF0000,1)
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)
black = Color(0x000000,1)
white = Color(0xFFFFFF,1)
yellow = Color(0xFFFF33,1)


whiteOutline = LineStyle(10, white)


def mouseClick(Event):
    num = randint(1,4)
    radius = randint(1,200)
    if num == 1:
        Circle = CircleAsset(radius, whiteOutline, green)
    elif num == 2:
        Circle = CircleAsset(radius, whiteOutline, blue)
    elif num == 3:
        Circle = CircleAsset(radius, whiteOutline, red)
    elif num == 4:
        Circle = CircleAsset(radius, whiteOutline, yellow)
    x = randint(100,900)
    y = randint(100,500)
    Sprite(Circle,(x,y))
        

App().listenMouseEvent('click',mouseClick)
App().run()