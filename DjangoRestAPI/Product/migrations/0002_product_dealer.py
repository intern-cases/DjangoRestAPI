# Generated by Django 2.2.4 on 2019-08-19 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Dealer', '0001_initial'),
        ('Product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='dealer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Dealer.Dealer'),
        ),
    ]