import pygame, random

"""Classes for tracking the current order, current toppings on pizza, and
the current time ellapsed since the time of ordering."""


class order_status:
    """
    A class to track the status of an order during gameplay
    Attributes:
        order_dict = dictionary of all toppings and their instances in the order
    """

    order_dict = {}


class pizza_status:
    """
    A class to track the toppings on the pizza during gameplay
    Attributes:
        toppings_dict = a dictionary of all toppings and their instances on the pizza's surface
    """


class timer_status:
    """
    A class to track gametime
        Attributes:
            time: an int representing elapsed time in seconds
    """


class customer_happiness(pizza_status, order_status):
    """
    A class to calculate customer happiness/tip based on player accuracy
    Attributes:
        accuracy = an integer representing player accuracy in percent
        tip = an integer representing the tip amount derived from customer happiness
    """


class total_money(customer_happiness):
    """
    A class to keep track of total money earned by the player
    Attributes:
        money: an integer representing money earned
    """
