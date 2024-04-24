import pygame
from game_model import Button, OrderStatus, Pizza, PizzaStatus

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


# game loop
run = True
while run:
    screen.blit(homescreen, (0, -100))  # display homescreen img

    if start_button.draw():
        screen.blit(pygame.image.load('assets/img/kitchen.png'), (0, 0)) # display kitchen
        order = OrderStatus() # initialized order
        print(order.order_dict)
        pizza_sprite = Pizza()
        pizza_stat = PizzaStatus()
        print(pizza_stat._current_toppings)
    if exit_button.draw():
        pygame.quit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()
