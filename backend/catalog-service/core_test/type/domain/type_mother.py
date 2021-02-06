from core.shared.base.domain.uuid import UUID
from core.type.domain.type_id import TypeId


class TypeMother:
    @staticmethod
    def random_id() -> TypeId:
        return TypeId(
            UUID.random()
        )
