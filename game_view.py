"""
Classes to display or update display.
"""

import os
import random
import pygame
import game_model as gm


class HomeScreen:
    """
    Class to display the home screen as a pygame surface.
    """

    def __init__(self, screen):
        """
        Initialize Home screen on display.

        Args:
            screen: a Surface to display on to.
        """
        screen.fill((153, 217, 234))  # background color
        title_text = pygame.image.load("assets/img/title.png")
        screen.blit(title_text, (0, 0))  # display title text


class EndScreen:
    """
    Class to display to end screen as a pygame surface.
    """

    def __init__(self, screen, money):
        """
        Initialize End Screen on display

        Args:
            screen: a Surface to display on to.
            money: an int representing the money the player accrued
            throughout the game
        """
        font = pygame.font.Font(None, 100)  # use default font

        scene = pygame.image.load("assets/img/end_screen.png")
        scene = pygame.image.load("assets/img/end_screen.png")
        screen.blit(scene, (0, 0))
        end_text = pygame.image.load("assets/img/end_text.png")
        screen.blit(end_text, (0, 0))
        money = f"${money}"
        money_text = font.render(money, True, (0, 0, 0))
        screen.blit(money_text, (160, 250))


class ButtonDisplay:
    """
    Class to display Buttons on screen surface.

    Attributes:
        __screen: The pygame surface being used for the game.
    """

    def __init__(self, screen):
        """
        Initializes an instance of the ButtonDisplay class.

        Args:
            screen: The pygame surface being used for the game.
        """
        self.__screen = screen

    def display_button(self, button):
        """
        Displays a button on the screen.

        Args:
            button: an instance of the button class
        """
        self.__screen.blit(
            button.converted_image, (button.rect.x, button.rect.y)
        )

    @property
    def screen(self):
        """
        Returns the __screen Surface.
        """
        return self.__screen


class Kitchen:
    """
    Class to display the Kitchen scene as a surface.
    """

    def __init__(self, screen):
        """
        Initialize Kitchen on display.

        Args:
            screen: a Surface to display on to.
        """
        scene = pygame.image.load("assets/img/kitchen.png")
        screen.blit(scene, (0, 0))


class Order:
    """
    Class to display order and update its position.

    Attributes:
        __order_dict: a dictionary of an instance of a order with keys
    representing the topping and values representing the number of toppings
    desired.
        __pizza_status: a PizzaStatus instance from game_model representing the
    pizza the user is currently making.
    """

    def __init__(self, screen, order_instance):
        """
        Initialize pizza on display.

        Args:
            screen: a Surface to display on to.
            order_instance: the instance of the current working order.
        """
        font = pygame.font.Font(None, 36)  # use default font

        pygame.draw.rect(
            screen, (255, 255, 255), (30, 25, 170, 155)
        )  # draw white box

        self.__order_dict = order_instance.order_dict
        self.__pizza_status = gm.PizzaStatus()

        i = 0
        while i < len(self.__order_dict):
            for topping, num in self.__order_dict.items():
                text = f"{topping}: {num}"
                order_text = font.render(text, True, (0, 0, 0))
                screen.blit(order_text, (35, 30 + (30 * i)))
                i += 1

    def update(self, screen, new_topping_added):
        """
        Update order status display.

        Args:
            screen: a Surface to display on to.
            new_topping_added: a string representing the topping that has
            to be updated in the order
        """
        font = pygame.font.Font(None, 36)

        pygame.draw.rect(
            screen, (255, 255, 255), (30, 25, 170, 155)
        )  # draw white box

        for topping in self.__order_dict:
            if topping == new_topping_added:
                self.__pizza_status.add_topping(topping)

        i = 0
        while i < len(self.__order_dict):
            for topping, num in self.__order_dict.items():
                text = f"{topping}: {num - self.__pizza_status.status[topping]}"
                order_text = font.render(text, True, (0, 0, 0))
                screen.blit(order_text, (35, 30 + (30 * i)))
                i += 1


class AllToppingsFr(
    pygame.sprite.Sprite
):
    """
    A parent class for the topping types.

    Attributes:
            image: a surface displaying the topping image.
            rect: a rectangle representing the topping's bounding box.
            x_pos: a randomly generated int representing the
            topping's x position.
            y_pos: an int representing the topping's starting y position.
            mask: the sprite mask generated from the image surface.
    """

    def __init__(self, image_file):
        """
        A class to initialize a topping instance.

        Args:
            image_file: a string representing the image file name to
            be passed to the surface.
        """
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((120, 120))
        self.image = pygame.image.load(
            os.path.join("assets/img", image_file)
        ).convert()
        self.image.set_colorkey(self.image.get_at((0, 0)))
        self.image = pygame.transform.smoothscale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.x_pos = random.randrange(30, 450)
        self.y_pos = 5
        self.rect.center = (self.x_pos, self.y_pos)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        """
        Move the sprite 5 pixels down.
        """
        self.rect.move_ip(0, 5)
        if self.rect.top > 800:
            self.kill()


class Sauce(AllToppingsFr):
    """
    Child of AllToppingsFr with the sauce image file passed as a string.

    Attributes:
        name: a string representing the type of topping.
    """

    def __init__(self):
        AllToppingsFr.__init__(self, "sauce.png")
        self.name = "sauce"


