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
    
    rects = [(8, 13, 20, 23)];
    displaySurface = None;
    bolt = None

    
    def __init__(self):
        self.data = []

    def main(self):
        self.update();
        #self.render();
        
    def init(self,boltIn):
        self.spriteSheet = pygame.image.load("Images/Ryu.png").convert();
        #objSurf.set_colorkey((0,162,232));
        self.image = self.spriteSheet.subsurface(pygame.Rect(self.rects[0]));
        self.bolt = boltIn
        
    def render(self, displaySurface):
        displaySurface.blit(self.image,self.image.get_rect(topleft = self.position));
        
    def MoveX(self,by):
        self.position[0]=self.position[0]+by;
    
    def MoveY(self,by):
        self.position[1]=self.position[1]+by;
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
            self.MoveX(-1);
        if(pygame.key.get_pressed()[pygame.K_RIGHT]):
            self.MoveX(1);
        if(pygame.key.get_pressed()[pygame.K_UP]):
            self.MoveY(-1);
        if(pygame.key.get_pressed()[pygame.K_DOWN]):
            self.MoveY(1);
        if(pygame.key.get_pressed()[pygame.K_SPACE]):
            self.bolt.fire(self.position[0],self.position[1])

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