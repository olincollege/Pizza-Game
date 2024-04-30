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

    Attributes:
        __pizza_speed: An integer representing the number of pixels the pizza
    moves with each press of an arrow key.
    """

    def __init__(self, speed):
        """
        Initiate an instance of the arrow class.

        Args:
            speed: An int representing the distance the pizza moves on a press
        of an arrow key.
        """
        self.__pizza_speed = speed

    def move_pizza(self, pizza):
        """
        A function to move the pizza left or right based on arrow interaction.

        Args:
            pizza: A PizzaStatus instance.
        """
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            pizza.update_position(-(self.__pizza_speed))
        elif keys[pygame.K_RIGHT]:
            pizza.update_position(self.__pizza_speed)
    
    @property
    def speed(self):
        """
        Returns an int representing the speed of the pizza.
        """
        return self.__pizza_speed
        

# tester code
# pygame.init()
# test_pizza = PizzaStatus()
# i =0
# while i == 10:
#     Arrow.move_pizza(test_pizza)
#     i += 1
