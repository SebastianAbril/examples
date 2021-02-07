from abc import ABCMeta, abstractmethod

from core.item.domain.item import Item
from core.item.domain.item_id import ItemId
from core.shared.base.domain.paginator import Paginator


class ItemRepository(metaclass=ABCMeta):

    @abstractmethod
    def find_by_id(self, item_id: ItemId) -> Item:
        pass

    @abstractmethod
    def store(self, item: Item) -> None:
        pass

    @abstractmethod
    def get_paginated_items(self, size: int, page: int) -> Paginator[Item]:
        pass
