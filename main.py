import pygame
import game_model as gmo
import game_view as gv
import game_controller as gc
import time

pygame.init()

# set up screen display
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 800
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# window display caption
pygame.display.set_caption("Cloudy with a Chance of Pizza")


# scene functions
def menu(screen):
    """
    A function to display home screen and menu.

    Args:
        screen: a Surface to display on.
    """
    # initialize buttons
    start_button = gmo.Button(50, 600, "assets/img/StartButton.png", 1, screen)
    exit_button_1 = gmo.Button(250, 600, "assets/img/ExitButton.png", 1, screen)

    # start loop
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # display home screen and buttons.
        gv.HomeScreen(screen)
        # checking for button clicks
        if start_button.draw():  # start, exit menu, start game
            running = False
        if exit_button_1.draw():  # exit, exit
            pygame.quit()

        pygame.display.update()
        clock.tick(60)  # limits FPS to 60


def play(screen):
    """
    A function to display Play window.

    Args:
        screen: a Surface to display on.
    """
    order_instance = gmo.OrderStatus(4)  # initialize first order
    pizza = gmo.PizzaStatus()  # initialize empty pizza
    gv.Pizza(screen)  # display pizza

    topping_view = gv.Toppings()  # initialize list of toppings
    topping_database = gmo.ToppingPosition()  # initialize topping info

    topping_interval = 25

    # start loop
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # set up
        gv.Kitchen(screen)  # display Kitchen scene

        # run orders
        gv.Order(screen, order_instance)  # display Order
        current_pizza = pizza.get_pizza_status()  # get status on current pizza
        # check if pizza order is completed
        if gmo.OrderStatus.check_order(order_instance, current_pizza) is True:
            order_instance = gmo.OrderStatus(4)  # initialize new order

        # move pizza
        arrow = gc.Arrow()  # initialize class for arrow inputs
        arrow.move_pizza(pizza)  # check for user arrow inputs
        gv.Pizza.update(pizza, screen)  # update pizza position on display

        # toppings
        if topping_interval == 25:  # attempt to generate toppings at slower rate
            topping_view.create_topping(
                screen, topping_database
            )  # create and display toppings
            topping_view.move_toppings_view()
            topping_interval = 0
        else:
            topping_view.move_toppings_view()
            topping_interval += 1

        pygame.display.flip()
        clock.tick(60)  # limits FPS to 60


menu(SCREEN)
play(SCREEN)
