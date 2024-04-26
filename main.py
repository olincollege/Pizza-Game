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

# clock = pygame.time.Clock()
# running = True

def menu():
    """
    A function to display home screen and menu.
    """
    start_button = gmo.Button(50, 600, "assets/img/StartButton.png", 1, SCREEN)
    exit_button_1 = gmo.Button(250, 600, "assets/img/ExitButton.png", 1, SCREEN)

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        gv.HomeScreen(SCREEN)
        if start_button.draw():
            running = False
        if exit_button_1.draw():
            pygame.quit()

        pygame.display.update()
        clock.tick(60)  # limits FPS to 60

def play():
    """
    A function to display Play window.
    """
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        gv.Kitchen(SCREEN)

        pygame.display.flip()
        clock.tick(60)  # limits FPS to 60

menu()
play()





# while running:
#     # poll for events
#     # pygame.QUIT event means the user clicked X to close your window
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # fill the screen with a color to wipe away anything from last frame
#     screen.fill((0,0,0))

#     # RENDER YOUR GAME HERE
#     gv.HomeScreen(screen)

#     # flip() the display to put your work on screen
#     pygame.display.flip()

#     clock.tick(60)  # limits FPS to 60

# pygame.quit()