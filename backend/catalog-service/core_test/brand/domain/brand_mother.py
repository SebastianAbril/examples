from typing import List

from core.brand.domain.brand import Brand
from core.brand.domain.brand_id import BrandId
from core.shared.base.domain.uuid import UUID


class BrandMother:
    @staticmethod
    def random_id() -> BrandId:
        return BrandId(
            UUID.random()
        )

    @staticmethod
    def random_brands() -> List[Brand]:
        brand_list = [
            Brand(
                brand_id=BrandMother.random_id(),
                name='any_brand_1'
            ),
            Brand(
                brand_id=BrandMother.random_id(),
                name='any_brand_2'
            )
        ]

        return brand_list
