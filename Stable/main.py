'''HadoukemUp (a Super-Mario/Street-fighter clone)
Daniel Divers
John Comrie
Duncan Bunting
Alec Cowan
Sam Cumming

Created using Pygame

'''

import pygame, sys, Player, HadoukenBolt, platform, Menu, Enemy
from pygame.locals import *

FPS = 60
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

global menu;
menu = Menu.Menu()

global enemy;
enemy = Enemy.Enemy()

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
    menu.init()
    enemy.init(200, 200)
    platforms[0].init(100, 200, 5)
    platforms[1].init(100, 250, 4)
    platforms[2].init(100, 300, 3)
    platforms[3].init(100, 350, 2)
    platforms[4].init(100, 400, 1)
    
    print(player.rect)
    print(enemy.rect)
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
    player.updateGravity(platforms)
    bolt.update()
    enemy.update()
    #print(pygame.sprite.collide_rect(player, enemy))
    #enemy.MoveX(-1)
    
    #---------COLLISION DETECTION
    #if pygame.sprite.collide_mask(player,enemy):
    #    enemy.MoveX(1)
    #else:
     #   enemy.MoveX(-1)
    
   # if (pygame.sprite.collide_mask(bolt, enemy):
    #enemy.Die()
    
    #---------

def game_render():
    DISPLAYSURF.fill(BGCOLOR)
    if(menu.StartMenu == True and menu.CharacterSelectionMenu == False):
        menu.renderMenu(DISPLAYSURF);
        menu.renderMenutext(DISPLAYSURF);
    elif(menu.CharacterSelectionMenu == True and menu.StartMenu == False):
        menu.CharacterChRender(DISPLAYSURF);
        menu.renderCharacterChText(DISPLAYSURF);
		
    for x in range (0, 8):
        platforms[x].render(DISPLAYSURF)
    bolt.render(DISPLAYSURF)
    player.render(DISPLAYSURF)
    enemy.render(DISPLAYSURF)

    pygame.display.update()
    FPSCLOCK.tick(FPS)

def terminate():
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()