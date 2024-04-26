import pygame
import game_model as gmo
import game_view as gv
import time

pygame.init()

# set up screen display
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 800
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(
    "Cloudy with a Chance of Pizza"
)  # window display caption

clock = pygame.time.Clock()
running = True

def menu(screen):
    """
    A function to display home screen and menu.
    """
    start_button = gmo.Button(50, 600, "assets/img/StartButton.png", 1, screen)
    exit_button_1 = gmo.Button(250, 600, "assets/img/ExitButton.png", 1, screen)

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        gv.HomeScreen(screen)
        if start_button.draw():
            running = False
        if exit_button_1.draw():
            pygame.quit()

        pygame.display.update()
        clock.tick(60)  # limits FPS to 60

def play(screen):
    """
    A function to display Play window.
    """
    clock = pygame.time.Clock()
    running = True

    order_instance = gmo.OrderStatus()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # set up
        gv.Kitchen(screen)
        gv.Pizza(screen)

        # run orders
        gv.Order(screen, order_instance)

        pygame.display.flip()
        clock.tick(60)  # limits FPS to 60

menu(SCREEN)
play(SCREEN)


# while running:
#     # poll for events
#     # pygame.QUIT event means the user clicked X to close your window
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # RENDER YOUR GAME HERE
#     gv.Kitchen(SCREEN)

#     # flip() the display to put your work on screen
#     pygame.display.flip()

#     clock.tick(60)  # limits FPS to 60

# pygame.quit()
