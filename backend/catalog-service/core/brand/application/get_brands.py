from typing import List

from core.brand.domain.brand import Brand
from core.brand.domain.brand_repository import BrandRepository


class GetBrands:
    _brand_repository: BrandRepository

    def __init__(self, brand_repository: BrandRepository):
        self._brand_repository = brand_repository

    def execute(self) -> List[Brand]:
        return self._brand_repository.find_all()
