from typing import List

from core.type.domain.type import Type
from core.type.domain.type_repository import TypeRepository


class GetTypes:
    _type_repository: TypeRepository

    def __init__(self, type_repository: TypeRepository):
        self._type_repository = type_repository

    def execute(self) -> List[Type]:
        return self._type_repository.find_all()
