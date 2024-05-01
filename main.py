"""
Functions and calls to run game.
"""

import pygame
import game_model as gmo
import game_view as gv
import game_controller as gc

pygame.init()

# set up screen display
SCREEN_WIDTH = gmo.SCREEN_WIDTH
SCREEN_HEIGHT = gmo.SCREEN_HEIGHT
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
    start_button = gmo.Button(70, 600, "assets/img/play_button.png", 1)
    exit_button = gmo.Button(260, 600, "assets/img/exit_button.png", 1)
    button_control = gc.ButtonControl()
    button_display = gv.ButtonDisplay(screen)
    # start loop
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # display home screen and buttons.
        gv.HomeScreen(screen)
        button_display.display_button(start_button)
        button_display.display_button(exit_button)

        # checking for button clicks
        if button_control.check_press(
            start_button
        ):  # start, exit menu, start game
            running = False
        if button_control.check_press(exit_button):  # exit, exit
            pygame.quit()

        pygame.display.update()
        clock.tick(60)  # limits FPS to 60


def play(screen):
    """
    A function to display Play window.

    Args:
        screen: a Surface to display on.

    Returns:
        total_money: a float representing the total amount of money earned.
    """
    toppings = 4  # the maximum amount of individual topping order could have.
    order_instance = gmo.OrderStatus(toppings)  # initialize first order
    order = gv.Order(screen, order_instance)
    pizza_status = gmo.PizzaStatus()  # initialize empty pizza
    pizza_view = gv.Pizza(screen)  # display pizza

    topping_view = gv.Toppings()  # initialize list of toppings
    toppings_group = pygame.sprite.Group()

    money = gmo.Money()  # initialize customer money

    topping_interval = 25  # every 25 frames add generate new topping

    orders_complete = 1  # number of orders to end game

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
        # gv.Order(screen, order_instance)  # display Order
        current_pizza = pizza_status.status  # get status on current pizza
        # check if pizza order is completed
        if gmo.OrderStatus.check_order(order_instance, current_pizza) is True:
            money.update_money(order_instance, pizza_status)
            pizza_status.clear_pizza()
            pizza_view.clear_topping()
            if orders_complete > 1:
                orders_complete -= 1
            else:
                running = False
            order_instance = gmo.OrderStatus(toppings)  # initialize new order
            order = gv.Order(screen, order_instance)

        # move pizza
        arrow = gc.Arrow(10)  # initialize class for arrow inputs
        arrow.move_pizza(pizza_status)  # check for user arrow inputs
        pizza_view.update(
            pizza_status,
            screen,
        )  # update pizza position on display

        # toppings
        # check for collision
        collided_topping = topping_view.collide_pizza(
            pizza_view, toppings_group
        )
        if collided_topping is not None:
            pizza_status.add_topping(collided_topping)
            pizza_view.add_topping(collided_topping)
        order.update(screen, collided_topping)  # update order display
        if topping_interval == 25:  # generate toppings at rate
            toppings_group.add(
                topping_view.create_topping()
            )  # create and display toppings
            topping_interval = 0
        else:
            topping_interval += 1
        toppings_group.update()
        toppings_group.draw(screen)

        pygame.display.flip()
        clock.tick(60)  # limits FPS to 60

    return money.get_money


def end(screen, money):
    """
    Display End scene, including score and option to play again.

    Args:
        screen: a Surface to display on.
    """
    # start loop
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # display home screen and buttons.
        gv.EndScreen(screen, money)

        pygame.display.update()
        clock.tick(60)  # limits FPS to 60


menu(SCREEN)
total_money = play(SCREEN)
end(SCREEN, total_money)
