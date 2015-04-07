import sys, pygame
from graph_v2 import Graph
from pellet import Pellet
from unit import pacman
from ghost import ghost
class GUI():
    BG_COLOR = (32, 32, 32)
    
    
    def __init__(self,screen_height,screen_width,
                 score_rect=(0,550,600,50),score_color =(0,0,255)):


        #Initialize screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((screen_width,screen_height))
        self.caption = pygame.display.set_caption("Pacman")        
        #Initialize score
        
        self.draw_rect(self.screen,score_color,score_rect)
        #Initialize background 
        background = pygame.Surface(self.screen.get_size())
        self.background = background.convert()
        self.background.fill((250, 250, 250))
        self.pellet_list = pygame.sprite.Group()
        self.pacman_and_pellets = pygame.sprite.Group()
        self.pellets_added = False
        self.count =0
        self.ghost_list = pygame.sprite.Group()
    def draw_background(self):
        self.draw_rect(self.screen,GUI.BG_COLOR,
                       (0,0,self.screen_width,self.screen_height))

    def draw_rect(self,screen,color,rect):
        return pygame.draw.rect(screen,color,rect)

    def draw_circle(self,screen, color, pos, radius):
        return pygame.draw.circle(screen, color, pos, radius)

    def map_array(self):

        maparray = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,0],
                    [0,0,1,0,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,0,1,0,0],
                    [0,0,1,0,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,0,1,0,0],
                    [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
                    [0,0,1,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,0,1,0,0],
                    [0,0,1,1,1,1,0,1,1,1,1,0,1,1,1,1,0,1,1,1,1,0,0],
                    [0,0,0,0,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0],
                    [0,0,0,0,0,1,0,1,1,1,1,1,1,1,1,1,0,1,0,0,0,0,0],
                    [0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0],
                    [0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0],
                    [0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0],
                    [0,0,0,0,0,1,0,1,1,1,1,1,1,1,1,1,0,1,0,0,0,0,0],
                    [0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0],
                    [0,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,0],
                    [0,0,1,0,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,0,1,0,0],
                    [0,0,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,0],
                    [0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,1,0,0,0],
                    [0,0,1,1,1,1,0,1,1,1,1,0,1,1,1,1,0,1,1,1,1,0,0],
                    [0,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,0],
                    [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
        return maparray

    def draw_map(self):
        tile_dim = 25
        maparray = self.map_array()
        for y in range(0,len(maparray)):
            for x in range(0,len(maparray[y])):
                if maparray[y][x] == 0:
                    self.draw_rect(self.screen,(0,0,255),(25*x,25*y,25,25))
 
 
    def map(self):
        edges = list()
        verticies = set()
        tile_dim = 25
        maparray = self.map_array()
        for y in range(0,len(maparray)):
            for x in range(0,len(maparray[y])):
                if maparray[y][x] == 1:
                    pellet = Pellet()
                    pellet.rect.x = 25*x+12
                    pellet.rect.y = 25*y+12
                    self.pellet_list.add(pellet)
                    self.pacman_and_pellets.add(pellet)
                    verticies.add((x*tile_dim, y*tile_dim))
                    #check for left neighbour
                    if(x!=0 and maparray[y][x-1] == 1):
                        edges.append(((x*tile_dim, y*tile_dim),
                                      ((x-1)*tile_dim, y*tile_dim)))
                        edges.append((((x-1)*tile_dim, y*tile_dim),
                                      (x*tile_dim, y*tile_dim)))                        
                    #check for upper neighbour
                    if(y!=0 and maparray[y-1][x] == 1):
                        #print(self.count)
                        #self.count += 1
                        edges.append(((x*tile_dim, y*tile_dim),
                                      (x*tile_dim, (y-1)*tile_dim)))
                        edges.append(((x*tile_dim, (y-1)*tile_dim),
                                      (x*tile_dim, y*tile_dim)))
                        
        return Graph(verticies,edges)
                           
                            
    
                
    def print_pacman(self):
        pacguy = pacman()
        #rect = pacman.get_rect()
        #self.screen.blit(pacman,[50,50])
        #pygame.display.update((50,50,25,25))
        self.pacman_and_pellets.add(pacguy)
        pacguy.start()
        pacguy.update()
        return pacguy


    def print_stuff(self, pacguy):
        #font = pygame.font.SysFont("monospace", 15)
        font1 = pygame.font.Font("Assets/pacfont.ttf", 16)
        font2 = pygame.font.Font(None, 30)
        font3 = pygame.font.Font("Assets/pacfont.ttf", 50)
        font3.set_bold(1)
        score1 = font1.render("Score: ", 1, (247,255,0))
        #print(pacguy.score)
        title = font3.render("PACMAN", 1, (247,255,0))
        score2 = font2.render(str(int(pacguy.score)), 1, (247,255,0))
        if pacguy.lives == 1:
            lives = font1.render("Lives: 1", 1, (247,255,0))
        if pacguy.lives == 2:
            lives = font1.render("Lives: 11", 1, (247,255,0))
        if pacguy.lives == 3:
            lives = font1.render("Lives: 111", 1, (247,255,0))
        self.screen.blit(title, (135,0))
        self.screen.blit(score1, (0,610))
        self.screen.blit(score2, (80,610))
        self.screen.blit(lives, (200,610))

