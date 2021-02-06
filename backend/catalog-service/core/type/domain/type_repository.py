from abc import ABCMeta, abstractmethod
from typing import List

from core.type.domain.type import Type


class TypeRepository(metaclass=ABCMeta):

    @abstractmethod
    def store(self, item_type: Type):
        pass

    @abstractmethod
    def find_all(self) -> List[Type]:
        pass