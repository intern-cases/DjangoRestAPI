from django.contrib.gis.db.models import PointField
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_company = models.BooleanField(default=False, null=True)
    is_dealer = models.BooleanField(default=False, null=True)
    is_customer = models.BooleanField(default=False, null=True)


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    location = PointField(default='POINT(41.06 28.99)')
    is_active = models.BooleanField(default=True)
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)
