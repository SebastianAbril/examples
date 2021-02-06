from core.brand.domain.brand_id import BrandId
from core.item.domain.item import Item
from core.item.domain.item_id import ItemId
from core.item.domain.item_repository import ItemRepository
from core.type.domain.type_id import TypeId


class CreateItem:
    _item_repository: ItemRepository

    def __init__(self, catalog_item_repository: ItemRepository):
        self._item_repository = catalog_item_repository

    def execute(self, item_id: ItemId, brand_id: BrandId, type_id: TypeId, description: str, picture_file_name: str,
                price: float):
        item = Item.create(
            item_id, brand_id, type_id, description, picture_file_name, price
        )

        self._item_repository.store(item)
