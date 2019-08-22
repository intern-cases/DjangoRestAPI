from django.db import models
from django.contrib.gis.db.models import PointField
from DjangoRestAPI.accounts.models import User
# Create your models here.
# company/models.py
from DjangoRestAPI import settings


class Company(models.Model):
    user = models.OneToOneField(on_delete=models.CASCADE, unique=True, default=None, to=settings.AUTH_USER_MODEL)
    id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=50, unique=True)
    working_area = models.CharField(max_length=30)
    establish_year = models.DateField()
    is_active = models.BooleanField(default=True)
    location = PointField(default='POINT(41.06 28.99)')
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.company_name)
