from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    category_price = models.IntegerField(default=100)


    # stringfy
    def __str__(self):
        return self.category_name

