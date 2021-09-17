from drf_spectacular.utils import extend_schema
from rest_framework import status, serializers
from rest_framework.decorators import api_view
from rest_framework.fields import CharField, FloatField, UUIDField
from rest_framework.response import Response


class CreateItemRequest(serializers.Serializer):
    item_id = UUIDField(required=True)
    brand_id = UUIDField(required=True)
    type_id = UUIDField(required=True)
    description = CharField(required=True)
    picture_file_name = CharField(required=True)
    price = FloatField(required=True)


@extend_schema(
    request=CreateItemRequest,
    responses={201: None}
)
@api_view(['POST'])
def create_item(request):
    serializer = CreateItemRequest(data=request.data)
    print(serializer.is_valid(raise_exception=True))


    return Response(status=status.HTTP_201_CREATED)
