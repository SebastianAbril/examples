from drf_spectacular.utils import extend_schema
from rest_framework import status, serializers
from rest_framework.decorators import api_view
from rest_framework.fields import CharField, UUIDField
from rest_framework.response import Response

from core.provider import Provider


class GetTypesResponse(serializers.Serializer):
    typeId = UUIDField(required=False)
    name = CharField(required=False)


@extend_schema(
    responses={200: GetTypesResponse(many=True)}
)
@api_view(['GET'])
def get_types(request):
    provider: Provider = request.provider
    result = provider.get_types.execute()

    response = GetTypesResponse(result, many=True)
    return Response(response.data, status=status.HTTP_200_OK)
