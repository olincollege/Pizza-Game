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

def check_clear_pizza():
    """
    Checks that the clear_topping function removes every topping from a pizza.

    Returns:
        True if a call to clear_topping on a PizzaStatus instance results in
    __current_toppings being a dictionary with every value equaling zero.
    """
    pizza = gmo.PizzaStatus()
    pizza.add_topping("sauce")
    pizza.add_topping("cheese")
    pizza.add_topping("cheese")
    pizza.add_topping("mushroom")
    pizza.clear_pizza()
    count = 0
    for num in pizza.status.values():
        count += num
    return count == 0

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
        check_clear_pizza,
    ],
)
def test_PizzaStatus(func):  # pylint: disable=invalid-name
    """
    Check that the PizzaStatus class in game_model is working as intended.

    Args:
        func: A function that returns a boolean, used to test various
    functionality of the PizzaStatus class.
    """
    assert func()

def check_evaluate_perfect_order():
    """
    Check that a perfect order leads to a __customer_happiness value of zero.

    Returns:
        True if a perfectly filled order results in the __customer_happiness
    having a value of zero, False otherwise.
    """
    money = gmo.Money()
    order = gmo.OrderStatus(1)
    pizza = gmo.PizzaStatus()
    # populates PizzaStatus with toppings to fill out order correctly.
    for topping, num in order.order_dict.items():
        if num == 1:
            pizza.add_topping(topping)
    money.evaluate_order(order, pizza)
    return money.customer_happiness == 0

def check_evaluate_imperfect_order():
    """
    Check an imperfect order leading to a __customer_happiness value of zero.

    Returns:
        True if a perfectly imperfect order results in the __customer_happiness
    having a value of one, False otherwise.
    """
    money = gmo.Money()
    order = gmo.OrderStatus(1)
    pizza = gmo.PizzaStatus()
    money.evaluate_order(order, pizza)
    return money.customer_happiness == 1.0

def check_get_perfect_tip():
    """
    Check that a perfect order's tip equals the number of toppings times 1.5.

    Returns:
        True if the tip of a perfect order is equal to 1.5 times the number of
    toppings that are in the order, False otherwise.
    """
    money = gmo.Money()
    order = gmo.OrderStatus(1)
    pizza = gmo.PizzaStatus()
    # populates PizzaStatus with toppings to fill out order correctly.
    for topping, num in order.order_dict.items():
        if num == 1:
            pizza.add_topping(topping)
    return money.get_tip(order, pizza) == money.desired_toppings * 1.5

def check_get_imperfect_tip():
    """
    Check that a perfect order's tip equals the number of toppings times 1.5.

    Returns:
        True if the tip for an order that is not filled out whatsoever has a
    tip of 0, False otherwise.
    """
    money = gmo.Money()
    order = gmo.OrderStatus(1)
    pizza = gmo.PizzaStatus()
    return money.get_tip(order, pizza) == 0

def check_update_money_perfect():
    """
    Check that an order with a nonzero tip changes the value of __total_money.

    Returns:
        True if the value of __total_money is greater than 0 after a call to
    get_tip on a completed order, False otherwise.
    """
    money = gmo.Money()
    order = gmo.OrderStatus(1)
    pizza = gmo.PizzaStatus()
    # populates PizzaStatus with toppings to fill out order correctly.
    for topping, num in order.order_dict.items():
        if num == 1:
            pizza.add_topping(topping)
    money.update_money(order, pizza)
    return money.get_money > 0

def check_update_money_imperfect():
    """
    Check that order with zero tip does not change the value of __total_money.

    Returns:
        True if the value of __total_money is 0 after a call to get_tip on an
    incomplete order, False otherwise.
    """
    money = gmo.Money()
    order = gmo.OrderStatus(1)
    pizza = gmo.PizzaStatus()
    # populates PizzaStatus with toppings to fill out order correctly.
    for topping, num in order.order_dict.items():
        if num == 1:
            pizza.add_topping(topping)
    money.update_money(order, pizza)
    return money.get_money > 0
@pytest.mark.parametrize(
    "func",
    [
        check_evaluate_perfect_order,
        check_evaluate_imperfect_order,
        check_get_perfect_tip,
        check_get_imperfect_tip,
        check_update_money_perfect,
        check_update_money_imperfect,
    ],
)

def test_Money(func):  # pylint: disable=invalid-name
    """
    Check that the Money class in game_model is working as intended.

    Args:
        func: A function that returns a boolean, used to test various
    functionality of the Money class.
    """
    assert func()