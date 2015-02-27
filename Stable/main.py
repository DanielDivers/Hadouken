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

MenuState = 0;
ChooseChState = 1;
PlayState = 2;

global State
State = MenuState

spawnPoint1 = [600, 170]
spawnPoint2 = [600, 270]
spawnPoint3 = [600, 370]


timer = 0
spawnControl = 3
#global platform;
#platform = platform.Platform()


platforms = []
enemies = []

for x in range(0, 100):
    platforms.append(platform.Platform())

enemies.append(Enemy.Enemy())
enemies.append(Enemy.Enemy())
enemies.append(Enemy.Enemy())
    

def main():
    init()
    #while True:
    runGame()

def init():
    global FPSCLOCK, DISPLAYSURF
    
    
    pygame.mixer.music.load('guile.mp3')
    pygame.mixer.music.play(0)
    
    
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
   
    bolt.init()
    player.init(bolt)
    menu.init()

    enemies[0].init(600, 170)
    enemies[1].init(600, 270)
    enemies[2].init(600, 370)
    platforms[0].init(0, 200, 26)
    platforms[1].init(0, 300, 26)
    platforms[2].init(0, 400, 26)
    #platforms[2].init(100, 300, 3)

    platforms[3].init(100, 350, 2)
    platforms[4].init(100, 400, 1)
    
    print(player.rect)
    #print(enemy.rect)

    print(platforms[0].rect)

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
    global State
    State = MenuState
    
    while True:
        if(State == MenuState or State == ChooseChState):
            MenuRender()
            MenuUpdate()
        elif(State == PlayState):
            game_update()
            game_render()

#def game_init():

def game_update():  
    global timer
    global spawnControl
    for event in pygame.event.get(): # event handling loop
        if event.type == QUIT:
            terminate()
            

    player.update(effect)
    player.updateGravity(platforms)
    bolt.update()
    for enemy in enemies:
        if(not enemy.image == None):
            enemy.render(DISPLAYSURF)
    
            enemy.update()
            if enemy.dying == False:
                enemy.MoveX(-1)
        
            if pygame.sprite.collide_mask(bolt, enemy):
                enemy.Die(0.01)
                enemy.position[0] = 800 
                enemy.position[1] = 800         
    

    #print(pygame.sprite.collide_rect(player, enemy))
    #enemy.MoveX(-1)
    
    #---------COLLISION DETECTION
    #if pygame.sprite.collide_mask(player,enemy):
    #    enemy.MoveX(1)
    #else:
    #for x in range(0, 5):
    if pygame.sprite.collide_rect(player, platforms[0]):
        print('Impact')
        
    print(timer) 
    if (timer > 60):
    
        enemies.append(Enemy.Enemy())
        enemies.append(Enemy.Enemy())
        enemies.append(Enemy.Enemy())
        enemies[spawnControl].init(600, 370)
        enemies[spawnControl+1].init(600, 270)
        enemies[spawnControl+2].init(600, 170)
        
        spawnControl += 3
        timer = 0
    
    timer+=1

    
    
    #---------
 
   
def MenuUpdate():
    global State;
    
    if(State == MenuState):
        for event in pygame.event.get(): # event handling loop
        
            #if left mouse button is pressed
            if pygame.mouse.get_pressed()[0]:
                MousePos = pygame.mouse.get_pos()

                #if clicked on Start Game
                if(pygame.Rect(180,50,255,35).collidepoint(MousePos)):
                    State = PlayState;
                #if clicked on Choose Character
                if(pygame.Rect(180,135,255,35).collidepoint(MousePos)):
                    State = ChooseChState;
                    menu.ChangeToChooseCh(DISPLAYSURF);
                #if clicked on exit or Escape
                if(pygame.Rect(180,225,255,35).collidepoint(MousePos) or pygame.key.get_pressed()[pygame.K_ESCAPE]):
                    terminate();
                    
    if(State == ChooseChState):
        for event in pygame.event.get(): # event handling loop
            if(pygame.key.get_pressed()[pygame.K_ESCAPE]):
                State = MenuState;
                menu.ChangeToMenu(DISPLAYSURF);
                
            #if left mouse button is pressed
            if pygame.mouse.get_pressed()[0]:
                MousePos = pygame.mouse.get_pos()
                
                #if the Rect "Ryu" is clicked
                if(pygame.Rect(20,WINDOWHEIGHT/2 - 35,255,35).collidepoint(MousePos)):
                    player.RyuType = player.Ryu
                    bolt.BoltType = bolt.RyuBolt;
                    State = MenuState;
                    menu.ChangeToMenu(DISPLAYSURF);
                    
                #if the Rect "Dark Ryu" is clicked
                if(pygame.Rect(315,WINDOWHEIGHT/2 - 35,255,35).collidepoint(MousePos)):
                    player.RyuType = player.DarkRyu;
                    bolt.BoltType = bolt.DarkRyuBolt;
                    State = MenuState;
                    menu.ChangeToMenu(DISPLAYSURF);
                    
                #if the Rect "Flash Ryu" is clicked
                if(pygame.Rect(165,WINDOWHEIGHT/2 + 100,255,35).collidepoint(MousePos)):
                    player.RyuType = player.FlashRyu;
                    bolt.BoltType = bolt.RyuBolt;
                    State = MenuState;
                    menu.ChangeToMenu(DISPLAYSURF);

    
    #---------

def MenuRender():
    #Main Menu State
    if(State == MenuState):
        DISPLAYSURF.fill(BGCOLOR)
        if(menu.StartMenu == True and menu.CharacterSelectionMenu == False):
            menu.renderMenu(DISPLAYSURF);
            menu.renderMenutext(DISPLAYSURF);
        
    #Character Selection State
    elif(State == ChooseChState):
        menu.CharacterChRender(DISPLAYSURF);
        menu.renderCharacterChText(DISPLAYSURF);
        
    pygame.display.update()
        
def game_render():


    menu.renderBackground(DISPLAYSURF)
        
    #DISPLAYSURF.fill(BGCOLOR)
    #Game Running 
    player.render(DISPLAYSURF)
    bolt.render(DISPLAYSURF)
    for enemy in enemies:
        if(not enemy.image == None):
            enemy.render(DISPLAYSURF)

    for x in range (0, 8):
        platforms[x].render(DISPLAYSURF)
    pygame.display.update()
    FPSCLOCK.tick(FPS)
    
    

def terminate():
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()