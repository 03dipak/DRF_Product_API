from rest_framework import serializers
from api1.models import Products

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id','productName','productDescription','productManufactureInfo','productSerialNumber','productDateManufacture','productWarrantyInfo','productCategory']
