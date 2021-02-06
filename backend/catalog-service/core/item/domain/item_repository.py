from abc import ABCMeta, abstractmethod

from core.item.domain.item import Item
from core.item.domain.item_id import ItemId


class ItemRepository(metaclass=ABCMeta):

    @abstractmethod
    def find_by_id(self, item_id: ItemId) -> Item:
        pass

    @abstractmethod
    def store(self, item: Item) -> None:
        pass
