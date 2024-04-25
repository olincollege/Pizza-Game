import pygame
import game_model as gm

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
    def __init__(self):
        sprite = gm.PizzaSprite()
        pygame.blit(sprite.pizza_rect, gm.PizzaStatus._position)

    def update(self):
        pass

class Toppings():
    def __init__(self):
        self.top_info = gm.ToppingPosition.__init__
    
    def create_topping(self):
        new_top_info = self.top_info.spawn_topping
        new_top_type = new_top_info[0]
        color = gm.new_top_type.color
        dimension = gm.new_top_type.bounding_box
        pos_x = new_top_info[1]
        pos_y = new_top_info[2]
        pygame.draw.rect(color, (dimension[1], dimension[2], pos_x, pos_y))
    
    def move_toppings_view(self):
        self.top_info.move_all_toppings
        for topping in self.top_info:
            new_top_type = topping[0]
            color = gm.new_top_type.color
            dimension = gm.new_top_type.bounding_box
            pos_x = topping[1]
            pos_y = topping[2]
            pygame.draw.rect(color, (dimension[1], dimension[2], pos_x, pos_y))
    
    def collide_pizza(self,pizza):






    



class Cheese(Toppings):

class Sauce(Toppings):

class Basil(Toppings):

class Mushroom(Toppings):