from drf_spectacular.utils import extend_schema
from rest_framework import status, serializers
from rest_framework.decorators import api_view
from rest_framework.fields import CharField, UUIDField
from rest_framework.response import Response

from core.provider import Provider


class GetBrandsResponse(serializers.Serializer):
    brandId = UUIDField(required=False, source='brand_id.value')
    name = CharField(required=False)


@extend_schema(
    responses={200: GetBrandsResponse(many=True)},
    description='hola',
    summary='sss'
)
@api_view(['GET'])
def get_brands(request):
    provider: Provider = request.provider
    result = provider.get_brands.execute()
    response = GetBrandsResponse(result, many=True)

    return Response(response.data, status=status.HTTP_200_OK)
