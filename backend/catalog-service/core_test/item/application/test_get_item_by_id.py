from unittest import TestCase

from hamcrest import assert_that, not_none, equal_to

from core.item.application.get_item_by_id import GetItemById
from core.item.application.get_paginated_items import GetPaginatedItems
from core.item.domain.item import Item
from core.item.domain.item_id import ItemId
from core.item.domain.item_repository import ItemRepository
from core.item.infrastructure.in_memory_item_repository import InMemoryItemRepository
from core_test.item.domain.item_mother import ItemMother


class TestGetItemById(TestCase):
    get_item_by_id: GetItemById
    item_repository: ItemRepository

    def test_get_item_by_id(self):
        item = ItemMother.random_item()

        self.given_a_get_item_by_id_use_case()
        self.and_items_in_the_repository(item)

        item_response = self.when_get_item_by_id_is_executed(item.item_id)

        self.then_the_item_response_has_this_information(item, item_response)

    def given_a_get_item_by_id_use_case(self):
        self.item_repository = InMemoryItemRepository()
        self.get_item_by_id = GetItemById(self.item_repository)

    def and_items_in_the_repository(self, item):
        self.item_repository.store(item)

    def when_get_item_by_id_is_executed(self, item_id: ItemId):
        item_response = self.get_item_by_id.execute(item_id)
        return item_response

    def then_the_item_response_has_this_information(self, item: Item, item_response: Item):
        assert_that(item_response, not_none())
        assert_that(item_response.item_id, equal_to(item.item_id))
        assert_that(item_response.brand_id, equal_to(item.brand_id))
        assert_that(item_response.type_id, equal_to(item.type_id))
        assert_that(item_response.name, equal_to(item.name))
        assert_that(item_response.description, equal_to(item.description))
        assert_that(item_response.picture_file_name, equal_to(item.picture_file_name))
        assert_that(item_response.price, equal_to(item.price))