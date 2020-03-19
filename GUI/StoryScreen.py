import pygame
import Screen
import AudioScreen
import HomeScreen
import winsound
import time

class storyScreen():
    
    def __init__(self, scr):
                
        self.backGround = pygame.image.load("data\\image\\" +Screen.screen.story + "cover.jpg")
        self.backGround = pygame.transform.scale(self.backGround, (Screen.screen.W, Screen.screen.H))

        self.iconPanel1 = pygame.image.load(r"data\image\iconPanel_1.png")
        self.iconPanel1 = pygame.transform.scale(self.iconPanel1, (Screen.screen.W, int(Screen.screen.H/3)))

        self.iconPanel2 = pygame.image.load(r"data\image\iconPanel_2.png")
        self.iconPanel2 = pygame.transform.scale(self.iconPanel2, (Screen.screen.W, int(Screen.screen.H/3)))
        self.script = open("data\\text\\"+Screen.screen.story +"story.txt").readlines()
        self.justBorn = True
        self.playing = True
        self.currentPage = 0
        self.currentLine = 0
        self.pages = []
        for i in range(Screen.screen.pageCount):
            img = pygame.image.load("data\\image\\"+Screen.screen.story+ "page" + str(i) + ".png")
            img = pygame.transform.scale(img, (int(Screen.screen.W), int(Screen.screen.H)))
            self.pages.append((img, "data\\audio\\"+Screen.screen.story+  "page" + str(i) + ".WAV"))

        self.scr = scr
        self.font = pygame.font.Font('freesansbold.ttf', Screen.screen.W // 42)        
        
    def render(self):

        self.scr.blit(self.backGround, (0,0))
        
        if self.justBorn:
            self.justBorn = False
            pygame.display.update()
            pygame.mixer.music.load("data\\audio\\"+Screen.screen.story+"title.WAV")
            pygame.mixer.music.play(0)
            time.sleep(2)
            pygame.mixer.music.load(self.pages[self.currentPage][1])
            pygame.mixer.music.play(0)
            self.line = 0
            self.start_time = pygame.time.get_ticks()
            self.sec = (pygame.time.get_ticks() - self.start_time) // (len(self.script[self.line])*80)

        self.scr.blit(self.pages[self.currentPage][0], (0,0))
        
        if self.playing:
            self.scr.blit(self.iconPanel2, (0, Screen.screen.H/1.3))
        else:
            self.scr.blit(self.iconPanel1, (0, Screen.screen.H/1.3))
        
        
        if ((pygame.time.get_ticks() - self.start_time) // (len(self.script[self.line])*80)) > self.sec and self.script[self.line][0] != "_" and self.playing:
            
            self.start_time = pygame.time.get_ticks()
            self.sec = (pygame.time.get_ticks() - self.start_time) // (len(self.script[self.line])*80)
            if self.line+1 < len(self.script):
                self.line+=1    

        self.scr.blit(Screen.screen.backIcon, (Screen.screen.W/20,Screen.screen.H/40))
        self.scr.blit(Screen.screen.homeIcon, (Screen.screen.W - Screen.screen.W/10,Screen.screen.H/40))

        text = self.font.render(self.script[self.line][:-1], True, (255,255,255)) 
        textRect = text.get_rect()  
        textRect.center = (Screen.screen.W/2, Screen.screen.H/1.1) 
        self.scr.blit(text, textRect)

        if not pygame.mixer.music.get_busy():
            if self.currentPage+1 < Screen.screen.pageCount:
                if self.script[self.line][0] == "_"  and self.line+1 < len(self.script):
                    self.line+=1
                else:
                    count = 0
                    for i in range(len(self.script)):
                        if self.script[i][0] == "_":
                            count+=1
                            if count == self.currentPage+1:
                                self.line = i+1
                                break
                self.start_time = pygame.time.get_ticks()
                self.currentPage+=1
                pygame.mixer.music.load(self.pages[self.currentPage][1])
                pygame.mixer.music.play(0)
            

    def checkClicked(self):
        if Screen.checkOver(  (pygame.mouse.get_pos()),
                                               (Screen.screen.W/20, Screen.screen.H/40),
                                               int(Screen.screen.W/20), int(Screen.screen.H/30)):
            pygame.mixer.Sound.play(Screen.screen.click)
            Screen.screen.currentScreen = AudioScreen.audioScreen(self.scr)
            pygame.mixer.music.stop()
            
        if Screen.checkOver(  (pygame.mouse.get_pos()),
                                               (Screen.screen.W - Screen.screen.W/10,Screen.screen.H/40),
                                               int(Screen.screen.W/20), int(Screen.screen.H/30)):
            pygame.mixer.Sound.play(Screen.screen.click)
            Screen.screen.currentScreen = HomeScreen.homeScreen(self.scr)
            pygame.mixer.music.stop()

        #pause/play
        if Screen.checkOver( (pygame.mouse.get_pos()),
                                               (Screen.screen.W/2  + Screen.screen.W/120,Screen.screen.H/1.3),
                                               int(Screen.screen.H/15), int(Screen.screen.H/15)):
    
            pygame.mixer.Sound.play(Screen.screen.click)
            self.playing = not self.playing

            if self.playing:
                pygame.mixer.music.unpause()
                self.start_time = pygame.time.get_ticks()
                self.sec = (pygame.time.get_ticks() - self.start_time) // (len(self.script[self.line])*80)
            else:
                pygame.mixer.music.pause()
                
        #next page 
        if Screen.checkOver( (pygame.mouse.get_pos()),
                                               ( Screen.screen.W/2 + Screen.screen.W/14, Screen.screen.H/1.3),
                                               int(Screen.screen.H/15), int(Screen.screen.H/15)):

            pygame.mixer.Sound.play(Screen.screen.click)
            if self.currentPage+1 < Screen.screen.pageCount:
                self.currentPage+=1
            pygame.mixer.music.load(self.pages[self.currentPage][1])
            pygame.mixer.music.play(0)
            self.playing =True
            count = 0
            for i in range(len(self.script)):
                if self.script[i][0] == "_":
                    count+=1
                    if count == self.currentPage:
                        self.line = i+1
                        self.start_time = pygame.time.get_ticks()
                        self.sec = (pygame.time.get_ticks() - self.start_time) // (len(self.script[self.line])*80)
                        break
            
        #previous page 
        if Screen.checkOver( (pygame.mouse.get_pos()),
                                               ( Screen.screen.W/2  - Screen.screen.W/17, Screen.screen.H/1.3),
                                               int(Screen.screen.H/15), int(Screen.screen.H/15)):
            
            pygame.mixer.Sound.play(Screen.screen.click)
            if self.currentPage >0:
                self.currentPage-=1
            pygame.mixer.music.load(self.pages[self.currentPage][1])
            pygame.mixer.music.play(0)
            self.playing = True
            if self.currentPage == 0:
                self.line = 0
            else:
                count = 0
                for i in range(len(self.script)):
                    if self.script[i][0] == "_":
                        count+=1
                        if count == self.currentPage:
                            self.line = i+1                            
                            break
                        
            self.start_time = pygame.time.get_ticks()
            self.sec = (pygame.time.get_ticks() - self.start_time) // (len(self.script[self.line])*80)
            
        #first page 
        if Screen.checkOver( (pygame.mouse.get_pos()),
                                               ( Screen.screen.W/2  - Screen.screen.W/8, Screen.screen.H/1.3),
                                               int(Screen.screen.H/15), int(Screen.screen.H/15)):
            
            pygame.mixer.Sound.play(Screen.screen.click)
            self.currentPage = 0
            pygame.mixer.music.load(self.pages[self.currentPage][1])
            pygame.mixer.music.play(0)
            self.playing = True
            self.line = 0
            self.start_time = pygame.time.get_ticks()
            self.sec = (pygame.time.get_ticks() - self.start_time) // (len(self.script[self.line])*80)
            
        #last page
        if Screen.checkOver( (pygame.mouse.get_pos()),
                                               ( Screen.screen.W/2  + Screen.screen.W/7.5, Screen.screen.H/1.3),
                                               int(Screen.screen.H/15), int(Screen.screen.H/15)):
            
            pygame.mixer.Sound.play(Screen.screen.click)
            self.currentPage = Screen.screen.pageCount-1
            pygame.mixer.music.load(self.pages[self.currentPage][1])
            pygame.mixer.music.play(0)
            self.playing = True
            for i in range(len(self.script)):
                    if self.script[i][0] == "_":
                            self.line = i+1                            
            self.start_time = pygame.time.get_ticks()
            self.sec = (pygame.time.get_ticks() - self.start_time) // (len(self.script[self.line])*80)
