import pygame
import ctypes

from HomeScreen import homeScreen

class screen:
    
    currentScreen = None
    W, H = None, None 

    backIcon = None
    homeIcon = None
    click = None

    pageCount = None

    story = ""
    
    def __init__(self):
        
        screen.W, screen.H = ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1)
        pygame.init()
        #pygame.mixer.init(frequency=41000)
        gameDisplay = pygame.display.set_mode((self.W,self.H), pygame.FULLSCREEN )
        pygame.display.set_caption('Personalized Audio Stories')
        self.clock = pygame.time.Clock()

        screen.backIcon = pygame.image.load(r"data\image\back.png")
        screen.backIcon = pygame.transform.scale(screen.backIcon, (int(screen.W/20), int(screen.H/30)) )

        screen.homeIcon = pygame.image.load(r"data\image\home.png")
        screen.homeIcon = pygame.transform.scale(screen.homeIcon, (int(screen.W/20), int(screen.H/30)) )

        screen.click = pygame.mixer.Sound(r"data\audio\click.wav")

        screen.currentScreen = homeScreen(gameDisplay)

        screen.pageCount = 4
        

    def endGame(self):
        pygame.quit()
        quit()



def checkOver(mouse, box, width, height):
    return (box[0] < mouse[0] < (box[0]+width)) and (box[1] < mouse[1] < (box[1]+height))
