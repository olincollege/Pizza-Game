import pygame, random, time, numpy, os

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 800

"""
Classes for tracking the current order, current toppings on pizza, and
the current time elapsed since the time of ordering.
"""


class OrderStatus:
    """
    A class to track the status of an order during game play.

    Attributes:
        __order_dict: A dictionary of all toppings and their quantity in the
    order.
        __max_toppings: The maximum ammount of each topping a pizza could have.
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
            "basil": 0,
            "mushroom": 0,
        }
        # variable to track total toppings on the pizza
        temp = 0
        # assign values to the topping quantities in __order_dict
        for topping in self.__order_dict:
            rand = random.randint(0, self.__max_toppings)
            temp += rand
            self.__order_dict[topping] = rand
        # checks if pizza with no toppings was created randomly
        if temp == 0:
            # assigns one topping at random to a quantity of 1
            self.__order_dict[numpy.random.choice(self.__order_dict.keys)] = 1

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


class PizzaStatus:
    """
    A class to track the toppings on the pizza and location during game play.

    Attributes:
        __current_toppings: A dictionary of all toppings and their quanitity on
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
        if new_pos[0] < 0:
            new_pos[0] = 0  # make X coordinate cap at left screen
        if new_pos[0] > 360:
            new_pos[0] = 360  # make X coordinate cap at right screen
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


class Toppings:
    """
    A parent class for the individual toppings.

    Attributes:
        value: A string denoting what topping the instance represents.
        color: A tuple of 3 numbers detailing the color key of the topping
        bounding_box: a tuple dictating the borders of the topping's
        bounding box
        fall_speed = an integer set to default value 5
    """

    def __init__(
        self,
        value,
        fall_speed=5,
    ):
        self._fall_speed = fall_speed
        self.topping_value = value

    def get_value(self):
        """
        Returns value of topping
        """
        return self.topping_value


class Cheese(Toppings):
    """
    A class to create an instance of Cheese topping based on the topping
    parent class.
    """

    def __init__(self):
        super().__init__("cheese")
        # # img = pygame.image.load('assets/img/cheese.png')
        # # super().__init__("Cheese", img, (30, 30))
        # super().__init__("cheese")


class Sauce(Toppings):
    """
    A class to create an instance of the sauce topping based on the
    topping parent class.
    """

    def __init__(self):
        super().__init__("sauce")


class Pepperoni(Toppings):
    """
    A class to create an instance of the pepperoni topping based on the
    toping parent class.
    """

    def __init__(self):
        super().__init__("pepperoni")


class Basil(Toppings):
    """
    A class to create an instance of the sauce topping based on the
    topping parent class.
    """

    def __init__(self):
        super().__init__("basil")


class Mushroom(Toppings):
    """
    A class to create an instance of the mushroom topping based on the
    topping parent class.
    """

    def __init__(self):

        super().__init__("mushroom")


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
        self._topping_list = (
            "cheese",
            "sauce",
            "pepperoni",
            "basil",
            "mushroom",
        )
        self._topping_info = []
        self._fall_speed = 5

    def spawn_topping(self):
        """
        A function to generate a topping at the top of the screen at a random x-value
        """
        top = random.choice(self._topping_list)
        if top == "cheese":
            top = Cheese()
        if top == "sauce":
            top = Sauce()
        if top == "pepperoni":
            top = Pepperoni()
        if top == "basil":
            top = Basil()
        if top == "mushroom":
            top = Mushroom()

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


class Money:
    """
    A class to calculate customer happiness/tip based on player accuracy.

    Attributes:
        __customer_happiness: A float representing the happiness of a customer,
    with a value closer to 0 meaning a more satisfied customer.
        __desired_toppings: An int representing the total number of toppings a
    customer wants on their pizza.
        __total_money: A float representing the total ammount of money that the
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

        self.__customer_happiness = min((topping_inaccuracies / self.__desired_toppings), 1)

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

    def __init__(self, x, y, image, scale):
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
        self.__rect.topleft = (x, y)

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
