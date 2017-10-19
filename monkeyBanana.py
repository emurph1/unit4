#Emily Murphy
#2017-10-19
#monkeyBanana.py - monkey banana game

from ggame import *

#constants
ROWS = 31
COLS = 54
CELL_SIZE = 20

def moveRight(event):
    monkey.x += CELL_SIZE

def moveLeft(event):
    monkey.x -= CELL_SIZE
    
def moveUp(event):
    monkey.y -= CELL_SIZE
    
def moveDown(event):
    monkey.y += CELL_SIZE

if __name__ == '__main__':
    
    green = Color(0x006600,1)
    brown = Color(0x884513,1)
    yellow = Color(0xFFFF00,1)
    
    jungleBox = RectangleAsset(COLS*CELL_SIZE,ROWS*CELL_SIZE,LineStyle(1,green),green)
    monkeyBox = RectangleAsset(CELL_SIZE, CELL_SIZE, LineStyle(1,brown),brown)
    bananaBox = RectangleAsset(CELL_SIZE, CELL_SIZE, LineStyle(1,yellow),yellow)
    
    Sprite(jungleBox)
    monkey = Sprite(monkeyBox)
    Sprite(bananaBox, ((COLS*CELL_SIZE)/2, (ROWS*CELL_SIZE)/2))
    
    App().listenKeyEvent('keydown', 'right arrow', moveRight)
    App().listenKeyEvent('keydown', 'left arrow', moveLeft)
    App().listenKeyEvent('keydown', 'up arrow', moveLeft)
    App().listenKeyEvent('keydown', 'down arrow', moveLeft)
    App().run()

