import pygame, random

"""Classes for tracking the current order, current toppings on pizza, and
the current time elapsed since the time of ordering."""


class OrderStatus:
    """
    A class to track the status of an order during game play
    Attributes:
        order_dict = dictionary of all toppings and their instances in the order
    """

    order_dict = {}


class PizzaStatus:
    """
    A class to track the toppings on the pizza and location during game play

    Attributes:
        current_toppings: a dictionary of all toppings and their instances on
        the pizza's surface.
    """
    def __init__(self):
        self._current_toppings = {
            'sauce': 0,
            'cheese': 0,
            'pepperoni': 0,
            'mushroom': 0
        }
        self._position = [240, 150]

    def add_topping(self, topping):
        """
        Update current toppings with new topping

        Args:
            topping: A string representing the type of topping to update
        """
        self._current_toppings[topping] += 1

    def get_pizza_status(self):
        """
        Get status of pizza which includes all current toppings

        Returns:
            A dictionary with keys representing the type of topping and values
            representing the quantity on the pizza.
        """
        return self._current_toppings
    
    def update_position(self):

    def get_position(self):



class TimerStatus:
    """
    A class to track game time
        Attributes:
            time: an int representing elapsed time in seconds
    """


class CustomerHappiness(PizzaStatus, OrderStatus):
    """
    A class to calculate customer happiness/tip based on player accuracy
    Attributes:
        accuracy: an integer representing player accuracy in percent
        tip: an integer representing the tip amount derived from
        customer happiness
    """


class TotalMoney(CustomerHappiness):
    """
    A class to keep track of total money earned by the player
    Attributes:
        money: an integer representing money earned
    """
