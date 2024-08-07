from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    product_price = models.IntegerField(default=0)
    category = models.CharField(max_length=200)
    added_date = models.DateField()
    def __str__(self):
        return self.name