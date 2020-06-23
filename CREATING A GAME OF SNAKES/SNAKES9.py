import pygame
import random

pygame.init() # Initialising the modules of pygame

# defining colors on the basis of THE RGB VALUES(STANDARD)
white = (255, 255, 255)
red = (255, 0, 0)
black = (0,0,0)
yellow = (255 , 255 , 0)

# CREATING OF THE GAME WINDOW 
screenwidth = 1000
screenheight = 800

gamewindow = pygame.display.set_mode((screenwidth , screenheight))

# CREATING THE GAME TITLE THAT WILL BE DISPLAYED ON THE TITLE BAR OF THE GAME WINDOW
pygame.display.set_caption("HUNGRY SNAKE")
pygame.display.update()


#GAME SPECIFIC VARIABLES
exitgame= False
gameover = False
position_x = 50
position_y = 50
speed_x = 0
speed_y = 0
speed_init = 10
snake_size = 40

#POSITION OF THE APPLE THAT WILL RANDOMLY APPEAR ON THE SCREEN
apple_x = random.randint(0, screenwidth/2)
apple_y = random.randint(0, screenheight/2)
score =0
fps = 50# frames per second which will decide the rate of the game 

clock = pygame.time.Clock() # # Creating an object to help in tracking time
font = pygame.font.SysFont(None, 55)



# A FUNCTION FOR DEFINING THE TEXT SCREEN
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gamewindow.blit(screen_text, [x,y])


def plot_snake(gamewindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gamewindow,color, [x,y,snake_size, snake_size])

snk_list =[]
snk_length = 1



#CREATING THE GAME LOOP
while not exitgame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exitgame = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                speed_x = speed_init
                speed_y = 0

            if event.key ==pygame.K_LEFT:
                speed_x = -speed_init
                speed_y = 0

            if event.key == pygame.K_UP:
                speed_y = - speed_init
                speed_x = 0

            if event.key == pygame.K_DOWN:
                speed_y = speed_init
                speed_x =0

        position_y = position_y+ speed_y
        position_x = position_x + speed_x

        if abs( position_x- apple_x)<20 and abs(position_y -apple_y)<20:
            score+=10
         #   print("Score: ", score)

            apple_x = random.randint(0, screenwidth/2)
            apple_y = random.randint(0, screenheight/2)
            snk_length+=5



        gamewindow.fill(yellow)
        text_screen("Score: " +str(score) , red, 5, 5)

        pygame.draw.rect(gamewindow, red, [apple_x, apple_y , snake_size, snake_size])
       
        head = []
        head.append(position_x)
        head.append(position_y)
        snk_list.append(head)


        if len(snk_list)>snk_length:
            del snk_list[0]





        #pygame.draw.rect(gamewindow, black, [position_x, position_y, snake_size, snake_size])
        plot_snake(gamewindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)


pygame.quit()
quit()



