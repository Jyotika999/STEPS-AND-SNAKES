import pygame
x = pygame.init()  ## this will initialise all the modules in the pygame

## print(x) # incase you want to ckeck if all the modules are sunning well

window = pygame.display.set_mode((500, 500 )) ## this is basically for creating the game window which takes parameters as width and height
 ## incase of displaying the window over which the game will get displayed
pygame.display.set_caption("My First Game")# for setting up the caption of the window






##Game Specific Variables
exit_game = False ## for ending the game
game_over = False ## this will become true when the game actually gets over
