import sys, pygame, gui
from gui import GUI
screen_width = 600
screen_height = 600

if __name__ == "__main__" :
    pygame.init()
    clock = pygame.time.Clock()
    argv = sys.argv[1:]
    main_gui = GUI(screen_height, screen_width)
    graph_tuple = main_gui.map()
    path_graph = graph_tuple[0]
    pac_dot_status = graph_tuple[1]
    pacguy = main_gui.print_pacman()
    
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                if ((event.key == pygame.K_RIGHT) or (event.key == pygame.K_LEFT) or
                    (event.key == pygame.K_UP) or (event.key == pygame.K_DOWN)):
                    pacguy.MoveKeyDown(event.key)
        pacguy.move()
        pellet_hit_list = pygame.sprite.spritecollide(pacguy, main_gui.pellet_list, False)
        
        for pellet in pellet_hit_list:
            pacguy.score += 100
            print(pacguy.score)
            
            pellet.kill()
        
                    
        main_gui.draw_background()
        main_gui.map()
        main_gui.pacman_and_pellets.draw(main_gui.screen)
      
        pygame.display.update()  
        clock.tick(60)
