from core.brand.application.get_brands import GetBrands
from core.brand.domain.brand_repository import BrandRepository
from core.brand.infrastructure.in_memory_brand_repository import InMemoryBrandRepository
from core.item.application.change_price_item import ChangePriceItem
from core.item.application.create_item import CreateItem
from core.shared.bus.domain.event_bus import EventBus
from core.type.application.get_types import GetTypes
from core.type.domain.type_repository import TypeRepository
from core.type.infrastructure.in_memory_type_repository import InMemoryTypeRepository
from core_test.brand.domain.brand_mother import BrandMother


class Provider:
    event_bus: EventBus

    # Brand
    get_brands: GetBrands

    # Type
    get_types: GetTypes

    # Item
    change_price_item: ChangePriceItem
    create_item: CreateItem

    def __init__(self):
        # Infrastructure
        brand_repository: BrandRepository = InMemoryBrandRepository()
        type_repository: TypeRepository = InMemoryTypeRepository()

        brands = BrandMother.random_brands()
        for brand in brands:
            brand_repository.store(brand)

        # InfrastructureServices

        # Application Services
        self.get_brands = GetBrands(brand_repository)
        self.get_types = GetTypes(type_repository)


provider = Provider()
