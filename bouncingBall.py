#Emily Murphy
#2017-10-27
#bouncingBall.py - ball bounces in frame

from ggame import *

blue = Color(0x0000FF,1)
black = Color(0x000000,1)


blackOutline = LineStyle(10, black)

blueRectangle = RectangleAsset(500, 700, blackOutine, blue)

Sprite(blueRectangle)
App().run()