import pygame, random

"""Classes for tracking the current order, current toppings on pizza, and
the current time elapsed since the time of ordering."""


class OrderStatus:
    """
    A class to track the status of an order during game play
    Attributes:
        order_dict = dictionary of all toppings and their instances in the order
    """

    def __init__(self):
        self.order_dict = {
            "sauce": 0,
            "cheese": 0,
            "pepperoni": 0,
            "mushroom": 0,
        }
        for topping in self.order_dict:
            self.order_dict[topping] = random.randint(0, 4)

    def check_order(self):
        temp_order_status_dict = {}
        for topping, num in self.order_dict.items():
            if num >= self._current_pizza[topping]:
                temp_order_status_dict[topping] = True
            else:
                temp_order_status_dict[topping] = False

        for topping, num in temp_order_status_dict:
            if num is False:
                return temp_order_status_dict, False
        return temp_order_status_dict, True
    
    def get_order(self):
        return self.order_dict

class PizzaStatus:
    """
    A class to track the toppings on the pizza and location during game play

    Attributes:
        current_toppings: a dictionary of all toppings and their instances on
        the pizza's surface.
    """

    def __init__(self):
        self._current_toppings = {
            "sauce": 0,
            "cheese": 0,
            "pepperoni": 0,
            "mushroom": 0,
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
        pass

    def get_position(self):
        pass


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


class Button:
    """ """

    def __init__(self, x, y, image, scale, screen):
        self.screen = screen
        image = pygame.image.load(image).convert_alpha()
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(
            image, (int(width * scale), int(height * scale))
        )
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditons
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked is False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        # draw button on screen
        self.screen.blit(self.image, (self.rect.x, self.rect.y))
        return action
