import pygame 
import Screen

class button:
    
    def __init__(self, x ,y, siz, scr):
        self.siz = siz
        self.x = x
        self.y = y
        self.color = 0
        self.state = False
        self.scr = scr

        
    def update(self):
        if self.overRect():
                self.state = not self.state
                self.color = self.state*255
                return True

        
    def overRect(self):
        mPos = pygame.mouse.get_pos()
        return  mPos[0] >= self.x and mPos[0] <= (self.x+self.siz) and mPos[1] >= self.y and mPos[1] <= (self.y+self.siz)
            

class RButton(button):
    def __init__(self,x,y,siz,scr):
        siz = int(siz)
        super().__init__(x ,y, siz, scr)

    def show(self):
        pygame.draw.rect(self.scr, (255,255,255), [self.x - self.siz/10, self.y - self.siz/8 , self.siz, self.siz])
        pygame.draw.rect(self.scr, (255*self.state,0,0), [self.x, self.y, self.siz*0.8, self.siz*0.8])

class PButton(button):
    def __init__(self, x ,y, siz, name1, name2, scr):
        siz = int(siz)
        super().__init__(x ,y, siz, scr)
        self.img1= pygame.image.load(r"data\image\ ".strip() + name1)
        self.img1= pygame.transform.scale(self.img1, (siz, siz) )

        self.img2 = pygame.image.load(r"data\image\ ".strip() + name2)
        self.img2 = pygame.transform.scale(self.img2, (siz, siz) )

    def show(self):
        if self.state:
            self.scr.blit(self.img1, (self.x,self.y))
        else:
            self.scr.blit(self.img2, (self.x,self.y))
    
