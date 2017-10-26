#Emily Murphy
#2017-10-26
#bubbles.py - opens window and click causes bubbles to appear


red = Color(0xFF0000,1)
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)
black = Color(0x000000,1)
white = Color(0xFFFFFF,1)

def mouseClick(Event):
    num = randint(1,4)
    if num == 1:
        Sprite(blueRectangle)
    elif num == 2:
        Sprite(greenRectangle)
    elif num == 3:
        Sprite(blackRectangle)
    elif num == 4:
        Sprite(redRectangle)
        

App().listenMouseEvent('click',mouseClick)
App().run()