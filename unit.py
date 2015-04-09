import pygame, gui, process_path, math
from pygame.sprite import Sprite


class pacman(Sprite):
    """
    this is the base unit class that will be inherited by the pacman class and 
    the ghost class. It will just generally have to do with any object that is
    printed to the map.
    """
    sprite = pygame.image.load("Assets/pacman.png")
    sprite1 = pygame.image.load("Assets/circle.png")
    def __init__(self,
                 loc_x ,
                 loc_y ,
                 path_graph):
        
        Sprite.__init__(self)
        
        
        #self.loc_x = loc_x
        #self.loc_y = loc_y
        self.derp = 0
        self.power = 0
        self.angle = 0
        #self.score = 0
        #self.lives = 3
        #Some default values so that nothing complains when trying to
        #assign later
        self._moving = False
        self._alive = False
        self.map = path_graph
        #pygame.init()
        self.sound1 = pygame.mixer.Sound("Assets/pacman_chomp.wav")       
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
        self.imgnum = 1       
        self.image = pacman.sprite.convert()
        self.image1 = pacman.sprite.convert()
        self.image2 = pacman.sprite1.convert()
        #self.imgnum = 1
        self.loopcount = 0
        self.lives = 3
        self.score = 0
        self.base_image = self.image
        self.rect = self.image.get_rect()
 

        self.image.set_colorkey((32,32,32))
        self.image1.set_colorkey((32,32,32))
        self.image2.set_colorkey((32,32,32))
        #def move(self):

        self.current_node = process_path.closest_node(loc_x,loc_y,self.map)
        #sync graph with Pacman
        self.rect.x = self.current_node[0]
        self.rect.y = self.current_node[1]
        self.next_node = process_path.next_node(self.current_node,self.map,
                                                self.angle)
        self.start_x = self.rect.x
        self.start_y = self.rect.y



    def die(self):
        self.lives -= 1


        
   
    def newimgrot(self):
        if self.angle == 0:
            self.image = pygame.transform.rotate(self.base_image,0)
        if self.angle == 90:
            self.image = pygame.transform.rotate(self.base_image,90)
        if self.angle == 180:
            self.image = pygame.transform.rotate(self.base_image,180)
        if self.angle == 270:
            self.image = pygame.transform.rotate(self.base_image,270)

    """def newangle(self,key):
        if (key == pygame.K_RIGHT):
            self.image1 = pygame.transform.rotate(self.base_image,0)
            self.angle = 0
        if (key == pygame.K_LEFT):
            self.image1 = pygame.transform.rotate(self.base_image,180)
            self.angle = 180
        if (key == pygame.K_UP):
            self.image1 = pygame.transform.rotate(self.base_image,90)
            self.angle = 90
        if (key == pygame.K_DOWN):
            self.image1 = pygame.transform.rotate(self.base_image,270)
            self.angle = 270"""

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
            if self.imgnum == 1:
                self.image = pygame.transform.rotate(self.image1,self.angle)
            elif self.imgnum == 2:
                self.image = pygame.transform.rotate(self.image2,self.angle)
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
        self.loopcount +=1
        #print(self.loopcount)
        if self.loopcount == 3:
            self.loopcount = 0
            #print(self.imgnum)
            if self.imgnum == 1:
                self.imgnum = 2
                #print(self.imgnum)
                self.image = self.image2
                self.sound1.play()
            elif self.imgnum == 2:
                self.imgnum = 1
                self.image = self.image1
                self.newimgrot()
                                
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
        
        
            
    def respawn(self):
        self.angle = 0
        self.move_state = "N"       
        
        self.current_node = process_path.closest_node(self.start_x,
                                                      self.start_y,self.map)
        #sync graph with Pacman
        self.rect.x = self.current_node[0]
        self.rect.y = self.current_node[1]
        self.next_node = process_path.next_node(self.current_node,self.map,
                                                self.angle)

