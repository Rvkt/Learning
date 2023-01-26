from django.db import models

# Create your models here.

class SizeVariant(models.Model):
    size_name = models.CharField(max_length=100)
    size_price = models.IntegerField(default=100)


    # stringfy
    def __str__(self):
        return self.size_name