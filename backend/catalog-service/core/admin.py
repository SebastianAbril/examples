from django.contrib import admin
from core.brand.infrastructure.django_brand_repository import BrandModel
from core.item.infrastructure.django_item_repository_repository import ItemModel
from core.type.infrastructure.django_type_repository import TypeModel

admin.site.register(BrandModel)
admin.site.register(TypeModel)
admin.site.register(ItemModel)
