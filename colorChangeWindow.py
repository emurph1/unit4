#Emily Murphy
#2017-10-16
#colorChangeWindow.py - pops up window to colored window

from random import randint
from ggame import *

num = randint(1,4)

red = Color(0xFF0000,1)
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)
black = Color(0x000000,1)
white = Color(0xFFFFFF,1)

whiteOutine = LineStyle(1, white)

blueRectangle = RectangleAsset(500, 200, whiteOutine, blue)
greenRectangle = RectangleAsset(500, 200, whiteOutine, green)
blackRectangle = RectangleAsset(500, 200, whiteOutine, black)
redRectangle = RectangleAsset(500, 200, whiteOutine, red)

def mouseClick(Event):
    if num == 1:
        Sprite(blueRectangle)
    elif num == 2:
        Sprite(greenRectangle)
    elif num == 3:
        Sprite(blackRectangle)
    elif num == 4:
        Sprite(redRectangle)

App().listenMouseEvent('click',mouseClick)



