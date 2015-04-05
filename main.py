import sys, pygame, gui
from gui import GUI
screen_width = 600
screen_height = 600
import process_path
if __name__ == "__main__" :
    pygame.init()
    clock = pygame.time.Clock()
    argv = sys.argv[1:]
    main_gui = GUI(screen_height, screen_width)
    graph_tuple = main_gui.map()
    path_graph = graph_tuple[0]
    pac_dot_status = graph_tuple[1]
    pacguy = main_gui.print_pacman()
    pacguy.map = path_graph
    edge_list = path_graph.edges()
    for edge in edge_list:
        print(edge)
    
    pacguy.current_node = process_path.closest_node(pacguy.rect.x,
                                                    pacguy.rect.y,path_graph)
    pacguy.next_node = process_path.next_node(pacguy.current_node,
                                                       pacguy.map,
                                                       pacguy.angle) 

    while 1:
        pacguy.move()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if ((event.key == pygame.K_RIGHT) or 
                    (event.key == pygame.K_LEFT) or
                    (event.key == pygame.K_UP) or (event.key == pygame.K_DOWN)):
                    pacguy.MoveKeyDown(event.key)
                   
        pellet_hit_list = pygame.sprite.spritecollide(pacguy,
                                                      main_gui.pellet_list, 
                                                      False)
        for pellet in pellet_hit_list:
            pacguy.score += 100
            print(pacguy.score)
            pellet.kill()
        main_gui.draw_background()
        main_gui.map()
        main_gui.pacman_and_pellets.draw(main_gui.screen)
        pygame.display.update()  
        clock.tick(10)
