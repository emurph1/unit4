#Emily Murphy
#2017-10-27
#bouncingBall.py - ball bounces in frame

from ggame import *

blue = Color(0x0000FF,1)
black = Color(0x000000,1)
white = Color(0xFFFFFF,1)

whiteOutline = LineStyle(1, white)
blackOutline = LineStyle(10, black)

blackRectangle = RectangleAsset(900, 600, whiteOutline, black)
blueCircle = CircleAsset(100, whiteOutline, blue)



Sprite(blackRectangle)
Sprite(blueCircle,(200,300))

App().run()