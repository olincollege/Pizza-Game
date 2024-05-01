import pygame
from game_model import *

class ButtonControl:
    """
    A class to define button functions within the game.

    Attributes:
        __button: A Button instance.
        __pos: A tuple of ints representing the location of the mouse.
    """
    def __init__(self):
        """
        Initialize an instance of the ButtonControl class.
        """
        self.__pos = pygame.mouse.get_pos()

    def check_press(self, button):
        """
        Checks if the button is pressed.

        Returns:
            A boolean representing whether or not a button is pressed.
        """
        action = False
        # get mouse position
        self.__pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditons
        if button.rect.collidepoint(self.__pos):
            if pygame.mouse.get_pressed()[0] == 1:
                action = True
        return action



class Arrow:
    """
    A class to define the function of a button press

    Attributes:
        __pizza_speed: An integer representing the number of pixels the pizza
    moves with each press of an arrow key.
    """

    def __init__(self, speed):
        """
        Initialize an instance of the arrow class.

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
