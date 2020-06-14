# This is a snake game created with pygame created by Jyotika 
#This section comes under the creation of the canvas and coloring it for the snakes
import pygame

pygame.init()

#defining colors which are just the RGB VALUES
white = (255, 255, 255)
red = (255, 0 , 0)
black = (0, 0, 0)
blue = (0, 0, 255)



#Creating a window
screen_width = 800
screen_height = 500

#Creating game window 
gamewindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption(" BEWARE OF SNAKES")
pygame.display.update()


# game specific variables

exit_game = False
game_over = False

# Game Loop
while not exit_game:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit_game = True


	gamewindow.fill(blue)
	pygame.display.update()

pygame.quit()
quit()