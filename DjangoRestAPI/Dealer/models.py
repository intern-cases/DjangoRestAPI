from django.db import models
from DjangoRestAPI.Company.models import Company


# Create your models here.

# dealers/models.py


class Dealer(models.Model):
    name = models.CharField(max_length=50, unique=True, primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    establish_year = models.DateField()
    is_active = models.BooleanField(default=True)
    # Location = models.
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)
