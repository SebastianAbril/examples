import unittest
from typing import List

from hamcrest import assert_that, equal_to, not_none

from core.type.application.get_types import GetTypes
from core.type.domain.type import Type
from core.type.domain.type_repository import TypeRepository
from core.type.infrastructure.in_memory_type_repository import InMemoryTypeRepository
from core_test.item_type.domain.type_mother import TypeMother


class TestGetTypes(unittest.TestCase):
    get_types: GetTypes
    type_repository: TypeRepository

    def test_get_types(self):
        types = TypeMother.random_types()

        self.given_a_get_types_use_case()
        self.and_a_random_types_in_the_repository(types)

        database_types = self.when_get_types_is_executed()

        self.then_the_types_has_this_information(types, database_types)

    def test_get_types_without_data_return_empty_array(self):
        self.given_a_get_types_use_case()

        database_types = self.when_get_types_is_executed()

        self.then_the_types_is_empty(database_types)

    def given_a_get_types_use_case(self):
        self.type_repository = InMemoryTypeRepository()
        self.get_types = GetTypes(self.type_repository)

    def when_get_types_is_executed(self):
        return self.get_types.execute()

    def and_a_random_types_in_the_repository(self, types):
        for type in types:
            self.type_repository.store(type)

    def then_the_types_is_empty(self, database_types):
        assert_that(database_types, not_none())
        assert_that(len(database_types), equal_to(0))

    def then_the_types_has_this_information(self, types: List[Type], database_types: List[Type]):
        assert_that(len(database_types), equal_to(len(types)))
        self.equal_type(types[0], database_types[0])
        self.equal_type(types[1], database_types[1])

    def equal_type(self, types: Type, database_types: Type):
        assert_that(database_types.type_id, equal_to(types.type_id))
        assert_that(database_types.name, equal_to(types.name))


if __name__ == '__main__':
    unittest.main()
