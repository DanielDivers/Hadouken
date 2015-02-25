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
    (2,7,21,25),(26,7,20,25), #Idle
    (47,9,26,23),(74,7,22,25),(100,9,22,23), #Running
    (125,7,31,25), #Running Punch
    (160,3,19,30),(181,1,22,32),(206,2,28,31), #Jumping
    (2,38,21,25), #Idle (Attack)
    (24,38,23,25),(50,38,28,25), #Normal Attack
    (80,34,25,31),(107,34,28,31), #Jump Attack
    (137,40,18,11),(158,40,20,11),(145,54,24,13), #Fireball (Color 1)
    (188,46,18,13),(171,65,20,11),(194,65,24,13), #Fireball (Color 2)
    (207,39,16,24) #Special Fireball (Ken Only) 
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
        self.spriteSheet = pygame.image.load("Images/E.Ryu.png").convert();
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
            self.Run(0.1);
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
