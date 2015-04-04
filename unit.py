import pygame, gui 
from pygame.sprite import Sprite


class pacman(Sprite):
    """
    this is the base unit class that will be inherited by the pacman class and 
    the ghost class. It will just generally have to do with any object that is
    printed to the map.
    """
    sprite = pygame.image.load("Assets/pacman.png")
    def __init__(self,
                 loc_x = None,
                 loc_y = None,
                 activate = False,
                 **keywords):
        
        Sprite.__init__(self)
        
        #self.loc_x = loc_x
        #self.loc_y = loc_y
        self.angle = 0
        #self.score = 0
        #self.lives = 3
        #Some default values so that nothing complains when trying to
        #assign later
        self._moving = False
        self._alive = False
        
       
        #Default unit stats
        self.move_sound = None
        self.hit_sound = None
        #self.die_sound
        #self.loc_x = loc_x
        #self.loc_y = loc_y
        #self.angle = 0
        #self.score = 0
        #self.lives = 3
        #Some default values so that nothing complains when trying to
        #assign later
        #self._moving = False
        #self._alive = False
        
       
        #Default unit stats
        #self.move_sound = None
        #self.hit_sound = None
        #self.die_sound
        self.image = pacman.sprite.convert()
        self.rect = self.image.get_rect()
        self.image.set_colorkey((32,32,32))
        #def move(self):

    def die(self):
        self.lives = self.live - 1
        if self.lives == 0:
            gameover()

    def start(self):
        self.lives = 3
        self.score = 0
        self.rect.y = 16*25
        self.rect.x = 12*25
        
   

    def newangle(self,key):
        if (key == pygame.K_RIGHT):
            if self.angle == 0:
                self.image = pygame.transform.rotate(self.image,0)
            if self.angle == 90:
                self.image = pygame.transform.rotate(self.image,270)
            if self.angle == 180:
                self.image = pygame.transform.rotate(self.image,180)
            if self.angle == 270:
                self.image = pygame.transform.rotate(self.image,90)
            self.angle = 0
        if (key == pygame.K_LEFT):
            if self.angle == 0:
                self.image = pygame.transform.rotate(self.image,180)
            if self.angle == 90:
                self.image = pygame.transform.rotate(self.image,90)
            if self.angle == 180:
                self.image = pygame.transform.rotate(self.image,0)
            if self.angle == 270:
                self.image = pygame.transform.rotate(self.image,270)
            self.angle = 180
        if (key == pygame.K_UP):
            if self.angle == 0:
                self.image = pygame.transform.rotate(self.image,90)
            if self.angle == 90:
                self.image = pygame.transform.rotate(self.image,0)
            if self.angle == 180:
                self.image = pygame.transform.rotate(self.image,270)
            if self.angle == 270:
                self.image = pygame.transform.rotate(self.image,180)
            self.angle = 90
        if (key == pygame.K_DOWN):
            if self.angle == 0:
                self.image = pygame.transform.rotate(self.image,270)
            if self.angle == 90:
                self.image = pygame.transform.rotate(self.image,180)
            if self.angle == 180:
                self.image = pygame.transform.rotate(self.image,90)
            if self.angle == 270:
                self.image = pygame.transform.rotate(self.image,0)
            self.angle = 270

    def MoveKeyDown(self,key): 
        self.newangle(key)
            

     #def pickup(self):
              
