from core.item.domain.item_id import ItemId
from core.item.domain.item_repository import ItemRepository
from core.shared.bus.domain.event_bus import EventBus


class ChangePriceItem:
    _event_bus: EventBus
    _item_repository: ItemRepository

    def __init__(self, item_repository: ItemRepository, event_bus: EventBus):
        self._event_bus = event_bus
        self._item_repository = item_repository

    def execute(self, item_id: ItemId, price: float):
        item = self._item_repository.find_by_id(item_id)

        item.change_price(price)

        self._item_repository.store(item)
        self._event_bus.publish(item.pull_domain_events())
