#Basic Python Test Using PyGame
 
import pygame, sys
from pygame.locals import *
 
#Global Constants
 
DISPLAY_WIDTH = 640;
DISPLAY_HEIGHT = 480;
BACK_COLOR = (0,0,255);
FPS_TARGET = 60;



class Player:
    spriteSheet = None;
    image = None;
    playerX = 100;
    playerY = 100;
    position = [playerX,playerY];

    Right = 0;
    Left = 1;
    counter = 0;
    Fired = False;
    Facing = Right;
    
    Ryu = [
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
    ]

    rect = []
    #position = [100,100];
    
    FlashRyu = [
    (7,152,21,24),(31,152,20,24), #Idle
    (52,153,26,25),(79,152,21,25),(101,154,22,22), #Running
    (126,152,31,24), #Running Punch
    (161,151,19,30),(185,150,22,31),(208,151,28,30), #Jumping
    (7,183,21,24), #Idle (Attack)
    (30,183,23,24),(55,183,28,24), #Normal Attack
    (87,182,25,30),(114,182,28,30), #Jump Attack
    (150,44,17,11),(170,44,20,11),(157,58,24,13), #Fireball (Color 1)
    (195,44,17,11),(215,44,20,11),(202,58,24,13) #Fireball (Color 2)
    ];
    
    #spriteSheet = None;
    #image = None;
    
    RyuType = Ryu;
    AnimCounter = None;
    displaySurface = None;
    bolt = None

    def __init__(self):
        self.data = []
        
    def changeFrame(self,n): 
        self.image = self.spriteSheet.subsurface(pygame.Rect(self.RyuType[n]));
        self.image = pygame.transform.scale2x(self.image);

    def main(self):
        self.update();
        
    def init(self,boltIn):
        self.spriteSheet = pygame.image.load("Images/Ryu.png").convert();
        self.spriteSheet.set_colorkey((255,0,255));
        self.AnimCounter = 0.0;
        self.changeFrame(0);

        self.image = self.spriteSheet.subsurface(pygame.Rect(self.RyuType[0]));


        #objSurf.set_colorkey((0,162,232));
        #self.image = self.spriteSheet.subsurface(pygame.Rect(self.rects[0]));
        self.rect = self.image.get_rect()
        self.rect.topleft = self.position
        self.bolt = boltIn
        self.rect[3] = self.rect[3]*2
        self.falling = True
        
    def render(self, displaySurface):
        displaySurface.blit(self.image,self.image.get_rect(topleft = self.position));
        
    def MoveX(self,by):
        self.position[0]=self.position[0]+by;
    
    def MoveY(self,by):
        self.position[1]=self.position[1]+by;
        
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

    def IdleFire(self,speed):
        self.AnimCounter+=speed;
        if(speed > 0 and self.AnimCounter > 2):
            self.AnimCounter = 0;
        
        self.changeFrame(10+int(self.AnimCounter));
    def CheckDirection(self):
        if(self.Facing == self.Left):
            self.image = pygame.transform.flip(self.image, True, False)
            
    def update(self, effectIn):
        #Update Function
        #Handle Events
        self.rect.topleft = self.position

        #Make Object Controllable
        if(pygame.key.get_pressed()[pygame.K_LEFT]):
            self.Run(0.1);
            self.MoveX(-1);
            self.Facing = self.Left;
        elif(pygame.key.get_pressed()[pygame.K_RIGHT]):
            self.Run(0.1);
            self.MoveX(1);
            self.Facing = self.Right;
        elif(pygame.key.get_pressed()[pygame.K_UP]):
            self.MoveY(-4);
            self.changeFrame(8)
            self.image = pygame.transform.flip(self.image, True, False)
        elif(pygame.key.get_pressed()[pygame.K_DOWN]):
            self.MoveY(1);
        elif(pygame.key.get_pressed()[pygame.K_SPACE] and self.bolt.hasFired == False):
            self.bolt.fire(self.position[0],self.position[1])
            self.Fired = True;
            effectIn.play()
        else:
            self.Idle(0.08);
            

        if(self.Fired == True):
            self.counter +=1;
            self.IdleFire(0.1);
            
            if(self.counter >= 10):
                self.Fired = False;
                self.counter = 0;
        self.CheckDirection();

        return;

    
    
    def updateGravity(self,platforms):
        
        platformRects = []
        
        for platform in platforms:
            if (not platform.image == None):
                platformRects.insert(0,pygame.Rect(platform.position[0],platform.position[1],platform.collideLengths[0],5));
            
            
        if(not pygame.Rect(self.rect.x,self.rect.y+self.rect.h,self.rect.w,3).collidelist(platformRects) == -1):
            self.falling = False;
        else:
            self.falling = True;
        
        if(self.falling):        
            self.MoveY(3);
    '''def render(self, surf):
        #Render Function
        #Clears The Screen
        surf.fill(BACK_COLOR);
    
        #Draw Object
        surf.blit(player_image,player_image.get_rect(topleft = objPos));
        #self.render(surf);
        
        #Updates The Display
       # pygame.display.update();
       
        #Syncs To Desired Framerate
        #CLOCK.tick(FPS_TARGET)
       
        return;'''
    

       
#def close():
 #       pygame.quit();
 #       sys.exit();
 
#Execute main
#main();

