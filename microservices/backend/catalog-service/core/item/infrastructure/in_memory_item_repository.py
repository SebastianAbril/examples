from core.item.domain.item import Item
from core.item.domain.item_id import ItemId
from core.item.domain.item_repository import ItemRepository
from core.shared.base.domain.paginator import Paginator
from django.core.paginator import Paginator as DjangoPaginator


class InMemoryItemRepository(ItemRepository):

    def __init__(self):
        self._database = {}

    def store(self, item: Item) -> None:
        self._database[item.item_id.value] = item
        pass

    def find_by_id(self, item_id: ItemId) -> Item:
        return self._database.get(item_id.value)

    def get_paginated_items(self, size: int, page: int) -> Paginator[Item]:
        database = list(self._database.values())
        django_paginator = DjangoPaginator(database, size)

        return Paginator[Item](
            total_items=django_paginator.count,
            total_pages=django_paginator.num_pages,
            current_page=page,
            data=django_paginator.page(page + 1).object_list
        )
