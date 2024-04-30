import pygame
import game_model as gm
import sys

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
        screen.fill((153, 217, 234)) # background color
        title_text = pygame.image.load('assets/img/title.png')
        screen.blit(title_text, (0, 0)) # display title text

class EndScreen:
    """
    Class to display to end screen.
    """
    def __init__(self, screen):
        end_text = pygame.image.load('assets/img/end_text.png')
        screen.blit(end_text, (0, 0))

        total_money = gm.TotalMoney.get_money
        print(total_money)
        screen.blit(screen, total_money, (240, 360))

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
        font = pygame.font.Font(None, 36) # use default font

        pygame.draw.rect(screen, (255, 255, 255), (30, 25, 163, 135)) # draw white box

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
        self.pizza_status.add_topping(new_topping_added)
        font = pygame.font.Font(None, 36)

        pygame.draw.rect(screen, (255, 255, 255), (30, 25, 163, 135))

        i = 0
        while i < len(self.order_dict):
            for topping, num in self.order_dict.items():
                text = f"{topping}: {num}, {self.pizza_status.status[topping]}"
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
        self.rectangle_top_list = []
        self._order_status = gm.OrderStatus(4)

    def create_topping(self, screen, database):
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
        topping_type = new_top_type.topping_value
        pos_x = new_top_info[1]
        new_rect = [
            screen,
            color,
            pygame.Rect(pos_x, 5, dimension[0], dimension[1]),
            topping_type,
        ]
        self.rectangle_top_list.append(new_rect)

    def move_toppings_view(self):
        """
        Moves all toppings down 5 pixels
        """
        # database.move_all_toppings()
        for topping in self.rectangle_top_list:
            topping[2] = pygame.Rect.move(topping[2], 0, 5)
            pygame.draw.rect(topping[0], topping[1], topping[2])

    def collide_pizza(self, pizza):
        """
        Checks if any of the toppings have collided with the pizza, and if so, delete them.
        Also updates order status.
        """
        for topping in self.rectangle_top_list:
            if pygame.Rect.colliderect(topping[2], pizza):
                topping_value = topping[3]
                del topping
                return topping_value
