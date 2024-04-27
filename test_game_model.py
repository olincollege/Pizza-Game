"""
Unit tests for game_model class.
"""

import pytest
import game_model as gmo


def check_check_order():
    """
    Check that a complete order is correctly marked.

    Args:
        pizza_status: A string representing the user's username.

    Returns:
        True if user.username exists and False otherwise.
    """
    order = gmo.OrderStatus()
    order.order_dict = {
        "sauce": 2,
        "cheese": 3,
        "pepperoni": 4,
        "mushroom": 5,
    }
    pizza_status = {
        "sauce": 1,
        "cheese": 1,
        "pepperoni": 1,
        "mushroom": 1,
    }
    return not order.check_order(pizza_status)


def check_get_order():
    """
    Check that a topping  has the username property.

    Args:
        username: A string representing the user's username.

    Returns:
        True if user.username exists and False otherwise.
    """
    order = gmo.OrderStatus()
    return order.order_dict == order.get_order()


@pytest.mark.parametrize(
    "func",
    [check_check_order, check_get_order],
)
def test_OrderStatus(func):
    """
    Check that post IDs are generated correctly.

    This is used to test Problem 2.3 (Moving the Post Goals).

    Args:
        func: A function that returns a boolean, used to test various
             functionality of the user's post history.
    """
    assert func()
