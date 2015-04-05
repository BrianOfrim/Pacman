
import sys, pygame
from graph_v2 import Graph
from pellet import Pellet
#from unit import pacman
from binary_heap import BinaryHeap
import math

def closest_node(pacman_x,pacman_y,graph):
    #returns the closest node to pacman
    x = pacman_x
    y = pacman_y 
    path = graph
    BH = BinaryHeap()
    for i in path._alist:
        dx = i[0] - x
        dy = i[1] - y
        distance = int(math.sqrt(dx**2 +dy**2))
        BH.add(i,distance)
    closest_vert = BH.pop_min()
    return closest_vert[0]

def next_node(current_node, graph, angle):
    neighbours = graph.neighbours(current_node)
    for neighbour in neighbours:
        print(neighbour)
        dx = neighbour[0]-current_node[0]
        dy = neighbour[1]-current_node[1]
        if dx > 0:
            node_to_node_angle = 0
        elif dx < 0:
            node_to_node_angle = 180
        elif dy > 0:
            node_to_node_angle = 90
        elif dy < 0:
            node_to_node_angle = 270
        if node_to_node_angle == angle:
            return neighbour
    return None

def num_neighbours(current_node, graph, angle):
    neighbours = graph.neighbours(current_node)
    num_neighbours = 0
    for neighbour in neighbours:    
        num_neighbours += 1
    return num_neighbours

        

    


    
    

