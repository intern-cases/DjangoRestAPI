from DjangoRestAPI.Dealer.models import Dealer
from django.db import models
# Create your models here.


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    dealer = models.ForeignKey(Dealer, related_name='products', on_delete=models.CASCADE, null=True)
    is_active = models.BooleanField(default=True)
    declaration = models.CharField(max_length=500)
    is_discount = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='db', null=True, editable=True)
    price = models.DecimalField(max_digits=14, decimal_places=2)
    created_date = models.DateField(auto_now_add=True, editable=False)
    modified_date = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.declaration)


class Discount(models.Model):
    product = models.ForeignKey(Product, related_name='discount', on_delete=models.CASCADE, null=True, unique=True)
    is_active = models.BooleanField(default=True)
    discount_price = models.DecimalField(max_digits=14, decimal_places=2)
    discount_start = models.DateField(auto_now=True)
    discount_finish = models.DateField()
    created_date = models.DateField(auto_now_add=True, editable=False)
    modified_date = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.product)

