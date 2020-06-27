import pygame
import random


# for loading and initialising the music modules
pygame.mixer.init()
pygame.mixer.music.load('song.mp3')  # for loading the song already present in that folder
pygame.mixer.music.play() # for playing the song mentioned in that folder

pygame.init()  # Initialising the modules of pygame

# defining colors on the basis of THE RGB VALUES(STANDARD)
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
# CREATING OF THE GAME WINDOW
screenwidth = 1000
screenheight = 800

gamewindow = pygame.display.set_mode((screenwidth, screenheight))

# CREATING THE GAME TITLE THAT WILL BE DISPLAYED ON THE TITLE BAR OF THE GAME WINDOW
pygame.display.set_caption("HUNGRY SNAKE")
pygame.display.update()

clock = pygame.time.Clock()  # # Creating an object to help in tracking time
font = pygame.font.SysFont(None, 55)


# A FUNCTION FOR DEFINING THE TEXT SCREEN
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gamewindow.blit(screen_text, [x, y])


def plot_snake(gamewindow, color, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.rect(gamewindow, color, [x, y, snake_size, snake_size])


snk_list = []
snk_length = 1

def welcome():
    exit_game = False
    while not exit_game:
        gamewindow.fill((233,210,229))
        text_screen("Welcome to Snakes", black, 260, 250)
        text_screen("Press Space Bar To Play", black, 232, 290)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('back.mp3')
                    pygame.mixer.music.play()
                    gameloop()

        pygame.display.update()
        clock.tick(60)

# CREATING THE GAME LOOP


def gameloop():

   # welcomebro
    # Game specific variables
    exitgame = False
    gameover = False
    position_x = 45
    position_y = 55
    speed_x = 0
    speed_y = 0
    snk_list = []
    snk_length = 1

    apple_x = random.randint(20, screenwidth / 2)
    apple_y = random.randint(20, screenheight / 2)
    score = 0
    initialspeed = 5
    snake_size = 30
    fps = 60

    #gameloop real time!!
    while not exitgame:

        if gameover:
            gamewindow.fill(yellow)
            text_screen("Game Over!!! Press Enter To Continue and Press Enter and then close button to QUIT", blue, 100, 250)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exitgame = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        speed_x = initialspeed
                        speed_y = 0

                    if event.key == pygame.K_LEFT:
                        speed_x = - initialspeed
                        speed_y = 0

                    if event.key == pygame.K_UP:
                        speed_y = - initialspeed
                        speed_x = 0

                    if event.key == pygame.K_DOWN:
                        speed_y = initialspeed
                        speed_x = 0

            position_x = position_x + speed_x
            position_y = position_y + speed_y

            if abs(position_x - apple_x)<20 and abs(position_y - apple_y)<20:
                score +=10
                apple_x = random.randint(20, screenwidth / 2)
                apple_y = random.randint(20, screenheight / 2)
                snk_length +=5

            gamewindow.fill(yellow)
            text_screen("Score: " + str(score), blue, 5, 5)
            pygame.draw.rect(gamewindow, red, [apple_x, apple_y, snake_size, snake_size])


            head = []
            head.append(position_x)
            head.append(position_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                gameover = True
                pygame.mixer.music.load('over.mp3')
                pygame.mixer.music.play()


            if position_x<0 or position_x>screenwidth or position_y<0 or position_y>screenheight:
                gameover = True
                pygame.mixer.music.load('over.mp3')
                pygame.mixer.music.play()



            plot_snake(gamewindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()

