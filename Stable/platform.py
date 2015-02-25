import pygame, sys
from pygame.locals import *

class Platform:
    spriteSheet = None
    image = None;
    platformX = None
    platformY = None
    position = [platformX, platformY]
    rects = [(2,1, 25,24 )]
    displaySurface = None;
    
    def __init__(self):
        self.data = []
        
    def init(self, initPosX, initPosY):
        self.spriteSheet = pygame.image.load("Images/platform.png").convert()
        self.image = self.spriteSheet.subsurface(pygame.Rect(self.rects[0]))
        self.position = [initPosX, initPosY]
        
    def render(self, displaySurface):
        displaySurface.blit(self.image, self.image.get_rect(topleft = self.position))
     