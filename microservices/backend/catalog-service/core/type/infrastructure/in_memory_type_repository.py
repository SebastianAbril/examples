from typing import List

from core.type.domain.type import Type
from core.type.domain.type_repository import TypeRepository


class InMemoryTypeRepository(TypeRepository):

    def __init__(self):
        self._database = {}

    def store(self, type: Type) -> None:
        self._database[type.type_id.value] = type

    def find_all(self) -> List[Type]:
        return list(self._database.values())

