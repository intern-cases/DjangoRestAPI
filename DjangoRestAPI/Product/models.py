from DjangoRestAPI.Dealer.models import Dealer
from django.db import models
# Create your models here.


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE, null=True)
    is_active = models.BooleanField(default=True)
    declaration = models.CharField(max_length=500)
    photo = models.ImageField(upload_to='db', null=True, editable=True)
    price = models.DecimalField(max_digits=14, decimal_places=2)
    created_date = models.DateField(auto_now_add=True, editable=False)
    modified_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.declaration


