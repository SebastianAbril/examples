from typing import List

from core.item.domain.item import Item
from core.item.domain.item_id import ItemId
from core.shared.base.domain.uuid import UUID
from core_test.brand.domain.brand_mother import BrandMother
from core_test.item_type.domain.type_mother import TypeMother


class ItemMother:

    @staticmethod
    def random_id() -> ItemId:
        return ItemId(
            UUID.random()
        )

    @classmethod
    def random_name(cls):
        return 'any random name'

    @staticmethod
    def random_description() -> str:
        return 'any random description'

    @staticmethod
    def random_price() -> float:
        return 1000

    @staticmethod
    def random_picture_file_name() -> str:
        return 'picture_fileName'

    @staticmethod
    def random_item(description: str = '') -> Item:
        item_id = ItemMother.random_id()
        brand_id = BrandMother.random_id()
        type_id = TypeMother.random_id()
        name = ItemMother.random_name()
        description = ItemMother.random_description() + description
        picture_file_name = ItemMother.random_picture_file_name()
        price = ItemMother.random_price()
        return Item(
            item_id,
            brand_id,
            type_id,
            name,
            description,
            picture_file_name,
            price
        )

    @staticmethod
    def random_item_with_this_price(price: float) -> Item:
        item_id = ItemMother.random_id()
        brand_id = BrandMother.random_id()
        type_id = TypeMother.random_id()
        name = ItemMother.random_name()
        description = ItemMother.random_description()
        picture_file_name = ItemMother.random_picture_file_name()
        return Item(
            item_id,
            brand_id,
            type_id,
            name,
            description,
            picture_file_name,
            price
        )

    @staticmethod
    def random_items(number_of_items: int) -> List[Item]:
        item_list = []
        range_items = range(number_of_items)
        for i in range_items:
            item_list.append(
                ItemMother.random_item(' ' + str(i))
            )
        return item_list
