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
        self.move_random()
        
