from unittest.mock import Mock

import pytest

from checkout import Checkout


def test_charges_the_payment_gateway_and_reports_paid():
    fake_payment_gateway = Mock()
    fake_payment_gateway.charge.return_value = True

    assert Checkout(fake_payment_gateway).pay(500) == "paid"
    fake_payment_gateway.charge.assert_called_once_with(500)


def test_reports_declined_when_the_gateway_refuses():
    fake_payment_gateway = Mock()
    fake_payment_gateway.charge.return_value = False

    assert Checkout(fake_payment_gateway).pay(500) == "declined"


def test_rejects_a_non_positive_amount_without_charging():
    fake_payment_gateway = Mock()

    with pytest.raises(ValueError, match="Amount must be positive"):
        Checkout(fake_payment_gateway).pay(0)
    fake_payment_gateway.charge.assert_not_called()
