import pygame
import Screen 

import HomeScreen
import AudioScreen

class bookScreen():
    def __init__(self, scr):
        self.backGround = pygame.image.load(r"data\image\shelf.png")
        self.backGround = pygame.transform.scale(self.backGround, (Screen.screen.W, Screen.screen.H))

        self.bookIconCount = 6
        self.bookIcons = [] 
        for i in range(self.bookIconCount):
            book = pygame.image.load(r"data\image\book" +str(i)+".jpg")
            book = pygame.transform.scale(book, (int(Screen.screen.W/10), int(Screen.screen.H/5)))
            self.bookIcons.append(book)

        self.scr = scr

    def render(self):
        self.scr.blit(self.backGround, (0,0))
        self.scr.blit(Screen.screen.backIcon, (Screen.screen.W/20,Screen.screen.H/40))
        self.scr.blit(Screen.screen.homeIcon, (Screen.screen.W - Screen.screen.W/10,Screen.screen.H/40))


        for i in range(self.bookIconCount):
            ##
            ## ENLARGE WHEN SELECTED
            ##
            if (i//4)%2==0:
                    self.scr.blit(self.bookIcons[i], 
                        (Screen.screen.W/20 + ((i%4)*Screen.screen.W/4),
                        Screen.screen.H/4 + ((i//4)*(Screen.screen.H/4))) )
            else:
                    self.scr.blit(self.bookIcons[i], 
                        (Screen.screen.W/20 + ((i%4)*Screen.screen.W/4) +Screen.screen.W/8,
                        Screen.screen.H/4 + ((i//4)*(Screen.screen.H/4)) ))


    def checkClicked(self):
        if Screen.checkOver(  (pygame.mouse.get_pos()),
                                               (Screen.screen.W/20, Screen.screen.H/40),
                                               int(Screen.screen.W/20), int(Screen.screen.H/30)):
            pygame.mixer.Sound.play(Screen.screen.click)
            Screen.screen.currentScreen = HomeScreen.homeScreen(self.scr)
            
        if Screen.checkOver(  (pygame.mouse.get_pos()),
                                               (Screen.screen.W - Screen.screen.W/10,Screen.screen.H/40),
                                               int(Screen.screen.W/20), int(Screen.screen.H/30)):
            pygame.mixer.Sound.play(Screen.screen.click)
            Screen.screen.currentScreen = HomeScreen.homeScreen(self.scr)

        for i in range(self.bookIconCount):
            
            if (i//4)%2==0:
                if Screen.checkOver(  (pygame.mouse.get_pos()),
                                               (Screen.screen.W/20 + ((i%4)*Screen.screen.W/4),Screen.screen.H/4 + ((i//4)*(Screen.screen.H/4))),
                                               int(Screen.screen.W/10), int(Screen.screen.H/4)):
                    Screen.screen.story = ""
                    Screen.screen.pageCount = 4
                    pygame.mixer.Sound.play(Screen.screen.click)
                    Screen.screen.currentScreen =  AudioScreen.audioScreen(self.scr)
                    
            else:
                if Screen.checkOver(  (pygame.mouse.get_pos()),
                                               (Screen.screen.W/20 + ((i%4)*Screen.screen.W/4)+Screen.screen.W/8 ,Screen.screen.H/4 + ((i//4)*(Screen.screen.H/4))),
                                               int(Screen.screen.W/10), int(Screen.screen.H/4)):
                    if i==self.bookIconCount-1:
                        Screen.screen.story = "C"
                        Screen.screen.pageCount = 6
                        
                    pygame.mixer.Sound.play(Screen.screen.click)
                    Screen.screen.currentScreen =  AudioScreen.audioScreen(self.scr)
        
    
