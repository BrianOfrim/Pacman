import pygame, gui, process_path, math,pdb
from pygame.sprite import Sprite
from binary_heap import BinaryHeap
from ghost import ghost
import random
class clyde(ghost):
    def __init__(self,x,y,path_graph):
        ghost.__init__(self,x,y,path_graph)
        next_node = process_path.next_node(
            (self.current_node[0],self.current_node[1]),
            self.map,self.angle)
        self.next_node = [next_node[0], next_node[1]]

    def move(self):
        self.move_random()
        
    def respawn(self):
        self.imgnum = 1
        self.angle = 0     
        #closest_node = process_path.closest_node(self.rect.x,self.rect.y
        #                                         ,self.map)
 
        self.current_node = [self.start_x, self.start_y]
        self.rect.x = self.start_x
        self.rect.y = self.start_y
        next_node = process_path.next_node(
            (self.current_node[0],self.current_node[1]),
            self.map,self.angle)
        self.next_node = [next_node[0],next_node[1]]
