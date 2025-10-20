from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class Creator(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.phone_number}, {self.country}"

class Product(models.Model):
    name = models.CharField(max_lengtsh=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    amount = models.DecimalField(max_digits=8, decimal_places=2)

    product_category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True,
                                         related_name='products')
    creator = models.ForeignKey(Creator, on_delete=models.SET_NULL, null=True, blank=True,
                                         related_name='products')

    def __str__(self):
        return f"{self.name} {self.product_category} {self.price} {self.creator} {self.amount}"




