from typing import List, Type
from django.db import models
from django.core.paginator import Paginator as DjangoPaginator
from core.brand.domain.brand_id import BrandId
from core.item.domain.item import Item
from core.item.domain.item_id import ItemId
from core.item.domain.item_repository import ItemRepository
from core.shared.base.domain.paginator import Paginator
from core.type.domain.type_id import TypeId


class DjangoItemRepository(ItemRepository):

    def find_by_id(self, item_id: ItemId) -> Item:
        result = ItemModel.objects.filter(id=item_id.value)
        result = _models_to_domain(result)
        if len(result) == 0:
            return None

        return result[0]

    def store(self, item: Item) -> None:
        model = _domain_to_model(item)
        model.save()

    def get_paginated_items(self, size: int, page: int) -> Paginator[Item]:
        item_list = ItemModel.objects.all()
        django_paginator = DjangoPaginator(item_list, size)

        return Paginator[Item](
            total_items=django_paginator.count,
            total_pages=django_paginator.num_pages,
            current_page=page,
            data=_models_to_domain(django_paginator.page(page + 1).object_list)
        )


class ItemModel(models.Model):
    class Meta:
        db_table = 'item'

    id = models.UUIDField(primary_key=True, editable=False)
    brand_id = models.UUIDField()
    type_id = models.UUIDField()
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    picture_file_name = models.CharField(max_length=300)
    price = models.BigIntegerField()


def _models_to_domain(model_list) -> List[Item]:
    def mapper(model: ItemModel):
        return Item(
            item_id=ItemId(str(model.id)),
            brand_id=BrandId(str(model.brand_id)),
            type_id=TypeId(str(model.type_id)),
            name=model.name,
            description=model.description,
            picture_file_name=model.picture_file_name,
            price=model.price
        )

    return list(map(mapper, list(model_list)))


def _domain_to_model(item: Item) -> Type[ItemModel]:
    model = ItemModel(
        id=item.item_id.value,
        brand_id=item.brand_id.value,
        type_id=item.type_id.value,
        name=item.name,
        description=item.description,
        picture_file_name=item.picture_file_name,
        price=item.price
    )
    return model
