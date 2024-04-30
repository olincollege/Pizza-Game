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
        scene = pygame.image.load("assets/img/homescreen.png")
        screen.blit(scene, (0, 0))


# class Button(HomeScreen):

# class StartButton(Button):

# class InstructionButton(Button):


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
        font = pygame.font.Font(None, 36)

        pygame.draw.rect(screen, (255, 255, 255), (30, 25, 163, 135))

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
        self.pizza_status.current_toppings[new_topping_added] += 1
        font = pygame.font.Font(None, 36)

        pygame.draw.rect(screen, (255, 255, 255), (30, 25, 163, 135))

        i = 0
        while i < len(self.order_dict):
            for topping, num in self.order_dict.items():
                text = f"{topping}: {num}, {self.pizza_status.current_toppings[topping]}"
                order_text = font.render(text, True, (0, 0, 0))
                screen.blit(order_text, (35, 30 + (30 * i)))
                i += 1


class Pizza:
    """
    Class to display pizza, update its position and toppings.
    """

    def __init__(self, screen):
        """
        Initialize Pizza on display.
        Args:
            screen: a Surface to display on to.
        """
        x_pos = 230
        # pygame.draw.ellipse(screen, (235, 198, 52), (x_pos, 700, 120, 70))
        dough_surf = pygame.image.load("assets/img/pizza_dough.png")
        self.pizza_dough = pygame.transform.scale_by(dough_surf, 0.27)
        pygame.Surface.blit(screen, self.pizza_dough, (x_pos, 600))

    def update(self, screen):
        """
        Update Pizza location on display.
        Args:
            screen: a Surface to display on to.
        """
        pos = gm.PizzaStatus.get_position(self)
        x_pos = pos[0]
        # pygame.draw.ellipse(screen, (235, 198, 52), (x_pos, 700, 120, 70))
        dough_surf = pygame.image.load("assets/img/pizza_dough.png")
        self.pizza_dough = pygame.transform.scale_by(dough_surf, 0.27)
        pygame.Surface.blit(screen, self.pizza_dough, (x_pos, 600))

    def add_topping(self, topping):
        """
        Docstring
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
        self.sprite_top_list = []
        self._order_status = gm.OrderStatus(4)

    def create_topping(self, screen, database):
        """
        Spawns a random topping at the top of the screen at a random x-value.
        Attributes:
            random_topping: the output of the model class
            ToppingPosition.spawn_topping
            screen: the surface to draw the topping on

        """
        mushroom_image = pygame.image.load(
            os.path.join("assets/img", "mushroom.png")
        ).convert()
        pepperoni_image = pygame.image.load(
            os.path.join("assets/img", "pepperoni.png")
        ).convert()
        sauce_image = pygame.image.load(
            os.path.join("assets/img", "sauce.png")
        ).convert()

        mushroom_image.set_colorkey(mushroom_image.get_at((0, 0)))
        pepperoni_image.set_colorkey(pepperoni_image.get_at((0, 0)))
        sauce_image.set_colorkey(sauce_image.get_at((0, 0)))
        mushroom_image = pygame.transform.smoothscale(
            mushroom_image, (120, 120)
        )
        pepperoni_image = pygame.transform.smoothscale(
            pepperoni_image, (120, 120)
        )
        sauce_image = pygame.transform.smoothscale(sauce_image, (120, 120))

        new_top_info = database.spawn_topping()
        new_top_type = new_top_info[0]
        dimension = (120, 120)
        topping_type = new_top_type.topping_value

        topping_sprite = pygame.sprite.Sprite()
        topping_sprite.image = pygame.Surface(dimension)
        topping_image = mushroom_image
        x_pos = random.randrange(5, 470)
        y_pos = 5
        if topping_type == "Cheese":
            screen.blit(mushroom_image, (x_pos, y_pos))
            topping_image = mushroom_image
        if topping_type == "Mushroom":
            screen.blit(mushroom_image, (x_pos, y_pos))
            topping_image = mushroom_image
        if topping_type == "Pepperoni":
            screen.blit(pepperoni_image, (x_pos, y_pos))
            topping_image = pepperoni_image
        if topping_type == "Sauce":
            screen.blit(sauce_image, (x_pos, y_pos))
            topping_image = sauce_image

        new_sprite = [
            screen,
            topping_sprite,
            topping_type,
            topping_image,
            x_pos,
            y_pos,
        ]
        self.sprite_top_list.append(new_sprite)

    def move_toppings_view(self, screen):
        """
        Moves all toppings down 5 pixels
        """
        # database.move_all_toppings()

        # for sprite in self.sprite_top_list:
        #     image = sprite[3]
        #     image.rect.x = sprite[4]
        #     image.rect.y = sprite[5] + 5

        screen.blit(screen, (0, 0))

        for sprite in self.sprite_top_list:
            x_pos = sprite[4]
            y_pos = sprite[5] + 5
            sprite[5] = y_pos
            topping_image = sprite[3]
            image_rect = sprite[1].image.get_rect()
            image_rect.y = y_pos
            screen.blit(topping_image, (x_pos, y_pos))
        pygame.display.update()

    def collide_pizza(self, pizza):
        """
        Checks if any of the toppings have collided with the pizza, and if so, delete them.
        Also updates order status.
        """
        for topping in self.sprite_top_list:
            if pygame.sprite.collide_rect(topping[2], pizza):
                topping_value = topping[3]
                del topping
                return topping_value
