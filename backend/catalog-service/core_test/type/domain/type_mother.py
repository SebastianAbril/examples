from typing import List

from core.shared.base.domain.uuid import UUID
from core.type.domain.type import Type
from core.type.domain.type_id import TypeId


class TypeMother:
    @staticmethod
    def random_id() -> TypeId:
        return TypeId(
            UUID.random()
        )

    @staticmethod
    def random_types() -> List[Type]:
        type_list = [
            Type(
                type_id=TypeMother.random_id(),
                name='any_type_1'
            ),
            Type(
                type_id=TypeMother.random_id(),
                name='any_type_2'
            )
        ]

        return type_list
