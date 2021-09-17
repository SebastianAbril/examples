from abc import ABCMeta, abstractmethod
from typing import List
from core.brand.domain.brand import Brand


class BrandRepository(metaclass=ABCMeta):

    @abstractmethod
    def store(self, brand: Brand) -> None:
        pass

    @abstractmethod
    def find_all(self) -> List[Brand]:
        pass