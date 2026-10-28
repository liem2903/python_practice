# Example code to show the setup works. Delete it once the interview problem starts.
from typing import Protocol


class PaymentGateway(Protocol):
    def charge(self, amount_in_cents: int) -> bool: ...


class Checkout:
    def __init__(self, payment_gateway: PaymentGateway) -> None:
        self.payment_gateway = payment_gateway

    def pay(self, amount_in_cents: int) -> str:
        if amount_in_cents <= 0:
            raise ValueError("Amount must be positive")
        return "paid" if self.payment_gateway.charge(amount_in_cents) else "declined"
