from typing import List

from core.brand.domain.brand import Brand
from core.brand.domain.brand_repository import BrandRepository


class InMemoryBrandRepository(BrandRepository):

    def __init__(self):
        self._database = {}

    def store(self, brand: Brand) -> None:
        self._database[brand.brand_id.value] = brand
        pass

    def find_all(self) -> List[Brand]:
        return self._database.values()

