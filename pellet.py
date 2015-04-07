import sys, pygame
YELLOW = (222,253,68)
OFFYELLOW = (240,253,68)
class Pellet(pygame.sprite.Sprite):
    
    def __init__(self,width = 2, height = 2, color = YELLOW):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
    #Draw the pellet
    #pygame.draw.ellipse(self.image, color, [0,0,width,height])
        self.rect = self.image.get_rect()


class Power_Pellet(pygame.sprite.Sprite):
    
    def __init__(self,width = 6, height = 6, color = OFFYELLOW):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
    #Draw the pellet
    #pygame.draw.ellipse(self.image, color, [0,0,width,height])
        self.rect = self.image.get_rect()
