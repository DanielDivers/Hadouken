#Basic Python Test Using PyGame
 #execfile("Player Class.py")
import pygame, sys, Menu
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
        menu = Menu.Menu();
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
                            
        if("""not Player Colliding With Rect"""):
            player.position[0]-=3;
       
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