# Generated by Django 2.2.4 on 2019-08-20 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0002_product_dealer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='location',
        ),
    ]
