from django.contrib import admin
from DjangoRestAPI.Product.models import Product, Discount
# Register your models here.


class ProductModelAdmin(admin.ModelAdmin):
    list_display = ["__str__", "created_date", "modified_date"]

    class Meta:
        model = Product


admin.site.register(Product, ProductModelAdmin)
admin.site.register(Discount)