from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    sku = models.CharField(max_length=50, unique=True, null=False)
class ProductDescription(models.Model):
    product_chosen = models.OneToOneField(Product,on_delete=models.CASCADE,related_name='description')
    description = models.TextField()
    specifications = models.TextField()
    warranty = models.CharField(max_length=50)