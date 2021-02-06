from drf_spectacular.utils import extend_schema
from rest_framework import status, serializers
from rest_framework.decorators import api_view
from rest_framework.fields import CharField, UUIDField, IntegerField, FloatField
from rest_framework.response import Response


class GetPaginatedItemsQuery(serializers.Serializer):
    page = IntegerField(required=False, default=0)
    size = IntegerField(required=False, default=10)


class ItemsResponse(serializers.Serializer):
    itemId = UUIDField(required=True)
    brandId = UUIDField(required=True)
    typeId = UUIDField(required=True)
    description = CharField(required=True)
    pictureFileName = CharField(required=True)
    price = FloatField(required=True)


class GetPaginatedItemsResponse(serializers.Serializer):
    totalItems = IntegerField(required=True)
    totalPages = IntegerField(required=True)
    currentPage = IntegerField(required=True)
    data = ItemsResponse(many=True)


@extend_schema(
    parameters=[GetPaginatedItemsQuery],
    responses={200: GetPaginatedItemsResponse},
    description='hola',
    summary='sss'
)
@api_view(['GET'])
def get_paginated_items(request):
    response = []
    serializer = GetPaginatedItemsResponse(response)
    return Response(serializer.data, status=status.HTTP_200_OK)
