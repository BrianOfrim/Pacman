import pygame, gui, process_path, math,pdb
from pygame.sprite import Sprite
from binary_heap import BinaryHeap
from ghost import ghost
import random
class clyde(ghost):
    def __init__(self,x,y,path_graph):
        ghost.__init__(self,x,y,path_graph)
        self.next_node = process_path.next_node(
            (self.current_node[0],self.current_node[1]),
            self.map,self.angle)


    def move(self):
        if self.angle == 0:
            self.rect.x += 5
        if self.angle == 90:
            self.rect.y -= 5
        if self.angle == 180:
            self.rect.x -= 5
        if self.angle == 270:
            self.rect.y += 5

        if((self.rect.x == self.next_node[0]) and 
           (self.rect.y == self.next_node[1])):
               self.current_node = self.next_node
               #print("lol")
               num_neighbours = process_path.num_neighbours(self.current_node,
                                                            self.map,
                                                            self.angle)
               if num_neighbours > 2:
                   self.random_choice()
                   return
               self.next_node = process_path.next_node(self.current_node,
                                                       self.map,
                                                       self.angle)
               if(self.next_node == None):
                   self.random_choice()
           
               
    def random_choice(self):
        neighbours = self.map.neighbours(self.current_node)
        self.next_node = random.choice(neighbours)
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
        if self.imgnum == 1:
            self.image = pygame.transform.rotate(self.image1,self.angle)
        if self.imgnum == 2:
            self.image = pygame.transform.rotate(self.image2,self.angle)
            
        
