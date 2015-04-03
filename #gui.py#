import sys, pygame
from graph_V2 import Graph

class GUI():
    BG_COLOR = (32, 32, 32)

    
    def __init__(self,screen_height,screen_width,
                 score_rect=(0,500,600,100),score_color =(0,0,255)):

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
        pygame.draw.rect(screen,color,rect)

    def draw_map(self,level_map):
        edges = list()
        verticies = set()
        
    
    
