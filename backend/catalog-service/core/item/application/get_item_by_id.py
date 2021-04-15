from core.item.domain.item import Item
from core.item.domain.item_id import ItemId
from core.item.domain.item_repository import ItemRepository


class GetItemById:
    _item_repository: ItemRepository

    def __init__(self, item_repository: ItemRepository):
        self._item_repository = item_repository

    def execute(self, item_id: ItemId) -> Item:
        return self._item_repository.find_by_id(item_id)
