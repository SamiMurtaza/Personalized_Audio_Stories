import pygame
import Screen
import ManagerScreen
import HomeScreen
import WaitScreen
import Button
import Recording

class recordScreen():
    def __init__(self, scr):
        self.scr = scr
        
        self.backGround = pygame.image.load(r"data\image\record.jpg")
        self.backGround = pygame.transform.scale(self.backGround, (Screen.screen.W, Screen.screen.H) )

        self.generateButton = pygame.image.load(r"data\image\generate.png")
        self.generateButton = pygame.transform.scale(self.generateButton, (int(Screen.screen.W/5), int(Screen.screen.H/10)) )

        self.micIcon = pygame.image.load(r"data\image\mic.png")
        self.micIcon = pygame.transform.scale(self.micIcon, (int(Screen.screen.W/25), int(Screen.screen.W/25)) )

        self.micIcon2 = pygame.image.load(r"data\image\mic2.png")
        self.micIcon2 = pygame.transform.scale(self.micIcon2, (int(Screen.screen.W/25), int(Screen.screen.W/25)) )

        self.tickIcon = pygame.image.load(r"data\image\tick.png")
        self.tickIcon = pygame.transform.scale(self.tickIcon, (int(Screen.screen.W/40), int(Screen.screen.W/40)) )

        self.crossIcon = pygame.image.load(r"data\image\cross.png")
        self.crossIcon = pygame.transform.scale(self.crossIcon, (int(Screen.screen.W/40), int(Screen.screen.W/40)) )

        self.sentences = open(r"data\text\record.txt").readlines()

        self.font = pygame.font.Font('freesansbold.ttf', Screen.screen.W // 52)

        self.button = Button.RButton(Screen.screen.W/8, Screen.screen.H/6.5 ,Screen.screen.W/25, scr)

        self.recorded = [0 for i in range(len(self.sentences))]
        self.iconType = [False for i in range(len(self.sentences))]
        
        self.rec = Recording.recording()
        #screenSize(Screen.screen.W, Screen.screen.H, fullscreen= True)

        self.filename = ""
        
        
    def render(self):

        temp = self.getPressed()
        if temp:
            if temp == "backspace":
                self.filename = self.filename[:-1]
            elif len(temp)==1 and len(self.filename) < 10:
                self.filename += temp
                
        self.scr.blit(self.backGround, (0,0))
        self.scr.blit(Screen.screen.backIcon, (Screen.screen.W/20,Screen.screen.H/40))
        self.scr.blit(Screen.screen.homeIcon, (Screen.screen.W - Screen.screen.W/10,Screen.screen.H/40))
        self.scr.blit(self.generateButton, (Screen.screen.W/2+ Screen.screen.W/6, Screen.screen.H/1.15))
        
        
        for i in range(len(self.sentences)):
            if self.iconType[i]:
                self.scr.blit(self.micIcon2, (Screen.screen.W/2 + Screen.screen.W/4, Screen.screen.H/3.6 + (i * Screen.screen.H/12)))
            else:
                self.scr.blit(self.micIcon, (Screen.screen.W/2 + Screen.screen.W/4, Screen.screen.H/3.6 + (i * Screen.screen.H/12)))
                          
            #if randint(0,100) > 80:
            #    self.scr.blit(self.crossIcon, (Screen.screen.W/2 - Screen.screen.W/2.65, Screen.screen.H/3.55 + (i * Screen.screen.H/12) ))
           # else:
            if self.recorded[i]:
                self.scr.blit(self.tickIcon, (Screen.screen.W/2 - Screen.screen.W/2.65, Screen.screen.H/3.55 + (i * Screen.screen.H/12) ))
            else:
                self.scr.blit(self.crossIcon, (Screen.screen.W/2 - Screen.screen.W/2.65, Screen.screen.H/3.55 + (i * Screen.screen.H/12) ))
                
            text = self.font.render(self.sentences[i].strip(), True, (255,255,255)) 
            textRect = text.get_rect()  
            textRect.center = (Screen.screen.W/2 - Screen.screen.W/16, Screen.screen.H/3.2 + i * Screen.screen.H/12)
            self.scr.blit(text, textRect)
            
        pygame.draw.rect(self.scr, (100,100,100), [Screen.screen.W/2 - Screen.screen.W/2.5, Screen.screen.H/8 , Screen.screen.W/1.3, Screen.screen.H/10])
        pygame.draw.rect(self.scr, (100,100,100), [Screen.screen.W/2 - Screen.screen.W/2.5, Screen.screen.H/1.15, Screen.screen.W/2.5, Screen.screen.H/10])
        pygame.draw.rect(self.scr, (220,220,220), [Screen.screen.W/2 - Screen.screen.W/3.5 + 10, Screen.screen.H/1.13, Screen.screen.W/3.9, (Screen.screen.H/10)*0.7])
    
        text = self.font.render("The app has my consent to use my voice in this story-telling context", True, (255,255,255)) 
        textRect = text.get_rect()  
        textRect.center = (Screen.screen.W/2 , Screen.screen.H/5.5)
        self.scr.blit(text, textRect)

        text = self.font.render("Voice Title: ", True, (255,255,255)) 
        textRect = text.get_rect()  
        textRect.center = (Screen.screen.W/2 - Screen.screen.W/3,  Screen.screen.H/1.08)
        self.scr.blit(text, textRect)
        self.button.show()

        text = self.font.render(self.filename, True, (0,0,0)) 
        textRect = text.get_rect()  
        textRect.center = (Screen.screen.W/2 - Screen.screen.W/8,  Screen.screen.H/1.08)
        self.scr.blit(text, textRect)
        self.button.show()

    def checkClicked(self):
        if Screen.checkOver(  (pygame.mouse.get_pos()),
                                               (Screen.screen.W/20, Screen.screen.H/40),
                                               int(Screen.screen.W/20), int(Screen.screen.H/30)):
            pygame.mixer.Sound.play(Screen.screen.click)
            Screen.screen.currentScreen = ManagerScreen.managerScreen(self.scr)
            
        if Screen.checkOver(  (pygame.mouse.get_pos()),
                                               (Screen.screen.W - Screen.screen.W/10,Screen.screen.H/40),
                                               int(Screen.screen.W/20), int(Screen.screen.H/30)):
            pygame.mixer.Sound.play(Screen.screen.click)
            Screen.screen.currentScreen = HomeScreen.homeScreen(self.scr)

        if Screen.checkOver(  (pygame.mouse.get_pos()),
                                               (Screen.screen.W/2 + Screen.screen.W/6,Screen.screen.H/1.15 ),
                                               int(Screen.screen.W/5), int(Screen.screen.H/10)) and self.button.state:
            pygame.mixer.Sound.play(Screen.screen.click)
            Screen.screen.currentScreen = WaitScreen.waitScreen(self.scr)

        for i in range(len(self.sentences)):
            if Screen.checkOver(  (pygame.mouse.get_pos()),
                                               (Screen.screen.W/2 + Screen.screen.W/4, Screen.screen.H/3.55 + (i * Screen.screen.H/12) ),
                                               int(Screen.screen.W/25), int(Screen.screen.W/25)):
                for j in range(len(self.sentences)):
                    if j!=i:
                        self.iconType[j] = False
                        
                self.iconType[i] = not self.iconType[i]
                
                if self.iconType[i]:
                    for k in range(len(self.sentences)):
                        if self.iconType[k]:
                            self.scr.blit(self.micIcon2, (Screen.screen.W/2 + Screen.screen.W/4, Screen.screen.H/3.6 + (k * Screen.screen.H/12)))
                        else:
                            self.scr.blit(self.micIcon, (Screen.screen.W/2 + Screen.screen.W/4, Screen.screen.H/3.6 + (k * Screen.screen.H/12)))
                        pygame.display.update()
                    text = self.rec.record(self.sentences[i],r"data/recorded/"+str(i)+".wav")
                    print(text, "_____ ",self.sentences[i])
                    if self.rec.get_validated(text, self.sentences[i]):
                        self.recorded[i] = True
                    self.iconType[i] = not self.iconType[i]
                    
        if self.button.update():
            pygame.mixer.Sound.play(Screen.screen.click)
        
    def getPressed(self):
        keys = pygame.key.get_pressed()
        pressed = [k for k, v in enumerate(keys) if v]
        keys_pressed = []
        for k in pressed: # Convert integers to keyboard symbols (strings)
            keys_pressed.append(pygame.key.name(k))
        keyes_pressed = list(set(keys_pressed))
        if keys_pressed:

            return "".join(keys_pressed)
        else:
            return ""
                
            
            
            
