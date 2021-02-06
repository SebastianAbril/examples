import unittest

from hamcrest import assert_that, equal_to, not_none

from core.brand.application.get_brands import GetBrands
from core.brand.domain.brand import Brand
from core.brand.domain.brand_repository import BrandRepository
from core.brand.infrastructure.in_memory_brand_repository import InMemoryBrandRepository
from core_test.brand.domain.brand_mother import BrandMother


class TestGetBrands(unittest.TestCase):
    get_brands: GetBrands
    brand_repository: BrandRepository

    def test_get_all_brands(self):
        brands = BrandMother.random_brands()

        self.given_a_get_brands_use_case()
        self.and_a_random_brands_in_the_repository(brands)

        database_brands = self.when_get_brands_is_executed()

        self.then_the_brands_has_this_information(brands, database_brands)

    def test_get_brands_without_data_return_empty_array(self):
        self.given_a_get_brands_use_case()

        database_brands = self.when_get_brands_is_executed()

        self.then_the_brands_is_empty(database_brands)

    def given_a_get_brands_use_case(self):
        self.brand_repository = InMemoryBrandRepository()
        self.get_brands = GetBrands(self.brand_repository)

    def when_get_brands_is_executed(self):
        database_brands = self.get_brands.execute()
        return database_brands

    def and_a_random_brands_in_the_repository(self, brands):
        for brand in brands:
            self.brand_repository.store(brand)

    def then_the_brands_has_this_information(self, brands, database_brands):
        assert_that(len(database_brands), equal_to(len(brands)))
        self.equal_brand(brands[0], database_brands[0])
        self.equal_brand(brands[1], database_brands[1])

    def then_the_brands_is_empty(self, database_brands):
        assert_that(database_brands, not_none())
        assert_that(len(database_brands), equal_to(0))

    def equal_brand(self, brand: Brand, database_brand: Brand):
        assert_that(database_brand.brand_id, equal_to(brand.brand_id))
        assert_that(database_brand.name, equal_to(brand.name))


if __name__ == '__main__':
    unittest.main()
