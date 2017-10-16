#Emily Murphy
#2017-10-16
#colorChangeWindow.py - pops up window to colored window

from random import randint
from ggame import *

red = Color(0xFF0000,1)
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)
black = Color(0x000000,1)
white = Color(0xFFFFFF,1)

whiteOutine = LineStyle(1, white)

blueRectangle = RectangleAsset(500, 200, whiteOutline, blue)
greenRectangle = RectangleAsset(500, 200, whiteOutline, green)
blackRectangle = RectangleAsset(500, 200, whiteOutline, black)
redRectangle = RectangleAsset(500, 200, whiteOutline, red)

def mouseClick(event):
    if event == 1:
        Sprite(blueRectangle)
    elif event == 2:
        Sprite(greenRectangle)
    elif event == 3:
        Sprite(blackRectangle)
    elif event == 4:
        Sprite(redRectangle)

App().listenMouseEvent('click',mouseClick)
App.run()
