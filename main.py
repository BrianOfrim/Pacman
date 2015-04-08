import sys, pygame, gui
import pdb
from gui import GUI
from ghost import ghost
from ghost2 import clyde
screen_width = 575
screen_height = 650
game_modes = ("normal", "ghosts_scared", "reset")
import process_path
if __name__ == "__main__" :
    pygame.init()
    clock = pygame.time.Clock()
    argv = sys.argv[1:]
    main_gui = GUI(screen_height, screen_width)
    pacguy = main_gui.print_pacman()
    temp_map = main_gui.map()
    pacguy.map = temp_map
    #ghost1 initialize
    ghost1 = ghost(9*25,3*25,temp_map)
    main_gui.ghost_list.add(ghost1)
    #ghost2 initialize
    ghost2 = clyde(15*25,3*25,temp_map)
    main_gui.ghost_list.add(ghost2)
    #ghost3 initialize
    ghost3 = clyde(12*25,3*25,temp_map)
    main_gui.ghost_list.add(ghost3)
    #ghost4 initialize
    ghost4 = ghost(14*25,3*25,temp_map)
    main_gui.ghost_list.add(ghost4)

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
        program_runtime = pygame.time.get_ticks()
        if(pacguy.alive()):
            pacguy.move()
        if(ghost1.alive()):
            ghost1.move(pacguy.current_node[0],pacguy.current_node[1])
        if(ghost4.alive()):
            ghost4.move(pacguy.current_node[0],pacguy.current_node[1])
        if(ghost2.alive()):
            ghost2.move()
        if(ghost3.alive()):
            ghost3.move()
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
        ppellet_hit_list = pygame.sprite.spritecollide(pacguy,
                                                      main_gui.ppellet_list,
                                                      False)
        ghost_hit_list = pygame.sprite.spritecollide(pacguy,
                                                      main_gui.ghost_list,
                                                      False)
        for ghost in ghost_hit_list:
            #pdb.set_trace()
            if pacguy.power == 0:
                pacguy.die()
                ghost.kill()
                pacguy.kill()
                pacguy.start() 
            elif pacguy.power == 1:
                ghost.kill()
                pacguy.score += 500
                #ghost1 = ghost(9*25,3*25,temp_map)      
           
        main_gui.ghost_list.draw(main_gui.screen)
        for pellet in pellet_hit_list:
            pacguy.score += 100
            pellet.kill()

        for ppellet in ppellet_hit_list:
            if pacguy.power == 1:
                clock1 = int(pygame.time.get_ticks())
            pacguy.power = 1
            ppellet.kill()
            ghost1.image = ghost1.image2
            ghost1.image.set_colorkey((255,255,255))
            ghost1.imgnum = 2
            ghost1.newimgrot()
            ghost2.image = ghost2.image2
            ghost2.image.set_colorkey((255,255,255))
            ghost2.imgnum = 2
            ghost2.newimgrot()
            ghost3.image = ghost3.image2
            ghost3.image.set_colorkey((255,255,255))
            ghost3.imgnum = 2
            ghost3.newimgrot()
            ghost4.image = ghost4.image2
            ghost4.image.set_colorkey((255,255,255))
            ghost4.imgnum = 2
            ghost4.newimgrot()
        if pacguy.power == 1:
            if pacguy.power == 1 and pacguy.derp == 0:
                clock1 = int(pygame.time.get_ticks())
                pacguy.derp +=1
            print(clock1)
            if program_runtime >= (clock1 + 10000):
                pacguy.power = 0
                pacguy.derp = 0
                ghost1.image = ghost1.image1
                ghost1.imgnum = 1
                ghost1.newimgrot()
                ghost2.image = ghost2.image1
                ghost2.imgnum = 1
                ghost2.newimgrot()
                ghost3.image = ghost3.image1
                ghost3.imgnum = 1
                ghost3.newimgrot()
                ghost4.image = ghost4.image1
                ghost4.imgnum = 1
                ghost4.newimgrot()


        main_gui.draw_background()
        main_gui.draw_map()
        main_gui.pacman_and_pellets.draw(main_gui.screen)
        main_gui.ghost_list.draw(main_gui.screen)
        main_gui.print_stuff(pacguy)
        pygame.display.update()  
        clock.tick(25)
