import pygame, sys
from pygame.locals import *

class HadoukenBolt:
    spriteSheet = None;
    image = None;
    position = [140, 100];
    rects = [(8, 13, 20, 23)];
    displaySurface = None;
    
    def __init__(self):
        self.data = []
        
    def init(self):
        self.spriteSheet = pygame.image.load("Images/Ryu.png").convert();
        self.image = self.spriteSheet.subsurface(pygame.Rect(self.rects[0]));
        
    def render(self, displaySurface):
        displaySurface.blit(self.image,self.image.get_rect(topleft = self.position));
        
    def fire(self, posX, posY):
        self.position = [posX+20, posY];
        