import pygame
import Screen
import Button
import HomeScreen
import RecordScreen

import winsound

class managerScreen():

    def __init__(self, scr):
        self.backGround = pygame.image.load(r"data\image\audiobg.png")
        self.backGround = pygame.transform.scale(self.backGround, (Screen.screen.W, Screen.screen.H) )

        self.addIcon = pygame.image.load(r"data\image\add.png")
        self.addIcon = pygame.transform.scale(self.addIcon, (int(Screen.screen.W/25), int(Screen.screen.W/25)) )

        self.buttons = [Button.PButton(Screen.screen.W/3, Screen.screen.H/6.2 + (i*Screen.screen.H/10),Screen.screen.W/25, "delete.png", "delete.png", scr) for i in range(3) ]
        self.audioButtons = [Button.PButton(Screen.screen.W/1.5, Screen.screen.H/6.2 + (i*Screen.screen.H/10),Screen.screen.W/25, "pauseIcon.png", "playIcon.png", scr) for i in range(3)]
        self.font = pygame.font.Font('freesansbold.ttf', Screen.screen.W // 52)
        self.scr = scr

        self.audioSamples = []
        self.audioSamples.append(r"data\audio\twinkle.wav")
        self.audioSamples.append(r"data\audio\ant.wav")
        self.audioSamples.append(r"data\audio\asked.wav")

    def render(self):
        self.scr.blit(self.backGround, (0,0))
        self.scr.blit(self.addIcon, (Screen.screen.W/3, Screen.screen.H/6.2 + (3*Screen.screen.H/10)))
        self.scr.blit(Screen.screen.backIcon, (Screen.screen.W/20,Screen.screen.H/40))
        self.scr.blit(Screen.screen.homeIcon, (Screen.screen.W - Screen.screen.W/10,Screen.screen.H/40))
        

        for i in self.buttons:
            i.show()

        for i in self.audioButtons:
            i.show()


        text = self.font.render('Ammi', True, (0,0,0)) 
        textRect = text.get_rect()  
        textRect.center = (Screen.screen.W/2, Screen.screen.H/4.8) 
        self.scr.blit(text, textRect)

        text = self.font.render('Dadi Jan', True, (0,0,0)) 
        textRect = text.get_rect()  
        textRect.center = (Screen.screen.W/2, Screen.screen.H/3.3) 
        self.scr.blit(text, textRect)

        text = self.font.render('Fatima Khala', True, (0,0,0)) 
        textRect = text.get_rect()  
        textRect.center = (Screen.screen.W/2, Screen.screen.H/2.5) 
        self.scr.blit(text, textRect)

        text = self.font.render('Record New Audio', True, (0,0,0)) 
        textRect = text.get_rect()  
        textRect.center = (Screen.screen.W/2, Screen.screen.H/2) 
        self.scr.blit(text, textRect) 
        
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

        if Screen.checkOver(  (pygame.mouse.get_pos()),
                                               (Screen.screen.W/3, Screen.screen.H/6.2 + (3*Screen.screen.H/10)),
                                               int(Screen.screen.W/25), int(Screen.screen.W/25)):
            pygame.mixer.Sound.play(Screen.screen.click)
            Screen.screen.currentScreen = RecordScreen.recordScreen(self.scr)
        
        for i in self.audioButtons :
            if i.update():
                pygame.mixer.Sound.play(Screen.screen.click)
                for j in self.audioButtons:
                    if i!=j:
                        j.state= False
                        winsound.PlaySound(None, winsound.SND_PURGE)
                if i.state:
                    winsound.PlaySound(self.audioSamples[self.audioButtons.index(i)], winsound.SND_ASYNC | winsound.SND_ALIAS )

        
