import pygame, sys
from pygame.locals import *

DISPLAY_WIDTH = 640;
DISPLAY_HEIGHT = 480;

#             R    G    B
WHITE     = (255, 255, 255)
BLACK     = (  0,   0,   0)
RED       = (255,   0,   0)
GREEN     = (  0, 255,   0)
DARKGREEN = (  0, 155,   0)
DARKGRAY  = ( 40,  40,  40)
BGCOLOR = BLACK

class Menu:

    #will contain the whole loaded image
    spriteSheet = None;
    background = None;
    RyuSprites = None;
    
    #will contain cut image from UV's
    image = None;
    backImage = None;
    RyuImage = None;
    DarkRyuImage = None;
    FlashRyuImage = None;
    
    #positions for drawing
    RyuPosition = ((DISPLAY_WIDTH / 4) - 10, (DISPLAY_HEIGHT / 2) - 80);
    DarkRyuPosition = (((3*(DISPLAY_WIDTH / 4) - 30), (DISPLAY_HEIGHT / 2) - 80));
    FlashRyuPosition = (DISPLAY_WIDTH/2 - 20, 300);
    position = [(DISPLAY_WIDTH/2) - 140, 50];
    
    #UV's 
    RyuUV = [(8, 13, 20, 25)];
    DarkRyuImageUV = [(7, 82, 20, 23)];
    FlashRyuImageUV = [(7, 152, 20, 23)]
    MenuRect = [(0, 0, 280, 233)];
    ChooseChRect = [(0, 175, 575, 195)];
    BackgroundRect = [(0, 0, 640, 480)];
    
    #internal bools for switching states
    StartMenu = True;
    CharacterSelectionMenu = False;
    
    def init(self):
        #load in the images
		self.background = pygame.image.load("Images/Background.png").convert();
		self.spriteSheet = pygame.image.load("Images/MenuHolder.png").convert();
		#self.DarkSprites  = pygame.image.load("Images/Ryu.png").convert();
		self.RyuSprites  = pygame.image.load("Images/Ryu.png").convert();
		#self.FlashSprites  = pygame.image.load("Images/Ryu.png").convert();
        
		#make these colours not be drawn for the corresponding Image
		self.RyuSprites.set_colorkey((255,0,255));
		self.spriteSheet.set_colorkey((255,0,255));
        
		#Cut the loaded images with Specified UV's and store it
		self.image = self.spriteSheet.subsurface(pygame.Rect(self.MenuRect[0]));
		self.backImage = self.background.subsurface(pygame.Rect(self.BackgroundRect[0]));
		self.RyuImage = self.RyuSprites.subsurface(pygame.Rect(self.RyuUV[0]));
		self.DarkRyuImage = self.RyuSprites.subsurface(pygame.Rect(self.DarkRyuImageUV[0]));
		self.FlashRyuImage = self.RyuSprites.subsurface(pygame.Rect(self.FlashRyuImageUV[0]));

		#Scale the Sprites
		self.RyuImage = pygame.transform.scale2x(self.RyuImage);
		self.DarkRyuImage = pygame.transform.scale2x(self.DarkRyuImage)
		self.FlashRyuImage = pygame.transform.scale2x(self.FlashRyuImage)
 
    #renders the main menu
    def renderMenu(self,displaySurface):
        displaySurface.blit(self.backImage,self.backImage.get_rect(topleft = (0,0)));
        displaySurface.blit(self.image,self.image.get_rect(topleft = self.position));
        
    #will render the text for the main menu
    def renderMenutext(self, displaySurface):
        #Set up Font Style
        MenuFont = pygame.font.Font('freesansbold.ttf', 25);
        
        #Set the text to be written
        StartSurf = MenuFont.render('Start Game', True, WHITE);
        ChooseChSurf = MenuFont.render('Choose Character', True, WHITE);
        ExitSurf = MenuFont.render('Exit', True, WHITE);
        
        #make rectangles 
        StartRect = StartSurf.get_rect();
        ChooseChRect = ChooseChSurf.get_rect();
        ExitRect = ExitSurf.get_rect();
        
        #set up Coords for display
        StartRect.midtop = (DISPLAY_WIDTH / 2, 65);
        ChooseChRect.midtop = (DISPLAY_WIDTH / 2, StartRect.height + 125);
        ExitRect.midtop = (DISPLAY_WIDTH / 2, StartRect.height + 215);
        
        #Draw the text
        displaySurface.blit(StartSurf, StartRect);
        displaySurface.blit(ChooseChSurf, ChooseChRect);
        displaySurface.blit(ExitSurf, ExitRect);
    
    #will render the Character Selection Menu
    def CharacterChRender(self, displaySurface):
        displaySurface.blit(self.backImage,self.backImage.get_rect(topleft = (0,0)));
        displaySurface.blit(self.image,self.image.get_rect(topleft = self.position));
        
        #Displays Ryu Sprites
        displaySurface.blit(self.RyuImage,self.RyuImage.get_rect(topleft = self.RyuPosition));
        displaySurface.blit(self.DarkRyuImage ,self.DarkRyuImage.get_rect(topleft = self.DarkRyuPosition));
        displaySurface.blit(self.FlashRyuImage,self.FlashRyuImage.get_rect(topleft = self.FlashRyuPosition));
        
    #will render the Character Selection Menu's text
    def renderCharacterChText(self, displaySurface):
        #Set up Font Style
        MenuFont = pygame.font.Font('freesansbold.ttf', 25);
        
        #Set the text to be written
        RyuSurf = MenuFont.render('Ryu', True, WHITE);
        DarkRyuSurf = MenuFont.render('Dark Ryu', True, WHITE);
        FlashRyuSurf = MenuFont.render('Flash Ryu', True, WHITE);
        
        #make rectangles 
        RyuRect = RyuSurf.get_rect();
        DarkRyuRect = DarkRyuSurf.get_rect();
        FlashRyuRect = FlashRyuSurf.get_rect();
        
        #set up Coords for display
        RyuRect.midtop = (DISPLAY_WIDTH / 4, DISPLAY_HEIGHT/2 - 25);
        DarkRyuRect.midtop = (3*(DISPLAY_WIDTH/4) - 20, DISPLAY_HEIGHT/2 - 25);
        FlashRyuRect.midtop = (DISPLAY_WIDTH / 2 - 5, 3*(DISPLAY_HEIGHT/4) - 7);
        
        #Draw the text
        displaySurface.blit(RyuSurf, RyuRect);
        displaySurface.blit(DarkRyuSurf, DarkRyuRect);
        displaySurface.blit(FlashRyuSurf, FlashRyuRect);
        
    #wilExitSurf = MenuFont.render('Exit', True, WHITE);l switch UV's to the Character Selections
    def ChangeToChooseCh(self, displaySurface):
        self.position = [25, 200];
        self.image = self.spriteSheet.subsurface(pygame.Rect(self.ChooseChRect[0]));
    #will switch UV's to the Normal Menu's
    def ChangeToMenu(self, displaySurface):
        self.position = [(DISPLAY_WIDTH/2) - 140, 50];
        self.image = self.spriteSheet.subsurface(pygame.Rect(self.MenuRect[0]));