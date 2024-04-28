import pygame, random, time

# from game_main import SCREEN_WIDTH, SCREEN_HEIGHT

"""
Classes for tracking the current order, current toppings on pizza, and
the current time elapsed since the time of ordering.
"""


class OrderStatus:
    """
    A class to track the status of an order during game play.

    Attributes:
        __order_dict: A dictionary of all toppings and their instances
        in the order.
        __max_toppings: The max ammount of each topping a pizza could have.
    """

    def __init__(self, topping):
        """
        A function to initiate a populated order for reference.

        Args:
            topping: An int representing the maximum individual ammount of
        toppings a pizza could have.
        """
        self.__max_toppings = topping
        self.__order_dict = {
            "sauce": 0,
            "cheese": 0,
            "pepperoni": 0,
            "mushroom": 0,
        }
        for topping in self.__order_dict:
            self.__order_dict[topping] = random.randint(0, self.__max_toppings)

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


class Pizza(pygame.sprite.Sprite):
    """
    A class to create and keep track of the Pizza object and its location.
    """

    def __init__(self):
        """
        Initialize an instance of Pizza object.
        """
        pygame.sprite.Sprite.__init__(self)

        # pizza = pygame.image.load("assets/img/pizza.png").convert_alpha()
        # pizza_rect = pizza.get_rect()
        # pizza_mask = pygame.mask.from_surface(pizza)
        # self.mask_img = pizza_mask.to_surface()

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

    def update_position(self, x_update):
        """
        A function to update the x-coordinates of the pizza
        Args:
            x_update: an int representing the number of pixels to move the pizza
        Returns:
            new_pos: a list of the pizza's xy coordinates with altered x values.
        """
        new_pos = self._position # get position
        new_pos[0] = new_pos[0] + x_update # update position's X coordinate
        # check that position is within bounds
        if new_pos[0] < 0:
            new_pos[0] = 0 # make X coordinate cap at left screen
        if new_pos[0] > 360:
            new_pos[0] = 360 # make X coordinate cap at right screen
        return new_pos

    def get_position(self):
        """
        A function that returns the pizza's current position
        """
        return self._position


class Toppings:
    """
    A parent class for the individual toppings.
    Attributes:
        value: a string denoting what topping the instance is
        color: a tuple of 3 numbers detailing the color key
        bounding_box: a tuple dictating the borders of the topping's
        bounding box
        fall_speed = an integer set to default value 5
    """

    def __init__(
        self,
        value,
        color,
        bounding_box,
        fall_speed=5,
    ):
        self._fall_speed = fall_speed
        self.value = value
        self.color = color
        self.bounding_box = bounding_box

    def get_color(self):
        """
        Returns topping color
        """
        return self.color


class Cheese(Toppings):
    """
    A class to create an instance of Cheese topping based on the topping
    parent class.
    """

    def __init__(self):
        super().__init__("Cheese", (255, 255, 224), (30, 30))


class Sauce(Toppings):
    """
    A class to create an instance of the sauce topping based on the
    topping parent class.
    """

    def __init__(self):
        super().__init__("Sauce", (255, 0, 0), (30, 30))


class Pepperoni(Toppings):
    """
    A class to create an instance of the pepperoni topping based on the
    toping parent class.
    """

    def __init__(self):
        super().__init__("Pepperoni", (165, 42, 42), (30, 30))


class Basil(Toppings):
    """
    A class to create an instance of the sauce topping based on the
    topping parent class.
    """

    def __init__(self):
        super().__init__("Basil", (0, 255, 0), (30, 30))


class Pepper(Toppings):
    """
    A class to create an instance of the pepper topping based on the
    topping parent class.
    """

    def __init__(self):

        super().__init__("Pepper", (255, 165, 0), (30, 30))


