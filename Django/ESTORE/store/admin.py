from django.contrib import admin
from .models import *

# Register your models here.

class AdminProduct(admin.ModelAdmin):
    list_display = ['product_name', 'product_price', 'category']

    
class AdminCategory(admin.ModelAdmin):
    list_display = ['category_name']


admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)

admin.site.register(ColorVariant)
admin.site.register(SizeVariant)
