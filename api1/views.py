from api1.models import Products
from api1.serializer import ProductsSerializer
from rest_framework import generics
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

class ProductsList(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['productName', 'productManufactureInfo', 'productCategory']
    authentication_classes = [ JWTAuthentication ]
    permission_classes = [ IsAuthenticated ]


class ProductsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['productName', 'productManufactureInfo', 'productCategory']
    authentication_classes = [ JWTAuthentication ]
    permission_classes = [ IsAuthenticated ]
