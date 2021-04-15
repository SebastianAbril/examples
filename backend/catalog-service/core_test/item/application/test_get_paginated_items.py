from unittest import TestCase

from hamcrest import assert_that, not_none, equal_to

from core.item.application.get_paginated_items import GetPaginatedItems
from core.item.domain.item_repository import ItemRepository
from core.item.infrastructure.in_memory_item_repository import InMemoryItemRepository
from core_test.item.domain.item_mother import ItemMother


class TestGetPaginatedItems(TestCase):
    get_paginated_items: GetPaginatedItems
    item_repository: ItemRepository

    def test_get_paginated_items(self):
        page = 0
        size = 1
        number_of_items = 3
        items = ItemMother.random_items(number_of_items)

        self.given_a_get_paginated_items_use_case()
        self.and_items_in_the_repository(items)

        paginated_items = self.when_get_paginated_items_is_executed(page, size)

        self.then_the_paginated_items_has_this_information(number_of_items, page, paginated_items, size)

    def given_a_get_paginated_items_use_case(self):
        self.item_repository = InMemoryItemRepository()
        self.get_paginated_items = GetPaginatedItems(self.item_repository)

    def when_get_paginated_items_is_executed(self, page, size):
        paginated_items = self.get_paginated_items.execute(size, page)
        return paginated_items

    def and_items_in_the_repository(self, items):
        for item in items:
            self.item_repository.store(item)

    def then_the_paginated_items_has_this_information(self, number_of_items, page, paginated_items, size):
        assert_that(paginated_items, not_none())
        assert_that(paginated_items.total_pages, equal_to(number_of_items))
        assert_that(paginated_items.current_page, equal_to(page))
        assert_that(paginated_items.total_items, equal_to(number_of_items))
        assert_that(len(paginated_items.data), equal_to(size))
