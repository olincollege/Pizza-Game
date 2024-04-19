import pygame
from game_model import Button

pygame.init()

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption(
    "Cloudy with a Chance of Pizza"
)  # window display caption

homescreen = pygame.image.load("assets/img/homescreen.png")


# load button images
start_img = pygame.image.load("assets/img/StartButton.png").convert_alpha()
exit_img = pygame.image.load("assets/img/ExitButton.png").convert_alpha()


# create button instances
start_button = Button(50, 600, start_img, 1, screen)
exit_button = Button(250, 600, exit_img, 1, screen)


# game loop
run = True
while run:

    if start_button.draw():
        screen.blit(homescreen, (0, -100))  # display homescreen img
    if exit_button.draw():
        pygame.quit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
