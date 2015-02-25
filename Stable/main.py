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

global platform;
platform = platform.Platform()


platforms = []

for x in range(0, 100):
    platforms.append(platform)


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
    pygame.display.update()
    FPSCLOCK.tick(FPS)

def terminate():
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()