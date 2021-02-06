import unittest

from hamcrest import assert_that, equal_to

from core.brand.application.get_brands import GetBrands
from core.brand.domain.brand import Brand
from core.brand.domain.brand_repository import BrandRepository
from core.brand.domain.in_memory_brand_repository import InMemoryBrandRepository
from core_test.brand.domain.brand_mother import BrandMother


class TestGetBrands(unittest.TestCase):
    get_brands: GetBrands
    brand_repository: BrandRepository

    def test_get_all_brands(self):
        self.brand_repository = InMemoryBrandRepository()
        self.get_brands = GetBrands(self.brand_repository)

        brands = BrandMother.random_brands()

        for brand in brands:
            self.brand_repository.store(brand)

        database_brands = self.get_brands.execute()

        assert_that(len(database_brands), equal_to(len(brands)))
        self.equal_brand(brands[0], database_brands[0])
        self.equal_brand(brands[1], database_brands[1])

    def equal_brand(self, brand: Brand, database_brand: Brand):
        assert_that(database_brand.brand_id, equal_to(brand.brand_id))
        assert_that(database_brand.name, equal_to(brand.name))


if __name__ == '__main__':
    unittest.main()
