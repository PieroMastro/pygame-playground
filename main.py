#########################################################
## File Name: main.py                                  ##
## Description: Demo project for Algorithmic Academy   ##
#########################################################
from pygame import *

init()
SCREEN_HEIGHT = 900
SCREEN_WIDTH = 500
window = display.set_mode((SCREEN_HEIGHT,  SCREEN_WIDTH))

def main():
    run = True
    while run:
        for e in event.get():
            if e.type() == QUIT:
                run : False
                
    quit()
    
if __name__ == '__main__':
    main()
