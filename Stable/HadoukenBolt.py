import pygame, sys
from pygame.locals import *

class HadoukenBolt:
	spriteSheet = None;
	image = None;
	boltX = 140
	boltY = 100
	position = [boltX, boltY];
	rects = [(150,44,17,11),(170,44,20,11),(157,58,24,13)];
	displaySurface = None;
	hasFired = False
	speed = 5
	count = 0
	rect = []

	def __init__(self):
		self.data = []

	def init(self):
		self.spriteSheet = pygame.image.load("Images/Ryu.png").convert();
		self.spriteSheet.set_colorkey((255,0,255));
		self.image = self.spriteSheet.subsurface(pygame.Rect(self.rects[0]));
		self.hasFired = False
		self.rect = self.image.get_rect()
		self.rect.topleft = self.position
		
	def reset(self):
		self.image = self.spriteSheet.subsurface(pygame.Rect(self.rects[0]));
		self.count=0
		self.hasFired = False

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
			self.count+=1
			if(self.count>=20):
				self.image = self.spriteSheet.subsurface(pygame.Rect(self.rects[1]));
			if(self.count>=40):
				self.image = self.spriteSheet.subsurface(pygame.Rect(self.rects[2]));