import sys, pygame
BG_COLOR = (32, 32, 32)
BLUE = (0,0,255)
screen_width = 600
screen_height = 600
score_rect =(0,500,600,100)

def initialize():
    # Initialize screen
    pygame.init()
    screen = pygame.display.set_mode((screen_width,screen_height))
    pygame.display.set_caption("Pacman")
    
    #Initialize score
    pygame.draw.rect(screen,BLUE,score_rect)
    #Initialize background 
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))
    clock = pygame.time.Clock()
    argv = sys.argv[1:]
    return screen

def draw_rect(x,y,
