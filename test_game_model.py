"""
Unit tests for game_model class.
"""

import pytest
import game_model as gmo


def check_check_order_incomplete():
    """
    Check that an incomplete order is correctly identified.

    Returns:
        True if check_order correctly identifies the pizza as being incomplete.
    """
    maximum = 4
    order = gmo.OrderStatus(maximum)
    pizza_status = {
        "sauce": 0,
        "cheese": 0,
        "pepperoni": 0,
        "mushroom": 0,
    }
    return not order.check_order(pizza_status)


def check_check_order_complete():
    """
    Check that a complete order is correctly identified.

    Returns:
        True if check_order correctly identifies the pizza as being complete.
    """
    maximum = 4
    order = gmo.OrderStatus(maximum)
    pizza_status = {
        "sauce": maximum,
        "cheese": maximum,
        "pepperoni": maximum,
        "mushroom": maximum,
    }
    return order.check_order(pizza_status)


def check_access_order():
    """
    Check that an order can be accessed as a dictionary outside of OrderStatus.
    """
    order = gmo.OrderStatus(0)
    return isinstance(order.order_dict, dict)


@pytest.mark.parametrize(
    "func",
    [
        check_check_order_incomplete,
        check_check_order_complete,
        check_access_order,
    ],
)
def test_OrderStatus(func):  # pylint: disable=invalid-name
    """
    Check that the OrderStatus class in game_model is working as intended

    Args:
        func: A function that returns a boolean, used to test various
             functionality of the OrderStatus class.
    """
    assert func()

