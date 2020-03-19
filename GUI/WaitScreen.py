import pygame
import Screen
import HomeScreen

import mel__randomcnn3

class waitScreen():

    def __init__(self, scr):

        self.backGround = pygame.image.load(r"data\image\record.jpg")
        self.backGround = pygame.transform.scale(self.backGround, (Screen.screen.W, Screen.screen.H) )

        self.glass = pygame.image.load(r"data\image\hourglass.png")
        self.glass = pygame.transform.scale(self.glass, (int(Screen.screen.W/4), int(Screen.screen.W/4)) )

        self.font = pygame.font.Font('freesansbold.ttf', 42)
        self.scr = scr
        mel__randomcnn3.imp()        

    def render(self):
        self.scr.blit(self.backGround, (0,0))
        self.scr.blit(self.glass, (Screen.screen.W/2 - Screen.screen.W/8,Screen.screen.H/2 - Screen.screen.H/4))
        text = self.font.render('Please Wait...', True, (255,255,255)) 
        textRect = text.get_rect()  
        textRect.center = (Screen.screen.W/2, Screen.screen.H/1.3) 
        self.scr.blit(text, textRect)

    def checkClicked(self):
        Screen.screen.currentScreen = HomeScreen.homeScreen(self.scr)
        
