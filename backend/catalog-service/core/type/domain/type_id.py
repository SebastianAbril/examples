from core.shared.base.domain.uuid import UUID


class TypeId(UUID):
    def __init__(self, value: str):
        super().__init__(value)
