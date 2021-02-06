from drf_spectacular.utils import extend_schema
from rest_framework import status, serializers
from rest_framework.decorators import api_view
from rest_framework.fields import CharField, UUIDField,  FloatField
from rest_framework.response import Response



class GetItemByIdResponse(serializers.Serializer):
    itemId = UUIDField(required=True)
    brandId = UUIDField(required=True)
    typeId = UUIDField(required=True)
    description = CharField(required=True)
    pictureFileName = CharField(required=True)
    price = FloatField(required=True)

@extend_schema(
    responses={200: GetItemByIdResponse},
    description='hola',
    summary='sss'
)
@api_view(['GET'])
def get_item_by_id(request, item_id):
    print(item_id)
    response = {}
    serializer = GetItemByIdResponse(response)
    return Response(serializer.data, status=status.HTTP_200_OK)
