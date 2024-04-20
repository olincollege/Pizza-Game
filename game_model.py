import pygame, random

"""Classes for tracking the current order, current toppings on pizza, and
the current time elapsed since the time of ordering."""


class OrderStatus:
    """
    A class to track the status of an order during game play.

    Attributes:
        order_dict: A dictionary of all toppings and their instances in the order.
    """

    def __init__(self):
        """
        A function to initiate a populated order for reference. 
        Attributes:
            order_dict = dictionary of all toppings and their instances in the order
        """
        self.order_dict = {
            "sauce": 0,
            "cheese": 0,
            "pepperoni": 0,
            "mushroom": 0,
        }
        for topping in self.order_dict:
            self.order_dict[topping] = random.randint(0, 4)

    def check_order(self, pizza):
        """
        Function to check the order against a pizza's status
        Attributes:
            pizza: a dictionary of toppings with their current instances on the pizza

        """
        """
        Compare order toppings and current toppings on pizza.

        Returns:
            A boolean where True means the order is complete and False means
            the order is incomplete.
        """
        temp_order_status_dict = {}
        for topping, num in self.order_dict.items():
            if (
                num >= self._current_pizza[topping]
            ):  # check for if it's over the requested amount
                temp_order_status_dict[topping] = True
            else:
                temp_order_status_dict[topping] = False

        for topping, num in temp_order_status_dict:
            if num is False:
                return temp_order_status_dict, False
        return temp_order_status_dict, True

    def get_order(self):
        return self.order_dict


class Pizza(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        pizza = pygame.image.load('assets/img/pizza.png').convert_alpha()
        pizza_rect = pizza.get_rect()
        pizza_mask = pygame.mask.from_surface(pizza)
        self.mask_img = pizza_mask.to_surface()

    def update(self):
        pass

class PizzaStatus:
    """
    A class to track the toppings on the pizza and location during game play

    Attributes:
        _current_toppings: a dictionary of all toppings and their instances on
        the pizza's surface.
        _position: A list representing the x and y position.
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


class CustomerHappiness():
    """
    A class to calculate customer happiness/tip based on player accuracy
    Attributes:
        accuracy: an integer representing player accuracy in percent
        tip: an integer representing the tip amount derived from
        customer happiness
    """
    def __init__(self):
        self.happiness_level = 80

    def evaluate_order(self,desired_order, pizza_status):
        """
        A function to evaluate the cutomer's desired order versus the given pizza. 
        Attributes:
            desired_order: a dictionery representing the customer's order with 
            toppings as the keys and topping instances as the values.

            pizza_status: a dictionary representing the toppings actually on the pizza
            with toppings as the keys and num topping instances as the values
        Returns: 
            customer_happiness_change: an int to represent cutomer happiness level based on the order's accurateness
        """
    
    def get_tip(self):
        """
        A function to get the customer's final tip based on customer happiness
        Returns:
            tip: an int representing the tip given
        """
        
        





class TotalMoney(CustomerHappiness):
    """
    A class to keep track of total money earned by the player
    Attributes:
        money: an integer representing money earned
    """


class Button:
    """
    A class for the buttons that display at the start of the game.

    Attributes:
        x: A float representing the x position of the top left corner of the
    button.
        y: A float representing the y position of the top left corner of the
    button.
        image: A string representing the file path where the image of the
    button is stored.
        scale: A float representing how much the image should be scaled from
    its default resolution
        converted_image: A surface representing the image.
        screen: The pygame surface being used for the game.
        width: An int representing the width in pixels of the image.
        height: An int representing the height in pixels of the image.
        rect: A rect representing the image.
        clicked: A boolean representing whether or not a button is actively
    being pressed.
    """

    def __init__(self, x, y, image, scale, screen):
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
            screen: The pygame surface being used for the game.
        """
        self.screen = screen
        image = pygame.image.load(image).convert_alpha()
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(
            image, (int(width * scale), int(height * scale))
        )
        self.rect = self.converted_image.get_rect()
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
        self.screen.blit(self.converted_image, (self.rect.x, self.rect.y))
        return action
