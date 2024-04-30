import pygame
import game_model as gmo
import game_view as gv
import game_controller as gc
import time

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
        if button_control.check_press(start_button):  # start, exit menu, start game
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
    order_instance = gmo.OrderStatus(4)  # initialize first order
    pizza_status = gmo.PizzaStatus()  # initialize empty pizza
    pizza_view = gv.Pizza(screen)  # display pizza
    pizza = gv.PizzaView()
    pizza_sprite = pizza.pizza_sprite

    topping_view = gv.Toppings()  # initialize list of toppings
    topping_database = gmo.ToppingPosition()  # initialize topping info

    customer_happiness = gmo.CustomerHappiness() # initialize customer happiness
    total_money_instance = gmo.TotalMoney() # initialize money count

    topping_interval = 25  # every 25 frames add generate new topping

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
        current_pizza = pizza_status.status  # get status on current pizza
        # check if pizza order is completed
        if gmo.OrderStatus.check_order(order_instance, current_pizza) is True:
            customer_happiness.evaluate_order(
                order_instance.order_dict, pizza_status.status
            )
            total_money_instance.update_money()
            #### ADD METHOD TO CLEAR PIZZA
            order_instance = gmo.OrderStatus(4)  # initialize new order

        # move pizza
        arrow = gc.Arrow(10)  # initialize class for arrow inputs
        arrow.move_pizza(pizza_status)  # check for user arrow inputs
        pizza_view.update(
            pizza_status, screen
        )  # update pizza position on display

        # toppings
        if topping_interval == 25:  # generate toppings at rate
            topping_view.create_topping(
                screen, topping_database
            )  # create and display toppings
            topping_view.move_toppings_view(screen)
            topping_interval = 0
            #running = False
        else:
            topping_view.move_toppings_view(screen)
            topping_interval += 1

        pizza_status.add_topping(topping_view.collide_pizza(pizza))
        pygame.display.flip()
        clock.tick(60)  # limits FPS to 60

    return total_money_instance.get_money


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
        screen.fill((153, 217, 234))
        gv.EndScreen(screen, money)

        pygame.display.update()
        clock.tick(60)  # limits FPS to 60


menu(SCREEN)
# play(SCREEN)
end(SCREEN, play(SCREEN))
