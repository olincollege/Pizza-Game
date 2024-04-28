import pygame
import game_model as gmo
import game_view as gv
import time

pygame.init()

ORDERS = 1
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 800

topping_view = gv.Toppings()
topping_database = gmo.ToppingPosition()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption(
    "Cloudy with a Chance of Pizza"
)  # window display caption

homescreen = pygame.image.load("assets/img/homescreen.png")


# create button instances
start_button = gmo.Button(50, 600, "assets/img/StartButton.png", 1, screen)
exit_button_1 = gmo.Button(250, 600, "assets/img/ExitButton.png", 1, screen)

button_run = True
while button_run:
    screen.blit(homescreen, (0, -100))  # display homescreen img
    if start_button.draw():
        button_run = False
    if exit_button_1.draw():
        pygame.quit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            button_run = False

    pygame.display.update()


print(1)
# create exit button instance
exit_button_2 = gmo.Button(400, 0, "assets/img/ExitButton.png", 0.5, screen)

# game loop
for i in range(ORDERS):
    game_run = True
    while game_run:
        screen.blit(
            pygame.image.load("assets/img/kitchen.png"), (0, 0)
        )  # display kitchen
        order = gmo.OrderStatus(4)  # initialized order
        print(order.order_dict)
        pizza_sprite = gmo.Pizza()
        pizza_stat = gmo.PizzaStatus()
        happiness = gmo.CustomerHappiness()
        print(
            happiness.evaluate_order(
                order.order_dict, pizza_stat._current_toppings
            )
        )

        print(pizza_stat._current_toppings)
        topping_view.create_topping(screen, topping_database)
        topping_view.move_toppings_view()

        if exit_button_2.draw():
            pygame.quit()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_run = False
        pygame.display.update()
        time.sleep(1)
