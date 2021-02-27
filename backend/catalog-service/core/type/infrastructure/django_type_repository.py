from typing import List
from django.db import models
from django.db.models import Model
from core.type.domain.type import Type
from core.type.domain.type_id import TypeId
from core.type.domain.type_repository import TypeRepository


class DjangoTypeRepository(TypeRepository):

    def store(self, type: Type):
        model = _domain_to_model(type)
        model.save()

    def find_all(self) -> List[Type]:
        result = _models_to_domain(TypeModel.objects.all())

        return result


class TypeModel(models.Model):
    class Meta:
        db_table = 'type'

    id = models.UUIDField(primary_key=True, editable=False)
    name = models.CharField(max_length=200)


def _models_to_domain(model_list) -> List[Type]:
    def mapper(model):
        return Type(
            TypeId(str(model.id)),
            model.name
        )

    return list(map(mapper, list(model_list)))


def _domain_to_model(type: Type) -> Model:
    model = TypeModel(
        id=type.type_id.value,
        name=type.name,
    )
    return model
