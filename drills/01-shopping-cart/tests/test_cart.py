# Write your tests here. Start with requirement 1 in README.md.
# Your first line will probably be:  from cart import ShoppingCart
import pytest
from cart import ShoppingCart
from items import Items
from functools import reduce

@pytest.fixture()
def starting_cart():
    return ShoppingCart("Liem")

def test_new_cart_has_default_total_zero(starting_cart):
    cart = starting_cart     
    assert cart.total == 0

def test_new_cart_has_fixture_name(starting_cart):
    cart = starting_cart 
    assert cart.owner == "Liem"

@pytest.mark.parametrize("given_items, expected_total, expected_items", [([("pig", 10), ("horse", 20)], 30, {"pig": (10, 1), "horse": (20, 1)}), ([("pig", 10000), ("pig", 10000)], 20000, {"pig": (10000, 2)})])
def test_add_item_and_get_correct_total(starting_cart, given_items, expected_total, expected_items):
    cart = starting_cart 

    for name, price in given_items:
        cart.add_item(name, price)

    assert cart.items == expected_items
    assert cart.total == expected_total

def test_item_price_less_than_zero_raises_value_error(starting_cart):
    with pytest.raises(ValueError):
        starting_cart.add_item("Fake Item", -100)

    assert len(starting_cart.items) == 0

def test_add_same_item_and_get_it_twice(starting_cart):
    starting_cart.add_item("Fishing Rod", 100)
    starting_cart.add_item("Fishing Rod", 100)


    assert starting_cart.total == 200
    assert starting_cart.items == {"Fishing Rod": (100, 2)}

def test_delete_item_not_in_items_raises_value_error(starting_cart):
    with pytest.raises(ValueError):
        starting_cart.remove_item("hello")

    starting_cart.add_item("Fishing Rod", 100)
    starting_cart.add_item("Fishing Rod", 100)
    starting_cart.remove_item("Fishing Rod")
    
    assert starting_cart.items == {"Fishing Rod": (100, 1)}
    assert starting_cart.total == 100

@pytest.mark.parametrize("name, price, number_apples, expected_price, expected_item", [("apple", 100, 3, 200, {"apple": (100, 3)}), ("apple", 200, 6, 800, {"apple": (200, 6)})])
def test_apples_are_buy_three_for_price_of_two(starting_cart, name, price, number_apples, expected_price, expected_item):
    for i in range(number_apples):
        starting_cart.add_item(name, price)

    assert starting_cart.items == expected_item
    assert starting_cart.total == expected_price
