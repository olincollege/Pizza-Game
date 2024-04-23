"""
Unit tests for game_model class.
"""

import pytest
import game_model as gmo


def check_topping_name():
    """
    Check that a topping  has the username property.

    Args:
        username: A string representing the user's username.

    Returns:
        True if user.username exists and False otherwise.
    """
    topping = gmo.Pepper()
    return topping.value == "Pepper"


def check_topping_nombre():
    """
    Check that a topping  has the username property.

    Args:
        username: A string representing the user's username.

    Returns:
        True if user.username exists and False otherwise.
    """
    topping = gmo.Pepper()
    print(topping.value)
    return topping.value == "Pepper"


def check_one_equals_one():
    return 1 == 1


@pytest.mark.parametrize(
    "func",
    [check_topping_name, check_topping_nombre, check_one_equals_one],
)
def test_toppings(func):
    """
    Check that post IDs are generated correctly.

    This is used to test Problem 2.3 (Moving the Post Goals).

    Args:
        func: A function that returns a boolean, used to test various
             functionality of the user's post history.
    """
    assert func()
