from DjangoRestAPI.Company.models import Company
from django.db import models
from django.contrib.gis.db.models import PointField
from DjangoRestAPI.accounts.models import User
# Create your models here.

# dealers/models.py

class Dealer(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField(max_length=50, unique=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    establish_year = models.DateField()
    is_active = models.BooleanField(default=True)
    location = PointField(default='POINT(0.0 0.0)')
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
