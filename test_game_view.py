"""
Unit tests for game_view class.
"""

import pytest
import pygame
import game_view as gv

def test_collision_length_less_than_zero():
    """
    Check that function returns None type if collision doesn't occur.

    Returns:
        A boolean. True if no collision is accurately detected.
    """
    screen = pygame.display.set_mode((10,10))
    topping_group = pygame.sprite.Group()
    pizza = gv.Pizza(screen)
    collision = gv.Toppings().collide_pizza(pizza, topping_group)

    return collision is None


@pytest.mark.parametrize(
    "func",
    [
        test_collision_length_less_than_zero,
    ],
)
def test_Topping(func):  # pylint: disable=invalid-name
    """
    Check that the Topping class in game_view is working as intended.

    Args:
        func: A function that returns a boolean, used to test various
    functionality of the Topping class.
    """
    assert func()
