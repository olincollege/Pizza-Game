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
        "basil": 0,
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
        "basil": maximum,
        "mushroom": maximum,
    }
    return order.check_order(pizza_status)


def check_access_order():
    """
    Check that an order can be accessed as a dictionary outside of OrderStatus.

    Returns:
        True if order.order_dict is a dictionary, False otherwise.
    """
    order = gmo.OrderStatus(1)
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

def check_access_status():
    """
    Check that a pizza's toppings can be accessed as a dictionary.

    Returns:
        True if pizza.status is a dictionary, False otherwise.
    """
    pizza = gmo.PizzaStatus()
    return isinstance(pizza.status, dict)

def check_add_topping():
    """
    Checks that the add_topping function in PizzaStatus is working as intended.

    Returns:
        True if add toppings correctly increases a specific topping on a pizza
    by 1.
    """
    pizza = gmo.PizzaStatus()
    test_pizza = {
        "sauce": 1,
        "cheese": 2,
        "pepperoni": 0,
        "basil": 0,
        "mushroom": 1,
    }
    pizza.add_topping("sauce")
    pizza.add_topping("cheese")
    pizza.add_topping("cheese")
    pizza.add_topping("mushroom")
    return test_pizza == pizza.status

def check_update_postion_right_side():
    """
    Checks that the update_position function stops pizzas from leaving screen.

    Returns:
        True if a call to update_position with a big positive x_update value
    results in new_pos being a list equal to [360, 150].
    """
    pizza = gmo.PizzaStatus()
    pizza.update_position(1000)
    return pizza.position == [360, 150]

def check_update_postion_left_side():
    """
    Checks that the update_position function stops pizzas from leaving screen.

    Returns:
        True if a call to update_position with a big negative x_update value
    results in new_pos being a list equal to [0, 150].
    """
    pizza = gmo.PizzaStatus()
    pizza.update_position(-1000)
    return pizza.position == [0, 150]

@pytest.mark.parametrize(
    "func",
    [
        check_access_status,
        check_add_topping,
        check_update_postion_right_side,
        check_update_postion_left_side,
    ],
)
def test_PizzaStatus(func):  # pylint: disable=invalid-name
    """
    Check that the PizzaStatus class in game_model is working as intended

    Args:
        func: A function that returns a boolean, used to test various
    functionality of the PizzaStatus class.
    """
    assert func()
