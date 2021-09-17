from core.type.domain.type_id import TypeId
from core.shared.base.domain.aggregate_root import AggregateRoot


class Type(AggregateRoot):
    _type_id: TypeId
    _name: str

    def __init__(self, type_id: TypeId, name: str):
        super().__init__()
        self._type_id = type_id
        self._name = name

    @property
    def type_id(self) -> TypeId:
        return self._type_id

    @property
    def name(self) -> str:
        return self._name