class Cheese(AllToppingsFr):
    """
    Child of AllToppingsFr with the cheese image file passed as a string.

    Attributes:
        name: a string representing the type of topping.
    """

    def __init__(self):
        AllToppingsFr.__init__(self, "cheese.png")
        self.name = "cheese"


class Mushroom(AllToppingsFr):
    """
    Child of AllToppingsFr with the mushroom image file passed as a string.

    Attributes:
        name: a string representing the type of topping.
    """

    def __init__(self):
        AllToppingsFr.__init__(self, "mushroom.png")
        self.name = "mushroom"


class Basil(AllToppingsFr):
    """
    Child of AllToppingsFr with the basil image file passed as a string.

    Attributes:
        name: a string representing the type of topping.

    """

    def __init__(self):
        AllToppingsFr.__init__(self, "basil.png")
        self.name = "basil"


class Pepperoni(AllToppingsFr):
    """
    Child of AllToppingsFr with the pepperoni image file passed as a string.

    Attributes:
        name: a string representing the type of topping.
    """

    def __init__(self):
        AllToppingsFr.__init__(self, "pepperoni.png")
        self.name = "pepperoni"


class Toppings(pygame.sprite.Sprite):
    """
    A class to spawn toppings and alter their positions.

    Attributes:
        sprite_top_list = a list to hold all rectangles 'toppings'
        represented in the database.
    """

    def __init__(self):
        """
        Initiates a list to monitor and create toppings.
        """
        self.sprite_top_list = []

    def create_topping(self):
        """
        Spawns a random topping at the top of the screen at a random x-value.

        Returns:
            topping_sprite: an instance of a specific topping sprite.
        """
        topping_type = random.choice(
            (
                "cheese",
                "sauce",
                "pepperoni",
                "basil",
                "mushroom",
            )
        )
        if topping_type == "basil":
            topping_sprite = Basil()
        if topping_type == "cheese":
            topping_sprite = Cheese()
        if topping_type == "mushroom":
            topping_sprite = Mushroom()
        if topping_type == "pepperoni":
            topping_sprite = Pepperoni()
        if topping_type == "sauce":
            topping_sprite = Sauce()

        return topping_sprite

    def collide_pizza(self, pizza, topping_group):
        """
        Checks if any of the toppings have collided with the pizza.

        This function checks if any of the toppings have collided with the
        pizza, and if they have, it deletes the toppings. It
        and if so, delete them. Also updates order status.

        Args:
            pizza: an instance of Pizza sprite.
            topping_group: a group of topping sprites.

        Returns:
            A string representing the name of the topping pizza collided with.
        If no collision, returns None.
        """
        collisions = pygame.sprite.spritecollide(
            pizza, topping_group, True, pygame.sprite.collide_mask
        )
        if len(collisions) > 0:
            return collisions[0].name

        return None


class Pizza(pygame.sprite.Sprite):
    """
    Class to display pizza, update its position and toppings.

    Attributes:
        image: a surface displaying the pizza image.
        rect: a rectangle representing the pizza's bounding box.
        x_pos: an int representing the pizza's starting x position.
        y_pos: an int representing the pizza's y position.
        mask: the sprite mask generated from the image surface.
        toppings_on_pizza: a list with elements representing all the
    current toppings on pizza.
    """

    def __init__(self, screen):
        """
        Initialize Pizza on display.

        Args:
            screen: a Surface to display on to.
        """
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/img/pizza_dough.png")
        self.image = pygame.transform.scale_by(self.image, 0.27)
        pygame.Surface.blit(screen, self.image, (230, 600))
        self.rect = pygame.Rect(
            240,
            600,
            self.image.get_width(),
            self.image.get_height(),
        )
        self.mask = pygame.mask.from_surface(self.image)
        self.toppings_on_pizza = []

    def update(self, pizza_status, screen):
        """
        Update Pizza location on display.

        Args:
            pizza_status: A PizzaStatus instance.
            screen: a Surface to display on to.
        """
        pos = pizza_status.position
        x_pos = pos[0]
        self.rect.update(
            x_pos,
            600,
            self.image.get_width(),
            self.image.get_height(),
        )
        pygame.Surface.blit(screen, self.image, (x_pos, 600))
        for image in self.toppings_on_pizza:
            image = pygame.transform.smoothscale(image, (150, 150))
            pygame.Surface.blit(screen, image, (x_pos, 600))

    def add_topping(self, topping_image):
        """
        Display new topping on pizza.

        Args:
            topping_image: an image of desired topping.
        """
        sauce_image = Sauce()
        cheese_image = Cheese()
        basil_image = Basil()
        pepperoni_image = Pepperoni()
        mushroom_image = Mushroom()

        if topping_image == "sauce":
            self.toppings_on_pizza.append(sauce_image.image)
        if topping_image == "cheese":
            self.toppings_on_pizza.append(cheese_image.image)
        if topping_image == "basil":
            self.toppings_on_pizza.append(basil_image.image)
        if topping_image == "pepperoni":
            self.toppings_on_pizza.append(pepperoni_image.image)
        if topping_image == "mushroom":
            self.toppings_on_pizza.append(mushroom_image.image)

    def clear_topping(self):
        """
        Clear pizza display of all its toppings.
        """
        self.toppings_on_pizza = []
