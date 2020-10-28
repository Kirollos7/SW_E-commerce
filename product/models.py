from django.db import models
from djmoney.models.fields import MoneyField

# Create your models here.


class Product(models.Model):
    class Meta:
        pass
    product_id = models.CharField(primary_key=True,max_length=255)
    name = models.CharField(max_length=255, null=True, unique=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    description = models.TextField(null=True)
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='EGY',null=True)
    image = models.ImageField(upload_to='media',null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    class Meta:
        pass
    name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name


 