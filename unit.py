import pygame, gui, process_path, math, pdb
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

        self.derp = 0
        #power is temperarily set to 1 if a power pellet is consumed
        self.power = 0
        self.angle = 0
        self._moving = False
        self._alive = False
        #graph of the path that pacman is to travel on
        #the graph has nodes that are spaced 25 pixels apart
        #these nodes represent path tiles
        #pacman makes node to node movements 5 pixels at a time
        self.map = path_graph
        self.sound1 = pygame.mixer.Sound("Assets/pacman_chomp.wav")       
        self.move_sound = None
        self.hit_sound = None
        #move_start = 'N' for Normal OR 'D' for desision when a wall 
        #is encountered
        self.move_state = "N"
        #images used for pacman open and closed mouth
        self.imgnum = 1       
        self.image = pacman.sprite.convert()
        self.image1 = pacman.sprite.convert()
        self.image2 = pacman.sprite1.convert()
        self.loopcount = 0
        self.lives = 3
        #score is based on the number of pellets and ghosts pacman consumes
        self.score = 0
        self.base_image = self.image
        self.rect = self.image.get_rect()
        self.image.set_colorkey((32,32,32))
        self.image1.set_colorkey((32,32,32))
        self.image2.set_colorkey((32,32,32))
        #current node is calculated and pacman is placed on it
        self.current_node = process_path.closest_node(loc_x,loc_y,self.map)
        #coords of the top left corner of pacman in screen coords
        self.rect.x = self.current_node[0]
        self.rect.y = self.current_node[1]
        self.next_node = process_path.next_node(self.current_node,self.map,
                                                self.angle)
        #initial coords are stored for respawn purposes
        self.start_x = self.rect.x
        self.start_y = self.rect.y

    def die(self):
        #decrements pacman lives
        self.lives -= 1


    def newimgrot(self):
        #configure the image based on the current angle
        if self.angle == 0:
            self.image = pygame.transform.rotate(self.base_image,0)
        if self.angle == 90:
            self.image = pygame.transform.rotate(self.base_image,90)
        if self.angle == 180:
            self.image = pygame.transform.rotate(self.base_image,180)
        if self.angle == 270:
            self.image = pygame.transform.rotate(self.base_image,270)


    def process_angle(self, key):
        '''
        Processes the requested direction change form the keyboard

        Args: key = the key that was pressed (must be an arrow key)
        
        Note: In the case where a 90 degree direction change is requested
              two checks are preformed. One to see if the current node has
              a neighbour in the direction requested and on that checks if 
              the next node has a neighbour in the diection requested
              
        '''
        if (key == pygame.K_RIGHT):
            requested_angle = 0
        if (key == pygame.K_UP):
            requested_angle = 90
        if (key == pygame.K_LEFT):
            requested_angle = 180
        if (key == pygame.K_DOWN):
            requested_angle = 270

        #get the neighbour of the current node in the direction of 
        #the requested angle
        potential_next_node = process_path.next_node(self.current_node,
                                                     self.map, requested_angle)
        
        if(potential_next_node == None):
            if self.move_state == 'D':
                #pacman is at a wall and there is no path in the direction
                #that was requested
                return
            #get the neighbour of the next node in the direction of 
            #the requested angle
            potential_next_next_node = process_path.next_node(self.next_node,
                                                     self.map, requested_angle)
            if(potential_next_next_node == None):
                # no node in the requested direction
                return 
            #check if a 90 degree turn was requested
            #this applies to the next node
            if((abs(self.angle - requested_angle) == 90)
               or (self.angle == 0 and requested_angle == 270)
               or (self.angle == 270 and requested_angle == 0)):
                #check if the pacman is close enough to the next node
                #for the dirction change to be valid
                if((abs(self.rect.x - self.next_node[0]) <= 5) and
                   (abs(self.rect.y - self.next_node[1]) <= 5)):
                    #initialize the pacman on its new direction
                    self.current_node = self.next_node
                    self.next_node = potential_next_next_node
                    self.angle = requested_angle
                    self.image = pygame.transform.rotate(self.base_image,
                                                         self.angle)
                    self.move_state = 'N'
                    self.rect.x = self.current_node[0]
                    self.rect.y = self.current_node[1]
                    return
                return

        #check if a 180 degree direction change was requested or at a wall
        if((requested_angle ==(self.angle + 180) % 360) or 
           self.move_state =='D'):
            #initialize the direction change
            self.next_node = potential_next_node
            self.angle = requested_angle
            if self.imgnum == 1:
                self.image = pygame.transform.rotate(self.image1,self.angle)
            elif self.imgnum == 2:
                self.image = pygame.transform.rotate(self.image2,self.angle)
            self.move_state = 'N'
            return


        #check if a 90 degree dirction change was requested
        #this check applies to the current node
        if((abs(self.angle - requested_angle) == 90)
           or (self.angle == 0 and requested_angle == 270)
           or (self.angle == 270 and requested_angle == 0)):
            #check if the pacman is close enough to the next node
            #for the dirction change to be valid
            if((abs(self.rect.x - self.current_node[0]) <= 5) and
               (abs(self.rect.y - self.current_node[1]) <= 5)):
                #initialize direction change
                self.next_node = potential_next_node
                self.angle = requested_angle
                self.image = pygame.transform.rotate(self.base_image,self.angle)
                self.move_state = 'N'
                self.rect.x = self.current_node[0]
                self.rect.y = self.current_node[1]
                return



           
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

            

    def move(self):
        #handels pacman movement and animation
        '''
        If pacman is in the 'N' (Normal) move state then move it in
        the dirction that it is facing, if it is in the 'D' (Decision)
        state then do nothing. 
        '''
        if self.move_state == 'D': return
        if self.angle == 0:
            self.rect.x += 5
        if self.angle == 90:
            self.rect.y -= 5
        if self.angle == 180:
            self.rect.x -= 5
        if self.angle == 270:
            self.rect.y += 5
        #Pacman mouth open/close animation
        self.loopcount +=1
        if self.loopcount == 3:
            self.loopcount = 0
            if self.imgnum == 1:
                self.imgnum = 2
                self.image = self.image2
                self.sound1.play()
            elif self.imgnum == 2:
                self.imgnum = 1
                self.image = self.image1
                self.newimgrot()
        #if pacman has reached its next_node then update
        #current_node and next_node
        if((self.rect.x == self.next_node[0]) and 
           (self.rect.y == self.next_node[1])):
               self.current_node = self.next_node
               num_neighbours = process_path.num_neighbours(self.current_node,
                                                            self.map,
                                                            self.angle)

               self.next_node = process_path.next_node(self.current_node,
                                                       self.map,
                                                       self.angle)
               if(self.next_node == None):
                   #pacman is at a wall and now will have to make a decision
                   self.move_state = 'D'
           

            
    def MoveKeyDown(self,key):
        '''
        called when valid keyboard input is detected
        Args: key = the key that was pressed
        '''
        self.process_angle(key)
        
        
            
    def respawn(self):
        '''
        Reinitialize the pacman to how it was at the stat of the game
        '''
        self.angle = 0
        self.move_state = "N"       
        self.current_node = process_path.closest_node(self.start_x,
                                                      self.start_y,self.map)
        #sync graph with Pacman
        self.rect.x = self.current_node[0]
        self.rect.y = self.current_node[1]
        self.next_node = process_path.next_node(self.current_node,self.map,
                                                self.angle)

