from drf_spectacular.utils import extend_schema
from rest_framework import status, serializers
from rest_framework.decorators import api_view
from rest_framework.fields import CharField, UUIDField
from rest_framework.response import Response


class GetTypesResponse(serializers.Serializer):
    typeId = UUIDField(required=False)
    name = CharField(required=False)


@extend_schema(
    responses={200: GetTypesResponse(many=True)}
)
@api_view(['GET'])
def get_types(request):
    result = []

    serializer = GetTypesResponse(result, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
