# Drill 1: Shopping cart

Practise plain Python with tests first. No mocks in this drill.

## Requirements

Build these in order, one test at a time.

1. A new cart has a total of `0`.
2. `add_item(name, price_in_pence)` adds an item, and `total()` returns the sum.
3. Adding the same item twice counts it twice.
4. A price of zero or less raises `ValueError`.
5. `remove_item(name)` removes one of that item. Removing an item that isn't in the cart raises `ValueError`.
6. **Offer:** apples are "buy 3, pay for 2".

## Rules

- Prices are in pence (integers), not pounds (floats).
- Name each test as a sentence that describes the behaviour.
- Say what you're doing out loud as you go.
- Stuck for more than about 5 minutes? Ask for a hint.

## For each requirement

1. Write a test in `tests/test_cart.py`.
2. Run the tests and watch the new one **fail**.
3. Write just enough code in `src/cart.py` to make it **pass**.
4. Run the tests again, then move on.

## Running the tests

    cd ~/interview-starter-python
    source .venv/bin/activate
    cd drills/01-shopping-cart
    pytest -v

Until you've written your first test, pytest will say "no tests ran". That's expected.
