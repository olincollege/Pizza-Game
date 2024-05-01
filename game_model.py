"""
Classes for tracking the current order, current toppings on pizza, and
the current time elapsed since the time of ordering.
"""

import random
import pygame
import numpy

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 800


class OrderStatus:
    """
    A class to track the status of an order during game play.

    Attributes:
        __order_dict: A dictionary of all toppings and their quantity in the
    order.
        __max_toppings: The maximum amount of each topping a pizza could have.
    """

    def __init__(self, topping):
        """
        A function to initiate a populated order for reference.

        Args:
            topping: An int representing the maximum individual amount of
        toppings a pizza could have.
        """
        self.__max_toppings = topping
        self.__order_dict = {
            "sauce": 0,
            "cheese": 0,
            "pepperoni": 0,
            "basil": 0,
            "mushroom": 0,
        }
        # variable to track total toppings on the pizza
        temp = 0
        # assign values to the topping quantities in __order_dict
        for toppings in self.__order_dict:
            rand = random.randint(0, self.__max_toppings)
            temp += rand
            self.__order_dict[toppings] = rand
        # checks if pizza with no toppings was created randomly
        if temp == 0:
            # assigns one topping at random to a quantity of 1
            keys = list(self.__order_dict.keys())
            random_topping = numpy.random.choice(keys)
            self.__order_dict[random_topping] = 1

    def check_order(self, current_pizza):
        """
        Function to check the order against a pizza's status.

        Args:
            current_pizza: a dictionary with toppings as keys and their count
        as values.

        Returns:
            A boolean where True means the order is complete and False means
        the order is incomplete.
        """
        for topping, num in self.__order_dict.items():
            if current_pizza[topping] < num:
                return False
        return True

    def get_total_toppings(self):
        """
        Function to get the total number of toppings in an order.

        Returns:
            An int representing the total number of toppings in an order.
        """
        temp = 0
        for num in self.__order_dict.values():
            temp += num
        return temp

    @property
    def order_dict(self):
        """
        Returns a dictionary representing the order of an OrderStatus instance.
        """
        return self.__order_dict

    @property
    def max_toppings(self):
        """
        Returns an integer the topping maximum of an OrderStatus instance.
        """
        return self.__max_toppings


class PizzaStatus:
    """
    A class to track the toppings on the pizza and location during game play.

    Attributes:
        __current_toppings: A dictionary of all toppings and their quantity on
    the pizza's surface.
        __position: A two element list representing the x and y position of a
    pizza.
    """

    def __init__(self):
        self.__current_toppings = {
            "sauce": 0,
            "cheese": 0,
            "pepperoni": 0,
            "basil": 0,
            "mushroom": 0,
        }
        self.__position = [240, 150]

    def add_topping(self, topping):
        """
        Update current toppings with new topping.

        Args:
            topping: A string representing the name of the topping to update.
        """
        self.__current_toppings[topping] += 1

    def clear_pizza(self):
        """
        Clear all toppings off a pizza (used when order is completed).
        """
        self.__current_toppings = {
            "sauce": 0,
            "cheese": 0,
            "pepperoni": 0,
            "basil": 0,
            "mushroom": 0,
        }

    def update_position(self, x_update):
        """
        A function to update the x-coordinate of the pizza.

        Args:
            x_update: An int representing the number of pixels to move the
        pizza.

        Returns:
            new_pos: A list of the pizza's xy coordinates with altered x
        values.
        """
        new_pos = self.__position  # get position
        new_pos[0] = new_pos[0] + x_update  # update position's X coordinate
        # check that position is within bounds
        if new_pos[0] < -5:
            new_pos[0] = -5  # make X coordinate cap at left screen
        if new_pos[0] > 328:
            new_pos[0] = 328  # make X coordinate cap at right screen
        return new_pos

    @property
    def position(self):
        """
        Returns a two element list representing the pizza's x and y location.
        """
        return self.__position

    @property
    def status(self):
        """
        Returns a dictionary representing the toppings on the pizza.
        """
        return self.__current_toppings


class Money:
    """
    A class to calculate customer happiness/tip based on player accuracy.

    Attributes:
        __customer_happiness: A float representing the happiness of a customer,
    with a value closer to 0 meaning a more satisfied customer.
        __desired_toppings: An int representing the total number of toppings a
    customer wants on their pizza.
        __total_money: A float representing the total amount of money that the
    player has made playing the game.
    """

    def __init__(self):
        """
        Function to initialize a CustomerHappiness instance.
        """
        self.__customer_happiness = 0
        self.__desired_toppings = 0
        self.__total_money = 0

    def evaluate_order(self, desired_order, pizza_status):
        """
        A function to evaluate how well a pizza fits an order.

        Args:
            desired_order: An OrderStatus instance representing the desired
        order of the customer.
            pizza_status: A PizzaStatus instance representing the current pizza
        that the user is making.
        """
        topping_inaccuracies = 0
        # loops through dictionary of the desired toppings
        for topping, num in desired_order.order_dict.items():
            topping_inaccuracies += abs(num - pizza_status.status[topping])

        for num in desired_order.order_dict.values():
            self.__desired_toppings += num

        self.__customer_happiness = min(
            (
                topping_inaccuracies
                / (OrderStatus.get_total_toppings(desired_order))
            ),
            1,
        )

    def get_tip(self, desired_order, pizza_status):
        """
        A function to get the customer's final tip based on customer happiness.

        Args:
            desired_order: An OrderStatus instance representing the desired
        order of the customer.
            pizza_status: A PizzaStatus instance representing the current pizza
        that the user is making.

        Returns:
            tip: an int representing the tip given for an individual order.
        """
        self.evaluate_order(desired_order, pizza_status)
        tip = (self.__desired_toppings * 1.5) * (1 - self.__customer_happiness)
        return tip

    def update_money(self, desired_order, pizza_status):
        """
        A method to update total_money after every order.
        """
        self.__total_money += self.get_tip(desired_order, pizza_status)

    @property
    def desired_toppings(self):
        """
        Returns an int representing the total number of toppings in the order.
        """
        return self.__desired_toppings

    @property
    def customer_happiness(self):
        """
        Returns a float representing the happiness of a customer.
        """
        return self.__customer_happiness

    @property
    def get_money(self):
        """
        Returns a float representing total money earned (two decimal places).
        """
        return round(self.__total_money, 2)


class Button:
    """
    A class for the buttons that display at the start of the game.

    Attributes:
        __converted_image: A surface representing the image.
        __rect: A rect representing the image.
    """

    def __init__(self, x_pos, y_pos, image, scale):
        """
        Initializes a Button object.

        Args:
            x: A float representing the x position of the top left corner of
        the button.
            y: A float representing the y position of the top left corner of
        the button.
            image: A string representing the file path where the image of the
        button is stored.
            scale: A float representing how much the image should be scaled from
        its default resolution
        """
        # load image
        self.__converted_image = pygame.image.load(image).convert_alpha()
        # get image file's width and height
        width = self.__converted_image.get_width()
        height = self.__converted_image.get_height()
        # scale image
        self.__converted_image = pygame.transform.scale(
            self.__converted_image, (int(width * scale), int(height * scale))
        )
        # create rectangle out of image
        self.__rect = self.__converted_image.get_rect()
        self.__rect.topleft = (x_pos, y_pos)

    @property
    def rect(self):
        """
        Returns the __rect Rect.
        """
        return self.__rect

    @property
    def converted_image(self):
        """
        Returns the __converted_image Surface.
        """
        return self.__converted_image
