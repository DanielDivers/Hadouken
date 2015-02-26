#Basic Python Test Using PyGame

#execfile("Player Class.py")

import pygame, sys
from pygame.locals import *

#Global Constants

DISPLAY_WIDTH = 640;
DISPLAY_HEIGHT = 480;
BACK_COLOR = (0,0,255);
FPS_TARGET = 60;

class Player:

    position = [100,100];
    rects = [
    (8,13,21,24),(32,13,20,24), #Idle
    (53,12,26,25),(80,12,21,25),(102,15,22,22), #Running
    (127,13,31,24), #Running Punch
    (164,12,19,30),(188,11,22,31),(211,12,28,30), #Jumping
    (8,40,21,24), #Idle (Attack)
    (32,40,23,24),(57,40,28,24), #Normal Attack
    (88,39,25,30),(115,39,28,30), #Jump Attack
    (150,44,17,11),(170,44,20,11),(157,58,24,13), #Fireball (Color 1)
    (195,44,17,11),(215,44,20,11),(202,58,24,13) #Fireball (Color 2)
    ];
    
    DarkRyu = [
    (7,82,21,24),(31,82,20,24), #Idle
    (52,83,26,25),(79,82,21,25),(101,84,22,22), #Running
    (126,82,31,24), #Running Punch
    (161,81,19,30),(185,80,22,31),(208,81,28,30), #Jumping
    (7,110,21,24), #Idle (Attack)
    (30,110,23,24),(55,110,28,24), #Normal Attack
    (87,109,25,30),(114,109,28,30), #Jump Attack
    (145,114,17,11),(165,114,20,11),(153,128,24,13), #Fireball (Color 1)
    (195,44,17,11),(215,44,20,11),(202,58,24,13) #Fireball (Color 2)
    ];
    
    spriteSheet = None;
    image = None;
   
    
    AnimCounter = None;
    
    def __init__(self):
        self.spriteSheet = pygame.image.load("Images/Ryu.png").convert();
        self.spriteSheet.set_colorkey((0,255,0));
        self.AnimCounter = 0.0;
        self.changeFrame(0);    
        
    def changeFrame(self,n): 
        self.image = self.spriteSheet.subsurface(pygame.Rect(self.DarkRyu[n]));
        self.image = pygame.transform.scale2x(self.image);

    def render(self,displaySurface):
        displaySurface.blit(self.image,self.image.get_rect(topleft = self.position));
        
    def Run(self,speed):
        self.AnimCounter+=speed;
        if(speed > 0 and self.AnimCounter > 2):
            self.AnimCounter = 0;
        if(speed < 0 and self.AnimCounter < 0):
            self.AnimCounter = 2;
        self.changeFrame(2+int(self.AnimCounter));
        
    def Idle(self,speed):
        self.AnimCounter+=speed;
        if(speed > 0 and self.AnimCounter > 2):
            self.AnimCounter = 0;
        
        self.changeFrame(int(self.AnimCounter));
        

    def MoveX(self,by):
        self.position[0]=self.position[0]+by;

    def MoveY(self,by):
        self.position[1]=self.position[1]+by;


#Functions

def main():
    pygame.init();
    init();

    while True:
        update();
        render();
        
    return;

def init():
    global CLOCK, VIEWPORT, FONT;

    CLOCK = pygame.time.Clock();
    VIEWPORT = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT));
    FONT = pygame.font.Font('freesansbold.ttf',18);
    pygame.display.set_caption('Simple Game');

    #FontSurface = FONT.render("Test",True,(255,255,255));

    global player;
    player = Player();
    
    return;

def update():
    #Update Function

    #Handle Events
    for event in pygame.event.get():
        if(event.type == QUIT):
            close();
        if(event.type == KEYDOWN):
            if(event.key == K_ESCAPE):
                close();
                


    #Make Object Controllable
    if(pygame.key.get_pressed()[pygame.K_LEFT]):
        player.Run(-0.1);
        player.image = pygame.transform.flip(player.image,True,False);
        player.MoveX(-1);
    elif(pygame.key.get_pressed()[pygame.K_RIGHT]):
        player.Run(0.1);
        #player.image = pygame.transform.flip(player.image,True,False);
        player.MoveX(1);
    else:
        player.Idle(0.08);
        
    if(pygame.key.get_pressed()[pygame.K_UP]):
        player.MoveY(-1);
    if(pygame.key.get_pressed()[pygame.K_DOWN]):
        player.MoveY(1);
        
    if(player.image.get_rect(topleft = player.position).collidepoint(300,100)):
        player.changeFrame(11);

    return;

def render():
    #Render Function

    #Clears The Screen
    VIEWPORT.fill(BACK_COLOR);

    #Draw Object
    #VIEWPORT.blit(player_image,player_image.get_rect(topleft = objPos));
    player.render(VIEWPORT);

    #Updates The Display
    pygame.display.update();

    #Syncs To Desired Framerate
    CLOCK.tick(FPS_TARGET)

    return;

def close():
    pygame.quit();
    sys.exit();

#Execute main
main();