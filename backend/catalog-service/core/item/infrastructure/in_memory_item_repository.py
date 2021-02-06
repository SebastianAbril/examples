from core.item.domain.item import Item
from core.item.domain.item_id import ItemId
from core.item.domain.item_repository import ItemRepository


class InMemoryItemRepository(ItemRepository):

    def __init__(self):
        self._database = {}

    def store(self, item: Item) -> None:
        self._database[item.item_id.value] = item
        pass

    def find_by_id(self, item_id: ItemId) -> Item:
        return self._database.get(item_id.value)
