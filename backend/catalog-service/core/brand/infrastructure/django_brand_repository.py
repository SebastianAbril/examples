from typing import List, Type
from django.db import models

from core.brand.domain.brand import Brand
from core.brand.domain.brand_id import BrandId
from core.brand.domain.brand_repository import BrandRepository


class DjangoBrandRepository(BrandRepository):

    def store(self, brand: Brand) -> None:
        model = _domain_to_model(brand)
        model.save()

    def find_all(self) -> List[Brand]:
        result = _models_to_domain(BrandModel.objects.all())

        return result


class BrandModel(models.Model):
    class Meta:
        db_table = 'brand'

    id = models.UUIDField(primary_key=True, editable=False)
    name = models.CharField(max_length=200)


def _models_to_domain(model_list) -> List[Brand]:
    def mapper(model):
        return Brand(
            BrandId(str(model.id)),
            model.name
        )

    return list(map(mapper, list(model_list)))


def _domain_to_model(brand: Brand) -> Type[BrandModel]:
    model = BrandModel(
        id=brand.brand_id.value,
        name=brand.name,
    )
    return model
