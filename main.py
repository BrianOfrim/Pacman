import sys, pygame, gui
import pdb
from gui import GUI
from ghost import ghost
from ghost2 import clyde
from unit import pacman
screen_width = 575
screen_height = 650
game_modes = ("normal", "ghosts_scared", "reset")
import process_path
if __name__ == "__main__" :
    pygame.init()
    pygame.mixer.init()
    clock = pygame.time.Clock()
    argv = sys.argv[1:]
    main_gui = GUI(screen_height, screen_width) 
    #rect = pacman.get_rect()
    #self.screen.blit(pacman,[50,50])
    #pygame.display.update((50,50,25,25))

    while main_gui.start == 0:
        main_gui.draw_titlecard()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    main_gui.start = 1
        
    


    temp_map = main_gui.map()
    pacguy = pacman(11*25 ,18*25,temp_map)
    main_gui.pacman_and_pellets.add(pacguy)
    #tuple containing the ghost map and starting locations
    ghost_tuple = main_gui.ghost_map()
    ghost_map = ghost_tuple[0]
    #list containing ghost start locations
    ghost_start = ghost_tuple[1]
    pacguy.map = temp_map
    #ghost1 initialize
    ghost1 = ghost(ghost_start[0][0],ghost_start[0][1]
                   ,ghost_map)
    main_gui.ghost_list.add(ghost1)
    #ghost2 initialize
    ghost2 = clyde(ghost_start[1][0],ghost_start[1][1]
                   ,ghost_map)
    main_gui.ghost_list.add(ghost2)
    #ghost3 initialize
    ghost3 = clyde(ghost_start[2][0],ghost_start[2][1]
                   ,ghost_map)
    main_gui.ghost_list.add(ghost3)
    #ghost4 initialize
    ghost4 = ghost(ghost_start[3][0],ghost_start[3][1]
                   ,ghost_map)
    main_gui.ghost_list.add(ghost4)

    edge_list = pacguy.map.edges()
    #for edge in edge_list:
    #    print(edge)
    
    
    while 1:
        program_runtime = pygame.time.get_ticks()
        if(pacguy.alive()):
            pacguy.move()
        else:
            pacguy.respawn()
            ghost1.respawn()
            ghost2.respawn()
            ghost3.respawn()
            ghost4.respawn()
            main_gui.pacman_and_pellets.add(pacguy)
            pygame.time.delay(1000)

        if(ghost1.alive()):
            ghost1.move(pacguy.current_node[0],pacguy.current_node[1])
        else:
            if ghost1.derp == 0:
                clock2 = int(pygame.time.get_ticks())
                ghost1.derp = 1
            if program_runtime >= (clock2 + 10000):
                ghost1.respawn()
                main_gui.ghost_list.add(ghost1)
                ghost1.derp = 0

        if(ghost4.alive()):
            ghost4.move(pacguy.current_node[0],pacguy.current_node[1])
        else:
            if ghost1.derp == 0:
                clock3 = int(pygame.time.get_ticks())
                ghost4.derp = 1
            if program_runtime >= (clock3 + 2500):
                ghost4.respawn()
                main_gui.ghost_list.add(ghost4)
                ghost4.derp = 0

        if(ghost2.alive()):
            ghost2.move()
        else:
            if ghost2.derp == 0:
                clock4 = int(pygame.time.get_ticks())
                ghost2.derp = 1
            if program_runtime >= (clock4 + 2500):
                ghost2.respawn()
                main_gui.ghost_list.add(ghost2)
                ghost2.derp = 0

        if(ghost3.alive()):
            ghost3.move()
        else:
            if ghost3.derp == 0:
                clock5 = int(pygame.time.get_ticks())
                ghost3.derp = 1
            if program_runtime >= (clock5 + 2500):
                ghost3.respawn()
                main_gui.ghost_list.add(ghost3)
                ghost3.derp = 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit()
            elif event.type  == pygame.KEYDOWN:
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
            if ghost.imgnum == 1:
                if pacguy.lives != 0:
                    pacguy.die()
                #ghost.kill()
                pacguy.kill()
                #pacguy.start() 
            elif ghost.imgnum == 2:
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
            #print(clock1)
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
        if pacguy.lives == 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()
            
