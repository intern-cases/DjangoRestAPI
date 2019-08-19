from django.db import models
from DjangoRestAPI.Dealer.models import Dealer
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE, null=True)
    is_active = models.BooleanField(default=True)
    declaration = models.CharField(max_length=500)
    photo = models.ImageField(upload_to='db', null=True, editable=True)
    price = models.DecimalField(max_digits=14, decimal_places=2)
    # Location = models.
    created_date = models.DateField(auto_now_add=True, editable=False)
    modified_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.declaration

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_date = timezone.now()
        self.modified_date = timezone.now()
        return super(Product, self).save(*args, **kwargs)
