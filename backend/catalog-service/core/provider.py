from core.brand.application.get_brands import GetBrands
from core.brand.domain.brand_repository import BrandRepository
from core.brand.infrastructure.django_brand_repository import DjangoBrandRepository
from core.item.application.change_price_item import ChangePriceItem
from core.item.application.create_item import CreateItem
from core.item.application.get_paginated_items import GetPaginatedItems
from core.item.domain.item_repository import ItemRepository
from core.item.infrastructure.django_item_repository_repository import DjangoItemRepository
from core.shared.bus.domain.event_bus import EventBus
from core.type.application.get_types import GetTypes
from core.type.domain.type_repository import TypeRepository
from core.type.infrastructure.django_type_repository import DjangoTypeRepository


class Provider:
    event_bus: EventBus

    # Brand
    get_brands: GetBrands

    # Type
    get_types: GetTypes

    # Item
    get_paginated_items: GetPaginatedItems
    change_price_item: ChangePriceItem
    create_item: CreateItem

    def __init__(self):
        # Infrastructure
        brand_repository: BrandRepository = DjangoBrandRepository()
        type_repository: TypeRepository = DjangoTypeRepository()
        item_repository: ItemRepository = DjangoItemRepository()

        # InfrastructureServices

        # Application Services
        self.get_brands = GetBrands(brand_repository)
        self.get_types = GetTypes(type_repository)
        self.get_paginated_items = GetPaginatedItems(item_repository)


provider = Provider()
