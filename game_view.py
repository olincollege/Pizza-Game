import pygame
import game_model as gm
import sys
import os
import random

"""
Classes for viewing the game.
"""


class HomeScreen:
    """
    Class to display the home screen.
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
    Class to display to end screen.
    """

    def __init__(self, screen, money):
        font = pygame.font.Font(None, 165)  # use default font

        end_text = pygame.image.load("assets/img/end_text.png")
        screen.blit(end_text, (0, 0))
        money = f"${money}"
        money_text = font.render(money, True, (0, 0, 0))
        screen.blit(money_text, (180, 240))


class ButtonDisplay:
    """
    Class to display Buttons on screen.

    Atrributes:
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
    Class to display the Kitchen scene.
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

        self.order_dict = order_instance.order_dict
        self.pizza_status = gm.PizzaStatus()

        i = 0
        while i < len(self.order_dict):
            for topping, num in self.order_dict.items():
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

        for topping in self.order_dict:
            if topping == new_topping_added:
                self.order_dict[topping] -= 1

        i = 0
        while i < len(self.order_dict):
            for topping, num in self.order_dict.items():
                text = f"{topping}: {num}"
                order_text = font.render(text, True, (0, 0, 0))
                screen.blit(order_text, (35, 30 + (30 * i)))
                i += 1


class AllToppingsFr(pygame.sprite.Sprite):
    """
    DOC STRING
    """
    def __init__(self, image_file):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((120, 120))
        self.image = pygame.image.load(
            os.path.join("assets/img", image_file)
        ).convert()
        self.image.set_colorkey(self.image.get_at((0, 0)))
        self.image = pygame.transform.smoothscale(self.image, (120, 120))
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
    Docstring
    """

    def __init__(self):
        AllToppingsFr.__init__(self, "sauce.png")
        self.name = 'sauce'


class Cheese(AllToppingsFr):
    """
    Docstring
    """

    def __init__(self):
        AllToppingsFr.__init__(self, "cheese.png")
        self.name = 'cheese'


class Mushroom(AllToppingsFr):
    """
    Docstring
    """

    def __init__(self):
        AllToppingsFr.__init__(self, "mushroom.png")
        self.name = 'mushroom'


class Basil(AllToppingsFr):
    """
    Docstring
    """

    def __init__(self):
        AllToppingsFr.__init__(self, "basil.png")
        self.name = 'basil'


class Pepperoni(AllToppingsFr):
    """
    Docstring
    """

    def __init__(self):
        AllToppingsFr.__init__(self, "pepperoni.png")
        self.name = 'pepperoni'


class Toppings(pygame.sprite.Sprite):
    """
    A class to spawn toppings and alter their positions
    """

    def __init__(self):
        """
        Initiates a list to monitor and create toppings.
        Attributes:
            sprite_top_list = a list to hold all rectangles 'toppings' represented in the database
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
        Checks if any of the toppings have collided with the pizza,
        and if so, delete them. Also updates order status.

        Args:
            pizza: an instance of Pizza sprite.
            topping_group: a group of topping sprites.
        
        Returns:
            A string representing the name of the topping pizza collided with.
        """
        collisions = pygame.sprite.spritecollide(
            pizza, topping_group, True, pygame.sprite.collide_mask
        )
        if len(collisions) > 0:
            return collisions[0].name


class Pizza(pygame.sprite.Sprite):
    """
    Class to display pizza, update its position and toppings.
    """

    def __init__(self, screen):
        """
        Initialize Pizza on display.
        Args:
            screen: a Surface to display on to.
        """
        pygame.sprite.Sprite.__init__(self)
        # pygame.draw.ellipse(screen, (235, 198, 52), (x_pos, 700, 120, 70))
        self.image = pygame.image.load("assets/img/pizza_dough.png")
        self.image = pygame.transform.scale_by(self.image, 0.27)
        pygame.Surface.blit(screen, self.image, (230, 600))
        # dough_surf = pygame.image.load("assets/img/pizza_dough.png")
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
        # pygame.draw.ellipse(screen, (235, 198, 52), (x_pos, 700, 120, 70))
        self.rect.update(
            x_pos,
            600,
            self.image.get_width(),
            self.image.get_height(),
        )
        pygame.Surface.blit(screen, self.image, (x_pos, 600))
        for image in self.toppings_on_pizza:
            pygame.Surface.blit(screen, image, (x_pos, 650))

    def add_topping(self, topping_image):
        """
        Docstring
        """
        self.toppings_on_pizza.append(topping_image)
