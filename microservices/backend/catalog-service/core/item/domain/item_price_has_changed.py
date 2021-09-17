from core.shared.bus.domain.domain_event import DomainEvent


class ItemPriceHasChanged(DomainEvent):
    _new_price: float
    _old_price: float

    def __init__(self, new_price: float, old_price: float):
        super().__init__()
        self._new_price = new_price
        self._old_price = old_price

    def body(self) -> dict:
        return {
            'newPrice': self._new_price,
            'oldPrice': self._old_price
        }
