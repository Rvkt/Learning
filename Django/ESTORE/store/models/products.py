from django.db import models

from .category import Category
from .color import ColorVariant
from .size import SizeVariant


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_price = models.IntegerField(default=100)
    image = models.ImageField(upload_to='products')
    product_description = models.TextField()

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    color_variant = models.ManyToManyField(ColorVariant, blank=True)
    size_variant = models.ManyToManyField(SizeVariant, blank=True)


    # stringfy
    def __str__(self):
        return self.product_name