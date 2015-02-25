'''HadoukemUp (a Super-Mario/Street-fighter clone)
Daniel Divers
John Comrie
Duncan Bunting
Alec Cowan
Sam Cumming

Created using Pygame

'''

import pygame, sys, Player, HadoukenBolt, platform
from pygame.locals import *

FPS = 15
WINDOWWIDTH = 640
WINDOWHEIGHT = 480

#             R    G    B
WHITE     = (255, 255, 255)
BLACK     = (  0,   0,   0)
RED       = (255,   0,   0)
GREEN     = (  0, 255,   0)
DARKGREEN = (  0, 155,   0)
DARKGRAY  = ( 40,  40,  40)
BGCOLOR = BLACK


pygame.init()
effect = pygame.mixer.Sound('hadoukenogg.ogg')

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

global player;
player = Player.Player()

global bolt;
bolt = HadoukenBolt.HadoukenBolt()

#global platform;
#platform = platform.Platform()


platforms = []

for x in range(0, 100):
    platforms.append(platform.Platform())


def main():
    init()
    #while True:
    runGame()

def init():
    global FPSCLOCK, DISPLAYSURF
    
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
   
    bolt.init()
    player.init(bolt)
    platforms[0].init(100, 100, 10)
    #for x in range(0, 10):
    ''' platforms[0].init(100 + 20, 100)
    platforms[1].init(100 + 40, 100)
    platforms[2].init(100 + 60, 100)
    platforms[3].init(100 + 80, 100)
    platforms[4].init(100 + 100, 100)
    platforms[5].init(100 + 120, 100)
    platforms[6].init(100 + 140, 100)
    platforms[7].init(100 + 160, 100)
    platforms[8].init(0 + 180, 100) '''
    
    

def runGame():
    #game_init()
    while True:
        game_update()
        game_render()

#def game_init():

def game_update():

    for event in pygame.event.get(): # event handling loop
        if event.type == QUIT:
            terminate()
            
    player.update()
    bolt.update()


def game_render():
    DISPLAYSURF.fill(BGCOLOR)
    player.render(DISPLAYSURF)
    bolt.render(DISPLAYSURF)
    for x in range (0, 8):
        platforms[x].render(DISPLAYSURF)
    pygame.display.update()
    FPSCLOCK.tick(FPS)

def terminate():
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()