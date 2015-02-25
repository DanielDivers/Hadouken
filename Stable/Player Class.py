#Basic Python Test Using PyGame
 #execfile("Player Class.py")
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
    RyuImageUV = [(8, 13, 20, 23)];
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
        self.RyuSprites  = pygame.image.load("Images/Ryu.png").convert();
        
        #make these colours not be drawn for the corresponding Image
        self.RyuSprites.set_colorkey((255,0,255));
        self.spriteSheet.set_colorkey((255,0,255));
        
        #Cut the loaded images with Specified UV's and store it
        self.image = self.spriteSheet.subsurface(pygame.Rect(self.MenuRect[0]));
        self.backImage = self.background.subsurface(pygame.Rect(self.BackgroundRect[0]));
        self.RyuImage = self.RyuSprites.subsurface(pygame.Rect(self.RyuImageUV[0]));
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
                        if(event.key == K_UP):
                            menu.CharacterSelectionMenu = True;
                            menu.StartMenu = False;
                            menu.ChangeToChooseCh(VIEWPORT);
                        if(event.key == K_DOWN):
                            menu.CharacterSelectionMenu = False;
                            menu.StartMenu = True;
                            menu.ChangeToMenu(VIEWPORT);
       
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
        
        if(menu.StartMenu == True and menu.CharacterSelectionMenu == False):
            menu.renderMenu(VIEWPORT);
            menu.renderMenutext(VIEWPORT);
        elif(menu.CharacterSelectionMenu == True and menu.StartMenu == False):
            menu.CharacterChRender(VIEWPORT);
            menu.renderCharacterChText(VIEWPORT);
        
            
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