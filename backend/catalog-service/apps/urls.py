"""apps URL Configuration

The `urlpatterns` list operations URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from apps.api.operations.brand.get_brands import get_brands
from apps.api.operations.item.change_price_item import change_price_item
from apps.api.operations.item.create_item import create_item
from apps.api.operations.item.get_item_by_id import get_item_by_id
from apps.api.operations.item.get_paginated_items import get_paginated_items
from apps.api.operations.type.get_types import get_types

urlpatterns = [
    path('admin/', admin.site.urls),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='schema-swagger-ui'),
    path('api/v1/item/create_item', create_item),
    path('api/v1/item/change_price_item', change_price_item),
    path('api/v1/item/get_paginated_items', get_paginated_items),
    path('api/v1/item/get_item_by_id/<uuid:item_id>/', get_item_by_id),
    path('api/v1/brand/get_brands', get_brands),
    path('api/v1/type/get_types', get_types),
]
