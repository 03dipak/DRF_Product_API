from django.db import models

# Create your models here.
class Products(models.Model):
    productName = models.CharField(max_length = 64)
    productDescription = models.TextField(max_length = 64)
    productManufactureInfo = models.CharField(max_length = 64)
    productSerialNumber = models.CharField(max_length=64, unique=True)
    productDateManufacture = models.DateTimeField()
    productWarrantyInfo = models.CharField(max_length = 64)
    productCategory = models.CharField(max_length = 64)
