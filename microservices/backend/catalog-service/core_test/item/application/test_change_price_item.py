import unittest
from unittest.mock import create_autospec

from hamcrest import assert_that, not_none, equal_to

from core.item.application.change_price_item import ChangePriceItem
from core.item.domain.item_repository import ItemRepository
from core.item.infrastructure.in_memory_item_repository import InMemoryItemRepository
from core.shared.bus.domain.event_bus import EventBus
from core_test.item.domain.item_mother import ItemMother


class TestChangePriceItem(unittest.TestCase):
    change_price: ChangePriceItem
    item_repository: ItemRepository
    event_bus: EventBus

    def test_change_price_item(self):
        new_price = 2000
        old_price = 500
        item = ItemMother.random_item_with_this_price(old_price)

        self.given_a_change_price_item_use_case()
        self.and_a_stored_item_in_the_database(item)

        self.when_changing_the_price(item, new_price)

        self.then_item_change_the_price(item, new_price)
        self.then_change_price_has_changed_event_was_record(new_price, old_price)

    def test_change_price_item_for_the_same_value(self):
        new_price = 500
        old_price = 500
        item = ItemMother.random_item_with_this_price(old_price)

        self.given_a_change_price_item_use_case()
        self.and_a_stored_item_in_the_database(item)

        self.when_changing_the_price(item, new_price)

        self.then_item_change_the_price(item, new_price)
        self.then_change_price_has_changed_event_was_not_fired()

    def given_a_change_price_item_use_case(self):
        self.item_repository = InMemoryItemRepository()
        self.event_bus = create_autospec(EventBus)
        self.change_price_item = ChangePriceItem(self.item_repository, self.event_bus)

    def and_a_stored_item_in_the_database(self, item):
        self.item_repository.store(item)

    def when_changing_the_price(self, item, new_price):
        self.change_price_item.execute(item.item_id, new_price)

    def then_item_change_the_price(self, item, new_price):
        save_item = self.item_repository.find_by_id(item.item_id)
        assert_that(save_item, not_none())
        assert_that(save_item.item_id, equal_to(item.item_id))
        assert_that(save_item.brand_id, equal_to(item.brand_id))
        assert_that(save_item.type_id, equal_to(item.type_id))
        assert_that(save_item.name, equal_to(item.name))
        assert_that(save_item.description, equal_to(item.description))
        assert_that(save_item.picture_file_name, equal_to(item.picture_file_name))
        assert_that(save_item.price, equal_to(new_price))

    def then_change_price_has_changed_event_was_record(self, new_price: float, old_price: float):
        events = self.event_bus.publish.call_args[0][0]
        assert_that(len(events), equal_to(1))
        assert_that(events[0].event_type, equal_to('ItemPriceHasChanged'))
        assert_that(events[0].body(), equal_to({
            'newPrice': new_price,
            'oldPrice': old_price
        }))

    def then_change_price_has_changed_event_was_not_fired(self):
        events = self.event_bus.publish.call_args[0][0]
        assert_that(len(events), equal_to(0))



if __name__ == '__main__':
    unittest.main()