class ToppingPosition:
    """
    A class to monitor the positions of all toppings on screen
    Attributes:
        topping_info: A list of lists, where the list entries contain a topping
        value in index 0, topping x pos in index 1, and y pos in index 2
    """

    def __init__(self):
        """
        Create an instance of the ToppingPosition class
        """
        self._topping_list = ("Cheese", "Sauce", "Pepperoni", "Basil", "Pepper")
        self._topping_info = []
        self._fall_speed = 5

    def spawn_topping(self):
        """
        A function to generate a topping at the top of the screen at a random x-value
        """
        SCREEN_HEIGHT = 800
        SCREEN_WIDTH = 480
        top = random.choice(self._topping_list)
        if top == "Cheese":
            top = Cheese()
        if top == "Sauce":
            top = Sauce()
        if top == "Pepperoni":
            top = Pepperoni()
        if top == "Basil":
            top = Basil()
        if top == "Pepper":
            top = Pepper()

        pos_x = random.choice(range(15, SCREEN_WIDTH - 15))
        top_position = [top, pos_x]
        self._topping_info.append(top_position)
        return top_position

    def move_all_toppings(self):
        """
        A function to update the topping positions and remove out of bounds toppings
        """
        for topping in self._topping_info:
            if topping[2] <= SCREEN_HEIGHT:
                del [topping]
            else:
                topping[2] -= self._fall_speed

    def get_topping_info(self):
        """
        A function that refturns the value of list _topping_info
        """
        return self._topping_info


class TimerStatus:
    """
    A class to track game time.

    Attributes:
        time_current: A float representing the time in seconds since the Epoch
    when the instance of TimerStatus was initialized.
    """

    def __init__(self):
        """
        Initializes a TimerStatus object.
        """
        self.time_current = time.time()

    def __repr__(self):
        """
        Makes a TimerStatus easily convertible to a float.

        Returns:
            A float representing the time since the creation of the
            TimerStatus object.
        """
        return time.time() - self.time_current


class CustomerHappiness:
    """
    A class to calculate customer happiness/tip based on player accuracy
    Attributes:
        accuracy: an integer representing player accuracy in percent
        tip: an integer representing the tip amount derived from
        customer happiness
    """

    def __init__(self):
        self._customer_happiness = 0
        self._desired_toppings = 0

    def evaluate_order(self, desired_order, pizza_status):
        """
        A function to evaluate the customer's desired order versus
        the given pizza.
        Attributes:
            desired_order: a dictionary representing the customer's order with
            toppings as the keys and topping instances as the values.

            pizza_status: a dictionary representing the toppings actually
            on the pizza with toppings as the keys and num topping
            instances as the values.

        Returns:
            customer_happiness_change: a float to represent customer
            happiness level based on the order's accurateness.
        """
        topping_inaccuracies = 0
        # loops through dictionary of the desired toppings
        for topping, num in desired_order.items():
            topping_inaccuracies += abs(num - pizza_status[topping])

        for num in desired_order.values():
            self._desired_toppings += num

        topping_differences = self._desired_toppings - topping_inaccuracies

        if topping_differences < 1:
            return self._customer_happiness
        self._customer_happiness = topping_inaccuracies / self._desired_toppings
        return self._customer_happiness

    def get_tip(self):
        """
        A function to get the customer's final tip based on customer happiness
        Returns:
            tip: an int representing the tip given.
        """
        tip = (self._desired_toppings * 1.5) * self._customer_happiness
        return tip


class TotalMoney:
    """
    A class to keep track of total money earned by the player
    Attributes:
        total_money: an integer representing money earned
    """

    def __init__(self):
        """
        Initialize money.
        """
        self.total_money = 0

    def update_money(self):
        """
        A method to update total_money after every order.
        """
        self.total_money += CustomerHappiness.get_tip(self)


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
        self.converted_image = pygame.image.load(image).convert_alpha()
        width = self.converted_image.get_width()
        height = self.converted_image.get_height()
        self.converted_image = pygame.transform.scale(
            self.converted_image, (int(width * scale), int(height * scale))
        )
        self.rect = self.converted_image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        """
        This function both draws the button and checks if it is pressed.

        A call to this function will both display the button on the surface
        being used for the game and also return a boolean.

        Returns:
            A boolean representing whether or not the button is being pressed
        during the call to draw.
        """
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
