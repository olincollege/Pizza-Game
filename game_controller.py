import pygame
from game_model import *

class Button:
    """
    A class to define button functions within the game.

    Attributes:
        Goes-to: a string of the name of the environment that the button
        leads to.
    """


class Arrow:
    """
    A class to define the function of a button press

        direction: whether the left or right button was pressed
        move-pizza: true or false depending if the player is in active play
        of the game.
    """

    def __init__(self):
        """
        Initiate an instance of the arrow class.

        Attributes:
            _pizza_speed: An integer representing the number of pixels the
            Pizza moves with each press of key.
        """
        self._pizza_speed = 10

    def move_pizza(self, pizza):
        """
        A function to move the pizza left or right based on arrow interaction.
        """
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            PizzaStatus.update_position(pizza, -(self._pizza_speed))
        elif keys[pygame.K_RIGHT]:
            PizzaStatus.update_position(pizza, self._pizza_speed)
        print(PizzaStatus.get_position(pizza))

# tester code
# pygame.init()
# test_pizza = PizzaStatus()
# i =0
# while i == 10:
#     Arrow.move_pizza(test_pizza)
#     i += 1
