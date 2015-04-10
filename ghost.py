import pygame, gui, process_path, math,pdb
from pygame.sprite import Sprite
from binary_heap import BinaryHeap
import random
class ghost(Sprite):
    #ghosts are the enimies of pacman
    #the image used when the ghosts are in their normal state
    sprite = pygame.image.load("Assets/ghost1.png")
    #the image used when the ghosts are in their scared state
    sprite1 = pygame.image.load("Assets/ghost_scared.png")
    def __init__(self,x,y,path_graph):
        Sprite.__init__(self)
        self.angle = 0
        #map is the map that the ghost is to travel on
        #the graph has nodes that are spaced 25 pixels apart
        #these nodes represent path tiles
        #ghosts make node to node movements 5 pixels at a time
        self.map = path_graph
        #image for normal state
        self.image1 = ghost.sprite.convert()
        #current image
        self.image = self.image1
        self.rect = self.image.get_rect()
        #image for scared state
        self.image2 = ghost.sprite1.convert()
        #node that the ghost is traveling to
        self.next_node = None
        #imgnum is used to diaply the appropriate image
        #imgnum = 1 for normal state and 2 for scarred state
        self.imgnum = 1
        #position of the upper left postion of the ghost sprite
        #in screen coordinates
        self.rect.x = x
        self.rect.y = y
        #node the ghost is currently at or traveling from
        self.current_node = [x, y]
        #initial coordiates
        self.start_x = x
        self.start_y = y
        self.derp = 0
        #previous state of the ghost
        self.prev_num = self.imgnum
        


        

    def move(self,pacman_x,pacman_y):
        '''
        Called when the ghost is to move
        
        Args: pacman_x (int) = x coord of pacman in screen coordinates
              pacman_y (int) = y coord of pacman in screen coordinates
           
        '''
        #if the ghost is going form its normal state to its scrared state then
        #make sure the ghost is on the path by re initializing its current and
        # next node
        if((self.prev_num == 1) and (self.imgnum == 2)):
           self.make_sure_ghost_on_path()
        self.prev_num = self.imgnum
        
        if self.imgnum == 1:
            #normal state
            self.move_closest_path(pacman_x, pacman_y)
        else:
            #scarred
            self.move_random()
            

    def move_closest_path(self,pacman_x,pacman_y):
        '''
        calcualtes the shortest path to pacman and move in that direction

        Args: pacman_x (int) = x coord of pacman in screen coordinates
              pacman_y (int) = y coord of pacman in screen coordinates

        '''
        #compute the position of the current node
        self.find_current_node()
        #compute the shortest path
        path = self.least_cost_path(self.map,
                                  (self.current_node[0], self.current_node[1])
                                    ,(pacman_x,pacman_y),self.cost_distance)
        #next node is set to the first move in the shortest path
        self.next_node = path[1]
        #movements are made and correct image is configured        
        dx = self.next_node[0] - self.current_node[0]
        dy = self.next_node[1] - self.current_node[1]
        if dx > 0:
            self.angle = 0
            self.rect.x += 5
        elif dx < 0:
            self.angle = 180
            self.rect.x -= 5
        elif dy < 0:
            self.angle = 90
            self.rect.y -= 5
        elif dy > 0:
            self.angle = 270
            self.rect.y += 5
        if(self.angle != 180):
            if self.imgnum == 1:
                self.image = pygame.transform.rotate(self.image1,self.angle)
            if self.imgnum == 2:
                self.image = pygame.transform.rotate(self.image2,self.angle)
        else:
            if self.imgnum == 1:
                self.image = pygame.transform.flip(self.image1,True,False)
            if self.imgnum == 2:
                self.image = pygame.transform.flip(self.image2,True,False)

    def move_random(self):
        '''
        moves the pacman in the current direction and if a wall or 
        intersection is approached then make a random choice
        '''
        if self.angle == 0:
            self.rect.x += 5
        if self.angle == 90:
            self.rect.y -= 5
        if self.angle == 180:
            self.rect.x -= 5
        if self.angle == 270:
            self.rect.y += 5
        #check if the ghost has reached the node it was traveling to
        if((self.rect.x == self.next_node[0]) and
           (self.rect.y == self.next_node[1])):
            self.current_node = self.next_node
            #get the neighbours of the current node
            num_neighbours = process_path.num_neighbours((
                    self.current_node[0],self.current_node[1]),
                                                         self.map,self.angle)
            
            if num_neighbours > 2:
                #an intersection has been approached, make a random choice
                self.random_choice()
                return
            #compute the next node in the current direction
            next_node = process_path.next_node((
                    self.current_node[0],self.current_node[1]),
                                                    self.map,self.angle)
            
            if(next_node == None):
                #a wall has been approached so make a random choice
                self.next_node = None
                self.random_choice() 
                return
            #a node in the current direction exists
            self.next_node = [next_node[0], next_node[1]]

           
               
    def random_choice(self):
        '''
        makes a random choice for the next node
        '''
        neighbours = self.map.neighbours((self.current_node[0]
                                          ,self.current_node[1]))
        next_node = random.choice(neighbours)
        if(next_node == None):
            print("No next node in the random state")
        self.next_node = [next_node[0], next_node[1]]
        #compute the angle and configure the image
        dx = self.next_node[0]-self.current_node[0]
        dy = self.next_node[1]-self.current_node[1]
        if dx > 0:
            self.angle = 0
        elif dx < 0:
            self.angle = 180
        elif dy < 0:
            self.angle = 90
        elif dy > 0:
            self.angle = 270
        if(self.angle != 180):
            if self.imgnum == 1:
                self.image = pygame.transform.rotate(self.image1,self.angle)
            if self.imgnum == 2:
                self.image = pygame.transform.rotate(self.image2,self.angle)
        else:
            if self.imgnum == 1:
                self.image = pygame.transform.flip(self.image1,True,False)
            if self.imgnum == 2:
                self.image = pygame.transform.flip(self.image2,True,False)
            
            
    def newimgrot(self):
        '''
        configure the image according to the current angle
        '''
        if self.angle == 0:
            self.image = pygame.transform.rotate(self.image,0)
        if self.angle == 90:
            self.image = pygame.transform.rotate(self.image,90)
        if self.angle == 180:
            self.image = pygame.transform.flip(self.image,True,False)
        if self.angle == 270:
            self.image = pygame.transform.rotate(self.image,270)

    def least_cost_path(self,graph, start, dest, cost):
        """
        Find and return the least cost path in graph from start
        vertex to dest vertex.
        
        Efficiency: If E is the number of edges, the run-time is
        O( E log(E) ).
        
        Args:
        graph (Graph): The digraph defining the edges between the
        vertices.
        start: The vertex where the path starts. It is assumed
        that start is a vertex of graph.
        dest: The vertex where the path ends. It is assumed
        that start is a vertex of graph.
        cost: A function, taking a single edge as a parameter and
        returning the cost of the edge. For its interface,
        see the definition of cost_distance.
        
        Returns:
        list: A potentially empty list (if no path can be found) of
        the vertices in the graph. If there was a path, the first
        vertex is always start, the last is always dest in the list.
        Any two consecutive vertices correspond to some
        edge in graph.
        >>> graph = Graph({1,2,3,4,5,6}, [(1,2), (1,3), (1,6), (2,1),\
        (2,3), (2,4), (3,1), (3,2), (3,4), (3,6), (4,2), (4,3),\
        (4,5), (5,4), (5,6), (6,1), (6,3), (6,5)])
        >>> weights = {(1,2): 7, (1,3):9, (1,6):14, (2,1):7, (2,3):10,\
        (2,4):15, (3,1):9, (3,2):10, (3,4):11, (3,6):2,\
        (4,2):15, (4,3):11, (4,5):6, (5,4):6, (5,6):9, (6,1):14,\
        (6,3):2, (6,5):9}
        >>> cost = lambda e: weights.get(e, float("inf"))
        >>> least_cost_path(graph, 1,5, cost)
        [1, 3, 6, 5]
        """  
        R = {}
        dist = {}
        PQ = BinaryHeap()
        PQ.add((start,start),0)
        while PQ:
            weighted_edge = PQ.pop_min()
            if(weighted_edge[0][1] not in R):
                curr = weighted_edge[0][1]
                prev = weighted_edge[0][0]
                val = weighted_edge[1]
                R[curr] = prev
                dist[curr] = val
                for succ in graph.neighbours(curr):
                    if(succ != prev):
                        PQ.add((curr,succ),(val + cost((curr,succ))))

    #return empty list if no path exist, else return a list of waypoints
        if(dest not in R):
            return list()
        else:
            path = list()
            path.append(dest)
            while(path[0] != start):
                path.insert(0,(R[path[0]]))
            return path





    def cost_distance(self,e):
        '''
        Computes and returns the straight-line distance between the two
        vertices at the endpoints of the edge e.
        Args:
        e: An indexable container where e[0] is the vertex id for the
        starting vertex of the edge, and e[1] is the vertex id for the
        ending vertex of the edge.
        Returns:
        numeric value: the distance between the two vertices.
    
        >>> a = cost_distance((36396914,29577354))
        >>> a
        159
        '''
        start_vertex = e[0]
        end_vertex = e[1]
        delta_lat = end_vertex[0] - start_vertex[0]
        delta_lon = end_vertex[1] - start_vertex[1]
        distance = int(math.sqrt(delta_lat**2 + delta_lon**2))
        return distance

    def find_current_node(self):
        '''
        compute the current node based on the ghosts position and angle
        '''
        if(self.angle == 0):
            self.current_node[0] = self.rect.x - (self.rect.x % 25)
            return
        if(self.angle == 180):
            if (self.rect.x % 25 == 0):
                self.current_node[0] = self.rect.x  
            else:
                self.current_node[0] = self.rect.x + (25 - self.rect.x % 25)
            return
        if(self.angle == 90):
            if (self.rect.y % 25 ==0):
                self.current_node[1] = self.rect.y
            else :                
                self.current_node[1] = self.rect.y + (25 - self.rect.y % 25)
            return
        if(self.angle == 270):
             self.current_node[1] = self.rect.y - (self.rect.y % 25)


    def respawn(self):
        '''
        Reinitialize the ghost to how it was at the stat of the game
        '''
        self.imgnum = 1
        self.angle = 0      
        self.current_node = [self.start_x, self.start_y]
        self.rect.x = self.start_x
        self.rect.y = self.start_y
        self.next_node = None



    def make_sure_ghost_on_path(self):
        '''
        compute the current and next nodes based on where the ghost is
        and its angle. Placr the ghost on the current node
        '''
           
        current_node = process_path.closest_node(self.rect.x,
                                                     self.rect.y,self.map)
        self.current_node = [current_node[0], current_node[1]]
        self.rect.x = self.current_node[0]
        self.rect.y = self.current_node[1]
        next_node = process_path.next_node((
                self.current_node[0],self.current_node[1]),
                                                    self.map,self.angle)     
        if(next_node == None):
            self.next_node = None
            self.random_choice() 
        else:
            self.next_node = [next_node[0], next_node[1]]
  
