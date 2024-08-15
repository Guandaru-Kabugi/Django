from django.contrib import admin
from .models import Product,ProductDescription
# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','sku')
    list_filter = ('price', )
    
@admin.register(ProductDescription)
class ProductDescriptionAdmin(admin.ModelAdmin):
    list_display = ('product_chosen','description','specifications','warranty')
    list_filter = ('product_chosen', )