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
    
    #position = [100,100];
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
    #spriteSheet = None;
    #image = None;
    
    AnimCounter = None;
    
    #rects = [(8, 13, 20, 23)];
    displaySurface = None;
    bolt = None

    
    def __init__(self):
        self.data = []
        #self.spriteSheet = pygame.image.load("Images/Ryu.png").convert();
        

        
        
    def changeFrame(self,n): 
        self.image = self.spriteSheet.subsurface(pygame.Rect(self.rects[n]));
        self.image = pygame.transform.scale2x(self.image);

    def main(self):
        self.update();
        #self.render();
        
    def init(self,boltIn):
        self.spriteSheet = pygame.image.load("Images/Ryu.png").convert();
        self.spriteSheet.set_colorkey((255,0,255));
        self.AnimCounter = 0.0;
        self.changeFrame(0);
        #objSurf.set_colorkey((0,162,232));
        self.image = self.spriteSheet.subsurface(pygame.Rect(self.rects[0]));
        self.bolt = boltIn
        
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
    #Functions
    #def init(self):
    #global CLOCK, VIEWPORT, FONT
     #  
    #CLOCK = pygame.time.Clock();
    #VIEWPORT = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT));
    #FONT = pygame.font.Font('freesansbold.ttf',18);
    #pygame.display.set_caption('Simple Game');
    #FontSurface = FONT.render("Test",True,(255,255,255));       
    def update(self):
        #Update Function
        #Handle Events
               
        #Make Object Controllable
        if(pygame.key.get_pressed()[pygame.K_LEFT]):
            self.Run(-0.1);
            self.image = pygame.transform.flip(self.image, True, False)
            self.MoveX(-1);
        elif(pygame.key.get_pressed()[pygame.K_RIGHT]):
            self.Run(0.1);
            self.MoveX(1);
        elif(pygame.key.get_pressed()[pygame.K_UP]):
            self.MoveY(-1);
        elif(pygame.key.get_pressed()[pygame.K_DOWN]):
            self.MoveY(1);
        elif(pygame.key.get_pressed()[pygame.K_SPACE]):
            self.bolt.fire(self.position[0],self.position[1])
        else:
            self.Idle(0.08);
        
        #if(self.image.get_rect(topleft = self.position).collidepoint(300,100)):
        #   self.changeFrame(11);

        return;
        
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