from core.brand.domain.brand_id import BrandId
from core.item.domain.item_id import ItemId
from core.item.domain.item_price_has_changed import ItemPriceHasChanged
from core.shared.base.domain.aggregate_root import AggregateRoot
from core.type.domain.type_id import TypeId


class Item(AggregateRoot):
    _item_id: ItemId
    _brand_id: BrandId
    _type_id: TypeId
    _description: str
    _picture_file_name: str
    _price: float

    def __init__(self, item_id: ItemId, brand_id: BrandId, type_id: TypeId, description: str, picture_file_name: str,
                 price: float):
        super().__init__()
        self._item_id = item_id
        self._brand_id = brand_id
        self._type_id = type_id
        self._description = description
        self._picture_file_name = picture_file_name
        self._price = price

    @staticmethod
    def create(item_id: ItemId, brand_id: BrandId, type_id: TypeId, description: str, picture_file_name: str,
               price: float):
        return Item(
            item_id, brand_id, type_id, description, picture_file_name, price
        )

    def change_price(self, price: float) -> None:
        if self._price != price:
            self.record(
                ItemPriceHasChanged(
                    new_price=price,
                    old_price=self._price
                )
            )
        self._price = price

    @property
    def item_id(self) -> ItemId:
        return self._item_id

    @property
    def brand_id(self) -> BrandId:
        return self._brand_id

    @property
    def type_id(self) -> TypeId:
        return self._type_id

    @property
    def description(self) -> str:
        return self._description

    @property
    def picture_file_name(self) -> str:
        return self._picture_file_name

    @property
    def price(self) -> float:
        return self._price
