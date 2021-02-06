from core.item.domain.item import Item
from core.item.domain.item_id import ItemId
from core.shared.base.domain.uuid import UUID
from core_test.brand.domain.brand_mother import BrandMother
from core_test.type.domain.type_mother import TypeMother


class ItemMother:

    @staticmethod
    def random_id() -> ItemId:
        return ItemId(
            UUID.random()
        )

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
    def random_item() -> Item:
        item_id = ItemMother.random_id()
        brand_id = BrandMother.random_id()
        type_id = TypeMother.random_id()
        description = ItemMother.random_description()
        picture_file_name = ItemMother.random_picture_file_name()
        price = ItemMother.random_price()
        return Item(
            item_id,
            brand_id,
            type_id,
            description,
            picture_file_name,
            price
        )

    @staticmethod
    def random_item_with_this_price(price: float) -> Item:
        item_id = ItemMother.random_id()
        brand_id = BrandMother.random_id()
        type_id = TypeMother.random_id()
        description = ItemMother.random_description()
        picture_file_name = ItemMother.random_picture_file_name()
        return Item(
            item_id,
            brand_id,
            type_id,
            description,
            picture_file_name,
            price
        )
