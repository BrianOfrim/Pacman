import sys, pygame, gui
from gui import GUI
screen_width = 600
screen_height = 600

if __name__ == "__main__" :
    pygame.init()
    clock = pygame.time.Clock()
    argv = sys.argv[1:]
    main_gui = GUI(screen_height, screen_width)
    #pygame.draw.circle(screen,BLUE,(100,100),50,0 )
    main_gui.map()
    
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit()
        pygame.display.update()  
