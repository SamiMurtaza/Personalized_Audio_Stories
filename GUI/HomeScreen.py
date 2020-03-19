import pygame
import Screen

from ManagerScreen import managerScreen
from BookScreen import bookScreen

class homeScreen():
    
    def __init__(self, scr):
        self.backGround = pygame.image.load(r"data\image\background.jpg")
        self.backGround = pygame.transform.scale(self.backGround, (Screen.screen.W, Screen.screen.H) )
        
        self.icon = pygame.image.load(r"data\image\red_book.png")
        self.icon = pygame.transform.scale(self.icon, (int(Screen.screen.W/5), int(Screen.screen.W/5)) )

        self.listen_button = pygame.image.load(r"data\image\listen.jpg")
        self.listen_button = pygame.transform.scale(self.listen_button, (int(Screen.screen.W/5), int(Screen.screen.H/15)) )

        self.manager_button = pygame.image.load(r"data\image\manager.jpg")
        self.manager_button = pygame.transform.scale(self.manager_button, (int(Screen.screen.W/5), int(Screen.screen.H/15)) )

        ##
        ## ADD HIGHLIGHTED BUTTONS
        ##
        
        self.scr = scr
        
    def render(self):
        self.scr.blit(self.backGround, (0,0))
        self.scr.blit(self.icon, (Screen.screen.W/2 - Screen.screen.W/10, Screen.screen.H/5))
        self.scr.blit(self.listen_button, (Screen.screen.W/2 - Screen.screen.W/10, Screen.screen.H/1.6))
        self.scr.blit(self.manager_button, (Screen.screen.W/2 - Screen.screen.W/10, Screen.screen.H/1.4))


    def checkClicked(self):
        ##check for listen to story wala button
        if Screen.checkOver(  (pygame.mouse.get_pos()),
                                               (Screen.screen.W/2 - Screen.screen.W/10, Screen.screen.H/1.6),
                                               int(Screen.screen.W/5), int(Screen.screen.H/15)):
            pygame.mixer.Sound.play(Screen.screen.click)
            Screen.screen.currentScreen = bookScreen(self.scr)

        ##check for manage story wala button 
        if Screen.checkOver(  (pygame.mouse.get_pos()),
                                               (Screen.screen.W/2 - Screen.screen.W/10, Screen.screen.H/1.4),
                                               int(Screen.screen.W/5), int(Screen.screen.H/15)):
            pygame.mixer.Sound.play(Screen.screen.click)
            Screen.screen.currentScreen = managerScreen(self.scr)
            

