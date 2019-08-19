from django.db import models
from django.contrib.auth.admin import UserAdmin
# Create your models here.


#company/models.py
class Company(models.Model):
    company_name = models.CharField(max_length=50, unique=True, primary_key=True)
    working_area = models.CharField(max_length=30)
    establish_year = models.DateField()
    is_active = models.BooleanField(default=True)
    #Location = models.
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)
