# Generated by Django 2.2.4 on 2019-08-27 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0005_auto_20190827_0836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='discount', to='Product.Product', unique=True),
        ),
    ]
