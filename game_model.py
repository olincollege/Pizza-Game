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


class Button:
    def __init__(self, x, y, image, scale, screen):
        self.screen = screen
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
