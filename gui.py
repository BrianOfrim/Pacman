import sys, pygame
from graph_v2 import Graph
from pellet import Pellet
from pellet import Power_Pellet
from unit import pacman
from ghost import ghost
class GUI():
    '''
    The graphic user interface handels the drawing of the map
    and the creation of the graph that the pacman and ghosts travel on,
    printing the title card, gameover screen, win screen, pacman's score,
    pacman's lives etc.
    '''
    BG_COLOR = (0, 0, 0)

    def __init__(self,screen_height,screen_width,
                 score_rect=(0,550,600,50),score_color =(0,0,255)):


        #Initialize screen
        self.start = 0
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((screen_width,screen_height))     
        #Initialize score
        self.draw_rect(self.screen,score_color,score_rect)
        #Initialize background 
        background = pygame.Surface(self.screen.get_size())
        self.background = background.convert()
        self.background.fill((250, 250, 250))
        #various sprite lists
        self.pellet_list = pygame.sprite.Group()
        self.ppellet_list = pygame.sprite.Group()
        self.pacman_and_pellets = pygame.sprite.Group()
        self.pacman = pygame.sprite.Group()
        self.pellets_added = False
        self.count =0
        self.ghost_list = pygame.sprite.Group()


    def draw_background(self):
        #draw a rectangle covering the entire screen 
        #the map will be printed on top of this rectangle
        self.draw_rect(self.screen,GUI.BG_COLOR,
                       (0,0,self.screen_width,self.screen_height))
    def draw_titlecard(self):
        #draws the title card that the user sees when the game is started
        self.draw_rect(self.screen,GUI.BG_COLOR,
                       (0,0,self.screen_width,self.screen_height))
        background1 = pygame.Surface(self.screen.get_size())
        self.background1 = background1.convert()
        self.background1.fill((250, 250, 250))
        font = pygame.font.Font("Assets/pacfont.ttf", 100)
        font1 = pygame.font.Font("Assets/pacfont.ttf", 20)
        title = font.render("PACMAN", 1, (247,255,0))
        prompt = font1.render("Press Enter to Start Playing", 1, (247,255,0))
        self.screen.blit(title, (10,0))
        self.screen.blit(prompt, (50,300))
    
    def gameover(self):
        #draw the gameover screen
        self.draw_rect(self.screen,GUI.BG_COLOR,
                       (0,0,self.screen_width,self.screen_height))
        background2 = pygame.Surface(self.screen.get_size())
        self.background2 = background2.convert()
        self.background2.fill((250, 250, 250))
        font = pygame.font.Font("Assets/Chiller.ttf", 140)
        font1 = pygame.font.Font("Assets/pacfont.ttf", 40)
        yousuck = font.render("You Lose!", 1, (255,0,0))
        prompt = font1.render("Press Q to Quit", 1, (247,30,0))
        self.screen.blit(yousuck, (0,100))
        self.screen.blit(prompt, (70,300))
        
    def win(self):
        #draw the winning screen
        self.draw_rect(self.screen,GUI.BG_COLOR,
                       (0,0,self.screen_width,self.screen_height))
        background3 = pygame.Surface(self.screen.get_size())
        self.background3 = background3.convert()
        self.background3.fill((250, 250, 250))
        font = pygame.font.Font("Assets/pacfont.ttf", 80)
        font1 = pygame.font.Font("Assets/pacfont.ttf", 20)
        yousuck = font.render("You Won!!!!", 1, (247,255,0))
        prompt = font1.render("Press Q to Quit", 1, (247,255,0))
        message = font1.render("This is super hard, good job!!!", 1, (247,255,0))
        self.screen.blit(yousuck, (0,100))
        self.screen.blit(prompt, (70,300))
        self.screen.blit(message, (50,400))

    def draw_rect(self,screen,color,rect):
        '''
        Draws a rectangle with the input parameters

        Args: screen : A pygame screen that the rectangle is to be drawn on
              color : The RGB value of the rectange
              rect (tuple) : (x,y, width, height)

        Returns : A rectangle
        '''
        return pygame.draw.rect(screen,color,rect)

    def draw_circle(self,screen, color, pos, radius):
        '''
        Draws a circle with the input parameters

        Args: screen : A pygame screen that the rectangle is to be drawn on
              color : The RGB value of the rectange
              pos (tuple) : (x,y)
              radius (int) : radius of the circle

        Returns : A circle
        '''
        return pygame.draw.circle(screen, color, pos, radius)

    def map_array(self):
        #returns an array representing the pacman's path graph
        maparray = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,0],
                    [0,0,2,0,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,0,2,0,0],
                    [0,0,1,0,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,0,1,0,0],
                    [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
                    [0,0,1,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,0,1,0,0],
                    [0,0,1,1,1,1,0,1,1,1,1,0,1,1,1,1,0,1,1,1,1,0,0],
                    [0,0,0,0,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0],
                    [0,0,0,0,0,1,0,1,1,1,1,1,1,1,1,1,0,1,0,0,0,0,0],
                    [0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0],
                    [0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0],
                    [0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0],
                    [0,0,0,0,0,1,0,1,1,1,1,1,1,1,1,1,0,1,0,0,0,0,0],
                    [0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0],
                    [0,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,0],
                    [0,0,1,0,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,0,1,0,0],
                    [0,0,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,0],
                    [0,0,0,2,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,2,0,0,0],
                    [0,0,1,1,1,1,0,1,1,1,1,0,1,1,1,1,0,1,1,1,1,0,0],
                    [0,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,0],
                    [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
        return maparray

    def ghost_array(self):
        #returns an array representing the ghost's path graph
        ghost_array = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                       [0,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,0],
                       [0,0,2,0,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,0,2,0,0],
                       [0,0,1,0,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,0,1,0,0],
                       [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
                       [0,0,1,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,0,1,0,0],
                       [0,0,1,1,1,1,0,1,1,1,1,0,1,1,1,1,0,1,1,1,1,0,0],
                       [0,0,0,0,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0],
                       [0,0,0,0,0,1,0,1,1,1,1,1,1,1,1,1,0,1,0,0,0,0,0],
                       [0,0,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0],
                       [0,0,0,0,0,1,1,1,0,0,3,3,3,3,0,1,1,1,0,0,0,0,0],
                       [0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0],
                       [0,0,0,0,0,1,0,1,1,1,1,1,1,1,1,1,0,1,0,0,0,0,0],
                       [0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0],
                       [0,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,0],
                       [0,0,1,0,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,0,1,0,0],
                       [0,0,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,0],
                       [0,0,0,2,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,2,0,0,0],
                       [0,0,1,1,1,1,0,1,1,1,1,0,1,1,1,1,0,1,1,1,1,0,0],
                       [0,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,0],
                       [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
                       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
        return ghost_array

    def draw_map(self):
        '''
        Draw the game map (the walls that confine pacman/ghosts)
        '''
        tile_dim = 25
        maparray = self.map_array()
        #print walls
        for y in range(0,len(maparray)):
            for x in range(0,len(maparray[y])):
                if maparray[y][x] == 0:
                    self.draw_rect(self.screen,(0,0,255),(25*x,25*y,25,25))
 
 
    def map(self):
        '''
        Creates a graph that the pacman will travel on based on the arrary
        returned by map_array

        Returns (Graph) = the graph that is created
        '''
        edges = list()
        verticies = set()
        tile_dim = 25
        maparray = self.map_array()
        #create graph
        #outer loop for rows
        for y in range(0,len(maparray)):
            #inner loop for columns
            for x in range(0,len(maparray[y])):
                if maparray[y][x] != 0:
                    if maparray[y][x] == 1:
                        #create pellet and add to list
                        pellet = Pellet()
                        pellet.rect.x = 25*x+12
                        pellet.rect.y = 25*y+12
                        self.pellet_list.add(pellet)
                        self.pacman_and_pellets.add(pellet)

                    elif maparray[y][x] == 2:
                        #create power pellet and add to list
                        ppellet = Power_Pellet()
                        ppellet.rect.x = 25*x+12
                        ppellet.rect.y = 25*y+12
                        self.ppellet_list.add(ppellet)
                        self.pacman_and_pellets.add(ppellet)
                    verticies.add((x*tile_dim, y*tile_dim))
                    #check for left neighbour
                    if(x!=0 and maparray[y][x-1] != 0):
                        edges.append(((x*tile_dim, y*tile_dim),
                                      ((x-1)*tile_dim, y*tile_dim)))
                        edges.append((((x-1)*tile_dim, y*tile_dim),
                                      (x*tile_dim, y*tile_dim)))                
                    #check for upper neighbour
                    if(y!=0 and maparray[y-1][x] != 0):
                        edges.append(((x*tile_dim, y*tile_dim),
                                      (x*tile_dim, (y-1)*tile_dim)))
                        edges.append(((x*tile_dim, (y-1)*tile_dim),
                                      (x*tile_dim, y*tile_dim)))
                        
        return Graph(verticies,edges)
                           
                            

    def ghost_map(self):
        '''
        Creates a graph that the ghost will travel on based on the arrary
        returned by ghost_array

        Returns (Graph) = the graph that is created
                ghost_start_locations = list of the ghost start locations
        '''
        edges = list()
        verticies = set()
        ghost_start_locations = list()
        tile_dim = 25
        maparray = self.ghost_array()
        #outer loop for rows
        for y in range(0,len(maparray)):
            #inner loop for columns
            for x in range(0,len(maparray[y])):
                if maparray[y][x] != 0:
                    if maparray[y][x] == 3:
                        #ghost location (repesented by 3) 
                        #added to ghost_start_locations
                        ghost_start_locations.append((x*tile_dim, y*tile_dim))
                    verticies.add((x*tile_dim, y*tile_dim))
                    #check for left neighbour
                    if(x!=0 and maparray[y][x-1] != 0):
                        edges.append(((x*tile_dim, y*tile_dim),
                                      ((x-1)*tile_dim, y*tile_dim)))
                        edges.append((((x-1)*tile_dim, y*tile_dim),
                                      (x*tile_dim, y*tile_dim)))                        
                    #check for upper neighbour
                    if(y!=0 and maparray[y-1][x] != 0):
                        edges.append(((x*tile_dim, y*tile_dim),
                                      (x*tile_dim, (y-1)*tile_dim)))
                        edges.append(((x*tile_dim, (y-1)*tile_dim),
                                      (x*tile_dim, y*tile_dim)))
                        
        return Graph(verticies,edges) , ghost_start_locations

   


    def print_stuff(self, pacguy):
        '''
        Prints the title / pacmans score and lives

        Args : pacguy (pacman) = instance of the pacman class
        '''
        font1 = pygame.font.Font("Assets/pacfont.ttf", 16)
        font2 = pygame.font.Font(None, 30)
        font3 = pygame.font.Font("Assets/pacfont.ttf", 50)
        font3.set_bold(1)
        score1 = font1.render("Score: ", 1, (247,255,0))
        title = font3.render("PACMAN", 1, (247,255,0))
        score2 = font2.render(str(int(pacguy.score)), 1, (247,255,0))
        if pacguy.lives == 1:
            life = font1.render("Lives: 1", 1, (247,255,0))
        elif pacguy.lives == 2:
            life = font1.render("Lives: 11", 1, (247,255,0))
        elif pacguy.lives == 3:
            life = font1.render("Lives: 111", 1, (247,255,0))
        if pacguy.lives != 0:
            self.screen.blit(life, (200,610))
        elif pacguy.lives == 0:
            self.gameover()
        self.screen.blit(title, (135,0))
        self.screen.blit(score1, (0,610))
        self.screen.blit(score2, (80,610))
    
        

