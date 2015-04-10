                               Pacman
====================================================================
                   By: Brian Ofrim & Adam Sanche
====================================================================
================================================.       
     .-.   .-.     .--.                         |       
    | OO| | OO|   / _.-' .-.   .-.  .-.   .''.  |       
    |   | |   |   \\ '-. '-'   '-'  '-'   '..'  |       
    '^^^' '^^^'    '--'                         |       
===============.  .-.  .================.  .-.  |       
               | |   | |                |  '-'  |       
               | |   | |                |       |       
               | ':-:' |                |  .-.  |       
               |  '-'  |                |  '-'  |       
==============='       '================'       | 
Ascii Art via: http://www.asciiartfarts.com/pac-man.html\   
----------------------------------------------------------------------
Game Description:
     The game is a recreation of the classic arcade game, pacman 
     originaly developed by Namco. The game is controled with the 
     arrow keys on the keyboard. The path that the pacman and ghosts
     travel on is a graph that is created from a two dimensional
     arrary loacted in the gui file. It will be helpfull to note 
     that the nodes in the graph are spaced 25 pixels apart 
     but the pacman and ghosts only travel 5 pixels at a time
     from the a current node to a next node. The pacman will move by itself
     in its current dirction unless a wall encountered, a 180 turn is made,
     or a key is pressed when the pacman is close to an intersection
     to make a 90 degree turn. Enjoy!
-----------------------------------------------------------------------
File Description:
     binary_heap.py: -binary heap file from eclass

     ghost.py: -contains the base class for the ghosts
     	       -follows a closest path algorithm to try to kill pacman in normal
	        mode
	       -if in scared mode then random desicions will be made at 
	        intersections

     ghost2.py: -contains the class clyde which is an non-intelligent ghost
     		-will make random decisions at intersections whether it is in
		 normal mode or scared mode

     graph_v2.py: - graph class from eclass

     gui.py: -The graphic user interface handels the drawing of the map
     	      and the creation of the graph that the pacman and ghosts 
	      travel on,printing the title card, gameover screen, win 
	      screen, pacman's score,pacman's lives etc.

     main.py: contains the main game loop

     pellet.py: contains the classes for pellets and power pellets

     process_path.py :contains graph related helper functions used by
                      both pacman and the ghosts

     unit.py : contains the pacman class, inccluding its movement handeling
               and user input processing

-------------------------------------------------------------------------------
sources:

pac man images : https://svn.cc.jyu.fi/srv/svn/ohj1s12/pelit/mavavilj/trunk/Pacman/Pacman/PacmanContent/

graph_v2.py, binary_heap.py : Eclass

various help with learning pygame : http://programarcadegames.com/index.php?lang=en (pygame tutorial)

pygame documentation : http://www.pygame.org/docs/
------------------------------------------------------------------------------
Known Bugs:

Sometimes a ghost will fail to respawn




