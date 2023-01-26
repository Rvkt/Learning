from django.db import models

# Create your models here.

class ColorVariant(models.Model):
    color_name = models.CharField(max_length=100)
    color_price = models.IntegerField(default=100)


    # stringfy
    def __str__(self):
        return self.color_name