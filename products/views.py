from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Category, Product, ProductImage
from .serializers import ProductSerializers


@api_view(['GET'])
def get_products(request):
    queryset = Product.objects.all()
    serialized_data = ProductSerializers(queryset, many=True)
    return Response({'products': serialized_data.data}, status=status.HTTP_200_OK)
