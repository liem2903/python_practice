class ShoppingCart(): 
    def __init__(self, owner: str, balance: int = 0, total: int = 0) -> None:
        self.owner = owner
        self._total = total
        self._items: dict[str, tuple[int, int]] = {}

    @property
    def items(self) -> dict[str, tuple[int, int]]:
        return self._items
    @property
    def total(self) -> int:
        sum_before_apple = sum(i[0] * i[1] for i in self._items.values())

        return sum_before_apple if "apple" not in self._items else sum_before_apple - ((self._items["apple"][1] // 3) * (self._items["apple"][0]))
 
    def add_item(self, name, price) -> None: 
        if price <= 0:
            raise ValueError("Item price can not exist")
            
        if name not in self._items:
            self._items[name] = (price, 1)        
        else:
            old_price, old_amount = self._items[name]
            self._items[name] = (old_price, old_amount + 1)

    def remove_item(self, name: str):
        if name not in self._items:
            raise ValueError("The value is not in items")

        if self._items[name][1] == 1:
            del self._items[name]
        else:
            old_price, old_amount = self._items[name]
            self._items[name] = (old_price, old_amount - 1)
