## In this Tutorial , we will learn about creating game loop using which we can update all those things which are continously going on in our game !!
## Like taking actions according to the game arrows used 


import pygame
pygame.init()

#creating a window using setmode

window = pygame.display.set_mode((500 , 500 ))
pygame.display.set_caption("MY FIRST GAME")


# Game specific variables
exit_game = False # which means the game will continue , but the moment exit_game becomes true immediately the control will get exit out
game_over = False 

# Creating a Game Loop 
while not exit_game:
	pass 

##a step to quit the game loop 
   pygame.quit()  
   quit()
