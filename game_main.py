import pygame
from game_model import Button, OrderStatus, Pizza, PizzaStatus
import time

pygame.init()

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption(
    "Cloudy with a Chance of Pizza"
)  # window display caption

homescreen = pygame.image.load("assets/img/homescreen.png")


# create button instances
start_button = Button(50, 600, "assets/img/StartButton.png", 1, screen)
exit_button = Button(250, 600, "assets/img/ExitButton.png", 1, screen)

button_run = True
while button_run:
    screen.blit(homescreen, (0, -100))  # display homescreen img
    if start_button.draw():
        button_run = False
    if exit_button.draw():
        pygame.quit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            button_run = False

    pygame.display.update()


print(1)

# game loop
game_run = True
while game_run:
    screen.blit(
        pygame.image.load("assets/img/kitchen.png"), (0, 0)
    )  # display kitchen
    order = OrderStatus()  # initialized order
    print(order.order_dict)
    pizza_sprite = Pizza()
    pizza_stat = PizzaStatus()
    print(pizza_stat._current_toppings)
    pygame.display.update()
    time.sleep(1)
pygame.quit()
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        game_run = False
