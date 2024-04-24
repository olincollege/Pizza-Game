import pygame
import game_model

"""
Classes for viewing the game.
"""

class HomeScreen():
    """
    DOC STRING
    """
    def __init__(self):
        homescreen = pygame.image.load('assests/img/homescreen.png')
        screen.blit(homescreen, (0, 0))

class Button(HomeScreen):

class StartButton(Button):

class InstructionButton(Button):

class Kitchen():

class Order():

class Pizza():
    def __init__(self, x, y):
        img = pygame.image.load('assets/img/pizza.png')

    def update(self):

class Toppings():
    def __init__(self):
        top_info = game_model.ToppingPosition.__init__
    
    def create_topping(self):
        new_top_info = game_model.ToppingPosition.spawn_topping
        new_top_type = new_top_info[0]
        color = game_model.new_top_type.color
        dimension = game_model.new_top_type.bounding_box
        pos_x = new_top_info[1]
        pos_y = new_top_info[2]
        pygame.draw.rect(color, (dimension[1], dimension[2], pos_x, pos_y))


class Cheese(Toppings):

class Sauce(Toppings):

class Basil(Toppings):

class Mushroom(Toppings):