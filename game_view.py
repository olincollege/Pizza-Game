import pygame
import game_model as gm
import sys

"""
Classes for viewing the game.
"""

class HomeScreen:
    """
    DOC STRING
    """
    def __init__(self, screen):
        scene = pygame.image.load('assets/img/homescreen.png')
        screen.blit(scene, (0,0))

# class Button(HomeScreen):

# class StartButton(Button):

# class InstructionButton(Button):


class Kitchen:
    """
    Doc String
    """

    def __init__(self, screen):
        scene = pygame.image.load("assets/img/kitchen.png")
        screen.blit(scene, (0, 0))


class Order:
    """
    Class to display order and update its position.
    """
    def __init__(self, screen, order_instance):
        """
        Initialize pizza on display.
        """
        font = pygame.font.Font(None, 36)

        pygame.draw.rect(screen, (255, 255, 255), (30, 25, 163, 135))

        order_dict = order_instance.get_order()
        i = 0
        while i < len(order_dict):
            for topping, num in order_dict.items():
                text = f'{topping}: {num}'
                order_text = font.render(text, True, (0, 0 , 0))
                screen.blit(order_text, (35, 30 + (30 * i)))
                i += 1

    def update(self):
        """
        Update order status display.
        """
        pass


class Pizza:
    """
    Class to display pizza, update its position and toppings.
    """
    def __init__(self, screen):
        # pizza_surf = pygame.image.load('assets/img/pizza.png').convert_alpha()
        pygame.draw.ellipse(screen, (235, 198, 52), (230, 700, 120, 70))

    def update(self):
        """
        DOC STRING
        """
        pass


class Toppings:
    """
    A class to spawn toppings and alter their positions
    """

    def __init__(self):
        """
        Initiates a list to monitor and create toppings.
        Attributes:
            rectangle_top_list = a list to hold all rectangles 'toppings' represented in the database
        """
        self.rectangle_top_list = []

    def create_topping(self, database, screen):
        """
        Spawns a random topping at the top of the screen at a random x-value.
        Attributes:
            random_topping: the output of the model class
            ToppingPosition.spawn_topping
            screen: the surface to draw the topping on

        """
        new_top_info = database.spawn_topping()
        new_top_type = new_top_info[0]
        color = new_top_type.get_color()
        dimension = new_top_type.bounding_box
        pos_x = new_top_info[1]
        self.rectangle_top_list.append(
            [screen, color, pygame.Rect(pos_x, 5, dimension[0], dimension[1])]
        )

    def move_toppings_view(self, database):
        """
        Moves all toppings down 5 pixels
        """
        database.move_all_toppings()
        for topping in self.rectangle_top_list:
            pygame.Rect.move(topping[2], 0, -5)

    def collide_pizza(self, pizza):
        """
        Checks if any of the toppings have collided with the pizza, and if so, delete them.
        """
        for topping in self.rectangle_top_list:
            if pygame.Rect.colliderect(topping, pizza):
                del topping


# class Cheese(Toppings):

# class Sauce(Toppings):

# class Basil(Toppings):

# class Mushroom(Toppings):
