from django.db import models

# Create your models here.


class Filters(models.Model):
    f1 = models.CharField(max_length=255)
    f2 =  models.CharField(max_length=255)
    f3 =  models.CharField(max_length=255)
    f4 =  models.CharField(max_length=255)

    def __str__(self):
        return f'{self.f1} - {self.f2} - {self.f3} - {self.f4}'


class FiltredData(models.Model):
    name = models.CharField(max_length=255)
    product_code = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    currency = models.CharField(max_length=255)
    qty = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name} - {self.product_code} - {self.price} - {self.image} - {self.currency} - {self.qty}'