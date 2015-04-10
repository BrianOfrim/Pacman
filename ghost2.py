import pygame, gui, process_path, math,pdb
from pygame.sprite import Sprite
from binary_heap import BinaryHeap
from ghost import ghost
import random
class clyde(ghost):
    #clyde is a non-intelligent ghost that makes follows a random path
    def __init__(self,x,y,path_graph):
        ghost.__init__(self,x,y,path_graph)
        next_node = process_path.next_node(
            (self.current_node[0],self.current_node[1]),
            self.map,self.angle)
        self.next_node = [next_node[0], next_node[1]]

    def move(self):
        '''
        move in the current direction unless a intersection or a wall is 
        encountered, then make a random choice
        '''
        self.move_random()
        
    def respawn(self):
        '''
        Reinitialize the ghost to how it was at the stat of the game
        '''
        self.imgnum = 1
        self.angle = 0      
        self.current_node = [self.start_x, self.start_y]
        self.rect.x = self.start_x
        self.rect.y = self.start_y
        next_node = process_path.next_node(
            (self.current_node[0],self.current_node[1]),
            self.map,self.angle)
        self.next_node = [next_node[0],next_node[1]]
