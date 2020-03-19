import pygame
import winsound
from Screen import screen 

if __name__ == "__main__":
    S = screen()
    Quit = False
    
    while not Quit:
        events = pygame.event.get()
        for event in events:
            
            if event.type == pygame.QUIT:
                Quit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Quit = True
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                S.currentScreen.checkClicked()
            
        S.currentScreen.render()
        pygame.display.update()
        S.clock.tick(60)
        
    S.endGame()
