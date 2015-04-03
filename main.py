import sys, pygame, gui





if __name__ == "__main__" :
    screen = gui.initialize()
    #pygame.draw.circle(screen,BLUE,(100,100),50,0 )
    
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()  
