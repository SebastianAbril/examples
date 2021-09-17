from core.brand.domain.brand_id import BrandId
from core.shared.base.domain.aggregate_root import AggregateRoot


class Brand(AggregateRoot):
    _brand_id: BrandId
    _name: str

    def __init__(self, brand_id: BrandId, name: str):
        super().__init__()
        self._brand_id = brand_id
        self._name = name

    @property
    def brand_id(self) -> BrandId:
        return self._brand_id

    @property
    def name(self) -> str:
        return self._name

