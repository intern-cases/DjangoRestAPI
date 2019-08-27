from django.core.management.base import BaseCommand
from DjangoRestAPI.Product.models import Product, Discount
from datetime import date


def to_integer(dt_time):
    return 10000*dt_time.year + 100*dt_time.month + dt_time.day


class Command(BaseCommand):

    help = 'Delete expired discounts'

    def handle(self, *args, **options):
        queryset = Discount.objects.all()

        for entry in queryset:
            if to_integer(entry.discount_finish) < to_integer(date.today()):
                products = Product.objects.filter(id=entry.product_id).first()
                entry.delete()
                products.is_discount = False
                products.save()

        self.stdout.write(self.style.SUCCESS('Successfully checked discounts'))
