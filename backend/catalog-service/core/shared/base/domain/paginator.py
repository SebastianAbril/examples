from typing import List, TypeVar, Generic

T = TypeVar("T")

class Paginator(Generic[T]):
    total_items: int
    total_pages: int
    current_page: int
    data: List[T]

    def __init__(self, total_items: int, total_pages: int, current_page: int, data: List[T]):
        self.total_items = total_items
        self.total_pages = total_pages
        self.current_page = current_page
        self.data = data
