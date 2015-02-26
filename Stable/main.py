'''HadoukemUp (a Super-Mario/Street-fighter clone)
Daniel Divers
John Comrie
Duncan Bunting
Alec Cowan
Sam Cumming

Created using Pygame

'''

import pygame, sys, Player, HadoukenBolt, platform, Menu
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

#global platform;
#platform = platform.Platform()
MenuState = 0;
ChooseChState = 1;
PlayState = 2;

global State;
State = MenuState;

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
    platforms[0].init(100, 200, 5)
    platforms[1].init(200, 300, 4)
    platforms[2].init(500, 200, 3)
    platforms[3].init(100, 500, 2)
    platforms[4].init(100, 600, 1)
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
    global State;
    State = MenuState;
    
    #game_init()
    #player.RyuType = player.DarkRyu;
    
    while True:
       if(State == MenuState or State == ChooseChState): 
            MenuRender();
            MenuUpdate();
            
       elif(State == PlayState):  
            game_update()
            game_render()

#def game_init():

def game_update():
    player.update()
    bolt.update()
 
   
def MenuUpdate():
    global State;
    
    if(State == MenuState):
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT:
                terminate()
            if pygame.mouse.get_pressed()[0]:
                MousePos = pygame.mouse.get_pos()
                
                #if(MousePos[0] > 180 and MousePos[0] < 445 and MousePos[1] > 45 and MousePos[1] < 205):
                    #State = PlayState;
                    
                #if clicked on Start Game
                if(pygame.Rect(180,50,255,35).collidepoint(MousePos)):
                    State = PlayState;
                if(pygame.Rect(180,175,255,35).collidepoint(MousePos)):
                    State = ChooseChState;
                    menu.ChangeToChooseCh(DISPLAYSURF);
                if(pygame.Rect(180,225,255,35).collidepoint(MousePos)):
                    terminate();
                    
    if(State == ChooseChState):
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT:
                terminate()
    

def MenuRender():
    #Main Menu State
    if(State == MenuState):
        menu.renderMenu(DISPLAYSURF);
        menu.renderMenutext(DISPLAYSURF);
        
    #Character Selection State
    elif(State == ChooseChState):
        menu.CharacterChRender(DISPLAYSURF);
        menu.renderCharacterChText(DISPLAYSURF);
        
    pygame.display.update()
        
def game_render():

    DISPLAYSURF.fill(BGCOLOR)
    #Game Running 
    player.render(DISPLAYSURF)
    
    bolt.render(DISPLAYSURF)
    
    for x in range (0, 8):
        platforms[x].render(DISPLAYSURF)
        
    pygame.display.update()
    FPSCLOCK.tick(FPS)
    
    for event in pygame.event.get(): # event handling loop
        if event.type == QUIT:
            terminate()

def terminate():
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()