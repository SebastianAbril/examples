from drf_spectacular.utils import extend_schema
from rest_framework import status, serializers
from rest_framework.decorators import api_view
from rest_framework.fields import CharField, UUIDField, IntegerField, FloatField
from rest_framework.response import Response

from core.provider import Provider


class GetPaginatedItemsQuery(serializers.Serializer):
    page = IntegerField(required=False, default=0)
    size = IntegerField(required=False, default=10)


class ItemsResponse(serializers.Serializer):
    itemId = UUIDField(required=True, source='item_id.value')
    brandId = UUIDField(required=True, source='brand_id.value')
    typeId = UUIDField(required=True, source='type_id.value')
    name = CharField(required=True)
    description = CharField(required=True)
    pictureFileName = CharField(required=True, source='picture_file_name')
    price = FloatField(required=True)


class GetPaginatedItemsResponse(serializers.Serializer):
    totalItems = IntegerField(required=True, source='total_items')
    totalPages = IntegerField(required=True, source='total_pages')
    currentPage = IntegerField(required=True, source='current_page')
    data = ItemsResponse(many=True)


@extend_schema(
    parameters=[GetPaginatedItemsQuery],
    responses={200: GetPaginatedItemsResponse},
)
@api_view(['GET'])
def get_paginated_items(request):
    serializer = GetPaginatedItemsQuery(data=request.query_params)

    #TODO Check for invalid response
    serializer.is_valid()
    size = serializer.validated_data.get('size')
    page = serializer.validated_data.get('page')

    provider: Provider = request.provider
    result = provider.get_paginated_items.execute(size, page)

    serializer = GetPaginatedItemsResponse(result)
    return Response(serializer.data, status=status.HTTP_200_OK)
