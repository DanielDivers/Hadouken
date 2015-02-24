#Basic Python Test Using PyGame
 
import pygame, sys
from pygame.locals import *
 
#Global Constants
 
DISPLAY_WIDTH = 640;
DISPLAY_HEIGHT = 480;
BACK_COLOR = (0,0,255);
FPS_TARGET = 60;

#             R    G    B
WHITE     = (255, 255, 255)
BLACK     = (  0,   0,   0)
RED       = (255,   0,   0)
GREEN     = (  0, 255,   0)
DARKGREEN = (  0, 155,   0)
DARKGRAY  = ( 40,  40,  40)
BGCOLOR = BLACK

class Menu:
    spriteSheet = None;
    image = None;
    position = [(DISPLAY_WIDTH/2) - 140, 50];
    MenuRect = [(0, 0, 280, 233)];
    ChooseChRect = [(0, 175, 575, 195)];
    
    def init(self):
        self.spriteSheet = pygame.image.load("Images/MenuHolder.png").convert();
        #objSurf.set_colorkey((0,162,232));
        self.image = self.spriteSheet.subsurface(pygame.Rect(self.ChooseChRect[0]));
        #self.image = self.spriteSheet.subsurface(pygame.Rect(self.MenuRect[0]));
 
    def render(self,displaySurface):
        displaySurface.blit(self.image,self.image.get_rect(topleft = self.position));
        
    #will render the text for the Menu
    def rendertext(self, displaySurface):
        MenuFont = pygame.font.Font('freesansbold.ttf', 25);
        StartSurf = MenuFont.render('Start Game', True, WHITE);
        ChooseChSurf = MenuFont.render('Choose Character', True, WHITE);
        ExitSurf = MenuFont.render('Exit', True, WHITE);
        
        StartRect = StartSurf.get_rect();
        ChooseChRect = ChooseChSurf.get_rect();
        ExitRect = ExitSurf.get_rect();
        
        StartRect.midtop = (DISPLAY_WIDTH / 2, 65);
        ChooseChRect.midtop = (DISPLAY_WIDTH / 2, StartRect.height + 125);
        ExitRect.midtop = (DISPLAY_WIDTH / 2, StartRect.height + 215);
        
        displaySurface.blit(StartSurf, StartRect);
        displaySurface.blit(ChooseChSurf, ChooseChRect);
        displaySurface.blit(ExitSurf, ExitRect);
    
    #will render the Character Selection Menu
    def CharacterChRender(self, displaySurface):
        displaySurface.blit(self.image,self.image.get_rect(topleft = self.position));
    #will switch UV's to the Character Selections
    def ChangeToChooseCh(self, displaySurface):
        self.position = [25, 200];
        self.image = self.spriteSheet.subsurface(pygame.Rect(self.ChooseChRect[0]));
    #will switch UV's to the Normal Menu's
    def ChangeToMenu(self, displaySurface):
        self.position = [(DISPLAY_WIDTH/2) - 140, 50];
        self.image = self.spriteSheet.subsurface(pygame.Rect(self.MenuRect[0]));
        
class Player:
    
    spriteSheet = None;
    image = None;
    position = [100,100];
    rects = [(8, 13, 20, 23)];
    
    def init(self):
        self.spriteSheet = pygame.image.load("Images/Ryu.png").convert();
        #objSurf.set_colorkey((0,162,232));
        self.image = self.spriteSheet.subsurface(pygame.Rect(self.rects[0]));
    
    def render(self,displaySurface):
        displaySurface.blit(self.image,self.image.get_rect(topleft = self.position));
        
    def MoveX(self,by):
        self.position[0]=self.position[0]+by;
    
    def MoveY(self,by):
        self.position[1]=self.position[1]+by;
        
 
#Functions
 
def main():
        pygame.init();
        init();
        menu.ChangeToMenu(VIEWPORT);
        while True:
                update();
                render();
       
def init():
        global CLOCK, VIEWPORT, FONT
       
        CLOCK = pygame.time.Clock();
        VIEWPORT = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT));
        FONT = pygame.font.Font('freesansbold.ttf',18);
        pygame.display.set_caption('Simple Game');
        
        #FontSurface = FONT.render("Test",True,(255,255,255));
        
        global player;
        player = Player();
        player.init();
        
        global menu;
        menu = Menu();
        menu.init();

def update():
        #Update Function
       
        #Handle Events
        for event in pygame.event.get():
                if(event.type == QUIT):
                        close();
                if(event.type == KEYDOWN):
                        if(event.key == K_ESCAPE):
                                close();
       
        #Make Object Controllable
        if(pygame.key.get_pressed()[pygame.K_LEFT]):
                player.MoveX(-1);
        if(pygame.key.get_pressed()[pygame.K_RIGHT]):
                player.MoveX(1);
        if(pygame.key.get_pressed()[pygame.K_UP]):
                player.MoveY(-1);
        if(pygame.key.get_pressed()[pygame.K_DOWN]):
               player.MoveY(1);
       
        return;
 
def render():
        #Render Function
       
        #Clears The Screen
        VIEWPORT.fill(BACK_COLOR);
       
        #Draw Object
        #VIEWPORT.blit(player_image,player_image.get_rect(topleft = objPos));
        player.render(VIEWPORT);
        #menu.render(VIEWPORT);
        #menu.rendertext(VIEWPORT);
        menu.CharacterChRender(VIEWPORT);
        
        #Updates The Display
        pygame.display.update();
       
        #Syncs To Desired Framerate
        CLOCK.tick(FPS_TARGET)
       
        return;
       
def close():
        pygame.quit();
        sys.exit();
 
#Execute main
main();