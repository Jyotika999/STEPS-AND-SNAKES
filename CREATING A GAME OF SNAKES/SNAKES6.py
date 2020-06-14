# This is a snake game created with pygame created by Jyotika 
#This section comes under the giving the speed to the snake in x and y directions
# but in this section we have learnt about giving speed to the sanke in x and y direction both which will give the resultanat in the diagonwise speed , hence the snake will not be able to move under 
import pygame
pygame.init()

#defining colors which are just the RGB VALUES
white = (255, 255, 255)
red = (255, 0 , 0)
black = (0, 0, 0)
blue = (0, 0, 255)
yellow = (255, 255 , 0)


#Creating a window
screen_width = 800
screen_height = 500

#Creating game window 
gamewindow = pygame.display.set_mode((screen_width, screen_height))

#creating a game title
pygame.display.set_caption(" BEWARE OF SNAKES")
pygame.display.update()


# game specific variables

exit_game = False
game_over = False
position_x = 40
position_y = 50
snake_size = 15
speed_x = 10
speed_y = 10
fps = 30

clock = pygame.time.Clock()

# Game Loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                speed_x = 10
                speed_y = 0

            if event.key == pygame.K_LEFT:
                speed_x = -10
                speed_y = 0
               


            if event.key == pygame.K_UP:
                speed_y = -10
                speed_x = 0


            if event.key == pygame.K_DOWN:
                speed_y = 10
                speed_x = 0

            position_x = position_x + speed_x
            position_y = position_y + speed_y


    gamewindow.fill(blue)
    pygame.draw.rect(gamewindow, yellow, [position_x , position_y , snake_size , snake_size])
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()