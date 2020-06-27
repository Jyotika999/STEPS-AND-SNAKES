#In this tutorial , we will continue with sankes game development with the incresing length of snake logic

import pygame
import random

pygame.init()

##defining colors 
white = (255, 255, 255)
red = (255, 0, 0)
black = (0,0,0)
yellow = (255 , 255 , 0)
blue = (0,0,255)


# Creation of game window
screen_height = 500
screen_width = 800
gamewindow = pygame.display.set_mode((screen_width,screen_height))


#Title of the game
pygame.display.set_caption("HUNGRY SNAKES")
pygame.display.update()

#game specific variables
exitgame = False
gameover = False
position_x = 50
position_y = 50
speed_x = 0
speed_y = 0
apple_x = random.randint(20,screen_width/2)
apple_y = random.randint(20,screen_height/2)
score= 0
initialspeed= 5
snake_size = 25
fps= 65


#clock 
clock = pygame.time.Clock()
fontsize = pygame.font.SysFont(None, 50) # pygame module for loading and rendering of fonts

#function creation for the text screen to set up
def text_screen(text,color,x,y):  ## function for displaying text in a pygame 
	screen_text = font.render(text,True,color)
	gamewindow.blit(screen_text, [x,y])  

def drawsnake(gamewindow,color, snk_list, snake_size):
	for x,y in snk_list:
		pygame.draw.rect(gamwindow,color, [x,y,snake_size,snake_size])


snk_list = []  # creating empty list
lengthsnake = 1

# GRAND GAME LOOP

while not exit_game:


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit_game = True


			# IN CASE RIGHT KEY IS PRESSED
			if event.key == pygame.K_RIGHT: 
				speed_x = initialspeed
				speed_y = 0

			# IN CASE LEFT KEY IS PRESSED
			if event.key == pygame.K_LEFT:
				speed_x = - initialspeed
				speed_y = 0


		   # IN CASE UPWARD KEY IS PRESSED
			if event.key == pygame.K_UP:
				speed_y = -initialspeed
				speed_x = 0

		   #IN CASE DOWNWARD KEY IS PRESSED
			if event.key == pyagme.K_DOWN:
				speed_y = initialspeed
				speed_x = 0



		snake_x = snake_x + speed_x
		snake_y = snake_y + speed_y


   # TO MAKE THE SNAKE EAT FOOD, LET THE FOOD DISAPPEAR AND THEN CREATE A RANDOM FOOD ITEM
		if abs(position_x - apple_x)<20 and abs(position_y - apple_y)<20:
			score + = 10
			apple_x = random.randint(20,screen_width/2)
			apple_y = random.randint(20,screen_height/2)
			lengthsnake += 5


		# filling the game window and writing the text on the game screen window
		gamewindow.fill(yellow)
		text_screen("SCORE :  " +str(score), blue, 5, 5)
		pygame.draw.rect(gamwindow, red, [apple_x, apple_y,snake_size, snake_size ])


		head = []
		head.append(position_x)
		head.append(position_y)
		snk.list.append(head)


		if len(snk_list)>lengthsnake:
			del snk_list[0]


		# to draw the snake
		drawsnake(gamwindow, black, snk_list, snake_size)
		pygame.display.update()
		clock.tick(fps)



  pygame.quit()
  quit()




			


