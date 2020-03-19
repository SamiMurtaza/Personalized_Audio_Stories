import pygame

import Screen
import HomeScreen
import BookScreen
import StoryScreen
import Button

import winsound

class audioScreen():

    def __init__(self, scr):
        self.backGround = pygame.image.load(r"data\image\audiobg.png")
        self.backGround = pygame.transform.scale(self.backGround, (Screen.screen.W, Screen.screen.H))

        self.playButton = pygame.image.load(r"data\image\play.png")
        self.playButton = pygame.transform.scale(self.playButton, (int(Screen.screen.W/5), int(Screen.screen.W/20)))

        self.buttons = [Button.RButton(Screen.screen.W/3, Screen.screen.H/6 + (i*Screen.screen.H/10),Screen.screen.W/25, scr) for i in range(4) ]
        self.audioButtons = [Button.PButton(Screen.screen.W/1.5, Screen.screen.H/6.2 + (i*Screen.screen.H/10),Screen.screen.W/25, "pauseIcon.png", "playIcon.png", scr) for i in range(4)]

        self.audioSamples = []
        self.audioSamples.append(r"data\audio\die.wav")
        self.audioSamples.append(r"data\audio\twinkle.wav")
        self.audioSamples.append(r"data\audio\ant.wav")
        self.audioSamples.append(r"data\audio\asked.wav")

        self.font = pygame.font.Font('freesansbold.ttf', 42)
        self.scr = scr

        self.buttons[0].state = not self.buttons[0].state
        self.buttons[0].color = self.buttons[0].state*255

    def render(self):
        self.scr.blit(self.backGround, (0,0))
        self.scr.blit(Screen.screen.backIcon, (Screen.screen.W/20,Screen.screen.H/40))
        self.scr.blit(Screen.screen.homeIcon, (Screen.screen.W - Screen.screen.W/10,Screen.screen.H/40))
        self.scr.blit(self.playButton, (Screen.screen.W/2 - Screen.screen.W/10,Screen.screen.H - Screen.screen.H/7))
        
        for i in self.buttons :
            i.show()

        for i in self.audioButtons :
            i.show()

        text = self.font.render('Assistant', True, (0,0,0)) 
        textRect = text.get_rect()  
        textRect.center = (Screen.screen.W/2, Screen.screen.H/4.75) 
        self.scr.blit(text, textRect)

        text = self.font.render('Ammi', True, (0,0,0)) 
        textRect = text.get_rect()  
        textRect.center = (Screen.screen.W/2, Screen.screen.H/3.25) 
        self.scr.blit(text, textRect)

        text = self.font.render('Dadi Jan', True, (0,0,0)) 
        textRect = text.get_rect()  
        textRect.center = (Screen.screen.W/2, Screen.screen.H/2.45) 
        self.scr.blit(text, textRect)

        text = self.font.render('Fatima Khala', True, (0,0,0)) 
        textRect = text.get_rect()  
        textRect.center = (Screen.screen.W/2, Screen.screen.H/1.95) 
        self.scr.blit(text, textRect)

        
    def checkClicked(self):
        if Screen.checkOver(  (pygame.mouse.get_pos()),
                                               (Screen.screen.W/20, Screen.screen.H/40),
                                               int(Screen.screen.W/20), int(Screen.screen.H/30)):
            pygame.mixer.Sound.play(Screen.screen.click)
            Screen.screen.currentScreen = BookScreen.bookScreen(self.scr)
            
        if Screen.checkOver(  (pygame.mouse.get_pos()),
                                               (Screen.screen.W - Screen.screen.W/10,Screen.screen.H/40),
                                               int(Screen.screen.W/20), int(Screen.screen.H/30)):
            pygame.mixer.Sound.play(Screen.screen.click)
            Screen.screen.currentScreen = HomeScreen.homeScreen(self.scr)


        if Screen.checkOver(  (pygame.mouse.get_pos()),
                                               (Screen.screen.W/2 - Screen.screen.W/10, Screen.screen.H - Screen.screen.H/7),
                                               int(Screen.screen.W/5), int(Screen.screen.W/20)):
##            if any(i.state for i in self.buttons):
            pygame.mixer.Sound.play(Screen.screen.click)
            Screen.screen.currentScreen = StoryScreen.storyScreen(self.scr)

        for i in self.buttons:
            if i.update():
                pygame.mixer.Sound.play(Screen.screen.click)
                for j in self.buttons:
                    if i!=j:
                        j.state= False
                        j.color = 0

        for i in self.audioButtons :
            if i.update():
                pygame.mixer.Sound.play(Screen.screen.click)
                for j in self.audioButtons:
                    if i!=j:
                        j.state= False
                        winsound.PlaySound(None, winsound.SND_PURGE)
                if i.state:
                    winsound.PlaySound(self.audioSamples[self.audioButtons.index(i)], winsound.SND_ASYNC | winsound.SND_ALIAS )
                    
    
    
