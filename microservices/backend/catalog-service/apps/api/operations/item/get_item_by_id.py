from drf_spectacular.utils import extend_schema
from rest_framework import status, serializers
from rest_framework.decorators import api_view
from rest_framework.fields import CharField, UUIDField, FloatField
from rest_framework.response import Response

from core.item.domain.item_id import ItemId
from core.provider import Provider


class GetItemByIdResponse(serializers.Serializer):
    itemId = UUIDField(required=True, source='item_id.value')
    brandId = UUIDField(required=True, source='brand_id.value')
    typeId = UUIDField(required=True, source='type_id.value')
    name = CharField(required=True)
    description = CharField(required=True)
    pictureFileName = CharField(required=True, source='picture_file_name')
    price = FloatField(required=True)


@extend_schema(
    responses={200: GetItemByIdResponse}
)
@api_view(['GET'])
def get_item_by_id(request, item_id):
    provider: Provider = request.provider
    response = provider.get_item_by_id.execute(ItemId(str(item_id)))
    serializer = GetItemByIdResponse(response)

    return Response(serializer.data, status=status.HTTP_200_OK)
