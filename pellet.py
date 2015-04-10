import sys, pygame
YELLOW = (222,253,68)
OFFYELLOW = (240,253,68)

class Pellet(pygame.sprite.Sprite):
#pellet the pacman collects
    def __init__(self,width = 2, height = 2, color = YELLOW):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()


class Power_Pellet(pygame.sprite.Sprite):
#pellet that when consumed allows the pacman to consume the ghost
#for a limited amount of time
    def __init__(self,width = 6, height = 6, color = OFFYELLOW):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
