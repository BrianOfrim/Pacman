
import sys, pygame
from graph_v2 import Graph
from pellet import Pellet
from binary_heap import BinaryHeap
import math

def closest_node(x,y,graph):
    '''
    Computes the closest node to the input x and y coordiates
    on a specified graph

    Args: x (int) = an x coordinate
          y (int) = a y coordinate
          graph (Graph) = a valid graph 

    Returns : (vertex) = the closest vertex on the input graph
                         to the input x and y coordinates
    '''
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
    '''
    Computes the next node in a graph after current_node
             in the dirction given by angle

    Args: current_node = a vertex in the graph
          graph (Graph) = a valid graph 
          angle (int) = the angle relative to the horizontal
                        that the next node should be relative to 
                        current_node

    Returns : (vertex) = the next node if it exists; else None
    '''

    neighbours = graph.neighbours(current_node)
    for neighbour in neighbours:
        dx = neighbour[0]-current_node[0]
        dy = neighbour[1]-current_node[1]
        if dx > 0:
            node_to_node_angle = 0
        elif dx < 0:
            node_to_node_angle = 180
        elif dy < 0:
            node_to_node_angle = 90
        elif dy > 0:
            node_to_node_angle = 270
        if node_to_node_angle == angle:
            return neighbour
    return None

def num_neighbours(current_node, graph, angle):
    '''
    Computes the number of neighbours that the current node has

    Args: current_node = a vertex in the graph
          graph (Graph) = a valid graph 

    Returns : (int) number of neighbours that the current node has
    '''
    neighbours = graph.neighbours(current_node)
    num_neighbours = 0
    for neighbour in neighbours:    
        num_neighbours += 1
    return num_neighbours

        

    


    
    

