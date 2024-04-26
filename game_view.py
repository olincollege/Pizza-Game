import pygame
import game_model as gm

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
        scene = pygame.image.load('assets/img/kitchen.png')
        screen.blit(scene, (0,0))

class Order():
    """
    Class to display order.
    """
    pass


class Pizza:
    """
    DOC STRING
    """

    def __init__(self, screen):
        pygame.draw.ellipse(screen, (235, 198, 52), (75, 40))

    def update(self):
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

    def create_topping(self, random_topping, screen):
        """
        Spawns a random topping at the top of the screen at a random x-value.
        Attributes:
            random_topping: the output of the model class
            ToppingPosition.spawn_topping
            screen: the surface to draw the topping on

        """
        new_top_info = random_topping
        new_top_type = new_top_info[0]
        color = new_top_type.color
        dimension = new_top_type.bounding_box
        pos_x = new_top_info[1]
        pos_y = new_top_info[2]
        self.rectangle_top_list.append(
            pygame.draw.rect(
                screen, color, (dimension[1], dimension[2], pos_x, pos_y)
            )
        )

    def move_toppings_view(self):
        """
        Moves all toppings down 5 pixels
        """
        for topping in self.rectangle_top_list:
            pygame.Rect.move(topping, 0, -5)

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