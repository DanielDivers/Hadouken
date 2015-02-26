import pygame, sys
from pygame.locals import *

class Enemy:
    spriteSheet = None
    image = None
    enemyX = None
    enemyY = None
    position = [enemyX, enemyY]
    
    rect = []
    
    #anim rects
    rects = [
    (0,134,42,25),(49,133,43,23), #Charging
    (95,130,42,28),(140,131,42,28),(185,130,42,27), #Walking
    (230,127,40,29),(273,128,43,32)#Dying
    ]
    
    AnimCounter = 0
    displaySurface = None
    
    def __init__(self):
        self.data = []
        
    def changeFrame(self,n):
        self.image = self.spriteSheet.subsurface(pygame.Rect(self.rects[n]))
        #self.image = pygame.transform.scale2x(self.image)
        
    def main(self):
        self.update()
        
    def init(self, posXIn, posYIn):
        self.spriteSheet = pygame.image.load("Images/Enemies.png").convert()
        self.spriteSheet.set_colorkey((255,0,255))
        self.AnimCounter = 0.0
        self.changeFrame(0)
        self.image = self.spriteSheet.subsurface(pygame.Rect(self.rects[0]))
        self.rect = self.image.get_rect()
        self.position = [posXIn, posYIn]
        self.rect.topleft = self.position
        
    def render(self, displaySurface):
        displaySurface.blit(self.image,self.image.get_rect(topleft = self.position))
     
    def MoveX(self, by):
        self.position[0] = self.position[0]+by
        if (by > 0):
            self.Walk(0.1)
            self.image = pygame.transform.flip(self.image, True, False)
        elif (by < 0):
            self.Walk(0.1)
            
        
    def Walk(self,speed):
        self.AnimCounter += speed
        if (speed > 0 and self.AnimCounter > 3):
            self.AnimCounter = 0
        if (speed < 0 and self.AnimCounter < 0):
            self.AnimCounter = 3
        self.changeFrame(int(self.AnimCounter))
        
    def Charge(self,speed):
        self.AnimCounter += speed
        if (speed > 0 and self.AnimCounter > 2):
            self.AnimCounter = 0
        if (speed < 0 and self.AnimCounter < 0):
            self.AnimCounter = 2
        self.changeFrame(2+int(self.AnimCounter))
        
    def Die(self,speed):
        self.AnimCounter+=speed;
        if(speed > 0 and self.AnimCounter > 2):
            self.AnimCounter = 0;
        
        self.changeFrame(int(self.AnimCounter));       
        
    def update(self):
        self.rect.topleft = self.position
        self.Walk(0.1)
        return