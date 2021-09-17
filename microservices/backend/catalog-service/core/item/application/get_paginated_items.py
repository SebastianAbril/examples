from core.item.domain.item import Item
from core.item.domain.item_repository import ItemRepository
from core.shared.base.domain.paginator import Paginator


class GetPaginatedItems:
    _item_repository: ItemRepository

    def __init__(self, item_repository: ItemRepository):
        self._item_repository = item_repository

    def execute(self, size: int, page: int) -> Paginator[Item]:
        return self._item_repository.get_paginated_items(size, page)
