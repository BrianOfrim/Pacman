import sys, pygame, gui
from gui import GUI
from ghost import ghost
screen_width = 575
screen_height = 650

import process_path
if __name__ == "__main__" :
    pygame.init()
    clock = pygame.time.Clock()
    argv = sys.argv[1:]
    main_gui = GUI(screen_height, screen_width)
    pacguy = main_gui.print_pacman()
    ghost1 = ghost(9*25,3*25)
    main_gui.ghost_list.add(ghost1)
    temp_map = main_gui.map()
    pacguy.map = temp_map
    ghost1.map = temp_map

    edge_list = pacguy.map.edges()
    #for edge in edge_list:
    #    print(edge)
    
    pacguy.current_node = process_path.closest_node(pacguy.rect.x,
                                                    pacguy.rect.y,pacguy.map)
    # sync graph with Pacman
    pacguy.rect.x = pacguy.current_node[0]
    pacguy.rect.y = pacguy.current_node[1]
    pacguy.next_node = process_path.next_node(pacguy.current_node,
                                                       pacguy.map,
                                                       pacguy.angle) 
    
    while 1:
        pacguy.move()
        ghost1.move(pacguy.current_node[0],pacguy.current_node[1])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if ((event.key == pygame.K_RIGHT) or 
                    (event.key == pygame.K_LEFT) or
                    (event.key == pygame.K_UP) or (event.key == pygame.K_DOWN)):
                    pacguy.MoveKeyDown(event.key)
        main_gui.ghost_list.add(ghost1)
        pellet_hit_list = pygame.sprite.spritecollide(pacguy,
                                                      main_gui.pellet_list, 
                                                      False)
        ppellet_hit_list = pygame.sprite.spritecollide(pacguy,
                                                      main_gui.ppellet_list,
                                                      False)

        ghost_hit_list = pygame.sprite.spritecollide(pacguy,
                                                      main_gui.ghost_list,
                                                      False)
              
        for ghost in ghost_hit_list:
            pacguy.lives -=1
            pacguy.kill()
            if pacguy.lives != 0:
                main_gui.draw_background()
                main_gui.draw_map()
                main_gui.pacman.draw(main_gui.screen)

        main_gui.ghost_list.draw(main_gui.screen)
        for pellet in pellet_hit_list:
            pacguy.score += 100
            pellet.kill()
        for ppellet in ppellet_hit_list:
            pacguy.power = 1
            ppellet.kill()
        main_gui.draw_background()
        main_gui.draw_map()
        main_gui.pacman_and_pellets.draw(main_gui.screen)

        main_gui.ghost_list.draw(main_gui.screen)

        main_gui.print_stuff(pacguy)

        pygame.display.update()  
        clock.tick(25)
