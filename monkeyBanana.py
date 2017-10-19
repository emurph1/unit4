#Emily Murphy
#2017-10-19
#monkeyBanana.py - monkey banana game

from ggame import *

#constants
ROWS = 20
COLS = 40
CELL_SIZE = 20

if __name__ == '__main__':
    
    green = Color(0x006600,1)
    brown = Color(0x884513,1)
    
    jungleBox = RectangleAsset(COLS*CELL_SIZE,ROWS*CELL_SIZE,LineStyle(1,green),green)
    brownBox = RectangleAsset(CELL_SIZE, CELL_SIZE, LineStyle(1,brown),brown)
    
    Sprite(jungleBox)
    Sprite(brownBox)
    
    App().run()

