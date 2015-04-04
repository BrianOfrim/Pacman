import sys, pygame
from graph_v2 import Graph

class GUI():
    BG_COLOR = (32, 32, 32)
    
    
    def __init__(self,screen_height,screen_width,
                 score_rect=(0,550,600,50),score_color =(0,0,255)):


        #Initialize screen
        self.screen = pygame.display.set_mode((screen_width,screen_height))
        self.caption = pygame.display.set_caption("Pacman")        
        #Initialize score
        self.draw_rect(self.screen,score_color,score_rect)
        #Initialize background 
        background = pygame.Surface(self.screen.get_size())
        self.background = background.convert()
        self.background.fill((250, 250, 250))


    def draw_rect(self,screen,color,rect):
        return pygame.draw.rect(screen,color,rect)

    def draw_circle(self,screen, color, pos, radius):
        return pygame.draw.circle(screen, color, pos, radius)

    def map(self):
        edges = list()
        verticies = set()
        pac_dot_status = {}
        tile_dim = 25
        maparray = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,0,0],
                    [0,0,0,1,0,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,0,1,0,0,0],
                    [0,0,0,1,0,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,0,1,0,0,0],
                    [0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
                    [0,0,0,1,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,0,1,0,0,0],
                    [0,0,0,1,1,1,1,0,1,1,1,1,0,1,1,1,1,0,1,1,1,1,0,0,0],
                    [0,0,0,0,0,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0,0],
                    [0,0,0,0,0,0,1,0,1,1,1,1,1,1,1,1,1,0,1,0,0,0,0,0,0],
                    [0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0],
                    [0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0],
                    [0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0],
                    [0,0,0,0,0,0,1,0,1,1,1,1,1,1,1,1,1,0,1,0,0,0,0,0,0],
                    [0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0],
                    [0,0,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,0,0],
                    [0,0,0,1,0,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,0,1,0,0,0],
                    [0,0,0,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,0,0],
                    [0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0],
                    [0,0,0,1,1,1,1,0,1,1,1,1,0,1,1,1,1,0,1,1,1,1,0,0,0],
                    [0,0,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0],
                    [0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
        for y in range(0,len(maparray)):
            for x in range(0,len(maparray[y])):
                if maparray[y][x] == 0:
                    self.draw_rect(self.screen,(0,0,255),(25*x,25*y,25,25))
                else:
                    self.draw_circle(self.screen,(222,253,68),
                                     (25*x+12,25*y+12), 2)
                    verticies.add((x*tile_dim, y*tile_dim))
                    pac_dot_status[(x*tile_dim, y*tile_dim)] = 1
                    #check for left neighbour
                    if(x!=0 and maparray[y][x-1] == 1):
                        edges.append(((x*tile_dim, y*tile_dim),
                                     ((x-1)*tile_dim, y*tile_dim)))
                    #check for upper neighbour
                    if(y!=0 and maparray[y-1][x] == 1):
                        edges.append(((x*tile_dim, y*tile_dim),
                                     (x*tile_dim, (y-1)*tile_dim)))
        return Graph(verticies,edges), pac_dot_status
                           
                
                    
