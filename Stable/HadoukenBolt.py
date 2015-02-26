import pygame, sys
from pygame.locals import *

class HadoukenBolt:
    spriteSheet = None;
    image = None;
    boltX = 140
    boltY = 100
    position = [boltX, boltY];
    rects = [(2, 7, 21, 25)];
    displaySurface = None;
    hasFired = False
    speed = 5
    rect = []
    
    def __init__(self):
        self.data = []
        
    def init(self):
        self.spriteSheet = pygame.image.load("Images/Ryu.png").convert();
        self.image = self.spriteSheet.subsurface(pygame.Rect(self.rects[0]));
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
            
            
        