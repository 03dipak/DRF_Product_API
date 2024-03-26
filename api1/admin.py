from django.contrib import admin
from api1.models import Products
# Register your models here.

class ProductsAdmin(admin.ModelAdmin):
    list_display = ['id','productName','productDescription','productManufactureInfo','productSerialNumber','productDateManufacture','productWarrantyInfo','productCategory']

admin.site.register(Products,ProductsAdmin)
