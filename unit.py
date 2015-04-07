import pygame, gui, process_path, math
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
        self.map = None
       
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
        
        #move states: N = node to node D = decision
        self.move_state = "N"
        
        #Default unit stats
        #self.move_sound = None
        #self.hit_sound = None
        #self.die_sound
        
        self.image = pacman.sprite.convert()
        self.base_image = self.image
        self.rect = self.image.get_rect()
        self.image.set_colorkey((32,32,32))
        #def move(self):
        self.current_node = None
        self.next_node = None


    def die(self):
        self.lives = self.live - 1
        if self.lives == 0:
            gameover()

    def start(self):
        self.lives = 3
        self.score = 0
        self.rect.y = 18*25
        self.rect.x = 11*25
        
   

    def newangle(self,key):
        if (key == pygame.K_RIGHT):
            self.image = pygame.transform.rotate(self.base_image,0)
            self.angle = 0
        if (key == pygame.K_LEFT):
            self.image = pygame.transform.rotate(self.base_image,180)
            self.angle = 180
        if (key == pygame.K_UP):
            self.image = pygame.transform.rotate(self.base_image,90)
            self.angle = 90
        if (key == pygame.K_DOWN):
            self.image = pygame.transform.rotate(self.base_image,270)
            self.angle = 270

    def process_angle(self, key):
        if (key == pygame.K_RIGHT):
            requested_angle = 0
        if (key == pygame.K_UP):
            requested_angle = 90
        if (key == pygame.K_LEFT):
            requested_angle = 180
        if (key == pygame.K_DOWN):
            requested_angle = 270
        #check if directions are opposite
        if(requested_angle == ((self.angle + 180) % 360) 
           or self.move_state =='D'):
           #and (self.move_state == "N")):
            self.check_decision(requested_angle)
        
               #self.angle = requested_angle
               #self.image = pygame.transform.rotate(self.base_image,self.angle)
               #temp_node = self.current_node
               #self.current_node = self.next_node
               #self.next_node = self.current_node
               #return
        #if (self.move_state == 'D'):
            #self.check_decision(requested_angle)

           
    def check_decision(self,requested_angle):
        potential_next_node = process_path.next_node(self.current_node, 
                                                self.map, requested_angle)
        #if there is no next node then continue in decision mode
        if(potential_next_node == None):
            self.next_node = potential_next_node
            return 
        #check if it is a simple 180 degree turn on a path or desision mode
        if((requested_angle ==(self.angle + 180) % 360) or 
           self.move_state =='D'):
            self.next_node = potential_next_node
            self.angle = requested_angle
            self.image = pygame.transform.rotate(self.base_image,self.angle)
            self.move_state = 'N'
            
        #the request is to change paths while moving
        #check if it can be done
        #if(abs(self.angle - requested_angle) == 90):
        #    if((abs(self.rect.x - self.next_node[0]) <= 5) and
        #    (abs(self.rect.y - self.next_node[1]) <= 5)):
        #        self.current = self.next_node
        #        self.next_node = potential_next_node
        #        self.angle = requested_angle
        #        self.image = pygame.transform.rotate(self.base_image,self.angle)
        #        self.move_state = 'N'
        #        self.rect.x = self.current_node[0]
        #        self.rect.y = self.current_node[1]
            
        
        
           

        
        

        

    def move(self):
        #print(self.move_state)
        if self.move_state == 'D': return
        if self.angle == 0:
            self.rect.x += 5
        if self.angle == 90:
            self.rect.y -= 5
        if self.angle == 180:
            self.rect.x -= 5
        if self.angle == 270:
            self.rect.y += 5
        #print("")
        #print("Pacman x {}".format(self.rect.x))
        #print("Pacman y {}".format(self.rect.y))
        #print("NN x {}".format(self.next_node[0]))
        #print("NN y {}".format(self.next_node[1]))
        #change current node to next node
        if((self.rect.x == self.next_node[0]) and 
           (self.rect.y == self.next_node[1])):
               self.current_node = self.next_node
               #print("lol")
               num_neighbours = process_path.num_neighbours(self.current_node,
                                                            self.map,
                                                            self.angle)
               if num_neighbours > 2:
                   self.move_state = 'D'
                   return
               self.next_node = process_path.next_node(self.current_node,
                                                       self.map,
                                                       self.angle)
               if(self.next_node == None):
                   self.move_state = 'D'
           
               
               

    
    
    
        
            
    def MoveKeyDown(self,key):
        self.process_angle(key)
        
        
            
            

     #def pickup(self):
              
