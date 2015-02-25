import pygame, sys
from pygame.locals import *

class Platform:
    spriteSheet = None
    image = None
    platformX = None
    platformY = None
    position = [platformX, platformY]
    rects = [(2,1, 25,24 )]
    displaySurface = None;
    length = 0
    
    def __init__(self):
        self.data = []
        
    def init(self, initPosX, initPosY, lengthIn):
        self.spriteSheet = pygame.image.load("Images/platform.png").convert()
        self.image = self.spriteSheet.subsurface(pygame.Rect(self.rects[0]))
        self.position = [initPosX, initPosY]
        self.length = lengthIn
        
    def render(self, displaySurface):
        x=0
        localPos = self.position
        while x < self.length:
            #newX = 24*x
            localPos = [self.position[0] + (24*x), localPos[1]]
            displaySurface.blit(self.image, self.image.get_rect(topleft = localPos))
            x+=1
     