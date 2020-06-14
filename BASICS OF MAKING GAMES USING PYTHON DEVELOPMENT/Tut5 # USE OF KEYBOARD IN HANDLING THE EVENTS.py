## In this tutorial , we will learn about handling the events and the use of arrows in controlling these stuffs


import pygame
pygame.init()

# Creating window
gameWindow = pygame.display.set_mode((1200, 500))
pygame.display.set_caption("My First Game - Blank")

# Game specific variables
exit_game = False
game_over = False

# Creating a game loop
while not exit_game:
    for event in pygame.event.get():
    	if event.type == pygame.QUIT:
    		exit_game = TRUE


  ## which indicates if a key is pressed
    	if event.type == pygame.KEYDOWN:
    		if event.key == pygame.K_RIGHT:
    			print("YOU HAVE PRESSED A RIGHT ARROW KEY")

    	

pygame.quit()
quit()

