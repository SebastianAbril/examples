import unittest

from hamcrest import assert_that, not_none, equal_to

from core.item.application.create_item import CreateItem
from core.item.domain.item_repository import ItemRepository
from core.item.infrastructure.in_memory_item_repository import InMemoryItemRepository
from core_test.brand.domain.brand_mother import BrandMother
from core_test.item.domain.item_mother import ItemMother
from core_test.item_type.domain.type_mother import TypeMother


class TestCreateItem(unittest.TestCase):
    create_item: CreateItem
    item_repository: ItemRepository

    def test_create_a_catalog_item(self):
        item_id = ItemMother.random_id()
        brand_id = BrandMother.random_id()
        type_id = TypeMother.random_id()
        description = ItemMother.random_description()
        picture_file_name = ItemMother.random_picture_file_name()
        price = ItemMother.random_price()

        item_repository = InMemoryItemRepository()
        create_item = CreateItem(item_repository)

        create_item.execute(
            item_id,
            brand_id,
            type_id,
            description,
            picture_file_name,
            price
        )

        save_item = item_repository.find_by_id(item_id)
        assert_that(save_item, not_none())
        assert_that(save_item.item_id, equal_to(item_id))
        assert_that(save_item.brand_id, equal_to(brand_id))
        assert_that(save_item.type_id, equal_to(type_id))
        assert_that(save_item.description, equal_to(description))
        assert_that(save_item.picture_file_name, equal_to(picture_file_name))
        assert_that(save_item.price, equal_to(price))


if __name__ == '__main__':
    unittest.main()
