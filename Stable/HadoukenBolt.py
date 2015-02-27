import pygame, sys
from pygame.locals import *

DISPLAY_WIDTH = 640;
DISPLAY_HEIGHT = 480;

class HadoukenBolt:
    spriteSheet = None;
    image = None;
    boltX = 140
    boltY = 100
    position = [boltX, boltY];


    
    RyuBolt = [(149, 43, 19, 12),(169, 43, 21, 12),(158, 57, 25, 14)];
    DarkRyuBolt = [(145,114,17,11),(165,114,20,11),(153,128,24,13)];
    
    displaySurface = None;
    hasFired = False
    speed = 5

    AnimCounter = 0;
    
    BoltType = RyuBolt;

    rect = []

    
    def __init__(self):
        self.data = []
        self.AnimCounter = 0.0;
    def changeFrame(self, n):
        self.image = self.spriteSheet.subsurface(pygame.Rect(self.BoltType[n]));

        
    def init(self):
        self.spriteSheet = pygame.image.load("Images/Ryu.png").convert();

        self.image = self.spriteSheet.subsurface(pygame.Rect(self.RyuBolt[0]));

        self.image.set_colorkey((255,0,255));
        self.hasFired = False
        self.rect = self.image.get_rect()
        self.rect.topleft = self.position
        
    def render(self, displaySurface):
        displaySurface.blit(self.image,self.image.get_rect(topleft = self.position));
        
    def fire(self, posX, posY):
        self.boltX = posX
        self.boltY = posY
        self.position = [self.boltX+20, self.boltY]
        self.hasFired = True
        
    def update(self):
        if self.hasFired == True:
            self.boltX += self.speed
            self.position = [self.boltX, self.boltY]

            self.rect.topleft = self.position
            
        if(self.AnimCounter > 2):
            self.changeFrame(2);
        elif(self.AnimCounter > 1):
            self.changeFrame(1);
        elif(self.AnimCounter > 0):
            self.changeFrame(0);
            
        if(self.AnimCounter > 3):
            self.AnimCounter = 0;
        if(self.AnimCounter < 0):
            self.AnimCounter = 0;
            
        self.AnimCounter+=0.1;
        
        if(self.position[0] > DISPLAY_WIDTH or self.position[0] < 0):
            self.hasFired = False;
