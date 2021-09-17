from drf_spectacular.utils import extend_schema
from rest_framework import status, serializers
from rest_framework.decorators import api_view
from rest_framework.fields import CharField, FloatField, UUIDField
from rest_framework.response import Response


class ChangePriceItemRequest(serializers.Serializer):
    item_id = UUIDField(required=True)
    new_price = FloatField(required=True)


@extend_schema(
    request=ChangePriceItemRequest,
    responses={202: None}
)
@api_view(['PUT'])
def change_price_item(request):
    serializer = ChangePriceItemRequest(data=request.data)
    print(serializer.is_valid(raise_exception=True))

    return Response(status=status.HTTP_200_OK)
